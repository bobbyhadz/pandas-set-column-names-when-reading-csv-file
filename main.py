# Pandas: Setting column names when reading a CSV file 

import pandas as pd

column_names = ['first_name', 'last_name', 'salary']

df = pd.read_csv(
    'employees.csv',
    names=column_names,
    header=None
)

#   first_name last_name  salary
# 0      Alice     Smith     500
# 1        Bob     Smith     600
# 2       Carl     Smith     400
print(df)