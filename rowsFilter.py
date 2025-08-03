import pandas as pd

data  = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"],
    "Salary " : [50000, 60000, 70000]
}

df = pd.DataFrame(data)
print(df)
print (f'shape: {df.shape}')
print (f'columns: {df.columns}'  )
high_age = df[df ['Age']>25]
print (high_age)

#filtering rows age > 23 & salary > 60000
filtered_rows = df[(df['Age'] > 23) & (df['Salary '] > 60000)]
print("Filtered rows where Age > 23 and Salary > 60000:")
print(filtered_rows)
# using or condition
filter_or = df[ (df["Age"]>=30)| (df ["Salary "]>50000)]
print(filter_or)
