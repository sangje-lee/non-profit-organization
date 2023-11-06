# Data Analysis in Ontario only
# By Gender group, Age group, Immigration status, education level
# Further by averege wages, number of hours worked and number of job available.

import pandas as pd
import numpy as np


df = pd.read_csv('36100651.csv')

print(df.info())
print(df.head(10))


print("Grab the only the essential part of database.")
df_sorted = df[['REF_DATE','GEO','Sector','Characteristics','Indicators','UOM','SCALAR_FACTOR','VALUE']]
print(df_sorted.head(20))

print(df_sorted.info())
grouped = df.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.size]))

print("\nGrab the dataset only in Ontario.")
df_ontario = df_sorted.loc[df_sorted['GEO'] == 'Ontario']
print(df_ontario.head(20))
print(df_ontario.info())
grouped = df_ontario.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.size]))

print("\nAge group in Ontario")
df_ont_by_age = df_ontario.loc[
    (df_ontario['Characteristics'] == '15 to 24 years') |
    (df_ontario['Characteristics'] == '25 to 34 years') |
    (df_ontario['Characteristics'] == '35 to 44 years') |
    (df_ontario['Characteristics'] == '45 to 54 years') |
    (df_ontario['Characteristics'] == '55 to 64 years') |
    (df_ontario['Characteristics'] == '65 years old and over')]
print(df_ont_by_age.head(20))
grouped = df_ont_by_age.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_ont_by_age.index))

print("\nGender group in Ontario")
df_ont_by_gender = df_ontario.loc[
    (df_ontario['Characteristics'] == 'Female employees') |
    (df_ontario['Characteristics'] == 'Male employees')
]
print(df_ont_by_gender.head(20))
grouped = df_ont_by_gender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_ont_by_gender.index))

print("\nEducation group in Ontario")
df_ont_education = df_ontario.loc[
    (df_ontario['Characteristics'] == 'High school diploma and less') |
    (df_ontario['Characteristics'] == 'Trade certificate') |
    (df_ontario['Characteristics'] == 'University degree and higher')
]
print(df_ont_education.head(20))
grouped = df_ont_education.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_ont_education.index))

print("\nImmigrant group in Ontario")
df_ont_immigrant = df_ontario.loc[
    (df_ontario['Characteristics'] == 'Immigrant employees') |
    (df_ontario['Characteristics'] == 'Non-immigrant employees')
]
print(df_ont_immigrant.head(20))
grouped = df_ont_immigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_ont_immigrant.index))

print("\nIndigenous group in Ontario")
df_ont_indigenous = df_ontario.loc[
    (df_ontario['Characteristics'] == 'Indigenous identity employees') |
    (df_ontario['Characteristics'] == 'Non-indigenous identity employees')
]
print(df_ont_indigenous.head(20))
grouped = df_ont_indigenous.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_ont_indigenous.index))

print()
# By average annual hours worked in age group
print("By average annual hours")
df_ont_hours_worked_age = df_ont_by_age.loc[
    (df_ont_by_age['Indicators'] == 'Average annual hours worked') 
]
grouped = df_ont_hours_worked_age.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.mean, np.std, np.size]))
print("The total number of this one is ",len(df_ont_hours_worked_age.index))

# By average annual hours worked in gender group
df_ont_hours_worked_gender = df_ont_by_gender.loc[
    (df_ont_by_gender['Indicators'] == 'Average annual hours worked') 
]
grouped = df_ont_hours_worked_gender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.mean, np.std, np.size]))
print("The total number of this one is ",len(df_ont_hours_worked_gender.index))

# By average annual hours worked in education level
df_ont_hours_worked_education = df_ont_education.loc[
    (df_ont_education['Indicators'] == 'Average annual hours worked') 
]
grouped = df_ont_hours_worked_education.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.mean, np.std, np.size]))
print("The total number of this one is ",len(df_ont_hours_worked_education.index))

# By average annual hours worked in immigration level
df_ont_hours_worked_immigrant = df_ont_immigrant.loc[
    (df_ont_immigrant['Indicators'] == 'Average annual hours worked') 
]
grouped = df_ont_hours_worked_immigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.mean, np.std, np.size]))
print("The total number of this one is ",len(df_ont_hours_worked_immigrant.index))

# By average annual hours worked in age group
print("By average annual wages/salaries or hourly wage")

df_ont_hourly_salary_age = df_ont_by_age.loc[
    (df_ont_by_age['Indicators'] == 'Average hourly wage')
]

grouped = df_ont_hourly_salary_age.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.mean, np.std, np.size]))
print("The total number of this one is ",len(df_ont_hourly_salary_age.index))

df_ont_salary_age = df_ont_by_age.loc[
    (df_ont_by_age['Indicators'] == 'Average annual wages and salaries')
]

grouped = df_ont_salary_age.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.mean, np.std, np.size]))
print("The total number of this one is ",len(df_ont_salary_age.index))

# By average annual hours worked in gender group
df_ont_hourly_salary_gender = df_ont_by_gender.loc[
    (df_ont_by_gender['Indicators'] == 'Average hourly wage')
]

grouped = df_ont_hourly_salary_gender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.mean, np.std, np.size]))
print("The total number of this one is ",len(df_ont_hourly_salary_gender.index))

df_ont_salary_gender = df_ont_by_gender.loc[
    (df_ont_by_gender['Indicators'] == 'Average annual wages and salaries')
]

grouped = df_ont_salary_gender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.mean, np.std, np.size]))
print("The total number of this one is ",len(df_ont_salary_gender.index))

# By average annual hours worked in education level
df_ont_hourly_salary_education = df_ont_education.loc[
    (df_ont_education['Indicators'] == 'Average hourly wage')
]

grouped = df_ont_hourly_salary_education.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.mean, np.std, np.size]))
print("The total number of this one is ",len(df_ont_hourly_salary_education.index))

df_ont_salary_education = df_ont_education.loc[
    (df_ont_education['Indicators'] == 'Average annual wages and salaries')
]

grouped = df_ont_salary_education.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.mean, np.std, np.size]))
print("The total number of this one is ",len(df_ont_salary_education.index))

# By average annual hours worked in immigrant group
df_ont_hourly_salary_immigrant = df_ont_immigrant.loc[
    (df_ont_immigrant['Indicators'] == 'Average hourly wage')
]

grouped = df_ont_hourly_salary_immigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.mean, np.std, np.size]))
print("The total number of this one is ",len(df_ont_hourly_salary_immigrant.index))

df_ont_salary_immigrant = df_ont_immigrant.loc[
    (df_ont_immigrant['Indicators'] == 'Average annual wages and salaries')
]

grouped = df_ont_salary_immigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.mean, np.std, np.size]))
print("The total number of this one is ",len(df_ont_salary_immigrant.index))

# By number of the jobs in age group
print("By number of jobs available")
df_ont_num_jobs_age = df_ont_by_age.loc[df_ontario['Indicators'] == 'Number of jobs']
grouped = df_ont_num_jobs_age.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.mean, np.std, np.size]))
print("The total number of this one is ",len(df_ont_num_jobs_age.index))

# By number of the jobs in gender group
df_ont_num_jobs_gender = df_ont_by_gender.loc[df_ontario['Indicators'] == 'Number of jobs']
grouped = df_ont_num_jobs_gender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.mean, np.std, np.size]))
print("The total number of this one is ",len(df_ont_num_jobs_gender.index))

# By number of the jobs in number of the education
df_ont_num_jobs_education = df_ont_education.loc[df_ontario['Indicators'] == 'Number of jobs']
grouped = df_ont_num_jobs_education.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.mean, np.std, np.size]))
print("The total number of this one is ",len(df_ont_num_jobs_education.index))

# By number of the jobs in immigration status
df_ont_num_jobs_immigrant = df_ont_immigrant.loc[df_ontario['Indicators'] == 'Number of jobs']
grouped = df_ont_num_jobs_immigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.mean, np.std, np.size]))
print("The total number of this one is ",len(df_ont_num_jobs_immigrant.index))

# Resources #
# https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html
# https://datatofish.com/select-rows-pandas-dataframe/
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html
# https://sparkbyexamples.com/pandas/pandas-groupby-count-examples/
