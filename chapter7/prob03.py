#WRP a spam comment is defined as text containing following Keywords "make a lot of money", "buy now", "click this", "subscribe this", "free" write a program to detect these spams in comment entered by user

# comment = input("Enter your comment: ")
# spam_keywords = ["make a lot of money", "buy now", "click this", "subscribe this", "free"]

# if any(keyword in comment.lower() for keyword in spam_keywords):
#     print("This comment is a spam.")
# else:
#     print("This comment is not a spam.")

comment = input("Enter your comment: ").lower()

if "make a lot of money" in comment:
    print("Spam")
elif "buy now" in comment:
    print("Spam")
elif "click this" in comment:
    print("Spam")
elif "subscribe this" in comment:
    print("Spam")
elif "free" in comment:
    print("Spam")
else:
    print("Not Spam")