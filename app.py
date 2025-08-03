import pandas as pd

data  = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)
print(df)

df.to_csv("output.csv", index=False)  # Save DataFrame to CSV file
df.to_excel("output.xlsx", index=False)  # Save DataFrame to Excel file