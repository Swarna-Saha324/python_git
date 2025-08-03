#fillna()
# fillna() is used to fill NA/NaN values using the specified method or value.
#fillna( value,inplace=True)
import pandas as pd
data = {
    "Name": ["Alice", "None", "Charlie", "David", "Eve"],
    "Age": [25, None, 35, 28, 22],
    "Salary": [50000, None, 70000, 80000, 45000],
    "Performance score": [85, None, 95, 80, 75]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
df.fillna(0, inplace=True)  # Fill NaN values with 0
print("DataFrame after filling NaN values with 0:")
print(df)
df["Age"] = df["Age"].fillna(df["Age"].mean())  # Fill NaN in 'Age' with mean
print("DataFrame after filling NaN values in 'Age' with mean:")
print(df)
df.fillna(value={"Age": 30, "Salary": 60000, "Performance score": 90}, inplace=True)  # Fill NaN values
print("DataFrame after filling NaN values:")
print(df)    