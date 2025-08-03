import pandas as pd
data ={
    "Name":["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [25, 30, 35, 28, 22],
    "Salary": [50000, 60000, 70000, 80000, 45000],
    "Performance score": [85, 90, 95, 80, 75]

}
df = pd.DataFrame(data)
print(df)
#df.drop(columns=["ColumnName"], inplace=True)  # Remove a column
df.drop(columns=["Performance score"], inplace=True)  # Remove the "Performance score" column
print("DataFrame after removing 'Performance score' column:")
print(df)