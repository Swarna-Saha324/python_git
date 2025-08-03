import pandas as pd
data ={
    "Name" : ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age ": [25, 30, 35, 28, 22],
    "Salary" : [50000, 60000, 70000, 80000, 45000],
    "Performance score" : [85, 90, 95, 80, 75]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
avg_salary = df["Salary"].mean()  # Calculate the average salary
print(f"Average Salary: {avg_salary}")
df["Salary"] = df["Salary"].fillna(avg_salary)  # Fill NaN in 'Salary' with average
print("DataFrame after filling NaN values in 'Salary' with average:")
print(df)
grouped = df.groupby("Age") ["Salary"].sum() # Group by 'Age'
grouped1 = df.groupby["Age","Name"]["Performance score"].mean()  # Group by 'Age' and calculate mean of 'Performance score'
print("Grouped DataFrame by 'Age' with sum of 'Salary':")
print(grouped)
print(grouped1)