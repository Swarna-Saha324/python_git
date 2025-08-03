import pandas as pd
data ={
  "Time": [1,2,3,4,5],
  "Value": [10, 20, None, 40, 50]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
df["value"] = df["Value"].interpolate(method="linear")  # Interpolate missing values
print("DataFrame after linear interpolation:")
print(df)

"""1-time
    
"""