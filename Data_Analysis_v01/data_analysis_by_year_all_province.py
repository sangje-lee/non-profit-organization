# Python file
# Filterd by 2017, 2019, and 2021 by province.

import pandas as pd
import numpy as np

# Importing dataset
df = pd.read_csv('36100651.csv')

print(df.info())
print(df.head(10))

print("Grab the only the essential part of database.")
df_sorted = df[['REF_DATE','GEO','Sector','Characteristics','Indicators','UOM','SCALAR_FACTOR','VALUE']]
print(df_sorted.head(20))

print(df_sorted.info())
grouped = df.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.size]))

# Grabbing the data preivous from 2014-2016.
print("Grabbing the data previous from 2016.")
df_below_2016_year = df_sorted.loc[
    (df_sorted['REF_DATE'] == 2014) |
    (df_sorted['REF_DATE'] == 2015) |
    (df_sorted['REF_DATE'] == 2016)
]
print(df_below_2016_year.head(20))
print(df_below_2016_year.info())
grouped = df_below_2016_year.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_below_2016_year.index))

# Grabbing the data from 2017, 2019, and 2021.
print("Grabbing the data from 2017, 2019, and 2021.")
df_by_year = df_sorted.loc[
    (df_sorted['REF_DATE'] == 2017) |
    (df_sorted['REF_DATE'] == 2019) |
    (df_sorted['REF_DATE'] == 2021)
]
print(df_by_year.head(20))
print(df_by_year.info())
grouped = df_by_year.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_by_year.index))

# Group by the province.
grouped = df_by_year.groupby(['GEO'])
print(grouped['VALUE'].agg([np.sum, np.size]))

# Average annual hours worked in 2017 by province.
print("\n2017")
df_2017_hours_worked = df_by_year.loc[
    (df_by_year['Indicators'] == 'Average annual hours worked') &
    (df_by_year['REF_DATE'] == 2017)
]
grouped = df_2017_hours_worked.groupby(['GEO'])
print(grouped['VALUE'].agg([np.sum, np.mean, np.std, np.size]))
print("The total number of this one is ",len(df_2017_hours_worked.index))

# Average annual hours worked in 2019 by province.
print("\n2019")
df_2019_hours_worked = df_by_year.loc[
    (df_by_year['Indicators'] == 'Average annual hours worked') &
    (df_by_year['REF_DATE'] == 2019)
]
grouped = df_2019_hours_worked.groupby(['GEO'])
print(grouped['VALUE'].agg([np.sum, np.mean, np.std, np.size]))
print("The total number of this one is ",len(df_2019_hours_worked.index))

# Average annual hours worked in 2021 by province.
print("\n2021")
df_2021_hours_worked = df_by_year.loc[
    (df_by_year['Indicators'] == 'Average annual hours worked') &
    (df_by_year['REF_DATE'] == 2021)
]
grouped = df_2021_hours_worked.groupby(['GEO'])
print(grouped['VALUE'].agg([np.sum, np.mean, np.std, np.size]))
print("The total number of this one is ",len(df_2021_hours_worked.index))

# Resources
# https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html
# https://datatofish.com/select-rows-pandas-dataframe/
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html
# https://sparkbyexamples.com/pandas/pandas-groupby-count-examples/
