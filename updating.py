import pandas as pd
data ={
    "Name":["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [25, 30, 35, 28, 22],
    "Salary": [50000, 60000, 70000, 80000, 45000],
    "Performance score": [85, 90, 95, 80, 75]

}
#/loc[] this is used to access a group of rows and columns by labels or a boolean array & must be used with a DataFrame & Series & is used for modifying the DataFrame
#df.loc[row_index, "column_name"] = new_value
df = pd.DataFrame(data)
print(df)
df.loc[0, "Age"] = 26  # Update Alice's age
df.loc[1, "Salary"] = 62000  # Update Bob's salary
print("DataFrame after updates:")
print(df) 