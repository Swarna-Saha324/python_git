import pandas as pd
Data = {
  "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"],
    "salary " : [50000, 60000, 70000],
    "Performance": [85, 90, 95]
 }
df = pd.DataFrame(Data)
print("Sample DataFrame", df)
print("Description of DataFrame:")
print(df.describe())  # Get descriptive statistics of the DataFrame

name = df["Name"]
print(name)
subset = df[["Name", "Age"]]
print("Subset of DataFrame with Name and Age:")
print(subset)