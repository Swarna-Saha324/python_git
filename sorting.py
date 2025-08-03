#df.sort_values(by=["column_name",column_name], ascending= [True,False],inplace=True)
import pandas as pd
data = {
      "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
        "Age": [25, 30, 35, 28, 22],
        "Salary": [50000, 60000, 70000, 80000, 45000],
        "Performance score": [85, 90, 95, 80, 75]

}
df = pd.DataFrame(data)
df.sort_values(by="Age", ascending=True, inplace=True)  # Sort by 'Age' in ascending order
print("DataFrame after sorting by 'Age' in ascending order:")
print(df)
