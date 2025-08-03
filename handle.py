#dropna()
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
df.dropna(inplace=True)  # Remove rows with any NaN values
print("DataFrame after removing rows with NaN values:")
print(df)