
def GenerateMultiplicationTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} x {i} = {n * i}\n"
        
    with open(fr"C:\Users\LENOVO\.cursor\python_oneshot\chapter10\tables/table_{n}.txt", "w") as f:
        f.write(table)





for i in range(2,21):
    GenerateMultiplicationTable(i)
    print(f"Multiplication table for {i} generated and saved to file.")