f = open(r"C:\Users\LENOVO\.cursor\python_oneshot\chapter10\file.txt", encoding='utf-8')
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(line1,type(line1))
# print(line2,type(line2))
# print(line3,type(line3))
# f.close()


line = f.readline()

while(line!=""):
    print(line, end="")
    line = f.readline()
    
f.close()