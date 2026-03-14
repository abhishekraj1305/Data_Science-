import requests

r = requests.post(
    "http://localhost:11434/api/chat",
    json={
        "model": "llama3.2",
        "messages": [{"role": "user", "content": "Say hello"}],
        "stream": False
    }
)

print(r.status_code)
print(r.text)