import pandas as pd
data ={
    "Name":["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [25, 30, 35, 28, 22],
    "Salary": [50000, 60000, 70000, 80000, 45000],
    "Performance score": [85, 90, 95, 80, 75]

}

df = pd.DataFrame(data)
print(df)
df["Bonuus"] = df["Salary"] * 0.1
print("DataFrame with Bonus column:")
print(df)
print(f'shape: {df.shape}')
print(f'columns: {df.columns}')
print("Rows with Age > 25:")
high_age = df[df['Age'] > 25]
print(high_age)
df.insert(2, "Department", ["HR", "Finance", "IT", "Marketing", "Sales"])
print("DataFrame after inserting Department column:")
print(df)