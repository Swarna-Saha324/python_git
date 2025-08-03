import pandas as pd
df =pd.read_excel("working_hours_job_satisfaction_analysis.xlsx")
pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)
print(df)
#print(df.head(5),index=False)  # Display the first few rows of the DataFrame
print(df.head(5).to_string(index=False))
print(df.tail(5).to_string(index=False))  # Display the last few rows of the DataFrame
print(df.info())