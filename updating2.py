import pandas as pd
data ={
    "Name":["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [25, 30, 35, 28, 22],
    "Salary": [50000, 60000, 70000, 80000, 45000],
    "Performance score": [85, 90, 95, 80, 75]

}
df = pd.DataFrame(data)
print(df)
df["Salary"] = df["Salary"]* 1.1  # Increase all salaries by 10%
print("DataFrame after salary increase:")
print(df)