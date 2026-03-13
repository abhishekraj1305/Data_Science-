import os
import re
import time
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from playwright.sync_api import sync_playwright, TimeoutError as PWTimeoutError

COURSE_URL = "https://www.codewithharry.com/courses/the-ultimate-job-ready-data-science-course"

PROFILE_DIR = "pw_profile_codewithharry"
DOWNLOAD_DIR = Path("cwh_downloads")
DOWNLOAD_DIR.mkdir(exist_ok=True)

ASSET_EXTS = {".pdf", ".zip", ".rar", ".ppt", ".pptx", ".doc", ".docx", ".xls", ".xlsx", ".csv"}
ASSET_KEYWORDS = {"download", "handbook", "notes", "pdf", "worksheet", "resource", "file"}

DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    ),
    "Accept": "*/*",
    "Accept-Language": "en-IN,en;q=0.9",
    "Connection": "keep-alive",
}

def safe_name(s: str) -> str:
    s = re.sub(r"[^\w\-\. ]+", "_", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s[:180] if len(s) > 180 else s

def is_logged_in(page) -> bool:
    # If course is accessible and lesson links exist, you're logged in.
    # Works better than checking "Login" text.
    return page.locator("a[href*='/courses/the-ultimate-job-ready-data-science-course/'][href*='--']").count() > 0

def looks_like_asset(url: str, text: str) -> bool:
    url_l = (url or "").lower()
    text_l = (text or "").lower()
    if any(k in text_l for k in ASSET_KEYWORDS):
        return True
    path = urlparse(url_l).path
    return any(path.endswith(ext) for ext in ASSET_EXTS)

def get_extension_from_url(url: str) -> str:
    return os.path.splitext(urlparse(url).path)[1].lower()

def build_requests_session_from_context(context) -> requests.Session:
    sess = requests.Session()
    sess.headers.update(DEFAULT_HEADERS)
    for c in context.cookies():
        sess.cookies.set(c["name"], c["value"], domain=c.get("domain"), path=c.get("path", "/"))
    return sess

def download_with_requests(sess: requests.Session, url: str, out_path: Path) -> bool:
    try:
        r = sess.get(url, stream=True, timeout=60, allow_redirects=True)
        if r.status_code != 200:
            print(f"   ⚠️ HTTP {r.status_code} for {url}")
            return False
        with open(out_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=1024 * 256):
                if chunk:
                    f.write(chunk)
        print(f"   ✅ Saved: {out_path.name}")
        return True
    except Exception as e:
        print(f"   ⚠️ Download failed: {e}")
        return False

def collect_lesson_urls(page) -> list[str]:
    time.sleep(2)
    anchors = page.locator("a[href*='/courses/the-ultimate-job-ready-data-science-course/']").all()
    urls = []
    for a in anchors:
        href = a.get_attribute("href") or ""
        if href.startswith("/courses/the-ultimate-job-ready-data-science-course/") and "--" in href:
            urls.append(urljoin("https://www.codewithharry.com", href))
    seen, out = set(), []
    for u in urls:
        if u not in seen:
            seen.add(u)
            out.append(u)
    return out

def extract_download_links(page) -> list[tuple[str, str]]:
    links = []
    loc = page.locator("main a")
    for i in range(loc.count()):
        a = loc.nth(i)
        href = a.get_attribute("href") or ""
        if not href:
            continue
        try:
            text = (a.inner_text() or "").strip()
        except Exception:
            text = ""
        abs_url = urljoin("https://www.codewithharry.com", href)
        if looks_like_asset(abs_url, text):
            links.append((abs_url, text))
    seen, out = set(), []
    for u, t in links:
        if (u, t) not in seen:
            seen.add((u, t))
            out.append((u, t))
    return out

def lesson_title(page, fallback: str) -> str:
    h1 = page.locator("h1").first
    try:
        if h1.count():
            return safe_name(h1.inner_text(timeout=1500).strip())
    except Exception:
        pass
    return safe_name(fallback)

def main():
    with sync_playwright() as p:
        # Use real Chrome (less chance of Google issues)
        context = p.chromium.launch_persistent_context(
            user_data_dir=PROFILE_DIR,
            channel="chrome",
            headless=False,
            accept_downloads=True,
        )
        page = context.new_page()
        page.goto(COURSE_URL, wait_until="domcontentloaded")
        time.sleep(2)

        # Manual login gate (no bypass, no stealth)
        if not is_logged_in(page):
            print("\n🔐 Login required.")
            print("👉 In the opened Chrome window, click 'Continue with Google' and login manually.")
            print("👉 After login, open the course page and make sure the lesson list is visible.")
            input("\nOnce done, press ENTER here to continue...")

        page.goto(COURSE_URL, wait_until="networkidle")
        time.sleep(2)

        if not is_logged_in(page):
            print("❌ Still not logged in / lesson list not visible.")
            print("Open any lesson once (like 'What is Data Science?') then re-run.")
            return

        print("✅ Logged in. Starting downloads...")
        req = build_requests_session_from_context(context)

        lessons = collect_lesson_urls(page)
        print(f"Found lessons: {len(lessons)}")
        (DOWNLOAD_DIR / "lesson_urls.txt").write_text("\n".join(lessons), encoding="utf-8")

        for idx, url in enumerate(lessons, start=1):
            print(f"\n[{idx}/{len(lessons)}] {url}")
            page.goto(url, wait_until="networkidle")
            time.sleep(1.5)

            lt = lesson_title(page, f"lesson_{idx:03d}")
            links = extract_download_links(page)
            if not links:
                print("— No downloads.")
                continue

            print(f"— Download links found: {len(links)}")
            for j, (asset_url, text) in enumerate(links, start=1):
                ext = get_extension_from_url(asset_url)
                if ext not in ASSET_EXTS:
                    ext = ".pdf" if "pdf" in (asset_url.lower() + " " + text.lower()) else ""

                base = safe_name(text) if text else f"asset_{j:02d}"
                out = DOWNLOAD_DIR / safe_name(f"{lt}__{base}{ext}")

                if out.exists() and out.stat().st_size > 0:
                    print(f"   ⏭️ Exists: {out.name}")
                    continue

                download_with_requests(req, asset_url, out)

        print("\n✅ DONE:", DOWNLOAD_DIR.resolve())

if __name__ == "__main__":
    main()