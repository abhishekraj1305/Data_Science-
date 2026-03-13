'''
a = "A very long Email address that exceeds the typical length of an email address and is used for testing purposes only"
'''

import os


# f = open(r"C:\Users\LENOVO\.cursor\python_oneshot\chapter10\file.txt")
# data = f.read()
# print(data)
# f.close()


with open(r"E:\Downloads\Abhishek_data.txt", 'r', encoding='utf-8') as f:
    data = f.read()
    mydata = data
    print(mydata)



with open(r"C:\Users\LENOVO\.cursor\python_oneshot\chapter10\file.txt", 'w', encoding='utf-8') as f:
    f.write(mydata)
    f.close()
    
    