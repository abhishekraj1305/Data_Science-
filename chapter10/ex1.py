with open(r"C:\Users\LENOVO\.cursor\python_oneshot\chapter10\poem.txt", 'r') as f:
    data = f.read()
    # print(data)
    
    
if "twinkle" in data.lower():
    print("Twinkle is present in the poem.")
else:
    print("Twinkle is not present in the poem.")