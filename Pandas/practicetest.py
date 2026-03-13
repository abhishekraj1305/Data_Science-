import pandas as pd

df1 = pd.DataFrame({
    "emp_id": [1, 2, 3],
    "name": ["A", "B", "C"]
})

df2 = pd.DataFrame({
    "emp_id": [1, 2, 4],
    "salary": [50000, 60000, 70000]
})

merged = pd.merge(df1, df2, on="emp_id", how="outer")
print(merged)