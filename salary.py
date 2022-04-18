import profile
import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_csv('salary.csv')
print(df)

profile = ProfileReport(df)
profile.to_file(output_file="salary.html")