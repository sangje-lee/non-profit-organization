# %% [markdown]
# ## Data analysis for employment in non-profit organization

# %% [markdown]
# Divided by four datasets instead of two datasets and then later into another two datasets.

# %% [markdown]
# Import all requirement,

# %%
import pandas as pd
import numpy as np
import ydata_profiling as pp  
from ydata_profiling import ProfileReport 
import warnings
import os

warnings.filterwarnings('ignore')

# %% [markdown]
# Import unemployment dataset.

# %%
df = pd.read_csv('36100651.csv')

print(df.info())
print(df.head(10))

# %% [markdown]
# Filter only the essential columns of the original dataset.

# %%
print("Grab the only the essential part of database.")

# From the original, 
# DGUID, UOM_ID, SCALAR_ID, VECTOR, COORDINATE, STATUS, SYMBOL, TERMINATED, and DECIMALS columns are removed.

df_sorted = df[['REF_DATE','GEO','Sector','Characteristics','Indicators','UOM','SCALAR_FACTOR','VALUE']]

print(df_sorted.head(20))
print(df_sorted.info())

print("Sort by Characteristics")
grouped = df_sorted.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.size]))

print("Sort by Indicator")
grouped = df_sorted.groupby(['Indicators'])
print(grouped['VALUE'].agg([np.size]))


# %% [markdown]
# Check for the missing value from the sorted dataset done above.
# * Notice there is missing value in this dataset.

# %%
print("Original database null counter")
print(df.isnull().sum())
print("\n Modified dataset null counter.")
print(df_sorted.isnull().sum())

# %% [markdown]
# Dropping missing value from the sorted dataset.

# %%
df_sorted_na = df_sorted.dropna()

# %% [markdown]
# Check now if there's still a missing data inside modified sorted dataset done above.

# %%
print("Modified dataset modification after removing missing value and it's total counter")
print(df_sorted_na.isnull().sum())
# print(df_sorted_na.head(20))

print(df_sorted_na.info())
grouped = df_sorted_na.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.size]))

grouped = df_sorted_na.groupby(['Indicators'])
print(grouped['VALUE'].agg([np.size]))

# %% [markdown]
# Panda Profiling for original dataset (CSV file),

# %%
# https://medium.com/analytics-vidhya/pandas-profiling-5ecd0b977ecd

pp = ProfileReport(df, title="Pandas Profiling Report")
pp_df = pp.to_html()

f = open("df_NoMod.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

# %% [markdown]
# Panda Profiling for sorted dataset,

# %%
pp_sorted = ProfileReport(df_sorted, title="Pandas Profiling Report with Columns Sorted")
pp_df_sorted = pp_sorted.to_html()

f = open("df_Sorted.html", "a") # Expert modifying data into html file.
f.write(pp_df_sorted)
f.close()

# %% [markdown]
# Panda Profiling for modified sorted dataset (missing data removed),

# %%
pp = ProfileReport(df_sorted_na, title="Pandas Profiling Report with Columned Sorted and NA Removed")
pp_df_sorted = pp.to_html()

f = open("df_Sorted-no-na.html", "a") # Expert modifying data into html file.
f.write(pp_df_sorted)
f.close()

# %%
# Differences should be, there will be less data to work on.
# Particularly business non-profit organizations and community organizations haven't given more accurate data (more missing values).

# %% [markdown]
# Next step, I will filtered the dataset by all the 'Indicators' given below. All of them done with modified sorted dataset (filtered missing value)
# * Notice there will be seven indicators data inside.
# * Notice there will be divided by seven datasets based on indicators.

# %%
# All columns
print(df_sorted_na.info())

# All indicators
grouped = df_sorted_na.groupby(['Indicators'])
print(grouped['VALUE'].agg([np.size]))

# %% [markdown]
# Average annual hours worked from modified sorted dataset.

# %%
# Average annual hours worked        15120
print("\nAverage annual hours worked")
df_AvgAnnHrsWrk = df_sorted_na.loc[
    (df_sorted_na['Indicators'] == 'Average annual hours worked')
]
# grouped = df_AvgAnnHrsWrk.groupby(['GEO'])
grouped = df_AvgAnnHrsWrk.groupby(['Indicators'])
print(grouped['VALUE'].agg([np.sum, np.mean, np.std, np.size]))
print("The total number of this one is ",len(df_AvgAnnHrsWrk.index))

# %% [markdown]
# Panda Profiling only for "Average annual hours worked"

# %%
pp = ProfileReport(df_AvgAnnHrsWrk, title="Average annual hours worked")
pp_df = pp.to_html()

f = open("Average annual hours worked.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

# %% [markdown]
# Average annual wages and salaries from modified sorted dataset. (Mention above)

# %%
# Average annual wages and salaries  15120
print("\nAverage annual wages and salaries")
df_AvgAnnWages = df_sorted_na.loc[
    (df_sorted_na['Indicators'] == 'Average annual wages and salaries')
]
grouped = df_AvgAnnWages.groupby(['Indicators'])
print(grouped['VALUE'].agg([np.sum, np.mean, np.std, np.size]))
print("The total number of this one is ",len(df_AvgAnnWages.index))

# %% [markdown]
# Panda Profiling only for "Average annual wages and salaries"

# %%
pp = ProfileReport(df_AvgAnnWages, title="Average annual wages and salaries")
pp_df = pp.to_html()

f = open("Average annual wages and salaries.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

# %% [markdown]
# Average hourly wage from modified sorted dataset. (Mentions above)

# %%
# Average hourly wage                15120
print("\nAverage hourly wage")
df_AvgHrsWages = df_sorted_na.loc[
    (df_sorted_na['Indicators'] == 'Average hourly wage')
]
grouped = df_AvgHrsWages.groupby(['Indicators'])
print(grouped['VALUE'].agg([np.sum, np.mean, np.std, np.size]))
print("The total number of this one is ",len(df_AvgHrsWages.index))

# %% [markdown]
# Panda Profiling only for "Average hourly wages"

# %%
pp = ProfileReport(df_AvgHrsWages, title="Average hourly wage")
pp_df = pp.to_html()

f = open("Average hourly wages.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

# %% [markdown]
# Average weekly hours worked from modified sorted dataset.

# %%
# Average weekly hours worked        15120
print("\nAverage weekly hours worked")
df_AvgWeekHrsWrked = df_sorted_na.loc[
    (df_sorted_na['Indicators'] == 'Average weekly hours worked')
]
grouped = df_AvgWeekHrsWrked.groupby(['Indicators'])
print(grouped['VALUE'].agg([np.sum, np.mean, np.std, np.size]))
print("The total number of this one is ",len(df_AvgWeekHrsWrked.index))

# %% [markdown]
# Panda Profiling only for "Average weekly hours worked"

# %%
pp = ProfileReport(df_AvgWeekHrsWrked, title="Average weekly hours worked")
pp_df = pp.to_html()

f = open("Average weekly hours worked.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

# %% [markdown]
# Hours worked from modified sorted dataset.
# * Notice, Skewed left.

# %%
# Hours worked                       15120
print("\nHours worked")
df_Hrs_Wrked = df_sorted_na.loc[
    (df_sorted_na['Indicators'] == 'Hours worked')
]
grouped = df_Hrs_Wrked.groupby(['Indicators'])
print(grouped['VALUE'].agg([np.sum, np.mean, np.std, np.size]))
print(grouped['VALUE'].agg([np.amin, np.amax]))
print("The total number of this one is ",len(df_Hrs_Wrked.index))

# %% [markdown]
# Panda Profiling only for "Hours worked" (Skewed left, noticed)

# %%
pp = ProfileReport(df_Hrs_Wrked, title="Hours Worked")
pp_df = pp.to_html()

f = open("Hours worked.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

# %% [markdown]
# Number of jobs from modified sorted dataset.
# * Notice, skewed left.

# %%
# Number of jobs                     15120
print("\nNumber of jobs")
df_NumOfJob = df_sorted_na.loc[
    (df_sorted_na['Indicators'] == 'Number of jobs')
]
grouped = df_NumOfJob.groupby(['Indicators'])
print(grouped['VALUE'].agg([np.sum, np.mean, np.std, np.size]))
print(grouped['VALUE'].agg([np.amin, np.amax]))
print("The total number of this one is ",len(df_NumOfJob.index))

# %% [markdown]
# Panda Profiling only for "Number of the jobs" (Stewed toward left)

# %%
pp = ProfileReport(df_NumOfJob, title="Number of jobs")
pp_df = pp.to_html()

f = open("Number of jobs.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

# %% [markdown]
# Wages and salaries from modified sorted dataset.
# 
# * Noticed skewed left.

# %%
# Wages and salaries                 15120
print("\nWages and salaries")
df_WagesAndSalaries = df_sorted_na.loc[
    (df_sorted_na['Indicators'] == 'Wages and salaries')
]
grouped = df_WagesAndSalaries.groupby(['Indicators'])
print(grouped['VALUE'].agg([np.sum, np.mean, np.std, np.size]))
print(grouped['VALUE'].agg([np.amin, np.amax]))
print("The total number of this one is ",len(df_WagesAndSalaries.index))

# %% [markdown]
# Panda Profiling only for "Wages and salaries" (Strewed toward left)

# %%
pp = ProfileReport(df_WagesAndSalaries, title="Wages and Salaries")
pp_df = pp.to_html()

f = open("Wages and salaries.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

# %% [markdown]
# For next step, I will divide each Indicators dataset into three different datasets.<br />
# They are 2013-2015, 2016-2018, 2019-2021.<br />
# I have dataset prepared before 2010-2012. However, it will not be used after this section, there's too much to analysis to do.<br />
# It will also demonstrate here why.
# Originally, I used divide dataset into 2016-2017, 2018-2019, and 2020-2021 from dataset that was divided from 2016 and up.

# %%
print("There are seven Indicators to analysis,")
grouped = df_sorted_na.groupby('Indicators')
print(grouped['VALUE'].agg([np.size]))

print("\nThe data inside between 2010-2013, there's are # number of data and I will be repeating this seven more time.,")
df_Avg_Sample = df_AvgAnnHrsWrk.loc[
    (df_AvgAnnHrsWrk['REF_DATE'] == 2010) |
    (df_AvgAnnHrsWrk['REF_DATE'] == 2011) |
    (df_AvgAnnHrsWrk['REF_DATE'] == 2012)
]

grouped = df_Avg_Sample.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.size]))

print("\nTo data inside above 2013 and split into three datasets, I need to repeat this analysis for "+str(7*3)+" (7x3) times.")
print("\nThis is also total of spliting into "+str(7*3)+" datasets.")

df_Avg_Sample_2013 = df_AvgAnnHrsWrk.loc[
    (df_AvgAnnHrsWrk['REF_DATE'] == 2013) |
    (df_AvgAnnHrsWrk['REF_DATE'] == 2014) |
    (df_AvgAnnHrsWrk['REF_DATE'] == 2015)
]

df_Avg_Sample_2016 = df_AvgAnnHrsWrk.loc[
    (df_AvgAnnHrsWrk['REF_DATE'] == 2016) |
    (df_AvgAnnHrsWrk['REF_DATE'] == 2017) |
    (df_AvgAnnHrsWrk['REF_DATE'] == 2018)
]

df_Avg_Sample_2019 = df_AvgAnnHrsWrk.loc[
    (df_AvgAnnHrsWrk['REF_DATE'] == 2019) |
    (df_AvgAnnHrsWrk['REF_DATE'] == 2020) |
    (df_AvgAnnHrsWrk['REF_DATE'] == 2021)
]

grouped = df_Avg_Sample_2013.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.size]))

grouped = df_Avg_Sample_2016.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.size]))

grouped = df_Avg_Sample_2019.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.size]))

# %% [markdown]
# Grabbing the year (REF_DATE) from 2010, 2013, 2016, 2018, and 2019 individually for "Average annual hours worked".

# %%
# 2010-2012
df_AvgAnnHrsWrk_2010 = df_AvgAnnHrsWrk.loc[
    (df_AvgAnnHrsWrk['REF_DATE'] == 2010) |
    (df_AvgAnnHrsWrk['REF_DATE'] == 2011) |
    (df_AvgAnnHrsWrk['REF_DATE'] == 2012)
]

grouped = df_AvgAnnHrsWrk_2010.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

# %%
print("Grabbing the data from 2013, 2016, and 2019.")

# 2013 - 2015
df_AvgAnnHrsWrk_2013 = df_AvgAnnHrsWrk.loc[
    (df_AvgAnnHrsWrk['REF_DATE'] == 2013) |
    (df_AvgAnnHrsWrk['REF_DATE'] == 2014) |
    (df_AvgAnnHrsWrk['REF_DATE'] == 2015)
]

# 2016 - 2018
df_AvgAnnHrsWrk_2016 = df_AvgAnnHrsWrk.loc[
    (df_AvgAnnHrsWrk['REF_DATE'] == 2016) |
    (df_AvgAnnHrsWrk['REF_DATE'] == 2017) |
    (df_AvgAnnHrsWrk['REF_DATE'] == 2018)
]

# 20109- 2021
df_AvgAnnHrsWrk_2019 = df_AvgAnnHrsWrk.loc[
    (df_AvgAnnHrsWrk['REF_DATE'] == 2019) |
    (df_AvgAnnHrsWrk['REF_DATE'] == 2020) |
    (df_AvgAnnHrsWrk['REF_DATE'] == 2021)
]

grouped = df_AvgAnnHrsWrk_2013.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

grouped = df_AvgAnnHrsWrk_2016.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

grouped = df_AvgAnnHrsWrk_2019.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

# %% [markdown]
# Panda Profiling for year 2016, 2018, and 2020 for "Average annual hours worked".

# %%
# 2016-2017
pp = ProfileReport(df_AvgAnnHrsWrk_2013, title="Average annual hours worked 2013")
pp_df = pp.to_html()

f = open("Average annual hours worked 2016.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

# 2017 - 2019
pp = ProfileReport(df_AvgAnnHrsWrk_2016, title="Average annual hours worked 2016")
pp_df = pp.to_html()

f = open("Average annual hours worked 2018.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

# 2020 - 2021
pp = ProfileReport(df_AvgAnnHrsWrk_2019, title="Average annual hours worked 2019")
pp_df = pp.to_html()

f = open("Average annual hours worked 2020.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

# %% [markdown]
# Grabbing the year (REF_DATE) from 2010, 2013, 2016, and 2019 individually for "Average annual wages and salaries".

# %%
# 2010 - 2012
df_AvgAnnWages_2010 = df_AvgAnnWages.loc[
    (df_AvgAnnWages['REF_DATE'] == 2010) |
    (df_AvgAnnWages['REF_DATE'] == 2011) |
    (df_AvgAnnWages['REF_DATE'] == 2012)
]

grouped = df_AvgAnnWages_2010.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

# %%
print("Grabbing the data from 2017, 2019, and 2021.")

# 2013 - 2015
df_AvgAnnWages_2013 = df_AvgAnnWages.loc[
    (df_AvgAnnWages['REF_DATE'] == 2013) |
    (df_AvgAnnWages['REF_DATE'] == 2014) |
    (df_AvgAnnWages['REF_DATE'] == 2015)
]

# 2016 - 2018
df_AvgAnnWages_2016 = df_AvgAnnWages.loc[
    (df_AvgAnnWages['REF_DATE'] == 2016) |
    (df_AvgAnnWages['REF_DATE'] == 2017) |
    (df_AvgAnnWages['REF_DATE'] == 2018)
]

# 2019 - 2021
df_AvgAnnWages_2019 = df_AvgAnnWages.loc[
    (df_AvgAnnWages['REF_DATE'] == 2019) |
    (df_AvgAnnWages['REF_DATE'] == 2020) |
    (df_AvgAnnWages['REF_DATE'] == 2021)
]

grouped = df_AvgAnnWages_2013.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

grouped = df_AvgAnnWages_2016.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

grouped = df_AvgAnnWages_2019.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

# %% [markdown]
# Panda Profiling for year 2013, 2016, and 2019 for "Average annual wages and salaries".

# %%
pp = ProfileReport(df_AvgAnnWages_2013, title="Average annual wages and salaries 2013")
pp_df = pp.to_html()

f = open("Average annual wages and salaries 2013.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

pp = ProfileReport(df_AvgAnnWages_2016, title="Average annual wages and salaries 2016")
pp_df = pp.to_html()

f = open("Average annual wages and salaries 2016.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

pp = ProfileReport(df_AvgAnnWages_2019, title="Average annual wages and salaries 2019")
pp_df = pp.to_html()

f = open("Average annual wages and salaries 2019.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

# %% [markdown]
# Grabbing the year (REF_DATE) from 2010, 2013, 2016, and 2019 individually for "Average hourly wages".

# %%
# 2010 - 2012
df_AvgHrsWages_2010 = df_AvgHrsWages.loc[
    (df_AvgHrsWages['REF_DATE'] == 2010) |
    (df_AvgHrsWages['REF_DATE'] == 2011) |
    (df_AvgHrsWages['REF_DATE'] == 2012)
]

grouped = df_AvgHrsWages_2010.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

# %%
print("Grabbing the data from 2013, 2016, and 2019.")

# 2013 - 2015
df_AvgHrsWages_2013 = df_AvgHrsWages.loc[
    (df_AvgHrsWages['REF_DATE'] == 2013) |
    (df_AvgHrsWages['REF_DATE'] == 2014) |
    (df_AvgHrsWages['REF_DATE'] == 2015)
]

# 2016 - 2018
df_AvgHrsWages_2016 = df_AvgHrsWages.loc[
    (df_AvgHrsWages['REF_DATE'] == 2016) |
    (df_AvgHrsWages['REF_DATE'] == 2017) |
    (df_AvgHrsWages['REF_DATE'] == 2018)
]

# 2019 - 2021
df_AvgHrsWages_2019 = df_AvgHrsWages.loc[
    (df_AvgHrsWages['REF_DATE'] == 2019) |
    (df_AvgHrsWages['REF_DATE'] == 2020) |
    (df_AvgHrsWages['REF_DATE'] == 2021)
]

grouped = df_AvgHrsWages_2013.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

grouped = df_AvgHrsWages_2016.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

grouped = df_AvgHrsWages_2019.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

# %% [markdown]
# Panda Profiling for year 2013, 2016, and 2019 for "Average hourly wages".

# %%
pp = ProfileReport(df_AvgHrsWages_2013, title="Average hourly wage 2013")
pp_df = pp.to_html()

f = open("Average hourly wages 2013.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

pp = ProfileReport(df_AvgHrsWages_2016, title="Average hourly wage 2016")
pp_df = pp.to_html()

f = open("Average hourly wages 2016.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

pp = ProfileReport(df_AvgHrsWages_2019, title="Average hourly wage 2019")
pp_df = pp.to_html()

f = open("Average hourly wages 2019.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

# %% [markdown]
# Grabbing the year (REF_DATE) from 2010, 2013, 2016, and 2019 individually for "Average weekly hours worked".

# %%
# 2010 - 2012
df_AvgWeekHrsWrked_2010 = df_AvgWeekHrsWrked.loc[
    (df_AvgWeekHrsWrked['REF_DATE'] == 2010) |
    (df_AvgWeekHrsWrked['REF_DATE'] == 2011) |
    (df_AvgWeekHrsWrked['REF_DATE'] == 2012)
]

grouped = df_AvgWeekHrsWrked_2010.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

# %%
print("Grabbing the data from 2013, 2016, and 2019.")

# 2013 - 2015
df_AvgWeekHrsWrked_2013 = df_AvgWeekHrsWrked.loc[
    (df_AvgWeekHrsWrked['REF_DATE'] == 2013) |
    (df_AvgWeekHrsWrked['REF_DATE'] == 2014) |
    (df_AvgWeekHrsWrked['REF_DATE'] == 2015)
]

# 2016 - 2018
df_AvgWeekHrsWrked_2016 = df_AvgWeekHrsWrked.loc[
    (df_AvgWeekHrsWrked['REF_DATE'] == 2016) |
    (df_AvgWeekHrsWrked['REF_DATE'] == 2017) |
    (df_AvgWeekHrsWrked['REF_DATE'] == 2018)
]

# 2019 - 2021
df_AvgWeekHrsWrked_2019 = df_AvgWeekHrsWrked.loc[
    (df_AvgWeekHrsWrked['REF_DATE'] == 2019) |
    (df_AvgWeekHrsWrked['REF_DATE'] == 2020) |
    (df_AvgWeekHrsWrked['REF_DATE'] == 2021)
]

grouped = df_AvgWeekHrsWrked_2013.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

grouped = df_AvgWeekHrsWrked_2016.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

grouped = df_AvgWeekHrsWrked_2019.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

# %% [markdown]
# Panda Profiling for year 2013, 2016, and 2019 for "Average weekly hours worked".

# %%
pp = ProfileReport(df_AvgWeekHrsWrked_2013, title="Average weekly hours worked 2013")
pp_df = pp.to_html()

f = open("Average weekly hours worked 2013.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

pp = ProfileReport(df_AvgWeekHrsWrked_2016, title="Average weekly hours worked 2016")
pp_df = pp.to_html()

f = open("Average weekly hours worked 2016.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

pp = ProfileReport(df_AvgWeekHrsWrked_2019, title="Average weekly hours worked 2019")
pp_df = pp.to_html()

f = open("Average weekly hours worked 2019.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

# %% [markdown]
# Grabbing the year (REF_DATE) from 2010, 2013, 2016, and 2019 individually for "hours worked".

# %%
# 2010 - 2012
df_Hrs_Wrked_2010 = df_Hrs_Wrked.loc[
    (df_Hrs_Wrked['REF_DATE'] == 2010) |
    (df_Hrs_Wrked['REF_DATE'] == 2011) |
    (df_Hrs_Wrked['REF_DATE'] == 2012)
]

grouped = df_Hrs_Wrked_2010.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

# %%
print("Grabbing the data from 2013, 2016, and 2019.")

# 2013 - 2015
df_Hrs_Wrked_2013 = df_Hrs_Wrked.loc[
    (df_Hrs_Wrked['REF_DATE'] == 2013) |
    (df_Hrs_Wrked['REF_DATE'] == 2014) |
    (df_Hrs_Wrked['REF_DATE'] == 2015)
]

# 2016 - 2018
df_Hrs_Wrked_2016 = df_Hrs_Wrked.loc[
    (df_Hrs_Wrked['REF_DATE'] == 2016) |
    (df_Hrs_Wrked['REF_DATE'] == 2017) |
    (df_Hrs_Wrked['REF_DATE'] == 2018)
]

# 2019 - 2021
df_Hrs_Wrked_2019 = df_Hrs_Wrked.loc[
    (df_Hrs_Wrked['REF_DATE'] == 2019) |
    (df_Hrs_Wrked['REF_DATE'] == 2020) |
    (df_Hrs_Wrked['REF_DATE'] == 2021)
]

grouped = df_Hrs_Wrked_2013.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

grouped = df_Hrs_Wrked_2016.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

grouped = df_Hrs_Wrked_2019.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

# %% [markdown]
# Panda Profiling for year 2013, 2016, and 2019 for "hours worked".

# %%
pp = ProfileReport(df_Hrs_Wrked_2013, title="Hours Worked 2013")
pp_df = pp.to_html()

f = open("Hours worked 2013.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

pp = ProfileReport(df_Hrs_Wrked_2016, title="Hours Worked 2016")
pp_df = pp.to_html()

f = open("Hours worked 2016.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

pp = ProfileReport(df_Hrs_Wrked_2019, title="Hours Worked 2019")
pp_df = pp.to_html()

f = open("Hours worked 2019.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

# %% [markdown]
# Grabbing the year (REF_DATE) from 2010, 2013, 2016, and 2019 individually for "Number of jobs".

# %%
# 2010 - 2012
df_NumOfJob_2010 = df_NumOfJob.loc[
    (df_NumOfJob['REF_DATE'] == 2010) |
    (df_NumOfJob['REF_DATE'] == 2011) |
    (df_NumOfJob['REF_DATE'] == 2012)
]

grouped = df_NumOfJob_2010.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

# %%
print("Grabbing the data from 2013, 2016, and 2019.")

# 2013 - 2015
df_NumOfJob_2013 = df_NumOfJob.loc[
    (df_NumOfJob['REF_DATE'] == 2013) |
    (df_NumOfJob['REF_DATE'] == 2014) |
    (df_NumOfJob['REF_DATE'] == 2015)
]

# 2016 - 2018
df_NumOfJob_2016 = df_NumOfJob.loc[
    (df_NumOfJob['REF_DATE'] == 2016) |
    (df_NumOfJob['REF_DATE'] == 2017) |
    (df_NumOfJob['REF_DATE'] == 2018)
]

# 2019 - 2021
df_NumOfJob_2019 = df_NumOfJob.loc[
    (df_NumOfJob['REF_DATE'] == 2019) |
    (df_NumOfJob['REF_DATE'] == 2020) |
    (df_NumOfJob['REF_DATE'] == 2021)
]

grouped = df_NumOfJob_2013.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

grouped = df_NumOfJob_2016.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

grouped = df_NumOfJob_2019.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

# %% [markdown]
# Panda Profiling for year 2013, 2016, and 2019for "Number of jobs".

# %%
pp = ProfileReport(df_NumOfJob_2013, title="Number of jobs 2013")
pp_df = pp.to_html()

f = open("Number of jobs 2013.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

pp = ProfileReport(df_NumOfJob_2016, title="Number of jobs 2016")
pp_df = pp.to_html()

f = open("Number of jobs 2016.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

pp = ProfileReport(df_NumOfJob_2019, title="Number of jobs 2019")
pp_df = pp.to_html()

f = open("Number of jobs 2019.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

# %% [markdown]
# Grabbing the year (REF_DATE) from 2010, 2013, 2016, and 2019 individually for "Wages and Salaries".

# %%
# 2010 - 2012
df_WagesAndSalaries_2010 = df_WagesAndSalaries.loc[
    (df_WagesAndSalaries['REF_DATE'] == 2010) |
    (df_WagesAndSalaries['REF_DATE'] == 2011) |
    (df_WagesAndSalaries['REF_DATE'] == 2012)
]

grouped = df_WagesAndSalaries_2010.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

# %%
print("Grabbing the data from 2013, 2016, and 2019.")

# 2013 - 2015
df_WagesAndSalaries_2013 = df_WagesAndSalaries.loc[
    (df_WagesAndSalaries['REF_DATE'] == 2013) |
    (df_WagesAndSalaries['REF_DATE'] == 2014) |
    (df_WagesAndSalaries['REF_DATE'] == 2015)
]

# 2016 - 2018
df_WagesAndSalaries_2016 = df_WagesAndSalaries.loc[
    (df_WagesAndSalaries['REF_DATE'] == 2016) |
    (df_WagesAndSalaries['REF_DATE'] == 2017) |
    (df_WagesAndSalaries['REF_DATE'] == 2018)
]

# 2019 - 2021
df_WagesAndSalaries_2019 = df_WagesAndSalaries.loc[
    (df_WagesAndSalaries['REF_DATE'] == 2019) |
    (df_WagesAndSalaries['REF_DATE'] == 2020) |
    (df_WagesAndSalaries['REF_DATE'] == 2021)
]

grouped = df_WagesAndSalaries_2013.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

grouped = df_WagesAndSalaries_2016.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

grouped = df_WagesAndSalaries_2019.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

# %% [markdown]
# Panda Profiling for year 2013, 2016, and 2019 for "Wages and Salaries".

# %%
pp = ProfileReport(df_WagesAndSalaries_2013, title="Wages and Salaries 2013")
pp_df = pp.to_html()

f = open("Wages and Salaries 2013.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

pp = ProfileReport(df_WagesAndSalaries_2016, title="Wages and Salaries 2016")
pp_df = pp.to_html()

f = open("Wages and Salaries 2016.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

pp = ProfileReport(df_WagesAndSalaries_2019, title="Wages and Salaries 2019")
pp_df = pp.to_html()

f = open("Wages and Salaries 2019.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

# %% [markdown]
# For next step, I will filtered it by the following group, "age group", "gender level", "education level", "immigrant level" and "Aboriginal status".
# * I have comment, analysis of whole dataset, 2010-2013 (originally, before 2016).
# * I have analysis two training and testing set. (2013-2015), (2016-2018), (2019-2021)
# * There's also other characteristics there as well but I decided to drop them as well.

# %% [markdown]
# Filtered for "Average annual hours worked" by following: "Age group", "Gender level", "Education level", and "Immigration status".<br />
# "Aboriginal status" has been commented.

# %%
# Dataset year in 2010 inside Average Annual Hours Worked

# print("\nAge group in Alberta")
# df_AvgAnnHrsWrk_2010_ByAge = df_AvgAnnHrsWrk_2010.loc[
#     (df_AvgAnnHrsWrk_2010['Characteristics'] == '15 to 24 years') |
#     (df_AvgAnnHrsWrk_2010['Characteristics'] == '25 to 34 years') |
#     (df_AvgAnnHrsWrk_2010['Characteristics'] == '35 to 44 years') |
#     (df_AvgAnnHrsWrk_2010['Characteristics'] == '45 to 54 years') |
#     (df_AvgAnnHrsWrk_2010['Characteristics'] == '55 to 64 years') |
#     (df_AvgAnnHrsWrk_2010['Characteristics'] == '65 years old and over')]
# # print(df_AvgAnnHrsWrk_2010_ByAge.head(20))
# grouped = df_AvgAnnHrsWrk_2010_ByAge.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("Total size : ",len(df_AvgAnnHrsWrk_2010_ByAge.index))

# print("\nGender group in Alberta")
# df_AvgAnnHrsWrk_2010_ByGender = df_AvgAnnHrsWrk_2010.loc[
#     (df_AvgAnnHrsWrk_2010['Characteristics'] == 'Female employees') |
#     (df_AvgAnnHrsWrk_2010['Characteristics'] == 'Male employees')
# ]
# # print(df_AvgAnnHrsWrk_2010_ByGender.head(20))
# grouped = df_AvgAnnHrsWrk_2010_ByGender.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("Total size : ",len(df_AvgAnnHrsWrk_2010_ByGender.index))

# print("\nEducation group in Alberta")
# df_AvgAnnHrsWrk_2010_ByEducation = df_AvgAnnHrsWrk_2010.loc[
#     (df_AvgAnnHrsWrk_2010['Characteristics'] == 'High school diploma and less') |
#     (df_AvgAnnHrsWrk_2010['Characteristics'] == 'Trade certificate') |
#     (df_AvgAnnHrsWrk_2010['Characteristics'] == 'University degree and higher')
# ]
# # print(df_AvgAnnHrsWrk_2010_ByEducation.head(20))
# grouped = df_AvgAnnHrsWrk_2010_ByEducation.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("Total size : ",len(df_AvgAnnHrsWrk_2010_ByEducation.index))

# print("\nImmigrant group in Alberta")
# df_AvgAnnHrsWrk_2010_ByImmigrant = df_AvgAnnHrsWrk_2010.loc[
#     (df_AvgAnnHrsWrk_2010['Characteristics'] == 'Immigrant employees') |
#     (df_AvgAnnHrsWrk_2010['Characteristics'] == 'Non-immigrant employees')
# ]
# # print(df_AvgAnnHrsWrk_2010_ByImmigrant.head(20))
# grouped = df_AvgAnnHrsWrk_2010_ByImmigrant.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("Total size : ",len(df_AvgAnnHrsWrk_2010_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgAnnHrkWrk_2010_ByIndigenous = df_AvgAnnHrsWrk_2010.loc[
#     (df_AvgAnnHrsWrk_2010['Characteristics'] == 'Indigenous identity employees') |
#     (df_AvgAnnHrsWrk_2010['Characteristics'] == 'Non-indigenous identity employees')
# ]
# print(df_AvgAnnHrkWrk_2010_ByIndigenous.head(20))
# # grouped = df_AvgAnnHrkWrk_2010_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnHrkWrk_2010_ByIndigenous.index))

# %%
# Dataset year in 2013 inside Average Annual Hours Worked

print("\nAge group in Alberta")
df_AvgAnnHrsWrk_2013_ByAge = df_AvgAnnHrsWrk_2013.loc[
    (df_AvgAnnHrsWrk_2013['Characteristics'] == '15 to 24 years') |
    (df_AvgAnnHrsWrk_2013['Characteristics'] == '25 to 34 years') |
    (df_AvgAnnHrsWrk_2013['Characteristics'] == '35 to 44 years') |
    (df_AvgAnnHrsWrk_2013['Characteristics'] == '45 to 54 years') |
    (df_AvgAnnHrsWrk_2013['Characteristics'] == '55 to 64 years') |
    (df_AvgAnnHrsWrk_2013['Characteristics'] == '65 years old and over')]
# print(df_AvgAnnHrsWrk_2013_ByAge.head(20))
grouped = df_AvgAnnHrsWrk_2013_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("Total size : ",len(df_AvgAnnHrsWrk_2013_ByAge.index))

print("\nGender group in Alberta")
df_AvgAnnHrsWrk_2013_ByGender = df_AvgAnnHrsWrk_2013.loc[
    (df_AvgAnnHrsWrk_2013['Characteristics'] == 'Female employees') |
    (df_AvgAnnHrsWrk_2013['Characteristics'] == 'Male employees')
]
# print(df_AvgAnnHrsWrk_2013_ByGender.head(20))
grouped = df_AvgAnnHrsWrk_2013_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("Total size : ",len(df_AvgAnnHrsWrk_2013_ByGender.index))

print("\nEducation group in Alberta")
df_AvgAnnHrsWrk_2013_ByEducation = df_AvgAnnHrsWrk_2013.loc[
    (df_AvgAnnHrsWrk_2013['Characteristics'] == 'High school diploma and less') |
    (df_AvgAnnHrsWrk_2013['Characteristics'] == 'Trade certificate') |
    (df_AvgAnnHrsWrk_2013['Characteristics'] == 'University degree and higher')
]
# print(df_AvgAnnHrsWrk_2013_ByEducation.head(20))
grouped = df_AvgAnnHrsWrk_2013_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("Total size : ",len(df_AvgAnnHrsWrk_2013_ByEducation.index))

print("\nImmigrant group in Alberta")
df_AvgAnnHrsWrk_2013_ByImmigrant = df_AvgAnnHrsWrk_2013.loc[
    (df_AvgAnnHrsWrk_2013['Characteristics'] == 'Immigrant employees') |
    (df_AvgAnnHrsWrk_2013['Characteristics'] == 'Non-immigrant employees')
]
# print(df_AvgAnnHrsWrk_2013_ByImmigrant.head(20))
grouped = df_AvgAnnHrsWrk_2013_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("Total size : ",len(df_AvgAnnHrsWrk_2013_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgAnnHrsWrk_2013_ByIndigenous = df_AvgAnnHrsWrk_2013.loc[
#     (df_AvgAnnHrsWrk_2013['Characteristics'] == 'Indigenous identity employees') |
#     (df_AvgAnnHrsWrk_2013['Characteristics'] == 'Non-indigenous identity employees')
# ]
# print(df_AvgAnnHrsWrk_2013_ByIndigenous.head(20))
# # grouped = df_AvgAnnHrsWrk_2013_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnHrsWrk_2013_ByIndigenous.index))

# %%
# Dataset year in 2016 inside Average Annual Hours Worked

print("\nAge group in Alberta")
df_AvgAnnHrsWrk_2016_ByAge = df_AvgAnnHrsWrk_2016.loc[
    (df_AvgAnnHrsWrk_2016['Characteristics'] == '15 to 24 years') |
    (df_AvgAnnHrsWrk_2016['Characteristics'] == '25 to 34 years') |
    (df_AvgAnnHrsWrk_2016['Characteristics'] == '35 to 44 years') |
    (df_AvgAnnHrsWrk_2016['Characteristics'] == '45 to 54 years') |
    (df_AvgAnnHrsWrk_2016['Characteristics'] == '55 to 64 years') |
    (df_AvgAnnHrsWrk_2016['Characteristics'] == '65 years old and over')]
# print(df_AvgAnnHrsWrk_2016_ByAge.head(20))
grouped = df_AvgAnnHrsWrk_2016_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("Total size : ",len(df_AvgAnnHrsWrk_2016_ByAge.index))

print("\nGender group in Alberta")
df_AvgAnnHrsWrk_2016_ByGender = df_AvgAnnHrsWrk_2016.loc[
    (df_AvgAnnHrsWrk_2016['Characteristics'] == 'Female employees') |
    (df_AvgAnnHrsWrk_2016['Characteristics'] == 'Male employees')
]
# print(df_AvgAnnHrsWrk_2016_ByGender.head(20))
grouped = df_AvgAnnHrsWrk_2016_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("Total size : ",len(df_AvgAnnHrsWrk_2016_ByGender.index))

print("\nEducation group in Alberta")
df_AvgAnnHrsWrk_2016_ByEducation = df_AvgAnnHrsWrk_2016.loc[
    (df_AvgAnnHrsWrk_2016['Characteristics'] == 'High school diploma and less') |
    (df_AvgAnnHrsWrk_2016['Characteristics'] == 'Trade certificate') |
    (df_AvgAnnHrsWrk_2016['Characteristics'] == 'University degree and higher')
]
# print(df_AvgAnnHrsWrk_2016_ByEducation.head(20))
grouped = df_AvgAnnHrsWrk_2016_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("Total size : ",len(df_AvgAnnHrsWrk_2016_ByEducation.index))

print("\nImmigrant group in Alberta")
df_AvgAnnHrsWrk_2016_ByImmigrant = df_AvgAnnHrsWrk_2016.loc[
    (df_AvgAnnHrsWrk_2016['Characteristics'] == 'Immigrant employees') |
    (df_AvgAnnHrsWrk_2016['Characteristics'] == 'Non-immigrant employees')
]
# print(df_AvgAnnHrsWrk_2016_ByImmigrant.head(20))
grouped = df_AvgAnnHrsWrk_2016_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("Total size : ",len(df_AvgAnnHrsWrk_2016_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgAnnHrsWrk_2016_ByIndigenous = df_AvgAnnHrsWrk_2016.loc[
#     (df_AvgAnnHrsWrk_2016['Characteristics'] == 'Indigenous identity employees') |
#     (df_AvgAnnHrsWrk_2016['Characteristics'] == 'Non-indigenous identity employees')
# ]
# print(df_AvgAnnHrsWrk_2016_ByIndigenous.head(20))
# # grouped = df_AvgAnnHrsWrk_2016_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnHrsWrk_2016_ByIndigenous.index))

# %%
# Dataset year in 2019 inside Average Annual Hours Worked

print("\nAge group in Alberta")
df_AvgAnnHrsWrk_2019_ByAge = df_AvgAnnHrsWrk_2019.loc[
    (df_AvgAnnHrsWrk_2019['Characteristics'] == '15 to 24 years') |
    (df_AvgAnnHrsWrk_2019['Characteristics'] == '25 to 34 years') |
    (df_AvgAnnHrsWrk_2019['Characteristics'] == '35 to 44 years') |
    (df_AvgAnnHrsWrk_2019['Characteristics'] == '45 to 54 years') |
    (df_AvgAnnHrsWrk_2019['Characteristics'] == '55 to 64 years') |
    (df_AvgAnnHrsWrk_2019['Characteristics'] == '65 years old and over')]
# print(df_AvgAnnHrsWrk_2019_ByAge.head(20))
grouped = df_AvgAnnHrsWrk_2019_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("Total size : ",len(df_AvgAnnHrsWrk_2019_ByAge.index))

print("\nGender group in Alberta")
df_AvgAnnHrsWrk_2019_ByGender = df_AvgAnnHrsWrk_2019.loc[
    (df_AvgAnnHrsWrk_2019['Characteristics'] == 'Female employees') |
    (df_AvgAnnHrsWrk_2019['Characteristics'] == 'Male employees')
]
# print(df_AvgAnnHrsWrk_2019_ByGender.head(20))
grouped = df_AvgAnnHrsWrk_2019_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("Total size : ",len(df_AvgAnnHrsWrk_2019_ByGender.index))

print("\nEducation group in Alberta")
df_AvgAnnHrsWrk_2019_ByEducation = df_AvgAnnHrsWrk_2019.loc[
    (df_AvgAnnHrsWrk_2019['Characteristics'] == 'High school diploma and less') |
    (df_AvgAnnHrsWrk_2019['Characteristics'] == 'Trade certificate') |
    (df_AvgAnnHrsWrk_2019['Characteristics'] == 'University degree and higher')
]
# print(df_AvgAnnHrsWrk_2019_ByEducation.head(20))
grouped = df_AvgAnnHrsWrk_2019_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("Total size : ",len(df_AvgAnnHrsWrk_2019_ByEducation.index))

print("\nImmigrant group in Alberta")
df_AvgAnnHrsWrk_2019_ByImmigrant = df_AvgAnnHrsWrk_2019.loc[
    (df_AvgAnnHrsWrk_2019['Characteristics'] == 'Immigrant employees') |
    (df_AvgAnnHrsWrk_2019['Characteristics'] == 'Non-immigrant employees')
]
# print(df_AvgAnnHrsWrk_2019_ByImmigrant.head(20))
grouped = df_AvgAnnHrsWrk_2019_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("Total size : ",len(df_AvgAnnHrsWrk_2019_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgAnnHrsWrk_2019_ByIndigenous = df_AvgAnnHrsWrk_2019.loc[
#     (df_AvgAnnHrsWrk_2019['Characteristics'] == 'Indigenous identity employees') |
#     (df_AvgAnnHrsWrk_2019['Characteristics'] == 'Non-indigenous identity employees')
# ]
# print(df_AvgAnnHrsWrk_2019_ByIndigenous.head(20))
# # grouped = df_AvgAnnHrkWrk_2010_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnHrsWrk_2019_ByIndigenous.index))

# %% [markdown]
# Filtered for "Average annual wages and salaries" by following: "Age group", "Gender level", "Education level", and "Immigration status".<br />
# "Aboriginal status" has been commented.

# %%
# # Dataset year in 2010 inside Average annual wages and salaries

# print("\nAge group in Alberta")
# df_AvgAnnWages_2010_ByAge = df_AvgAnnWages_2010.loc[
#     (df_AvgAnnWages_2010['Characteristics'] == '15 to 24 years') |
#     (df_AvgAnnWages_2010['Characteristics'] == '25 to 34 years') |
#     (df_AvgAnnWages_2010['Characteristics'] == '35 to 44 years') |
#     (df_AvgAnnWages_2010['Characteristics'] == '45 to 54 years') |
#     (df_AvgAnnWages_2010['Characteristics'] == '55 to 64 years') |
#     (df_AvgAnnWages_2010['Characteristics'] == '65 years old and over')]
# # print(df_AvgAnnWages_2010_ByAge.head(20))
# grouped = df_AvgAnnWages_2010_ByAge.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnWages_2010_ByAge.index))

# print("\nGender group in Alberta")
# df_AvgAnnWages_2010_ByGender = df_AvgAnnWages_2010.loc[
#     (df_AvgAnnWages_2010['Characteristics'] == 'Female employees') |
#     (df_AvgAnnWages_2010['Characteristics'] == 'Male employees')
# ]
# # print(df_AvgAnnWages_2010_ByGender.head(20))
# grouped = df_AvgAnnWages_2010_ByGender.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnWages_2010_ByGender.index))

# print("\nEducation group in Alberta")
# df_AvgAnnWages_2010_ByEducation = df_AvgAnnWages_2010.loc[
#     (df_AvgAnnWages_2010['Characteristics'] == 'High school diploma and less') |
#     (df_AvgAnnWages_2010['Characteristics'] == 'Trade certificate') |
#     (df_AvgAnnWages_2010['Characteristics'] == 'University degree and higher')
# ]
# # print(df_AvgAnnWages_2010_ByEducation.head(20))
# grouped = df_AvgAnnWages_2010_ByEducation.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnWages_2010_ByEducation.index))

# print("\nImmigrant group in Alberta")
# df_AvgAnnWages_2010_ByImmigrant = df_AvgAnnWages_2010.loc[
#     (df_AvgAnnWages_2010['Characteristics'] == 'Immigrant employees') |
#     (df_AvgAnnWages_2010['Characteristics'] == 'Non-immigrant employees')
# ]
# # print(df_AvgAnnWages_2010_ByImmigrant.head(20))
# grouped = df_AvgAnnWages_2010_ByImmigrant.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnWages_2010_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgAnnWages_2010_ByIndigenous = df_AvgAnnWages_2010.loc[
#     (df_AvgAnnWages_2010['Characteristics'] == 'Indigenous identity employees') |
#     (df_AvgAnnWages_2010['Characteristics'] == 'Non-indigenous identity employees')
# ]
# # print(df_AvgAnnHrk_ByIndigenous.head(20))
# grouped = df_AvgAnnWages_2010_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnWages_2010_ByIndigenous.index))

# %%
# Dataset year in 2013 inside Average annual wages and salaries

print("\nAge group in Alberta")
df_AvgAnnWages_2013_ByAge = df_AvgAnnWages_2013.loc[
    (df_AvgAnnWages_2013['Characteristics'] == '15 to 24 years') |
    (df_AvgAnnWages_2013['Characteristics'] == '25 to 34 years') |
    (df_AvgAnnWages_2013['Characteristics'] == '35 to 44 years') |
    (df_AvgAnnWages_2013['Characteristics'] == '45 to 54 years') |
    (df_AvgAnnWages_2013['Characteristics'] == '55 to 64 years') |
    (df_AvgAnnWages_2013['Characteristics'] == '65 years old and over')]
# print(df_AvgAnnWages_2013_ByAge.head(20))
grouped = df_AvgAnnWages_2013_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgAnnWages_2013_ByAge.index))

print("\nGender group in Alberta")
df_AvgAnnWages_2013_ByGender = df_AvgAnnWages_2013.loc[
    (df_AvgAnnWages_2013['Characteristics'] == 'Female employees') |
    (df_AvgAnnWages_2013['Characteristics'] == 'Male employees')
]
# print(df_AvgAnnWages_2013_ByGender.head(20))
grouped = df_AvgAnnWages_2013_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgAnnWages_2013_ByGender.index))

print("\nEducation group in Alberta")
df_AvgAnnWages_2013_ByEducation = df_AvgAnnWages_2013.loc[
    (df_AvgAnnWages_2013['Characteristics'] == 'High school diploma and less') |
    (df_AvgAnnWages_2013['Characteristics'] == 'Trade certificate') |
    (df_AvgAnnWages_2013['Characteristics'] == 'University degree and higher')
]
# print(df_AvgAnnWages_2013_ByEducation.head(20))
grouped = df_AvgAnnWages_2013_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgAnnWages_2013_ByEducation.index))

print("\nImmigrant group in Alberta")
df_AvgAnnWages_2013_ByImmigrant = df_AvgAnnWages_2013.loc[
    (df_AvgAnnWages_2013['Characteristics'] == 'Immigrant employees') |
    (df_AvgAnnWages_2013['Characteristics'] == 'Non-immigrant employees')
]
# print(df_AvgAnnWages_2013_ByImmigrant.head(20))
grouped = df_AvgAnnWages_2013_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgAnnWages_2013_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgAnnWages_2013_ByIndigenous = df_AvgAnnWages_2013.loc[
#     (df_AvgAnnWages_2013['Characteristics'] == 'Indigenous identity employees') |
#     (df_AvgAnnWages_2013['Characteristics'] == 'Non-indigenous identity employees')
# ]
# # print(df_AvgAnnHrk_ByIndigenous.head(20))
# grouped = df_AvgAnnWages_2013_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnWages_2013_ByIndigenous.index))

# %%
# Dataset year in 2016 inside Average annual wages and salaries

print("\nAge group in Alberta")
df_AvgAnnWages_2016_ByAge = df_AvgAnnWages_2016.loc[
    (df_AvgAnnWages_2016['Characteristics'] == '15 to 24 years') |
    (df_AvgAnnWages_2016['Characteristics'] == '25 to 34 years') |
    (df_AvgAnnWages_2016['Characteristics'] == '35 to 44 years') |
    (df_AvgAnnWages_2016['Characteristics'] == '45 to 54 years') |
    (df_AvgAnnWages_2016['Characteristics'] == '55 to 64 years') |
    (df_AvgAnnWages_2016['Characteristics'] == '65 years old and over')]
# print(df_AvgAnnWages_2016_ByAge.head(20))
grouped = df_AvgAnnWages_2016_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgAnnWages_2016_ByAge.index))

print("\nGender group in Alberta")
df_AvgAnnWages_2016_ByGender = df_AvgAnnWages_2016.loc[
    (df_AvgAnnWages_2016['Characteristics'] == 'Female employees') |
    (df_AvgAnnWages_2016['Characteristics'] == 'Male employees')
]
# print(df_AvgAnnWages_2016_ByGender.head(20))
grouped = df_AvgAnnWages_2016_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgAnnWages_2016_ByGender.index))

print("\nEducation group in Alberta")
df_AvgAnnWages_2016_ByEducation = df_AvgAnnWages_2016.loc[
    (df_AvgAnnWages_2016['Characteristics'] == 'High school diploma and less') |
    (df_AvgAnnWages_2016['Characteristics'] == 'Trade certificate') |
    (df_AvgAnnWages_2016['Characteristics'] == 'University degree and higher')
]
# print(df_AvgAnnWages_2016_ByEducation.head(20))
grouped = df_AvgAnnWages_2016_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgAnnWages_2016_ByEducation.index))

print("\nImmigrant group in Alberta")
df_AvgAnnWages_2016_ByImmigrant = df_AvgAnnWages_2016.loc[
    (df_AvgAnnWages_2016['Characteristics'] == 'Immigrant employees') |
    (df_AvgAnnWages_2016['Characteristics'] == 'Non-immigrant employees')
]
# print(df_AvgAnnWages_2016_ByImmigrant.head(20))
grouped = df_AvgAnnWages_2016_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgAnnWages_2016_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgAnnWages_2016_ByIndigenous = df_AvgAnnWages_2016.loc[
#     (df_AvgAnnWages_2016['Characteristics'] == 'Indigenous identity employees') |
#     (df_AvgAnnWages_2016['Characteristics'] == 'Non-indigenous identity employees')
# ]
# # print(df_AvgAnnHrk_ByIndigenous.head(20))
# grouped = df_AvgAnnWages_2016_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnWages_2016_ByIndigenous.index))

# %%
# Dataset year in 2019 inside Average annual wages and salaries

print("\nAge group in Alberta")
df_AvgAnnWages_2019_ByAge = df_AvgAnnWages_2019.loc[
    (df_AvgAnnWages_2019['Characteristics'] == '15 to 24 years') |
    (df_AvgAnnWages_2019['Characteristics'] == '25 to 34 years') |
    (df_AvgAnnWages_2019['Characteristics'] == '35 to 44 years') |
    (df_AvgAnnWages_2019['Characteristics'] == '45 to 54 years') |
    (df_AvgAnnWages_2019['Characteristics'] == '55 to 64 years') |
    (df_AvgAnnWages_2019['Characteristics'] == '65 years old and over')]
# print(df_AvgAnnWages_2019_ByAge.head(20))
grouped = df_AvgAnnWages_2019_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgAnnWages_2019_ByAge.index))

print("\nGender group in Alberta")
df_AvgAnnWages_2019_ByGender = df_AvgAnnWages_2019.loc[
    (df_AvgAnnWages_2019['Characteristics'] == 'Female employees') |
    (df_AvgAnnWages_2019['Characteristics'] == 'Male employees')
]
# print(df_AvgAnnWages_2019_ByGender.head(20))
grouped = df_AvgAnnWages_2019_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgAnnWages_2019_ByGender.index))

print("\nEducation group in Alberta")
df_AvgAnnWages_2019_ByEducation = df_AvgAnnWages_2019.loc[
    (df_AvgAnnWages_2019['Characteristics'] == 'High school diploma and less') |
    (df_AvgAnnWages_2019['Characteristics'] == 'Trade certificate') |
    (df_AvgAnnWages_2019['Characteristics'] == 'University degree and higher')
]
# print(df_AvgAnnWages_2019_ByEducation.head(20))
grouped = df_AvgAnnWages_2019_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgAnnWages_2019_ByEducation.index))

print("\nImmigrant group in Alberta")
df_AvgAnnWages_2019_ByImmigrant = df_AvgAnnWages_2019.loc[
    (df_AvgAnnWages_2019['Characteristics'] == 'Immigrant employees') |
    (df_AvgAnnWages_2019['Characteristics'] == 'Non-immigrant employees')
]
# print(df_AvgAnnWages_2019_ByImmigrant.head(20))
grouped = df_AvgAnnWages_2019_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgAnnWages_2019_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgAnnWages_2019_ByIndigenous = df_AvgAnnWages_2019.loc[
#     (df_AvgAnnWages_2019['Characteristics'] == 'Indigenous identity employees') |
#     (df_AvgAnnWages_2019['Characteristics'] == 'Non-indigenous identity employees')
# ]
# # print(df_AvgAnnHrk_ByIndigenous.head(20))
# grouped = df_AvgAnnWages_2019_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnWages_2019_ByIndigenous.index))

# %% [markdown]
# Filtered for "Average hourly wage" by following: "Age group", "Gender level", "Education level", and "Immigration status". <br />
# "Aboriginal status" has been commented.

# %%
# # Dataset year of 2010 inside "Average hourly wage"

# print("\nAge group in Alberta")
# df_AvgHrsWages_2010_ByAge = df_AvgHrsWages_2010.loc[
#     (df_AvgHrsWages_2010['Characteristics'] == '15 to 24 years') |
#     (df_AvgHrsWages_2010['Characteristics'] == '25 to 34 years') |
#     (df_AvgHrsWages_2010['Characteristics'] == '35 to 44 years') |
#     (df_AvgHrsWages_2010['Characteristics'] == '45 to 54 years') |
#     (df_AvgHrsWages_2010['Characteristics'] == '55 to 64 years') |
#     (df_AvgHrsWages_2010['Characteristics'] == '65 years old and over')]
# # print(df_AvgHrsWages_2010_ByAge.head(20))
# grouped = df_AvgHrsWages_2010_ByAge.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgHrsWages_2010_ByAge.index))

# print("\nGender group in Alberta")
# df_AvgHrsWages_2010_ByGender = df_AvgHrsWages_2010.loc[
#     (df_AvgHrsWages_2010['Characteristics'] == 'Female employees') |
#     (df_AvgHrsWages_2010['Characteristics'] == 'Male employees')
# ]
# # print(df_AvgHrsWages_2010_ByGender.head(20))
# grouped = df_AvgHrsWages_2010_ByGender.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgHrsWages_2010_ByGender.index))

# print("\nEducation group in Alberta")
# df_AvgHrsWages_2010_ByEducation = df_AvgHrsWages_2010.loc[
#     (df_AvgHrsWages_2010['Characteristics'] == 'High school diploma and less') |
#     (df_AvgHrsWages_2010['Characteristics'] == 'Trade certificate') |
#     (df_AvgHrsWages_2010['Characteristics'] == 'University degree and higher')
# ]
# # print(df_AvgHrsWages_2010_ByEducation.head(20))
# grouped = df_AvgHrsWages_2010_ByEducation.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgHrsWages_2010_ByEducation.index))

# print("\nImmigrant group in Alberta")
# df_AvgHrsWages_2010_ByImmigrant = df_AvgHrsWages_2010.loc[
#     (df_AvgHrsWages_2010['Characteristics'] == 'Immigrant employees') |
#     (df_AvgHrsWages_2010['Characteristics'] == 'Non-immigrant employees')
# ]
# # print(df_AvgHrsWages_2010_ByImmigrant.head(20))
# grouped = df_AvgHrsWages_2010_ByImmigrant.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgHrsWages_2010_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgHrsWages_2010_ByIndigenous = df_AvgHrsWages_2010.loc[
#     (df_AvgHrsWages_2010['Characteristics'] == 'Indigenous identity employees') |
#     (df_AvgHrsWages_2010['Characteristics'] == 'Non-indigenous identity employees')
# ]
# # print(df_AvgHrsWages_2010_ByIndigenous.head(20))
# grouped = df_AvgHrsWages_2010_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgHrsWages_2010_ByIndigenous.index))

# %%
# Dataset year of 2013 inside "Average hourly wage"

print("\nAge group in Alberta")
df_AvgHrsWages_2013_ByAge = df_AvgHrsWages_2013.loc[
    (df_AvgHrsWages_2013['Characteristics'] == '15 to 24 years') |
    (df_AvgHrsWages_2013['Characteristics'] == '25 to 34 years') |
    (df_AvgHrsWages_2013['Characteristics'] == '35 to 44 years') |
    (df_AvgHrsWages_2013['Characteristics'] == '45 to 54 years') |
    (df_AvgHrsWages_2013['Characteristics'] == '55 to 64 years') |
    (df_AvgHrsWages_2013['Characteristics'] == '65 years old and over')]
# print(df_AvgHrsWages_2013_ByAge.head(20))
grouped = df_AvgHrsWages_2013_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgHrsWages_2013_ByAge.index))

print("\nGender group in Alberta")
df_AvgHrsWages_2013_ByGender = df_AvgHrsWages_2013.loc[
    (df_AvgHrsWages_2013['Characteristics'] == 'Female employees') |
    (df_AvgHrsWages_2013['Characteristics'] == 'Male employees')
]
# print(df_AvgHrsWages_2013_ByGender.head(20))
grouped = df_AvgHrsWages_2013_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgHrsWages_2013_ByGender.index))

print("\nEducation group in Alberta")
df_AvgHrsWages_2013_ByEducation = df_AvgHrsWages_2013.loc[
    (df_AvgHrsWages_2013['Characteristics'] == 'High school diploma and less') |
    (df_AvgHrsWages_2013['Characteristics'] == 'Trade certificate') |
    (df_AvgHrsWages_2013['Characteristics'] == 'University degree and higher')
]
# print(df_AvgHrsWages_2013_ByEducation.head(20))
grouped = df_AvgHrsWages_2013_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgHrsWages_2013_ByEducation.index))

print("\nImmigrant group in Alberta")
df_AvgHrsWages_2013_ByImmigrant = df_AvgHrsWages_2013.loc[
    (df_AvgHrsWages_2013['Characteristics'] == 'Immigrant employees') |
    (df_AvgHrsWages_2013['Characteristics'] == 'Non-immigrant employees')
]
# print(df_AvgHrsWages_2013_ByImmigrant.head(20))
grouped = df_AvgHrsWages_2013_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgHrsWages_2013_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgHrsWages_2013_ByIndigenous = df_AvgHrsWages_2013.loc[
#     (df_AvgHrsWages_2013['Characteristics'] == 'Indigenous identity employees') |
#     (df_AvgHrsWages_2013['Characteristics'] == 'Non-indigenous identity employees')
# ]
# # print(df_AvgHrsWages_2013_ByIndigenous.head(20))
# grouped = df_AvgHrsWages_2013_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgHrsWages_2013_ByIndigenous.index))

# %%
# Dataset year in 2017 inside "Average hourly wage"

print("\nAge group in Alberta")
df_AvgHrsWages_2016_ByAge = df_AvgHrsWages_2016.loc[
    (df_AvgHrsWages_2016['Characteristics'] == '15 to 24 years') |
    (df_AvgHrsWages_2016['Characteristics'] == '25 to 34 years') |
    (df_AvgHrsWages_2016['Characteristics'] == '35 to 44 years') |
    (df_AvgHrsWages_2016['Characteristics'] == '45 to 54 years') |
    (df_AvgHrsWages_2016['Characteristics'] == '55 to 64 years') |
    (df_AvgHrsWages_2016['Characteristics'] == '65 years old and over')]
# print(df_AvgHrsWages_2016_ByAge.head(20))
grouped = df_AvgHrsWages_2016_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgHrsWages_2016_ByAge.index))

print("\nGender group in Alberta")
df_AvgHrsWages_2016_ByGender = df_AvgHrsWages_2016.loc[
    (df_AvgHrsWages_2016['Characteristics'] == 'Female employees') |
    (df_AvgHrsWages_2016['Characteristics'] == 'Male employees')
]
# print(df_AvgHrsWages_2016_ByGender.head(20))
grouped = df_AvgHrsWages_2016_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgHrsWages_2016_ByGender.index))

print("\nEducation group in Alberta")
df_AvgHrsWages_2016_ByEducation = df_AvgHrsWages_2016.loc[
    (df_AvgHrsWages_2016['Characteristics'] == 'High school diploma and less') |
    (df_AvgHrsWages_2016['Characteristics'] == 'Trade certificate') |
    (df_AvgHrsWages_2016['Characteristics'] == 'University degree and higher')
]
# print(df_AvgHrsWages_2016_ByEducation.head(20))
grouped = df_AvgHrsWages_2016_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgHrsWages_2016_ByEducation.index))

print("\nImmigrant group in Alberta")
df_AvgHrsWages_2016_ByImmigrant = df_AvgHrsWages_2016.loc[
    (df_AvgHrsWages_2016['Characteristics'] == 'Immigrant employees') |
    (df_AvgHrsWages_2016['Characteristics'] == 'Non-immigrant employees')
]
# print(df_AvgHrsWages_2016_ByImmigrant.head(20))
grouped = df_AvgHrsWages_2016_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgHrsWages_2016_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgAnnHrk_ByIndigenous = df_AvgHrsWages_2016.loc[
#     (df_AvgHrsWages_2016['Characteristics'] == 'Indigenous identity employees') |
#     (df_AvgHrsWages_2016['Characteristics'] == 'Non-indigenous identity employees')
# ]
# # print(df_AvgAnnHrk_ByIndigenous.head(20))
# grouped = df_AvgAnnHrk_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnHrk_ByIndigenous.index))

# %%
# Dataset year in 2019 inside "Average hourly wage"

print("\nAge group in Alberta")
df_AvgHrsWages_2019_ByAge = df_AvgHrsWages_2019.loc[
    (df_AvgHrsWages_2019['Characteristics'] == '15 to 24 years') |
    (df_AvgHrsWages_2019['Characteristics'] == '25 to 34 years') |
    (df_AvgHrsWages_2019['Characteristics'] == '35 to 44 years') |
    (df_AvgHrsWages_2019['Characteristics'] == '45 to 54 years') |
    (df_AvgHrsWages_2019['Characteristics'] == '55 to 64 years') |
    (df_AvgHrsWages_2019['Characteristics'] == '65 years old and over')]
# print(df_AvgHrsWages_2019_ByAge.head(20))
grouped = df_AvgHrsWages_2019_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgHrsWages_2019_ByAge.index))

print("\nGender group in Alberta")
df_AvgHrsWages_2019_ByGender = df_AvgHrsWages_2019.loc[
    (df_AvgHrsWages_2019['Characteristics'] == 'Female employees') |
    (df_AvgHrsWages_2019['Characteristics'] == 'Male employees')
]
# print(df_AvgHrsWages_2019_ByGender.head(20))
grouped = df_AvgHrsWages_2019_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgHrsWages_2019_ByGender.index))

print("\nEducation group in Alberta")
df_AvgHrsWages_2019_ByEducation = df_AvgHrsWages_2019.loc[
    (df_AvgHrsWages_2019['Characteristics'] == 'High school diploma and less') |
    (df_AvgHrsWages_2019['Characteristics'] == 'Trade certificate') |
    (df_AvgHrsWages_2019['Characteristics'] == 'University degree and higher')
]
# print(df_AvgHrsWages_2019_ByEducation.head(20))
grouped = df_AvgHrsWages_2019_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgHrsWages_2019_ByEducation.index))

print("\nImmigrant group in Alberta")
df_AvgHrsWages_2019_ByImmigrant = df_AvgHrsWages_2019.loc[
    (df_AvgHrsWages_2019['Characteristics'] == 'Immigrant employees') |
    (df_AvgHrsWages_2019['Characteristics'] == 'Non-immigrant employees')
]
# print(df_AvgHrsWages_2019_ByImmigrant.head(20))
grouped = df_AvgHrsWages_2019_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgHrsWages_2019_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgHrsWages_2019_ByIndigenous = df_AvgHrsWages_2019.loc[
#     (df_AvgHrsWages_2019['Characteristics'] == 'Indigenous identity employees') |
#     (df_AvgHrsWages_2019['Characteristics'] == 'Non-indigenous identity employees')
# ]
# # print(df_AvgHrsWages_2019_ByIndigenous.head(20))
# grouped = df_AvgHrsWages_2019_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgHrsWages_2019_ByIndigenous.index))

# %% [markdown]
# Filtered for "Average weekly hours worked" by following: "Age group", "Gender level", "Education level", and "Immigration status".<br />
# "Aboriginal status" has been commented.

# %%
# # Dataset year in 2010 inside "Average weekly hours worked"

# print("\nAge group in Alberta")
# df_AvgWeekHrsWrked_2010_ByAge = df_AvgWeekHrsWrked_2010.loc[
#     (df_AvgWeekHrsWrked_2010['Characteristics'] == '15 to 24 years') |
#     (df_AvgWeekHrsWrked_2010['Characteristics'] == '25 to 34 years') |
#     (df_AvgWeekHrsWrked_2010['Characteristics'] == '35 to 44 years') |
#     (df_AvgWeekHrsWrked_2010['Characteristics'] == '45 to 54 years') |
#     (df_AvgWeekHrsWrked_2010['Characteristics'] == '55 to 64 years') |
#     (df_AvgWeekHrsWrked_2010['Characteristics'] == '65 years old and over')]
# # print(df_AvgWeekHrsWrked_2010_ByAge.head(20))
# grouped = df_AvgWeekHrsWrked_2010_ByAge.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgWeekHrsWrked_2010_ByAge.index))

# print("\nGender group in Alberta")
# df_AvgWeekHrsWrked_2010_ByGender = df_AvgWeekHrsWrked_2010.loc[
#     (df_AvgWeekHrsWrked_2010['Characteristics'] == 'Female employees') |
#     (df_AvgWeekHrsWrked_2010['Characteristics'] == 'Male employees')
# ]
# # print(df_AvgWeekHrsWrked_2010_ByGender.head(20))
# grouped = df_AvgWeekHrsWrked_2010_ByGender.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgWeekHrsWrked_2010_ByGender.index))

# print("\nEducation group in Alberta")
# df_AvgWeekHrsWrked_2010_ByEducation = df_AvgWeekHrsWrked_2010.loc[
#     (df_AvgWeekHrsWrked_2010['Characteristics'] == 'High school diploma and less') |
#     (df_AvgWeekHrsWrked_2010['Characteristics'] == 'Trade certificate') |
#     (df_AvgWeekHrsWrked_2010['Characteristics'] == 'University degree and higher')
# ]
# # print(df_AvgWeekHrsWrked_2010_ByEducation.head(20))
# grouped = df_AvgWeekHrsWrked_2010_ByEducation.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgWeekHrsWrked_2010_ByEducation.index))

# print("\nImmigrant group in Alberta")
# df_AvgWeekHrsWrked_2010_ByImmigrant = df_AvgWeekHrsWrked_2010.loc[
#     (df_AvgWeekHrsWrked_2010['Characteristics'] == 'Immigrant employees') |
#     (df_AvgWeekHrsWrked_2010['Characteristics'] == 'Non-immigrant employees')
# ]
# # print(df_AvgWeekHrsWrked_2010_ByImmigrant.head(20))
# grouped = df_AvgWeekHrsWrked_2010_ByImmigrant.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgWeekHrsWrked_2010_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgWeekHrsWrked_2010_ByIndigenous = df_AvgWeekHrsWrked_2010.loc[
#     (df_AvgWeekHrsWrked_2010['Characteristics'] == 'Indigenous identity employees') |
#     (df_AvgWeekHrsWrked_2010['Characteristics'] == 'Non-indigenous identity employees')
# ]
# # print(df_AvgWeekHrsWrked_2010_ByIndigenous.head(20))
# grouped = df_AvgWeekHrsWrked_2010_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgWeekHrsWrked_2010_ByIndigenous.index))

# %%
# Dataset year in 2013 inside "Average weekly hours worked"

print("\nAge group in Alberta")
df_AvgWeekHrsWrked_2013_ByAge = df_AvgWeekHrsWrked_2013.loc[
    (df_AvgWeekHrsWrked_2013['Characteristics'] == '15 to 24 years') |
    (df_AvgWeekHrsWrked_2013['Characteristics'] == '25 to 34 years') |
    (df_AvgWeekHrsWrked_2013['Characteristics'] == '35 to 44 years') |
    (df_AvgWeekHrsWrked_2013['Characteristics'] == '45 to 54 years') |
    (df_AvgWeekHrsWrked_2013['Characteristics'] == '55 to 64 years') |
    (df_AvgWeekHrsWrked_2013['Characteristics'] == '65 years old and over')]
# print(df_AvgWeekHrsWrked_2013_ByAge.head(20))
grouped = df_AvgWeekHrsWrked_2013_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgWeekHrsWrked_2013_ByAge.index))

print("\nGender group in Alberta")
df_AvgWeekHrsWrked_2013_ByGender = df_AvgWeekHrsWrked_2013.loc[
    (df_AvgWeekHrsWrked_2013['Characteristics'] == 'Female employees') |
    (df_AvgWeekHrsWrked_2013['Characteristics'] == 'Male employees')
]
# print(df_AvgWeekHrsWrked_2013_ByGender.head(20))
grouped = df_AvgWeekHrsWrked_2013_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgWeekHrsWrked_2013_ByGender.index))

print("\nEducation group in Alberta")
df_AvgWeekHrsWrked_2013_ByEducation = df_AvgWeekHrsWrked_2013.loc[
    (df_AvgWeekHrsWrked_2013['Characteristics'] == 'High school diploma and less') |
    (df_AvgWeekHrsWrked_2013['Characteristics'] == 'Trade certificate') |
    (df_AvgWeekHrsWrked_2013['Characteristics'] == 'University degree and higher')
]
# print(df_AvgWeekHrsWrked_2013_ByEducation.head(20))
grouped = df_AvgWeekHrsWrked_2013_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgWeekHrsWrked_2013_ByEducation.index))

print("\nImmigrant group in Alberta")
df_AvgWeekHrsWrked_2013_ByImmigrant = df_AvgWeekHrsWrked_2013.loc[
    (df_AvgWeekHrsWrked_2013['Characteristics'] == 'Immigrant employees') |
    (df_AvgWeekHrsWrked_2013['Characteristics'] == 'Non-immigrant employees')
]
# print(df_AvgWeekHrsWrked_2013_ByImmigrant.head(20))
grouped = df_AvgWeekHrsWrked_2013_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgWeekHrsWrked_2013_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgWeekHrsWrked_2013_ByIndigenous = df_AvgWeekHrsWrked_2013.loc[
#     (df_AvgWeekHrsWrked_2013['Characteristics'] == 'Indigenous identity employees') |
#     (df_AvgWeekHrsWrked_2013['Characteristics'] == 'Non-indigenous identity employees')
# ]
# # print(df_AvgWeekHrsWrked_2013_ByIndigenous.head(20))
# grouped = df_AvgWeekHrsWrked_2013_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgWeekHrsWrked_2013_ByIndigenous.index))

# %%
# Dataset year in 2016 inside "Average weekly hours worked"

print("\nAge group in Alberta")
df_AvgWeekHrsWrked_2016_ByAge = df_AvgWeekHrsWrked_2016.loc[
    (df_AvgWeekHrsWrked_2016['Characteristics'] == '15 to 24 years') |
    (df_AvgWeekHrsWrked_2016['Characteristics'] == '25 to 34 years') |
    (df_AvgWeekHrsWrked_2016['Characteristics'] == '35 to 44 years') |
    (df_AvgWeekHrsWrked_2016['Characteristics'] == '45 to 54 years') |
    (df_AvgWeekHrsWrked_2016['Characteristics'] == '55 to 64 years') |
    (df_AvgWeekHrsWrked_2016['Characteristics'] == '65 years old and over')]
# print(df_AvgWeekHrsWrked_2016_ByAge.head(20))
grouped = df_AvgWeekHrsWrked_2016_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgWeekHrsWrked_2016_ByAge.index))

print("\nGender group in Alberta")
df_AvgWeekHrsWrked_2016_ByGender = df_AvgWeekHrsWrked_2016.loc[
    (df_AvgWeekHrsWrked_2016['Characteristics'] == 'Female employees') |
    (df_AvgWeekHrsWrked_2016['Characteristics'] == 'Male employees')
]
# print(df_AvgWeekHrsWrked_2016_ByGender.head(20))
grouped = df_AvgWeekHrsWrked_2016_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgWeekHrsWrked_2016_ByGender.index))

print("\nEducation group in Alberta")
df_AvgWeekHrsWrked_2016_ByEducation = df_AvgWeekHrsWrked_2016.loc[
    (df_AvgWeekHrsWrked_2016['Characteristics'] == 'High school diploma and less') |
    (df_AvgWeekHrsWrked_2016['Characteristics'] == 'Trade certificate') |
    (df_AvgWeekHrsWrked_2016['Characteristics'] == 'University degree and higher')
]
# print(df_AvgWeekHrsWrked_2016_ByEducation.head(20))
grouped = df_AvgWeekHrsWrked_2016_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgWeekHrsWrked_2016_ByEducation.index))

print("\nImmigrant group in Alberta")
df_AvgWeekHrsWrked_2016_ByImmigrant = df_AvgWeekHrsWrked_2016.loc[
    (df_AvgWeekHrsWrked_2016['Characteristics'] == 'Immigrant employees') |
    (df_AvgWeekHrsWrked_2016['Characteristics'] == 'Non-immigrant employees')
]
# print(df_AvgWeekHrsWrked_2016_ByImmigrant.head(20))
grouped = df_AvgWeekHrsWrked_2016_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgWeekHrsWrked_2016_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgWeekHrsWrked_2016_ByIndigenous = df_AvgWeekHrsWrked_2016.loc[
#     (df_AvgWeekHrsWrked_2016['Characteristics'] == 'Indigenous identity employees') |
#     (df_AvgWeekHrsWrked_2016['Characteristics'] == 'Non-indigenous identity employees')
# ]
# # print(df_AvgAnnHrk_ByIndigenous.head(20))
# grouped = df_AvgWeekHrsWrked_2016_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgWeekHrsWrked_2016_ByIndigenous.index))

# %%
# Dataset year in 2019 inside "Average weekly hours worked"

print("\nAge group in Alberta")
df_AvgWeekHrsWrked_2019_ByAge = df_AvgWeekHrsWrked_2019.loc[
    (df_AvgWeekHrsWrked_2019['Characteristics'] == '15 to 24 years') |
    (df_AvgWeekHrsWrked_2019['Characteristics'] == '25 to 34 years') |
    (df_AvgWeekHrsWrked_2019['Characteristics'] == '35 to 44 years') |
    (df_AvgWeekHrsWrked_2019['Characteristics'] == '45 to 54 years') |
    (df_AvgWeekHrsWrked_2019['Characteristics'] == '55 to 64 years') |
    (df_AvgWeekHrsWrked_2019['Characteristics'] == '65 years old and over')]
# print(df_AvgWeekHrsWrked_2019_ByAge.head(20))
grouped = df_AvgWeekHrsWrked_2019_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgWeekHrsWrked_2019_ByAge.index))

print("\nGender group in Alberta")
df_AvgWeekHrsWrked_2019_ByGender = df_AvgWeekHrsWrked_2019.loc[
    (df_AvgWeekHrsWrked_2019['Characteristics'] == 'Female employees') |
    (df_AvgWeekHrsWrked_2019['Characteristics'] == 'Male employees')
]
# print(df_AvgWeekHrsWrked_2019_ByGender.head(20))
grouped = df_AvgWeekHrsWrked_2019_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgWeekHrsWrked_2019_ByGender.index))

print("\nEducation group in Alberta")
df_AvgWeekHrsWrked_2019_ByEducation = df_AvgWeekHrsWrked_2019.loc[
    (df_AvgWeekHrsWrked_2019['Characteristics'] == 'High school diploma and less') |
    (df_AvgWeekHrsWrked_2019['Characteristics'] == 'Trade certificate') |
    (df_AvgWeekHrsWrked_2019['Characteristics'] == 'University degree and higher')
]
# print(df_AvgWeekHrsWrked_2019_ByEducation.head(20))
grouped = df_AvgWeekHrsWrked_2019_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgWeekHrsWrked_2019_ByEducation.index))

print("\nImmigrant group in Alberta")
df_AvgWeekHrsWrked_2019_ByImmigrant = df_AvgWeekHrsWrked_2019.loc[
    (df_AvgWeekHrsWrked_2019['Characteristics'] == 'Immigrant employees') |
    (df_AvgWeekHrsWrked_2019['Characteristics'] == 'Non-immigrant employees')
]
# print(df_AvgWeekHrsWrked_2019_ByImmigrant.head(20))
grouped = df_AvgWeekHrsWrked_2019_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgWeekHrsWrked_2019_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgWeekHrsWrked_2019_ByIndigenous = df_AvgWeekHrsWrked_2019.loc[
#     (df_AvgWeekHrsWrked_2019['Characteristics'] == 'Indigenous identity employees') |
#     (df_AvgWeekHrsWrked_2019['Characteristics'] == 'Non-indigenous identity employees')
# ]
# # print(df_AvgWeekHrsWrked_2019_ByIndigenous.head(20))
# grouped = df_AvgWeekHrsWrked_2019_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgWeekHrsWrked_2019_ByIndigenous.index))

# %% [markdown]
# Filtered for "Hours worked" by following: "Age group", "Gender level", "Education level", and "Immigration status".<br />
# "Aboriginal status" has been commented.
# 

# %%
# # Dataset year in 2010 inside "Hours Worked"

# print("\nAge group in Alberta")
# df_Hrs_Wrked_2010_ByAge = df_Hrs_Wrked_2010.loc[
#     (df_Hrs_Wrked_2010['Characteristics'] == '15 to 24 years') |
#     (df_Hrs_Wrked_2010['Characteristics'] == '25 to 34 years') |
#     (df_Hrs_Wrked_2010['Characteristics'] == '35 to 44 years') |
#     (df_Hrs_Wrked_2010['Characteristics'] == '45 to 54 years') |
#     (df_Hrs_Wrked_2010['Characteristics'] == '55 to 64 years') |
#     (df_Hrs_Wrked_2010['Characteristics'] == '65 years old and over')]
# # print(df_Hrs_Wrked_2010_ByAge.head(20))
# grouped = df_Hrs_Wrked_2010_ByAge.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_Hrs_Wrked_2010_ByAge.index))

# print("\nGender group in Alberta")
# df_Hrs_Wrked_2010_ByGender = df_Hrs_Wrked_2010.loc[
#     (df_Hrs_Wrked_2010['Characteristics'] == 'Female employees') |
#     (df_Hrs_Wrked_2010['Characteristics'] == 'Male employees')
# ]
# # print(df_Hrs_Wrked_2010_ByGender.head(20))
# grouped = df_Hrs_Wrked_2010_ByGender.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_Hrs_Wrked_2010_ByGender.index))

# print("\nEducation group in Alberta")
# df_Hrs_Wrked_2010_ByEducation = df_Hrs_Wrked_2010.loc[
#     (df_Hrs_Wrked_2010['Characteristics'] == 'High school diploma and less') |
#     (df_Hrs_Wrked_2010['Characteristics'] == 'Trade certificate') |
#     (df_Hrs_Wrked_2010['Characteristics'] == 'University degree and higher')
# ]
# # print(df_Hrs_Wrked_2010_ByEducation.head(20))
# grouped = df_Hrs_Wrked_2010_ByEducation.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_Hrs_Wrked_2010_ByEducation.index))

# print("\nImmigrant group in Alberta")
# df_Hrs_Wrked_2010_ByImmigrant = df_Hrs_Wrked_2010.loc[
#     (df_Hrs_Wrked_2010['Characteristics'] == 'Immigrant employees') |
#     (df_Hrs_Wrked_2010['Characteristics'] == 'Non-immigrant employees')
# ]
# # print(df_Hrs_Wrked_2010_ByImmigrant.head(20))
# grouped = df_Hrs_Wrked_2010_ByImmigrant.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_Hrs_Wrked_2010_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_Hrs_Wrked_2010_ByIndigenous = df_Hrs_Wrked_2010.loc[
#     (df_Hrs_Wrked_2010['Characteristics'] == 'Indigenous identity employees') |
#     (df_Hrs_Wrked_2010['Characteristics'] == 'Non-indigenous identity employees')
# ]
# # print(df_Hrs_Wrked_2010_ByIndigenous.head(20))
# grouped = df_Hrs_Wrked_2010_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_Hrs_Wrked_2010_ByIndigenous.index))

# %%
# Dataset year in 2013 inside "Hours Worked"

print("\nAge group in Alberta")
df_Hrs_Wrked_2013_ByAge = df_Hrs_Wrked_2013.loc[
    (df_Hrs_Wrked_2013['Characteristics'] == '15 to 24 years') |
    (df_Hrs_Wrked_2013['Characteristics'] == '25 to 34 years') |
    (df_Hrs_Wrked_2013['Characteristics'] == '35 to 44 years') |
    (df_Hrs_Wrked_2013['Characteristics'] == '45 to 54 years') |
    (df_Hrs_Wrked_2013['Characteristics'] == '55 to 64 years') |
    (df_Hrs_Wrked_2013['Characteristics'] == '65 years old and over')]
# print(df_Hrs_Wrked_2013_ByAge.head(20))
grouped = df_Hrs_Wrked_2013_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_Hrs_Wrked_2013_ByAge.index))

print("\nGender group in Alberta")
df_Hrs_Wrked_2013_ByGender = df_Hrs_Wrked_2013.loc[
    (df_Hrs_Wrked_2013['Characteristics'] == 'Female employees') |
    (df_Hrs_Wrked_2013['Characteristics'] == 'Male employees')
]
# print(df_Hrs_Wrked_2013_ByGender.head(20))
grouped = df_Hrs_Wrked_2013_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_Hrs_Wrked_2013_ByGender.index))

print("\nEducation group in Alberta")
df_Hrs_Wrked_2013_ByEducation = df_Hrs_Wrked_2013.loc[
    (df_Hrs_Wrked_2013['Characteristics'] == 'High school diploma and less') |
    (df_Hrs_Wrked_2013['Characteristics'] == 'Trade certificate') |
    (df_Hrs_Wrked_2013['Characteristics'] == 'University degree and higher')
]
# print(df_Hrs_Wrked_2013_ByEducation.head(20))
grouped = df_Hrs_Wrked_2013_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_Hrs_Wrked_2013_ByEducation.index))

print("\nImmigrant group in Alberta")
df_Hrs_Wrked_2013_ByImmigrant = df_Hrs_Wrked_2013.loc[
    (df_Hrs_Wrked_2013['Characteristics'] == 'Immigrant employees') |
    (df_Hrs_Wrked_2013['Characteristics'] == 'Non-immigrant employees')
]
# print(df_Hrs_Wrked_2013_ByImmigrant.head(20))
grouped = df_Hrs_Wrked_2013_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_Hrs_Wrked_2013_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_Hrs_Wrked_2013_ByIndigenous = df_Hrs_Wrked_2013.loc[
#     (df_Hrs_Wrked_2013['Characteristics'] == 'Indigenous identity employees') |
#     (df_Hrs_Wrked_2013['Characteristics'] == 'Non-indigenous identity employees')
# ]
# # print(df_Hrs_Wrked_2013_ByIndigenous.head(20))
# grouped = df_Hrs_Wrked_2013_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_Hrs_Wrked_2013_ByIndigenous.index))

# %%
# Dataset year in 2016 inside "Hours Worked"

print("\nAge group in Alberta")
df_Hrs_Wrked_2016_ByAge = df_Hrs_Wrked_2016.loc[
    (df_Hrs_Wrked_2016['Characteristics'] == '15 to 24 years') |
    (df_Hrs_Wrked_2016['Characteristics'] == '25 to 34 years') |
    (df_Hrs_Wrked_2016['Characteristics'] == '35 to 44 years') |
    (df_Hrs_Wrked_2016['Characteristics'] == '45 to 54 years') |
    (df_Hrs_Wrked_2016['Characteristics'] == '55 to 64 years') |
    (df_Hrs_Wrked_2016['Characteristics'] == '65 years old and over')]
# print(df_Hrs_Wrked_2016_ByAge.head(20))
grouped = df_Hrs_Wrked_2016_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_Hrs_Wrked_2016_ByAge.index))

print("\nGender group in Alberta")
df_Hrs_Wrked_2016_ByGender = df_Hrs_Wrked_2016.loc[
    (df_Hrs_Wrked_2016['Characteristics'] == 'Female employees') |
    (df_Hrs_Wrked_2016['Characteristics'] == 'Male employees')
]
# print(df_Hrs_Wrked_2016_ByGender.head(20))
grouped = df_Hrs_Wrked_2016_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_Hrs_Wrked_2016_ByGender.index))

print("\nEducation group in Alberta")
df_Hrs_Wrked_2016_ByEducation = df_Hrs_Wrked_2016.loc[
    (df_Hrs_Wrked_2016['Characteristics'] == 'High school diploma and less') |
    (df_Hrs_Wrked_2016['Characteristics'] == 'Trade certificate') |
    (df_Hrs_Wrked_2016['Characteristics'] == 'University degree and higher')
]
# print(df_Hrs_Wrked_2016_ByEducation.head(20))
grouped = df_Hrs_Wrked_2016_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_Hrs_Wrked_2016_ByEducation.index))

print("\nImmigrant group in Alberta")
df_Hrs_Wrked_2016_ByImmigrant = df_Hrs_Wrked_2016.loc[
    (df_Hrs_Wrked_2016['Characteristics'] == 'Immigrant employees') |
    (df_Hrs_Wrked_2016['Characteristics'] == 'Non-immigrant employees')
]
# print(df_Hrs_Wrked_2016_ByImmigrant.head(20))
grouped = df_Hrs_Wrked_2016_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_Hrs_Wrked_2016_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_Hrs_Wrked_2016_ByIndigenous = df_Hrs_Wrked_2016.loc[
#     (df_Hrs_Wrked_2016['Characteristics'] == 'Indigenous identity employees') |
#     (df_Hrs_Wrked_2016['Characteristics'] == 'Non-indigenous identity employees')
# ]
# # print(df_AvgAnnHrk_ByIndigenous.head(20))
# grouped = df_Hrs_Wrked_2016_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_Hrs_Wrked_2016_ByIndigenous.index))

# %%
# Dataset year in 2019 inside "Hour Worked"

print("\nAge group in Alberta")
df_Hrs_Wrked_2019_ByAge = df_Hrs_Wrked_2019.loc[
    (df_Hrs_Wrked_2019['Characteristics'] == '15 to 24 years') |
    (df_Hrs_Wrked_2019['Characteristics'] == '25 to 34 years') |
    (df_Hrs_Wrked_2019['Characteristics'] == '35 to 44 years') |
    (df_Hrs_Wrked_2019['Characteristics'] == '45 to 54 years') |
    (df_Hrs_Wrked_2019['Characteristics'] == '55 to 64 years') |
    (df_Hrs_Wrked_2019['Characteristics'] == '65 years old and over')]
# print(df_Hrs_Wrked_2019_ByAge.head(20))
grouped = df_Hrs_Wrked_2019_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_Hrs_Wrked_2019_ByAge.index))

print("\nGender group in Alberta")
df_Hrs_Wrked_2019_ByGender = df_Hrs_Wrked_2019.loc[
    (df_Hrs_Wrked_2019['Characteristics'] == 'Female employees') |
    (df_Hrs_Wrked_2019['Characteristics'] == 'Male employees')
]
# print(df_Hrs_Wrked_2019_ByGender.head(20))
grouped = df_Hrs_Wrked_2019_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_Hrs_Wrked_2019_ByGender.index))

print("\nEducation group in Alberta")
df_Hrs_Wrked_2019_ByEducation = df_Hrs_Wrked_2019.loc[
    (df_Hrs_Wrked_2019['Characteristics'] == 'High school diploma and less') |
    (df_Hrs_Wrked_2019['Characteristics'] == 'Trade certificate') |
    (df_Hrs_Wrked_2019['Characteristics'] == 'University degree and higher')
]
# print(df_Hrs_Wrked_2019_ByEducation.head(20))
grouped = df_Hrs_Wrked_2019_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_Hrs_Wrked_2019_ByEducation.index))

print("\nImmigrant group in Alberta")
df_Hrs_Wrked_2019_ByImmigrant = df_Hrs_Wrked_2019.loc[
    (df_Hrs_Wrked_2019['Characteristics'] == 'Immigrant employees') |
    (df_Hrs_Wrked_2019['Characteristics'] == 'Non-immigrant employees')
]
# print(df_Hrs_Wrked_2019_ByImmigrant.head(20))
grouped = df_Hrs_Wrked_2019_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_Hrs_Wrked_2019_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_Hrs_Wrked_2019_ByIndigenous = df_Hrs_Wrked_2019.loc[
#     (df_Hrs_Wrked_2019['Characteristics'] == 'Indigenous identity employees') |
#     (df_Hrs_Wrked_2019['Characteristics'] == 'Non-indigenous identity employees')
# ]
# # print(df_Hrs_Wrked_2019_ByIndigenous.head(20))
# grouped = df_Hrs_Wrked_2019_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_Hrs_Wrked_2019_ByIndigenous.index))


# %% [markdown]
# Filtered for "Number of jobs" by following: "Age group", "Gender level", "Education level", and "Immigration status".<br />
# "Aboriginal status" has been commented.

# %%
# # Dataset year in 2010 inside "Number of jobs"

# print("\nAge group in Alberta")
# df_NumOfJob_2010_ByAge = df_NumOfJob_2010.loc[
#     (df_NumOfJob_2010['Characteristics'] == '15 to 24 years') |
#     (df_NumOfJob_2010['Characteristics'] == '25 to 34 years') |
#     (df_NumOfJob_2010['Characteristics'] == '35 to 44 years') |
#     (df_NumOfJob_2010['Characteristics'] == '45 to 54 years') |
#     (df_NumOfJob_2010['Characteristics'] == '55 to 64 years') |
#     (df_NumOfJob_2010['Characteristics'] == '65 years old and over')]
# # print(df_NumOfJob_2010_ByAge.head(20))
# grouped = df_NumOfJob_2010_ByAge.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_NumOfJob_2010_ByAge.index))

# print("\nGender group in Alberta")
# df_NumOfJob_2010_ByGender = df_NumOfJob_2010.loc[
#     (df_NumOfJob_2010['Characteristics'] == 'Female employees') |
#     (df_NumOfJob_2010['Characteristics'] == 'Male employees')
# ]
# # print(df_NumOfJob_2010_ByGender.head(20))
# grouped = df_NumOfJob_2010_ByGender.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_NumOfJob_2010_ByGender.index))

# print("\nEducation group in Alberta")
# df_NumOfJob_2010_ByEducation = df_NumOfJob_2010.loc[
#     (df_NumOfJob_2010['Characteristics'] == 'High school diploma and less') |
#     (df_NumOfJob_2010['Characteristics'] == 'Trade certificate') |
#     (df_NumOfJob_2010['Characteristics'] == 'University degree and higher')
# ]
# # print(df_NumOfJob_2010_ByEducation.head(20))
# grouped = df_NumOfJob_2010_ByEducation.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_NumOfJob_2010_ByEducation.index))

# print("\nImmigrant group in Alberta")
# df_NumOfJob_2010_ByImmigrant = df_NumOfJob_2010.loc[
#     (df_NumOfJob_2010['Characteristics'] == 'Immigrant employees') |
#     (df_NumOfJob_2010['Characteristics'] == 'Non-immigrant employees')
# ]
# # print(df_NumOfJob_2010_ByImmigrant.head(20))
# grouped = df_NumOfJob_2010_ByImmigrant.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_NumOfJob_2010_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_NumOfJob_2010_ByIndigenous = df_NumOfJob_2010.loc[
#     (df_NumOfJob_2010['Characteristics'] == 'Indigenous identity employees') |
#     (df_NumOfJob_2010['Characteristics'] == 'Non-indigenous identity employees')
# ]
# # print(df_NumOfJob_2010_ByIndigenous.head(20))
# grouped = df_NumOfJob_2010_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_NumOfJob_2010_ByIndigenous.index))

# %%
# Dataset year in 2013 inside "Number of jobs"

print("\nAge group in Alberta")
df_NumOfJob_2013_ByAge = df_NumOfJob_2013.loc[
    (df_NumOfJob_2013['Characteristics'] == '15 to 24 years') |
    (df_NumOfJob_2013['Characteristics'] == '25 to 34 years') |
    (df_NumOfJob_2013['Characteristics'] == '35 to 44 years') |
    (df_NumOfJob_2013['Characteristics'] == '45 to 54 years') |
    (df_NumOfJob_2013['Characteristics'] == '55 to 64 years') |
    (df_NumOfJob_2013['Characteristics'] == '65 years old and over')]
# print(df_NumOfJob_2013_ByAge.head(20))
grouped = df_NumOfJob_2013_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_NumOfJob_2013_ByAge.index))

print("\nGender group in Alberta")
df_NumOfJob_2013_ByGender = df_NumOfJob_2013.loc[
    (df_NumOfJob_2013['Characteristics'] == 'Female employees') |
    (df_NumOfJob_2013['Characteristics'] == 'Male employees')
]
# print(df_NumOfJob_2013_ByGender.head(20))
grouped = df_NumOfJob_2013_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_NumOfJob_2013_ByGender.index))

print("\nEducation group in Alberta")
df_NumOfJob_2013_ByEducation = df_NumOfJob_2013.loc[
    (df_NumOfJob_2013['Characteristics'] == 'High school diploma and less') |
    (df_NumOfJob_2013['Characteristics'] == 'Trade certificate') |
    (df_NumOfJob_2013['Characteristics'] == 'University degree and higher')
]
# print(df_NumOfJob_2013_ByEducation.head(20))
grouped = df_NumOfJob_2013_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_NumOfJob_2013_ByEducation.index))

print("\nImmigrant group in Alberta")
df_NumOfJob_2013_ByImmigrant = df_NumOfJob_2013.loc[
    (df_NumOfJob_2013['Characteristics'] == 'Immigrant employees') |
    (df_NumOfJob_2013['Characteristics'] == 'Non-immigrant employees')
]
# print(df_NumOfJob_2013_ByImmigrant.head(20))
grouped = df_NumOfJob_2013_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_NumOfJob_2013_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_NumOfJob_2013_ByIndigenous = df_NumOfJob_2013.loc[
#     (df_NumOfJob_2013['Characteristics'] == 'Indigenous identity employees') |
#     (df_NumOfJob_2013['Characteristics'] == 'Non-indigenous identity employees')
# ]
# # print(df_NumOfJob_2013_ByIndigenous.head(20))
# grouped = df_NumOfJob_2013_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_NumOfJob_2013_ByIndigenous.index))

# %%
# Dataset year in 2016 inside "Number of jobs"

print("\nAge group in Alberta")
df_NumOfJob_2016_ByAge = df_NumOfJob_2016.loc[
    (df_NumOfJob_2016['Characteristics'] == '15 to 24 years') |
    (df_NumOfJob_2016['Characteristics'] == '25 to 34 years') |
    (df_NumOfJob_2016['Characteristics'] == '35 to 44 years') |
    (df_NumOfJob_2016['Characteristics'] == '45 to 54 years') |
    (df_NumOfJob_2016['Characteristics'] == '55 to 64 years') |
    (df_NumOfJob_2016['Characteristics'] == '65 years old and over')]
# print(df_NumOfJob_2016_ByAge.head(20))
grouped = df_NumOfJob_2016_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_NumOfJob_2016_ByAge.index))

print("\nGender group in Alberta")
df_NumOfJob_2016_ByGender = df_NumOfJob_2016.loc[
    (df_NumOfJob_2016['Characteristics'] == 'Female employees') |
    (df_NumOfJob_2016['Characteristics'] == 'Male employees')
]
# print(df_NumOfJob_2016_ByGender.head(20))
grouped = df_NumOfJob_2016_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_NumOfJob_2016_ByGender.index))

print("\nEducation group in Alberta")
df_NumOfJob_2016_ByEducation = df_NumOfJob_2016.loc[
    (df_NumOfJob_2016['Characteristics'] == 'High school diploma and less') |
    (df_NumOfJob_2016['Characteristics'] == 'Trade certificate') |
    (df_NumOfJob_2016['Characteristics'] == 'University degree and higher')
]
# print(df_NumOfJob_2016_ByEducation.head(20))
grouped = df_NumOfJob_2016_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_NumOfJob_2016_ByEducation.index))

print("\nImmigrant group in Alberta")
df_NumOfJob_2016_ByImmigrant = df_NumOfJob_2016.loc[
    (df_NumOfJob_2016['Characteristics'] == 'Immigrant employees') |
    (df_NumOfJob_2016['Characteristics'] == 'Non-immigrant employees')
]
# print(df_NumOfJob_2016_ByImmigrant.head(20))
grouped = df_NumOfJob_2016_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_NumOfJob_2016_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_NumOfJob_2016_ByIndigenous = df_NumOfJob_2016.loc[
#     (df_NumOfJob_2016['Characteristics'] == 'Indigenous identity employees') |
#     (df_NumOfJob_2016['Characteristics'] == 'Non-indigenous identity employees')
# ]
# # print(df_NumOfJob_2016_ByIndigenous.head(20))
# grouped = df_NumOfJob_2016_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_NumOfJob_2016_ByIndigenous.index))

# %%
# Dataset year in 2019 inside "Number of jobs"

print("\nAge group in Alberta")
df_NumOfJob_2019_ByAge = df_NumOfJob_2019.loc[
    (df_NumOfJob_2019['Characteristics'] == '15 to 24 years') |
    (df_NumOfJob_2019['Characteristics'] == '25 to 34 years') |
    (df_NumOfJob_2019['Characteristics'] == '35 to 44 years') |
    (df_NumOfJob_2019['Characteristics'] == '45 to 54 years') |
    (df_NumOfJob_2019['Characteristics'] == '55 to 64 years') |
    (df_NumOfJob_2019['Characteristics'] == '65 years old and over')]
# print(df_NumOfJob_2019_ByAge.head(20))
grouped = df_NumOfJob_2019_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_NumOfJob_2019_ByAge.index))

print("\nGender group in Alberta")
df_NumOfJob_2019_ByGender = df_NumOfJob_2019.loc[
    (df_NumOfJob_2019['Characteristics'] == 'Female employees') |
    (df_NumOfJob_2019['Characteristics'] == 'Male employees')
]
# print(df_NumOfJob_2019_ByGender.head(20))
grouped = df_NumOfJob_2019_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_NumOfJob_2019_ByGender.index))

print("\nEducation group in Alberta")
df_NumOfJob_2019_ByEducation = df_NumOfJob_2019.loc[
    (df_NumOfJob_2019['Characteristics'] == 'High school diploma and less') |
    (df_NumOfJob_2019['Characteristics'] == 'Trade certificate') |
    (df_NumOfJob_2019['Characteristics'] == 'University degree and higher')
]
# print(df_NumOfJob_2019_ByEducation.head(20))
grouped = df_NumOfJob_2019_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_NumOfJob_2019_ByEducation.index))

print("\nImmigrant group in Alberta")
df_NumOfJob_2019_ByImmigrant = df_NumOfJob_2019.loc[
    (df_NumOfJob_2019['Characteristics'] == 'Immigrant employees') |
    (df_NumOfJob_2019['Characteristics'] == 'Non-immigrant employees')
]
# print(df_NumOfJob_2019_ByImmigrant.head(20))
grouped = df_NumOfJob_2019_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_NumOfJob_2019_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_NumOfJob_2019_ByIndigenous = df_NumOfJob_2019.loc[
#     (df_NumOfJob_2019['Characteristics'] == 'Indigenous identity employees') |
#     (df_NumOfJob_2019['Characteristics'] == 'Non-indigenous identity employees')
# ]
# # print(df_NumOfJob_2019_ByIndigenous.head(20))
# grouped = df_NumOfJob_2019_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_NumOfJob_2019_ByIndigenous.index))

# %% [markdown]
# Filtered for "Wages and Salaries" by following: "Age group", "Gender level", "Education level", and "Immigration status". <br />
# "Aboriginal status" has been commented.

# %%
# # Dataset year in 2010 inside "Wages and Salaries"

# print("\nAge group in Alberta")
# df_WagesAndSalaries_2010_ByAge = df_WagesAndSalaries_2010.loc[
#     (df_WagesAndSalaries_2010['Characteristics'] == '15 to 24 years') |
#     (df_WagesAndSalaries_2010['Characteristics'] == '25 to 34 years') |
#     (df_WagesAndSalaries_2010['Characteristics'] == '35 to 44 years') |
#     (df_WagesAndSalaries_2010['Characteristics'] == '45 to 54 years') |
#     (df_WagesAndSalaries_2010['Characteristics'] == '55 to 64 years') |
#     (df_WagesAndSalaries_2010['Characteristics'] == '65 years old and over')]
# # print(df_WagesAndSalaries_2010_ByAge.head(20))
# grouped = df_WagesAndSalaries_2010_ByAge.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_WagesAndSalaries_2010_ByAge.index))

# print("\nGender group in Alberta")
# df_WagesAndSalaries_2010_ByGender = df_WagesAndSalaries_2010.loc[
#     (df_WagesAndSalaries_2010['Characteristics'] == 'Female employees') |
#     (df_WagesAndSalaries_2010['Characteristics'] == 'Male employees')
# ]
# # print(df_WagesAndSalaries_2010_ByGender.head(20))
# grouped = df_WagesAndSalaries_2010_ByGender.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_WagesAndSalaries_2010_ByGender.index))

# print("\nEducation group in Alberta")
# df_WagesAndSalaries_2010_ByEducation = df_WagesAndSalaries_2010.loc[
#     (df_WagesAndSalaries_2010['Characteristics'] == 'High school diploma and less') |
#     (df_WagesAndSalaries_2010['Characteristics'] == 'Trade certificate') |
#     (df_WagesAndSalaries_2010['Characteristics'] == 'University degree and higher')
# ]
# # print(df_WagesAndSalaries_2010_ByEducation.head(20))
# grouped = df_WagesAndSalaries_2010_ByEducation.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_WagesAndSalaries_2010_ByEducation.index))

# print("\nImmigrant group in Alberta")
# df_WagesAndSalaries_2010_ByImmigrant = df_WagesAndSalaries_2010.loc[
#     (df_WagesAndSalaries_2010['Characteristics'] == 'Immigrant employees') |
#     (df_WagesAndSalaries_2010['Characteristics'] == 'Non-immigrant employees')
# ]
# # print(df_WagesAndSalaries_2010_ByImmigrant.head(20))
# grouped = df_WagesAndSalaries_2010_ByImmigrant.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_WagesAndSalaries_2010_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_WagesAndSalaries_2010_ByIndigenous = df_WagesAndSalaries_2010.loc[
#     (df_WagesAndSalaries_2010['Characteristics'] == 'Indigenous identity employees') |
#     (df_WagesAndSalaries_2010['Characteristics'] == 'Non-indigenous identity employees')
# ]
# # print(df_WagesAndSalaries_2010_ByIndigenous.head(20))
# grouped = df_WagesAndSalaries_2010_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_WagesAndSalaries_2010_ByIndigenous.index))

# %%
# Dataset year in 2013 inside "Wages and Salaries"

print("\nAge group in Alberta")
df_WagesAndSalaries_2013_ByAge = df_WagesAndSalaries_2013.loc[
    (df_WagesAndSalaries_2013['Characteristics'] == '15 to 24 years') |
    (df_WagesAndSalaries_2013['Characteristics'] == '25 to 34 years') |
    (df_WagesAndSalaries_2013['Characteristics'] == '35 to 44 years') |
    (df_WagesAndSalaries_2013['Characteristics'] == '45 to 54 years') |
    (df_WagesAndSalaries_2013['Characteristics'] == '55 to 64 years') |
    (df_WagesAndSalaries_2013['Characteristics'] == '65 years old and over')]
# print(df_WagesAndSalaries_2013_ByAge.head(20))
grouped = df_WagesAndSalaries_2013_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_WagesAndSalaries_2013_ByAge.index))

print("\nGender group in Alberta")
df_WagesAndSalaries_2013_ByGender = df_WagesAndSalaries_2013.loc[
    (df_WagesAndSalaries_2013['Characteristics'] == 'Female employees') |
    (df_WagesAndSalaries_2013['Characteristics'] == 'Male employees')
]
# print(df_WagesAndSalaries_2013_ByGender.head(20))
grouped = df_WagesAndSalaries_2013_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_WagesAndSalaries_2013_ByGender.index))

print("\nEducation group in Alberta")
df_WagesAndSalaries_2013_ByEducation = df_WagesAndSalaries_2013.loc[
    (df_WagesAndSalaries_2013['Characteristics'] == 'High school diploma and less') |
    (df_WagesAndSalaries_2013['Characteristics'] == 'Trade certificate') |
    (df_WagesAndSalaries_2013['Characteristics'] == 'University degree and higher')
]
# print(df_WagesAndSalaries_2013_ByEducation.head(20))
grouped = df_WagesAndSalaries_2013_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_WagesAndSalaries_2013_ByEducation.index))

print("\nImmigrant group in Alberta")
df_WagesAndSalaries_2013_ByImmigrant = df_WagesAndSalaries_2013.loc[
    (df_WagesAndSalaries_2013['Characteristics'] == 'Immigrant employees') |
    (df_WagesAndSalaries_2013['Characteristics'] == 'Non-immigrant employees')
]
# print(df_WagesAndSalaries_2013_ByImmigrant.head(20))
grouped = df_WagesAndSalaries_2013_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_WagesAndSalaries_2013_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_WagesAndSalaries_2013_ByIndigenous = df_WagesAndSalaries_2013.loc[
#     (df_WagesAndSalaries_2013['Characteristics'] == 'Indigenous identity employees') |
#     (df_WagesAndSalaries_2013['Characteristics'] == 'Non-indigenous identity employees')
# ]
# # print(df_WagesAndSalaries_2013_ByIndigenous.head(20))
# grouped = df_WagesAndSalaries_2013_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_WagesAndSalaries_2013_ByIndigenous.index))

# %%
# Dataset year in 2016 inside "Wages and Salaries"

print("\nAge group in Alberta")
df_WagesAndSalaries_2016_ByAge = df_WagesAndSalaries_2016.loc[
    (df_WagesAndSalaries_2016['Characteristics'] == '15 to 24 years') |
    (df_WagesAndSalaries_2016['Characteristics'] == '25 to 34 years') |
    (df_WagesAndSalaries_2016['Characteristics'] == '35 to 44 years') |
    (df_WagesAndSalaries_2016['Characteristics'] == '45 to 54 years') |
    (df_WagesAndSalaries_2016['Characteristics'] == '55 to 64 years') |
    (df_WagesAndSalaries_2016['Characteristics'] == '65 years old and over')]
# print(df_WagesAndSalaries_2016_ByAge.head(20))
grouped = df_WagesAndSalaries_2016_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_WagesAndSalaries_2016_ByAge.index))

print("\nGender group in Alberta")
df_WagesAndSalaries_2016_ByGender = df_WagesAndSalaries_2016.loc[
    (df_WagesAndSalaries_2016['Characteristics'] == 'Female employees') |
    (df_WagesAndSalaries_2016['Characteristics'] == 'Male employees')
]
# print(df_WagesAndSalaries_2016_ByGender.head(20))
grouped = df_WagesAndSalaries_2016_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_WagesAndSalaries_2016_ByGender.index))

print("\nEducation group in Alberta")
df_WagesAndSalaries_2016_ByEducation = df_WagesAndSalaries_2016.loc[
    (df_WagesAndSalaries_2016['Characteristics'] == 'High school diploma and less') |
    (df_WagesAndSalaries_2016['Characteristics'] == 'Trade certificate') |
    (df_WagesAndSalaries_2016['Characteristics'] == 'University degree and higher')
]
# print(df_WagesAndSalaries_2016_ByEducation.head(20))
grouped = df_WagesAndSalaries_2016_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_WagesAndSalaries_2016_ByEducation.index))

print("\nImmigrant group in Alberta")
df_WagesAndSalaries_2016_ByImmigrant = df_WagesAndSalaries_2016.loc[
    (df_WagesAndSalaries_2016['Characteristics'] == 'Immigrant employees') |
    (df_WagesAndSalaries_2016['Characteristics'] == 'Non-immigrant employees')
]
# print(df_WagesAndSalaries_2016_ByImmigrant.head(20))
grouped = df_WagesAndSalaries_2016_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_WagesAndSalaries_2016_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_WagesAndSalaries_2016_ByIndigenous = df_WagesAndSalaries_2016.loc[
#     (df_WagesAndSalaries_2016['Characteristics'] == 'Indigenous identity employees') |
#     (df_WagesAndSalaries_2016['Characteristics'] == 'Non-indigenous identity employees')
# ]
# # print(df_WagesAndSalaries_2016_ByIndigenous.head(20))
# grouped = df_WagesAndSalaries_2016_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_WagesAndSalaries_2016_ByIndigenous.index))


# %%
# Dataset year in 2019 inside "Wages and Salaries"

print("\nAge group in Alberta")
df_WagesAndSalaries_2019_ByAge = df_WagesAndSalaries_2019.loc[
    (df_WagesAndSalaries_2019['Characteristics'] == '15 to 24 years') |
    (df_WagesAndSalaries_2019['Characteristics'] == '25 to 34 years') |
    (df_WagesAndSalaries_2019['Characteristics'] == '35 to 44 years') |
    (df_WagesAndSalaries_2019['Characteristics'] == '45 to 54 years') |
    (df_WagesAndSalaries_2019['Characteristics'] == '55 to 64 years') |
    (df_WagesAndSalaries_2019['Characteristics'] == '65 years old and over')]
# print(df_WagesAndSalaries_2019_ByAge.head(20))
grouped = df_WagesAndSalaries_2019_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_WagesAndSalaries_2019_ByAge.index))

print("\nGender group in Alberta")
df_WagesAndSalaries_2019_ByGender = df_WagesAndSalaries_2019.loc[
    (df_WagesAndSalaries_2019['Characteristics'] == 'Female employees') |
    (df_WagesAndSalaries_2019['Characteristics'] == 'Male employees')
]
# print(df_WagesAndSalaries_2019_ByGender.head(20))
grouped = df_WagesAndSalaries_2019_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_WagesAndSalaries_2019_ByGender.index))

print("\nEducation group in Alberta")
df_WagesAndSalaries_2019_ByEducation = df_WagesAndSalaries_2019.loc[
    (df_WagesAndSalaries_2019['Characteristics'] == 'High school diploma and less') |
    (df_WagesAndSalaries_2019['Characteristics'] == 'Trade certificate') |
    (df_WagesAndSalaries_2019['Characteristics'] == 'University degree and higher')
]
# print(df_WagesAndSalaries_2019_ByEducation.head(20))
grouped = df_WagesAndSalaries_2019_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_WagesAndSalaries_2019_ByEducation.index))

print("\nImmigrant group in Alberta")
df_WagesAndSalaries_2019_ByImmigrant = df_WagesAndSalaries_2019.loc[
    (df_WagesAndSalaries_2019['Characteristics'] == 'Immigrant employees') |
    (df_WagesAndSalaries_2019['Characteristics'] == 'Non-immigrant employees')
]
# print(df_WagesAndSalaries_2019_ByImmigrant.head(20))
grouped = df_WagesAndSalaries_2019_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_WagesAndSalaries_2019_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_WagesAndSalaries_2019_ByIndigenous = df_WagesAndSalaries_2019.loc[
#     (df_WagesAndSalaries_2019['Characteristics'] == 'Indigenous identity employees') |
#     (df_WagesAndSalaries_2019['Characteristics'] == 'Non-indigenous identity employees')
# ]
# # print(df_WagesAndSalaries_2019_ByIndigenous.head(20))
# grouped = df_WagesAndSalaries_2019_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_WagesAndSalaries_2019_ByIndigenous.index))

# %% [markdown]
# Final output for Average annual hours worked

# %%
# dfa_Target_To_Analysis = [df_AvgAnnHrsWrk_2010_ByAge, df_AvgAnnHrsWrk_2010_ByEducation, df_AvgAnnHrsWrk_2010_ByEducation, df_AvgAnnHrsWrk_2010_ByImmigrant]
# for df_Target_To_Analysis in dfa_Target_To_Analysis:
#       grouped = df_Target_To_Analysis.groupby(['Characteristics'])
#       print("Year of 2010")
#       print(grouped['VALUE'].agg([np.sum, np.mean, np.min, np.median, np.max, np.size]))
#       print("Overall,")
#       print("Sum : ",np.sum(df_Target_To_Analysis['VALUE']))
#       print("Mean : ",np.mean(df_Target_To_Analysis['VALUE']))
#       print("Min/median/max :",np.min(df_Target_To_Analysis['VALUE']),"/",
#             np.median(df_Target_To_Analysis['VALUE']),"/",
#             np.max(df_Target_To_Analysis['VALUE']))
#       print("Skewnewss : ",df_Target_To_Analysis['VALUE'].skew())
#       print("Total size : ",len(df_Target_To_Analysis.index))

# print()
dfa_Target_To_Analysis = [df_AvgAnnHrsWrk_2013_ByAge, df_AvgAnnHrsWrk_2013_ByEducation, df_AvgAnnHrsWrk_2013_ByEducation, df_AvgAnnHrsWrk_2013_ByImmigrant]
for df_Target_To_Analysis in dfa_Target_To_Analysis:
      grouped = df_Target_To_Analysis.groupby(['Characteristics'])
      print("Year of 2013")
      print(grouped['VALUE'].agg([np.sum, np.mean, np.min, np.median, np.max, np.size]))
      print("Overall,")
      print("Sum : ",np.sum(df_Target_To_Analysis['VALUE']))
      print("Mean : ",np.mean(df_Target_To_Analysis['VALUE']))
      print("Min/median/max :",np.min(df_Target_To_Analysis['VALUE']),"/",
            np.median(df_Target_To_Analysis['VALUE']),"/",
            np.max(df_Target_To_Analysis['VALUE']))
      print("Skewnewss : ",df_Target_To_Analysis['VALUE'].skew())
      print("Total size : ",len(df_Target_To_Analysis.index))

print()
dfa_Target_To_Analysis = [df_AvgAnnHrsWrk_2016_ByAge, df_AvgAnnHrsWrk_2016_ByEducation, df_AvgAnnHrsWrk_2016_ByEducation, df_AvgAnnHrsWrk_2016_ByImmigrant]
for df_Target_To_Analysis in dfa_Target_To_Analysis:
      grouped = df_Target_To_Analysis.groupby(['Characteristics'])
      print("Year of 2016")
      print(grouped['VALUE'].agg([np.sum, np.mean, np.min, np.median, np.max, np.size]))
      print("Overall,")
      print("Sum : ",np.sum(df_Target_To_Analysis['VALUE']))
      print("Mean : ",np.mean(df_Target_To_Analysis['VALUE']))
      print("Min/median/max :",np.min(df_Target_To_Analysis['VALUE']),"/",
            np.median(df_Target_To_Analysis['VALUE']),"/",
            np.max(df_Target_To_Analysis['VALUE']))
      print("Skewnewss : ",df_Target_To_Analysis['VALUE'].skew())
      print("Total size : ",len(df_Target_To_Analysis.index))

print()
dfa_Target_To_Analysis = [df_AvgAnnHrsWrk_2019_ByAge, df_AvgAnnHrsWrk_2019_ByEducation, df_AvgAnnHrsWrk_2019_ByEducation, df_AvgAnnHrsWrk_2019_ByImmigrant]
for df_Target_To_Analysis in dfa_Target_To_Analysis:
      grouped = df_Target_To_Analysis.groupby(['Characteristics'])
      print("Year of 2020")
      print(grouped['VALUE'].agg([np.sum, np.mean, np.min, np.median, np.max, np.size]))
      print("Overall,")
      print("Sum : ",np.sum(df_Target_To_Analysis['VALUE']))
      print("Mean : ",np.mean(df_Target_To_Analysis['VALUE']))
      print("Min/median/max :",np.min(df_Target_To_Analysis['VALUE']),"/",
            np.median(df_Target_To_Analysis['VALUE']),"/",
            np.max(df_Target_To_Analysis['VALUE']))
      print("Skewnewss : ",df_Target_To_Analysis['VALUE'].skew())
      print("Total size : ",len(df_Target_To_Analysis.index))

# %% [markdown]
# Final output for "Average annual wages and salaries"

# %%
# dfa_Target_To_Analysis = [df_AvgAnnWages_2010_ByAge, df_AvgAnnWages_2010_ByEducation, df_AvgAnnWages_2010_ByEducation, df_AvgAnnWages_2010_ByImmigrant]
# for df_Target_To_Analysis in dfa_Target_To_Analysis:
#       grouped = df_Target_To_Analysis.groupby(['Characteristics'])
#       print("Year of 2010")
#       print(grouped['VALUE'].agg([np.sum, np.mean, np.min, np.median, np.max, np.size]))
#       print("Overall,")
#       print("Sum : ",np.sum(df_Target_To_Analysis['VALUE']))
#       print("Mean : ",np.mean(df_Target_To_Analysis['VALUE']))
#       print("Min/median/max :",np.min(df_Target_To_Analysis['VALUE']),"/",
#             np.median(df_Target_To_Analysis['VALUE']),"/",
#             np.max(df_Target_To_Analysis['VALUE']))
#       print("Skewnewss : ",df_Target_To_Analysis['VALUE'].skew())
#       print("Total size : ",len(df_Target_To_Analysis.index))

# print()
dfa_Target_To_Analysis = [df_AvgAnnWages_2013_ByAge, df_AvgAnnWages_2013_ByEducation, df_AvgAnnWages_2013_ByEducation, df_AvgAnnWages_2013_ByImmigrant]
for df_Target_To_Analysis in dfa_Target_To_Analysis:
      grouped = df_Target_To_Analysis.groupby(['Characteristics'])
      print("Year of 2013")
      print(grouped['VALUE'].agg([np.sum, np.mean, np.min, np.median, np.max, np.size]))
      print("Overall,")
      print("Sum : ",np.sum(df_Target_To_Analysis['VALUE']))
      print("Mean : ",np.mean(df_Target_To_Analysis['VALUE']))
      print("Min/median/max :",np.min(df_Target_To_Analysis['VALUE']),"/",
            np.median(df_Target_To_Analysis['VALUE']),"/",
            np.max(df_Target_To_Analysis['VALUE']))
      print("Skewnewss : ",df_Target_To_Analysis['VALUE'].skew())
      print("Total size : ",len(df_Target_To_Analysis.index))

print()
dfa_Target_To_Analysis = [df_AvgAnnWages_2016_ByAge, df_AvgAnnWages_2016_ByEducation, df_AvgAnnWages_2016_ByEducation, df_AvgAnnWages_2016_ByImmigrant]
for df_Target_To_Analysis in dfa_Target_To_Analysis:
      grouped = df_Target_To_Analysis.groupby(['Characteristics'])
      print("Year of 2016")
      print(grouped['VALUE'].agg([np.sum, np.mean, np.min, np.median, np.max, np.size]))
      print("Overall,")
      print("Sum : ",np.sum(df_Target_To_Analysis['VALUE']))
      print("Mean : ",np.mean(df_Target_To_Analysis['VALUE']))
      print("Min/median/max :",np.min(df_Target_To_Analysis['VALUE']),"/",
            np.median(df_Target_To_Analysis['VALUE']),"/",
            np.max(df_Target_To_Analysis['VALUE']))
      print("Skewnewss : ",df_Target_To_Analysis['VALUE'].skew())
      print("Total size : ",len(df_Target_To_Analysis.index))

print()
dfa_Target_To_Analysis = [df_AvgAnnWages_2019_ByAge, df_AvgAnnWages_2019_ByEducation, df_AvgAnnWages_2019_ByEducation, df_AvgAnnWages_2019_ByImmigrant]
for df_Target_To_Analysis in dfa_Target_To_Analysis:
      grouped = df_Target_To_Analysis.groupby(['Characteristics'])
      print("Year of 2020")
      print(grouped['VALUE'].agg([np.sum, np.mean, np.min, np.median, np.max, np.size]))
      print("Overall,")
      print("Sum : ",np.sum(df_Target_To_Analysis['VALUE']))
      print("Mean : ",np.mean(df_Target_To_Analysis['VALUE']))
      print("Min/median/max :",np.min(df_Target_To_Analysis['VALUE']),"/",
            np.median(df_Target_To_Analysis['VALUE']),"/",
            np.max(df_Target_To_Analysis['VALUE']))
      print("Skewnewss : ",df_Target_To_Analysis['VALUE'].skew())
      print("Total size : ",len(df_Target_To_Analysis.index))

# %% [markdown]
# Final output for "Average hourly wage"

# %%
# dfa_Target_To_Analysis = [df_AvgHrsWages_2010_ByAge, df_AvgHrsWages_2010_ByEducation, df_AvgHrsWages_2010_ByEducation, df_AvgHrsWages_2010_ByImmigrant]
# for df_Target_To_Analysis in dfa_Target_To_Analysis:
#       grouped = df_Target_To_Analysis.groupby(['Characteristics'])
#       print("Year of 2010")
#       print(grouped['VALUE'].agg([np.sum, np.mean, np.min, np.median, np.max, np.size]))
#       print("Overall,")
#       print("Sum : ",np.sum(df_Target_To_Analysis['VALUE']))
#       print("Mean : ",np.mean(df_Target_To_Analysis['VALUE']))
#       print("Min/median/max :",np.min(df_Target_To_Analysis['VALUE']),"/",
#             np.median(df_Target_To_Analysis['VALUE']),"/",
#             np.max(df_Target_To_Analysis['VALUE']))
#       print("Skewnewss : ",df_Target_To_Analysis['VALUE'].skew())
#       print("Total size : ",len(df_Target_To_Analysis.index))

# print()
dfa_Target_To_Analysis = [df_AvgHrsWages_2013_ByAge, df_AvgHrsWages_2013_ByEducation, df_AvgHrsWages_2013_ByEducation, df_AvgHrsWages_2013_ByImmigrant]
for df_Target_To_Analysis in dfa_Target_To_Analysis:
      grouped = df_Target_To_Analysis.groupby(['Characteristics'])
      print("Year of 2013")
      print(grouped['VALUE'].agg([np.sum, np.mean, np.min, np.median, np.max, np.size]))
      print("Overall,")
      print("Sum : ",np.sum(df_Target_To_Analysis['VALUE']))
      print("Mean : ",np.mean(df_Target_To_Analysis['VALUE']))
      print("Min/median/max :",np.min(df_Target_To_Analysis['VALUE']),"/",
            np.median(df_Target_To_Analysis['VALUE']),"/",
            np.max(df_Target_To_Analysis['VALUE']))
      print("Skewnewss : ",df_Target_To_Analysis['VALUE'].skew())
      print("Total size : ",len(df_Target_To_Analysis.index))

print()
dfa_Target_To_Analysis = [df_AvgHrsWages_2016_ByAge, df_AvgHrsWages_2016_ByEducation, df_AvgHrsWages_2016_ByEducation, df_AvgHrsWages_2016_ByImmigrant]
for df_Target_To_Analysis in dfa_Target_To_Analysis:
      grouped = df_Target_To_Analysis.groupby(['Characteristics'])
      print("Year of 2016")
      print(grouped['VALUE'].agg([np.sum, np.mean, np.min, np.median, np.max, np.size]))
      print("Overall,")
      print("Sum : ",np.sum(df_Target_To_Analysis['VALUE']))
      print("Mean : ",np.mean(df_Target_To_Analysis['VALUE']))
      print("Min/median/max :",np.min(df_Target_To_Analysis['VALUE']),"/",
            np.median(df_Target_To_Analysis['VALUE']),"/",
            np.max(df_Target_To_Analysis['VALUE']))
      print("Skewnewss : ",df_Target_To_Analysis['VALUE'].skew())
      print("Total size : ",len(df_Target_To_Analysis.index))

print()
dfa_Target_To_Analysis = [df_AvgHrsWages_2019_ByAge, df_AvgHrsWages_2019_ByEducation, df_AvgHrsWages_2019_ByEducation, df_AvgHrsWages_2019_ByImmigrant]
for df_Target_To_Analysis in dfa_Target_To_Analysis:
      grouped = df_Target_To_Analysis.groupby(['Characteristics'])
      print("Year of 2019")
      print(grouped['VALUE'].agg([np.sum, np.mean, np.min, np.median, np.max, np.size]))
      print("Overall,")
      print("Sum : ",np.sum(df_Target_To_Analysis['VALUE']))
      print("Mean : ",np.mean(df_Target_To_Analysis['VALUE']))
      print("Min/median/max :",np.min(df_Target_To_Analysis['VALUE']),"/",
            np.median(df_Target_To_Analysis['VALUE']),"/",
            np.max(df_Target_To_Analysis['VALUE']))
      print("Skewnewss : ",df_Target_To_Analysis['VALUE'].skew())
      print("Total size : ",len(df_Target_To_Analysis.index))

# %% [markdown]
# Final output for "Average weekly hours worked"

# %%
# dfa_Target_To_Analysis = [df_AvgWeekHrsWrked_2010_ByAge, df_AvgWeekHrsWrked_2010_ByEducation, df_AvgWeekHrsWrked_2010_ByEducation, df_AvgWeekHrsWrked_2010_ByImmigrant]
# for df_Target_To_Analysis in dfa_Target_To_Analysis:
#       grouped = df_Target_To_Analysis.groupby(['Characteristics'])
#       print("Year of 2010")
#       print(grouped['VALUE'].agg([np.sum, np.mean, np.min, np.median, np.max, np.size]))
#       print("Overall,")
#       print("Sum : ",np.sum(df_Target_To_Analysis['VALUE']))
#       print("Mean : ",np.mean(df_Target_To_Analysis['VALUE']))
#       print("Min/median/max :",np.min(df_Target_To_Analysis['VALUE']),"/",
#             np.median(df_Target_To_Analysis['VALUE']),"/",
#             np.max(df_Target_To_Analysis['VALUE']))
#       print("Skewnewss : ",df_Target_To_Analysis['VALUE'].skew())
#       print("Total size : ",len(df_Target_To_Analysis.index))

# print()
dfa_Target_To_Analysis = [df_AvgWeekHrsWrked_2013_ByAge, df_AvgWeekHrsWrked_2013_ByEducation, df_AvgWeekHrsWrked_2013_ByEducation, df_AvgWeekHrsWrked_2013_ByImmigrant]
for df_Target_To_Analysis in dfa_Target_To_Analysis:
      grouped = df_Target_To_Analysis.groupby(['Characteristics'])
      print("Year of 2013")
      print(grouped['VALUE'].agg([np.sum, np.mean, np.min, np.median, np.max, np.size]))
      print("Overall,")
      print("Sum : ",np.sum(df_Target_To_Analysis['VALUE']))
      print("Mean : ",np.mean(df_Target_To_Analysis['VALUE']))
      print("Min/median/max :",np.min(df_Target_To_Analysis['VALUE']),"/",
            np.median(df_Target_To_Analysis['VALUE']),"/",
            np.max(df_Target_To_Analysis['VALUE']))
      print("Skewnewss : ",df_Target_To_Analysis['VALUE'].skew())
      print("Total size : ",len(df_Target_To_Analysis.index))

print()
dfa_Target_To_Analysis = [df_AvgWeekHrsWrked_2016_ByAge, df_AvgWeekHrsWrked_2016_ByEducation, df_AvgWeekHrsWrked_2016_ByEducation, df_AvgWeekHrsWrked_2016_ByImmigrant]
for df_Target_To_Analysis in dfa_Target_To_Analysis:
      grouped = df_Target_To_Analysis.groupby(['Characteristics'])
      print("Year of 2016")
      print(grouped['VALUE'].agg([np.sum, np.mean, np.min, np.median, np.max, np.size]))
      print("Overall,")
      print("Sum : ",np.sum(df_Target_To_Analysis['VALUE']))
      print("Mean : ",np.mean(df_Target_To_Analysis['VALUE']))
      print("Min/median/max :",np.min(df_Target_To_Analysis['VALUE']),"/",
            np.median(df_Target_To_Analysis['VALUE']),"/",
            np.max(df_Target_To_Analysis['VALUE']))
      print("Skewnewss : ",df_Target_To_Analysis['VALUE'].skew())
      print("Total size : ",len(df_Target_To_Analysis.index))

print()
dfa_Target_To_Analysis = [df_AvgWeekHrsWrked_2019_ByAge, df_AvgWeekHrsWrked_2019_ByEducation, df_AvgWeekHrsWrked_2019_ByEducation, df_AvgWeekHrsWrked_2019_ByImmigrant]
for df_Target_To_Analysis in dfa_Target_To_Analysis:
      grouped = df_Target_To_Analysis.groupby(['Characteristics'])
      print("Year of 2019")
      print(grouped['VALUE'].agg([np.sum, np.mean, np.min, np.median, np.max, np.size]))
      print("Overall,")
      print("Sum : ",np.sum(df_Target_To_Analysis['VALUE']))
      print("Mean : ",np.mean(df_Target_To_Analysis['VALUE']))
      print("Min/median/max :",np.min(df_Target_To_Analysis['VALUE']),"/",
            np.median(df_Target_To_Analysis['VALUE']),"/",
            np.max(df_Target_To_Analysis['VALUE']))
      print("Skewnewss : ",df_Target_To_Analysis['VALUE'].skew())
      print("Total size : ",len(df_Target_To_Analysis.index))

# %% [markdown]
# Final output for "Hours Worked"

# %%
# dfa_Target_To_Analysis = [df_Hrs_Wrked_2010_ByAge, df_Hrs_Wrked_2010_ByEducation, df_Hrs_Wrked_2010_ByEducation, df_Hrs_Wrked_2010_ByImmigrant]
# for df_Target_To_Analysis in dfa_Target_To_Analysis:
#       grouped = df_Target_To_Analysis.groupby(['Characteristics'])
#       print("Year of 2010")
#       print(grouped['VALUE'].agg([np.sum, np.mean, np.min, np.median, np.max, np.size]))
#       print("Overall,")
#       print("Sum : ",np.sum(df_Target_To_Analysis['VALUE']))
#       print("Mean : ",np.mean(df_Target_To_Analysis['VALUE']))
#       print("Min/median/max :",np.min(df_Target_To_Analysis['VALUE']),"/",
#             np.median(df_Target_To_Analysis['VALUE']),"/",
#             np.max(df_Target_To_Analysis['VALUE']))
#       print("Skewnewss : ",df_Target_To_Analysis['VALUE'].skew())
#       print("Total size : ",len(df_Target_To_Analysis.index))

# print()
dfa_Target_To_Analysis = [df_Hrs_Wrked_2013_ByAge, df_Hrs_Wrked_2013_ByEducation, df_Hrs_Wrked_2013_ByEducation, df_Hrs_Wrked_2013_ByImmigrant]
for df_Target_To_Analysis in dfa_Target_To_Analysis:
      grouped = df_Target_To_Analysis.groupby(['Characteristics'])
      print("Year of 2013")
      print(grouped['VALUE'].agg([np.sum, np.mean, np.min, np.median, np.max, np.size]))
      print("Overall,")
      print("Sum : ",np.sum(df_Target_To_Analysis['VALUE']))
      print("Mean : ",np.mean(df_Target_To_Analysis['VALUE']))
      print("Min/median/max :",np.min(df_Target_To_Analysis['VALUE']),"/",
            np.median(df_Target_To_Analysis['VALUE']),"/",
            np.max(df_Target_To_Analysis['VALUE']))
      print("Skewnewss : ",df_Target_To_Analysis['VALUE'].skew())
      print("Total size : ",len(df_Target_To_Analysis.index))

print()
dfa_Target_To_Analysis = [df_Hrs_Wrked_2016_ByAge, df_Hrs_Wrked_2016_ByEducation, df_Hrs_Wrked_2016_ByEducation, df_Hrs_Wrked_2016_ByImmigrant]
for df_Target_To_Analysis in dfa_Target_To_Analysis:
      grouped = df_Target_To_Analysis.groupby(['Characteristics'])
      print("Year of 2016")
      print(grouped['VALUE'].agg([np.sum, np.mean, np.min, np.median, np.max, np.size]))
      print("Overall,")
      print("Sum : ",np.sum(df_Target_To_Analysis['VALUE']))
      print("Mean : ",np.mean(df_Target_To_Analysis['VALUE']))
      print("Min/median/max :",np.min(df_Target_To_Analysis['VALUE']),"/",
            np.median(df_Target_To_Analysis['VALUE']),"/",
            np.max(df_Target_To_Analysis['VALUE']))
      print("Skewnewss : ",df_Target_To_Analysis['VALUE'].skew())
      print("Total size : ",len(df_Target_To_Analysis.index))

print()
dfa_Target_To_Analysis = [df_Hrs_Wrked_2019_ByAge, df_Hrs_Wrked_2019_ByEducation, df_Hrs_Wrked_2019_ByEducation, df_Hrs_Wrked_2019_ByImmigrant]
for df_Target_To_Analysis in dfa_Target_To_Analysis:
      grouped = df_Target_To_Analysis.groupby(['Characteristics'])
      print("Year of 2019")
      print(grouped['VALUE'].agg([np.sum, np.mean, np.min, np.median, np.max, np.size]))
      print("Overall,")
      print("Sum : ",np.sum(df_Target_To_Analysis['VALUE']))
      print("Mean : ",np.mean(df_Target_To_Analysis['VALUE']))
      print("Min/median/max :",np.min(df_Target_To_Analysis['VALUE']),"/",
            np.median(df_Target_To_Analysis['VALUE']),"/",
            np.max(df_Target_To_Analysis['VALUE']))
      print("Skewnewss : ",df_Target_To_Analysis['VALUE'].skew())
      print("Total size : ",len(df_Target_To_Analysis.index))

# %% [markdown]
# Final output for "Number of jobs"

# %%
# dfa_Target_To_Analysis = [df_NumOfJob_2010_ByAge, df_NumOfJob_2010_ByEducation, df_NumOfJob_2010_ByEducation, df_NumOfJob_2010_ByImmigrant]
# for df_Target_To_Analysis in dfa_Target_To_Analysis:
#       grouped = df_Target_To_Analysis.groupby(['Characteristics'])
#       print("Year of 2010")
#       print(grouped['VALUE'].agg([np.sum, np.mean, np.min, np.median, np.max, np.size]))
#       print("Overall,")
#       print("Sum : ",np.sum(df_Target_To_Analysis['VALUE']))
#       print("Mean : ",np.mean(df_Target_To_Analysis['VALUE']))
#       print("Min/median/max :",np.min(df_Target_To_Analysis['VALUE']),"/",
#             np.median(df_Target_To_Analysis['VALUE']),"/",
#             np.max(df_Target_To_Analysis['VALUE']))
#       print("Skewnewss : ",df_Target_To_Analysis['VALUE'].skew())
#       print("Total size : ",len(df_Target_To_Analysis.index))

# print()
dfa_Target_To_Analysis = [df_NumOfJob_2013_ByAge, df_NumOfJob_2013_ByEducation, df_NumOfJob_2013_ByEducation, df_NumOfJob_2013_ByImmigrant]
for df_Target_To_Analysis in dfa_Target_To_Analysis:
      grouped = df_Target_To_Analysis.groupby(['Characteristics'])
      print("Year of 2013")
      print(grouped['VALUE'].agg([np.sum, np.mean, np.min, np.median, np.max, np.size]))
      print("Overall,")
      print("Sum : ",np.sum(df_Target_To_Analysis['VALUE']))
      print("Mean : ",np.mean(df_Target_To_Analysis['VALUE']))
      print("Min/median/max :",np.min(df_Target_To_Analysis['VALUE']),"/",
            np.median(df_Target_To_Analysis['VALUE']),"/",
            np.max(df_Target_To_Analysis['VALUE']))
      print("Skewnewss : ",df_Target_To_Analysis['VALUE'].skew())
      print("Total size : ",len(df_Target_To_Analysis.index))

print()
dfa_Target_To_Analysis = [df_NumOfJob_2016_ByAge, df_NumOfJob_2016_ByEducation, df_NumOfJob_2016_ByEducation, df_NumOfJob_2016_ByImmigrant]
for df_Target_To_Analysis in dfa_Target_To_Analysis:
      grouped = df_Target_To_Analysis.groupby(['Characteristics'])
      print("Year of 2016")
      print(grouped['VALUE'].agg([np.sum, np.mean, np.min, np.median, np.max, np.size]))
      print("Overall,")
      print("Sum : ",np.sum(df_Target_To_Analysis['VALUE']))
      print("Mean : ",np.mean(df_Target_To_Analysis['VALUE']))
      print("Min/median/max :",np.min(df_Target_To_Analysis['VALUE']),"/",
            np.median(df_Target_To_Analysis['VALUE']),"/",
            np.max(df_Target_To_Analysis['VALUE']))
      print("Skewnewss : ",df_Target_To_Analysis['VALUE'].skew())
      print("Total size : ",len(df_Target_To_Analysis.index))

print()
dfa_Target_To_Analysis = [df_NumOfJob_2019_ByAge, df_NumOfJob_2019_ByEducation, df_NumOfJob_2019_ByEducation, df_NumOfJob_2019_ByImmigrant]
for df_Target_To_Analysis in dfa_Target_To_Analysis:
      grouped = df_Target_To_Analysis.groupby(['Characteristics'])
      print("Year of 2019")
      print(grouped['VALUE'].agg([np.sum, np.mean, np.min, np.median, np.max, np.size]))
      print("Overall,")
      print("Sum : ",np.sum(df_Target_To_Analysis['VALUE']))
      print("Mean : ",np.mean(df_Target_To_Analysis['VALUE']))
      print("Min/median/max :",np.min(df_Target_To_Analysis['VALUE']),"/",
            np.median(df_Target_To_Analysis['VALUE']),"/",
            np.max(df_Target_To_Analysis['VALUE']))
      print("Skewnewss : ",df_Target_To_Analysis['VALUE'].skew())
      print("Total size : ",len(df_Target_To_Analysis.index))

# %% [markdown]
# Final output for "Wages and Salaries"

# %%
# dfa_Target_To_Analysis = [df_WagesAndSalaries_2010_ByAge, df_WagesAndSalaries_2010_ByEducation, df_WagesAndSalaries_2010_ByEducation, df_WagesAndSalaries_2010_ByImmigrant]
# for df_Target_To_Analysis in dfa_Target_To_Analysis:
#       grouped = df_Target_To_Analysis.groupby(['Characteristics'])
#       print("Year of 2010")
#       print(grouped['VALUE'].agg([np.sum, np.mean, np.min, np.median, np.max, np.size]))
#       print("Overall,")
#       print("Sum : ",np.sum(df_Target_To_Analysis['VALUE']))
#       print("Mean : ",np.mean(df_Target_To_Analysis['VALUE']))
#       print("Min/median/max :",np.min(df_Target_To_Analysis['VALUE']),"/",
#             np.median(df_Target_To_Analysis['VALUE']),"/",
#             np.max(df_Target_To_Analysis['VALUE']))
#       print("Skewnewss : ",df_Target_To_Analysis['VALUE'].skew())
#       print("Total size : ",len(df_Target_To_Analysis.index))

# print()
dfa_Target_To_Analysis = [df_WagesAndSalaries_2013_ByAge, df_WagesAndSalaries_2013_ByEducation, df_WagesAndSalaries_2013_ByEducation, df_WagesAndSalaries_2013_ByImmigrant]
for df_Target_To_Analysis in dfa_Target_To_Analysis:
      grouped = df_Target_To_Analysis.groupby(['Characteristics'])
      print("Year of 2013")
      print(grouped['VALUE'].agg([np.sum, np.mean, np.min, np.median, np.max, np.size]))
      print("Overall,")
      print("Sum : ",np.sum(df_Target_To_Analysis['VALUE']))
      print("Mean : ",np.mean(df_Target_To_Analysis['VALUE']))
      print("Min/median/max :",np.min(df_Target_To_Analysis['VALUE']),"/",
            np.median(df_Target_To_Analysis['VALUE']),"/",
            np.max(df_Target_To_Analysis['VALUE']))
      print("Skewnewss : ",df_Target_To_Analysis['VALUE'].skew())
      print("Total size : ",len(df_Target_To_Analysis.index))

print()
dfa_Target_To_Analysis = [df_WagesAndSalaries_2016_ByAge, df_WagesAndSalaries_2016_ByEducation, df_WagesAndSalaries_2016_ByEducation, df_WagesAndSalaries_2016_ByImmigrant]
for df_Target_To_Analysis in dfa_Target_To_Analysis:
      grouped = df_Target_To_Analysis.groupby(['Characteristics'])
      print("Year of 2016")
      print(grouped['VALUE'].agg([np.sum, np.mean, np.min, np.median, np.max, np.size]))
      print("Overall,")
      print("Sum : ",np.sum(df_Target_To_Analysis['VALUE']))
      print("Mean : ",np.mean(df_Target_To_Analysis['VALUE']))
      print("Min/median/max :",np.min(df_Target_To_Analysis['VALUE']),"/",
            np.median(df_Target_To_Analysis['VALUE']),"/",
            np.max(df_Target_To_Analysis['VALUE']))
      print("Skewnewss : ",df_Target_To_Analysis['VALUE'].skew())
      print("Total size : ",len(df_Target_To_Analysis.index))

print()
dfa_Target_To_Analysis = [df_WagesAndSalaries_2019_ByAge, df_WagesAndSalaries_2019_ByEducation, df_WagesAndSalaries_2019_ByEducation, df_WagesAndSalaries_2019_ByImmigrant]
for df_Target_To_Analysis in dfa_Target_To_Analysis:
      grouped = df_Target_To_Analysis.groupby(['Characteristics'])
      print("Year of 2019")
      print(grouped['VALUE'].agg([np.sum, np.mean, np.min, np.median, np.max, np.size]))
      print("Overall,")
      print("Sum : ",np.sum(df_Target_To_Analysis['VALUE']))
      print("Mean : ",np.mean(df_Target_To_Analysis['VALUE']))
      print("Min/median/max :",np.min(df_Target_To_Analysis['VALUE']),"/",
            np.median(df_Target_To_Analysis['VALUE']),"/",
            np.max(df_Target_To_Analysis['VALUE']))
      print("Skewnewss : ",df_Target_To_Analysis['VALUE'].skew())
      print("Total size : ",len(df_Target_To_Analysis.index))

# %%
print("Final steps, by sorting out by provinces.")

# -- sum          mean           std  size
# -- GEO                                                                    
# -- Alberta                     2193966.0   2031.450000   2695.836034  1080
# -- British Columbia            2401296.0   2223.422222   2804.925187  1080
# -- Canada                     18252439.0  16900.406481  22232.852533  1080
# -- Manitoba                     767802.0    710.927778    915.637659  1080
# -- New Brunswick                359320.0    332.703704    530.962762  1080
# -- Newfoundland and Labrador    315895.0    306.099806    482.634908  1032
# -- Northwest Territories         42804.0     41.476744     51.817046  1032
# -- Nova Scotia                  531805.0    492.412037    757.119411  1080
# -- Nunavut                       14235.0     15.208333     14.752372   936
# -- Ontario                     6601634.0   6112.624074   7594.433779  1080
# -- Prince Edward Island          77931.0     75.514535    121.297367  1032
# -- Quebec                      4271657.0   3955.237963   5580.294544  1080
# -- Saskatchewan                 650781.0    602.575000    876.896377  1080
# -- Yukon                         16914.0     18.070513     20.188135   936
# -- The total number of this one is  14688


# %% [markdown]
# As final step, I am classifying the data by province. This is the final step, and this is where I will get the final result with.<br />
# For this step, I will use class methods to avoid duplicated and repeatitive steps to do programming.<br />
# For the complex of the analysis, only the dataset of 2013-2015, 2016-2018, 2019-2021 will be used. <br />
# However, 2010-2012 one will get commented.

# %%
print("With year of 2013 and above (three dataset), I will have to analyize, "+str(7*3*4*14)+" times.")
print("\nUse the year from 2010 to 2021 (four dataasets), I will have to analyize, "+str(7*4*4*14)+" times!")

# %% [markdown]
# Main class for Province Analysis:

# %%
# https://www.w3schools.com/python/python_classes.asp
# https://www.w3schools.com/python/python_for_loops.asp
# https://www.educba.com/multidimensional-array-in-python/

class ProvinceAnalysis:

    # Province :
    # -- ['Alberta',  'British Columbia',    'Canada' , 'Manitoba' , 'New Brunswick' 
    # 'Newfoundland and Labrador', 'Northwest Territories' , 'Nova Scotia' , 'Nunavut'
    # 'Ontario' , 'Prince Edward Island', 'Quebec', 'Saskatchewan', 'Yukon']

    def __init__(self, df, pd, np, pp):
        self.df = df
        self.province = ['Alberta',  'British Columbia', 'Canada', 'Manitoba', 
                        'New Brunswick', 'Newfoundland and Labrador', 
                        'Northwest Territories' , 'Nova Scotia' , 'Nunavut',
                        'Ontario' , 'Prince Edward Island', 'Quebec', 
                        'Saskatchewan', 'Yukon'
                        ]
        self.indicator = ["Average annual hours worked",
                        "Average annual wages and salaries",
                        "Average hourly wage",
                        "Average weekly hours worked",
                        "Hours Worked",
                        "Number of jobs",
                        "Wages and Salaries"]
        self.characteristic = ["Age group", "Gender", "Education Level", "Immigrant status", "Aboriginal status"]
        self.year = ["2010",
                    "below 2015",
                    "above 2016",
                    "2013",
                    "2016",
                    "2019"]
        self.pd = pd
        self.np = np
        self.pp = pp
        self.df_ByProvince = []
        for x in self.province:
            df_sorted = df.loc[df['GEO'] == x]
            self.df_ByProvince.append(df_sorted)

    def outputProvince(self, province_id):
        print(self.province[province_id])

    def outputIndicator(self, indicator_id):
        print(self.province[indicator_id])

    def outputCharacteristic(self, cha_id):
        print(self.province[cha_id])

    def outputYear(self, year_id):
        print(self.province[year_id])

    def outputAnalysis(self, province_id):
        print("\nGrab the dataset only in " + str(self.province[province_id]))
        grouped = self.df_ByProvince[province_id].groupby(['Characteristics'])
        print(grouped['VALUE'].agg([np.sum, np.mean, np.min, np.median, np.max, np.size]))
        print("")
        print("Overall,")
        print("Sum : ",np.sum(self.df_ByProvince[province_id]['VALUE']))
        print("Mean : ",np.mean(self.df_ByProvince[province_id]['VALUE']))
        print("Min/median/max :",np.min(self.df_ByProvince[province_id]['VALUE']),"/",
            np.median(self.df_ByProvince[province_id]['VALUE']),"/",
            np.max(self.df_ByProvince[province_id]['VALUE']))
        print("Skewnewss : ",self.df_ByProvince[province_id]['VALUE'].skew())
        print("Total size : ",len(self.df_ByProvince[province_id].index))

    def outputAnalysisSimple(self, province_id):
        print("\nGrab the dataset only in " + str(self.province[province_id]))
        grouped = self.df_ByProvince[province_id].groupby(['Characteristics'])
        print(grouped['VALUE'].agg([self.np.sum, self.np.mean, self.np.size]))

    def outputList(self, province_id, num):
        print("\nGrab the dataset only in " + str(self.province[province_id]))
        print(self.df_ByProvince[province_id].head(num))
        print(self.df_ByProvince[province_id].info())

    def outputPandaProfiling(self, province_id, indicator_id, type_id):

        fileName = str(self.indicator[indicator_id]) + " " + str(self.year[type_id])+" in " + str(self.province[province_id]) + ".html"
        
        pp = ProfileReport(self.df_ByProvince[province_id])
        pp_df = pp.to_html()

        print("File name will be saved under "+str(fileName))
        f = open(fileName, "a")  # Expert into html file without modifying any columns in dataset.
        f.write(pp_df)
        f.close()

# %% [markdown]
# Filtered by provinces by "Average annual hours worked"

# %%
# By Average annual hours worked categories by provinces.

# df_AvgAnnHrsWrk_ByAge_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_ByAge, pd, np, pp)
# df_AvgAnnHrsWrk_2010_ByAge_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByAge, pd, np, pp)
df_AvgAnnHrsWrk_2013_ByAge_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByAge, pd, np, pp)
df_AvgAnnHrsWrk_2016_ByAge_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByAge, pd, np, pp)
df_AvgAnnHrsWrk_2019_ByAge_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByAge, pd, np, pp)

# df_AvgAnnHrsWrk_ByGender_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_ByGender, pd, np, pp)
# df_AvgAnnHrsWrk_2010_ByGender_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByGender, pd, np, pp)
df_AvgAnnHrsWrk_2013_ByGender_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByGender, pd, np, pp)
df_AvgAnnHrsWrk_2016_ByGender_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByGender, pd, np, pp)
df_AvgAnnHrsWrk_2019_ByGender_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByGender, pd, np, pp)

# df_AvgAnnHrsWrk_ByEducation_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_ByEducation, pd, np, pp)
# df_AvgAnnHrsWrk_2010_ByEducation_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation, pd, np, pp)
df_AvgAnnHrsWrk_2013_ByEducation_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation, pd, np, pp)
df_AvgAnnHrsWrk_2016_ByEducation_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByEducation, pd, np, pp)
df_AvgAnnHrsWrk_2019_ByEducation_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation, pd, np, pp)

# df_AvgAnnHrsWrk_ByImmigrant_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_ByImmigrant, pd, np, pp)
# df_AvgAnnHrsWrk_2010_ByImmigrant_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByImmigrant, pd, np, pp)
df_AvgAnnHrsWrk_2013_ByImmigrant_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByImmigrant, pd, np, pp)
df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByImmigrant, pd, np, pp)
df_AvgAnnHrsWrk_2019_ByImmigrant_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByImmigrant, pd, np, pp)

# df_AvgAnnHrsWrk_ByIndigenous_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_ByIndigenous, pd, np, pp)
# df_AvgAnnHrsWrk_2010_ByIndigenous_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByIndigenous, pd, np, pp)
# df_AvgAnnHrsWrk_2013_ByIndigenous_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByIndigenous, pd, np, pp)
# df_AvgAnnHrsWrk_2016_ByIndigenous_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByIndigenous, pd, np, pp)
# df_AvgAnnHrsWrk_2019_ByIndigenous_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByIndigenous, pd, np, pp)

# %% [markdown]
# Filtered by provinces by "Average wages and salaries"

# %%
# By Average annual wages and salaries worked categories by provinces.

# df_AvgAnnWages_ByAge_Provinces = ProvinceAnalysis(df_AvgAnnWages_ByAge, pd, np, pp)
# df_AvgAnnWages_2010_ByAge_Provinces = ProvinceAnalysis(df_AvgAnnWages_2010_ByAge, pd, np, pp)
df_AvgAnnWages_2013_ByAge_Provinces = ProvinceAnalysis(df_AvgAnnWages_2013_ByAge, pd, np, pp)
df_AvgAnnWages_2016_ByAge_Provinces = ProvinceAnalysis(df_AvgAnnWages_2016_ByAge, pd, np, pp)
df_AvgAnnWages_2019_ByAge_Provinces = ProvinceAnalysis(df_AvgAnnWages_2019_ByAge, pd, np, pp)

# df_AvgAnnWages_ByGender_Provinces = ProvinceAnalysis(df_AvgAnnWages_ByGender, pd, np, pp)
# df_AvgAnnWages_2010_ByGender_Provinces = ProvinceAnalysis(df_AvgAnnWages_2010_ByGender, pd, np, pp)
df_AvgAnnWages_2013_ByGender_Provinces = ProvinceAnalysis(df_AvgAnnWages_2013_ByGender, pd, np, pp)
df_AvgAnnWages_2016_ByGender_Provinces = ProvinceAnalysis(df_AvgAnnWages_2016_ByGender, pd, np, pp)
df_AvgAnnWages_2019_ByGender_Provinces = ProvinceAnalysis(df_AvgAnnWages_2019_ByGender, pd, np, pp)

# df_AvgAnnWages_ByEducation_Provinces = ProvinceAnalysis(df_AvgAnnWages_ByEducation, pd, np, pp)
# df_AvgAnnWages_2010_ByEducation_Provinces = ProvinceAnalysis(df_AvgAnnWages_2010_ByEducation, pd, np, pp)
df_AvgAnnWages_2013_ByEducation_Provinces = ProvinceAnalysis(df_AvgAnnWages_2013_ByEducation, pd, np, pp)
df_AvgAnnWages_2016_ByEducation_Provinces = ProvinceAnalysis(df_AvgAnnWages_2016_ByEducation, pd, np, pp)
df_AvgAnnWages_2019_ByEducation_Provinces = ProvinceAnalysis(df_AvgAnnWages_2019_ByEducation, pd, np, pp)

# df_AvgAnnWages_ByImmigrant_Provinces = ProvinceAnalysis(df_AvgAnnWages_ByImmigrant, pd, np, pp)
# df_AvgAnnWages_2010_ByImmigrant_Provinces = ProvinceAnalysis(df_AvgAnnWages_2010_ByImmigrant, pd, np, pp)
df_AvgAnnWages_2013_ByImmigrant_Provinces = ProvinceAnalysis(df_AvgAnnWages_2013_ByImmigrant, pd, np, pp)
df_AvgAnnWages_2016_ByImmigrant_Provinces = ProvinceAnalysis(df_AvgAnnWages_2016_ByImmigrant, pd, np, pp)
df_AvgAnnWages_2019_ByImmigrant_Provinces = ProvinceAnalysis(df_AvgAnnWages_2019_ByImmigrant, pd, np, pp)

# df_AvgAnnWages_ByIndigenous_Provinces = ProvinceAnalysis(df_AvgAnnWages_ByIndigenous, pd, np, pp)
# df_AvgAnnWages_2010_ByIndigenous_Provinces = ProvinceAnalysis(df_AvgAnnWages_2010_ByIndigenous, pd, np, pp)
# df_AvgAnnWages_2013_ByIndigenous_Provinces = ProvinceAnalysis(df_AvgAnnWages_2013_ByIndigenous, pd, np, pp)
# df_AvgAnnWages_2016_ByIndigenous_Provinces = ProvinceAnalysis(df_AvgAnnWages_2016_ByIndigenous, pd, np, pp)
# df_AvgAnnWages_2019_ByIndigenous_Provinces = ProvinceAnalysis(df_AvgAnnWages_2019_ByIndigenous, pd, np, pp)

# %% [markdown]
# Filtered by provinces by "Average hourly wage"

# %%
# By Average hourly wages and salaries worked categories by provinces.

# df_AvgHrsWages_ByAge_Provinces = ProvinceAnalysis(df_AvgHrsWages_ByAge, pd, np, pp)
# df_AvgHrsWages_2010_ByAge_Provinces = ProvinceAnalysis(df_AvgHrsWages_2010_ByAge, pd, np, pp)
df_AvgHrsWages_2013_ByAge_Provinces = ProvinceAnalysis(df_AvgHrsWages_2013_ByAge, pd, np, pp)
df_AvgHrsWages_2016_ByAge_Provinces = ProvinceAnalysis(df_AvgHrsWages_2016_ByAge, pd, np, pp)
df_AvgHrsWages_2019_ByAge_Provinces = ProvinceAnalysis(df_AvgHrsWages_2019_ByAge, pd, np, pp)

# df_AvgHrsWages_ByGender_Provinces = ProvinceAnalysis(df_AvgHrsWages_ByGender, pd, np, pp)
# df_AvgHrsWages_2010_ByGender_Provinces = ProvinceAnalysis(df_AvgHrsWages_2010_ByGender, pd, np, pp)
df_AvgHrsWages_2013_ByGender_Provinces = ProvinceAnalysis(df_AvgHrsWages_2013_ByGender, pd, np, pp)
df_AvgHrsWages_2016_ByGender_Provinces = ProvinceAnalysis(df_AvgHrsWages_2016_ByGender, pd, np, pp)
df_AvgHrsWages_2019_ByGender_Provinces = ProvinceAnalysis(df_AvgHrsWages_2019_ByGender, pd, np, pp)

# df_AvgHrsWages_ByEducation_Provinces = ProvinceAnalysis(df_AvgHrsWages_ByEducation, pd, np, pp)
# df_AvgHrsWages_2010_ByEducation_Provinces = ProvinceAnalysis(df_AvgHrsWages_2010_ByEducation, pd, np, pp)
df_AvgHrsWages_2013_ByEducation_Provinces = ProvinceAnalysis(df_AvgHrsWages_2013_ByEducation, pd, np, pp)
df_AvgHrsWages_2016_ByEducation_Provinces = ProvinceAnalysis(df_AvgHrsWages_2016_ByEducation, pd, np, pp)
df_AvgHrsWages_2019_ByEducation_Provinces = ProvinceAnalysis(df_AvgHrsWages_2019_ByEducation, pd, np, pp)

# df_AvgHrsWages_ByImmigrant_Provinces = ProvinceAnalysis(df_AvgHrsWages_ByImmigrant, pd, np, pp)
# df_AvgHrsWages_2010_ByImmigrant_Provinces = ProvinceAnalysis(df_AvgHrsWages_2010_ByImmigrant, pd, np, pp)
df_AvgHrsWages_2013_ByImmigrant_Provinces = ProvinceAnalysis(df_AvgHrsWages_2013_ByImmigrant, pd, np, pp)
df_AvgHrsWages_2016_ByImmigrant_Provinces = ProvinceAnalysis(df_AvgHrsWages_2016_ByImmigrant, pd, np, pp)
df_AvgHrsWages_2019_ByImmigrant_Provinces = ProvinceAnalysis(df_AvgHrsWages_2019_ByImmigrant, pd, np, pp)

# df_AvgHrsWages_ByIndigenous_Provinces = ProvinceAnalysis(df_AvgHrsWages_ByIndigenous, pd, np, pp)
# df_AvgHrsWages_2010_ByIndigenous_Provinces = ProvinceAnalysis(df_AvgHrsWages_2010_ByIndigenous, pd, np, pp)
# df_AvgHrsWages_2013_ByIndigenous_Provinces = ProvinceAnalysis(df_AvgHrsWages_2013_ByIndigenous, pd, np, pp)
# df_AvgHrsWages_2016_ByIndigenous_Provinces = ProvinceAnalysis(df_AvgHrsWages_2016_ByIndigenous, pd, np, pp)
# df_AvgHrsWages_2019_ByIndigenous_Provinces = ProvinceAnalysis(df_AvgHrsWages_2019_ByIndigenous, pd, np, pp)

# %% [markdown]
# Filtered by provinces by "Average weekly hours worked"

# %%
# By Average annual wages and salaries worked categories by provinces.

# df_AvgWeekHrsWrked_ByAge_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_ByAge, pd, np, pp)
# df_AvgWeekHrsWrked_2010_ByAge_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_2010_ByAge, pd, np, pp)
df_AvgWeekHrsWrked_2013_ByAge_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_2013_ByAge, pd, np, pp)
df_AvgWeekHrsWrked_2016_ByAge_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_2016_ByAge, pd, np, pp)
df_AvgWeekHrsWrked_2019_ByAge_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_2019_ByAge, pd, np, pp)

# df_AvgWeekHrsWrked_ByGender_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_ByGender, pd, np, pp)
# df_AvgWeekHrsWrked_2010_ByGender_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_2010_ByGender, pd, np, pp)
df_AvgWeekHrsWrked_2013_ByGender_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_2013_ByGender, pd, np, pp)
df_AvgWeekHrsWrked_2016_ByGender_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_2016_ByGender, pd, np, pp)
df_AvgWeekHrsWrked_2019_ByGender_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_2019_ByGender, pd, np, pp)

# df_AvgWeekHrsWrked_ByEducation_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_ByEducation, pd, np, pp)
# df_AvgWeekHrsWrked_2010_ByEducation_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_2010_ByEducation, pd, np, pp)
df_AvgWeekHrsWrked_2013_ByEducation_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_2013_ByEducation, pd, np, pp)
df_AvgWeekHrsWrked_2016_ByEducation_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_2016_ByEducation, pd, np, pp)
df_AvgWeekHrsWrked_2019_ByEducation_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_2019_ByEducation, pd, np, pp)

# df_AvgWeekHrsWrked_ByImmigrant_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_ByImmigrant, pd, np, pp)
# df_AvgWeekHrsWrked_2010_ByImmigrant_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_2010_ByImmigrant, pd, np, pp)
df_AvgWeekHrsWrked_2013_ByImmigrant_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_2013_ByImmigrant, pd, np, pp)
df_AvgWeekHrsWrked_2016_ByImmigrant_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_2016_ByImmigrant, pd, np, pp)
df_AvgWeekHrsWrked_2019_ByImmigrant_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_2019_ByImmigrant, pd, np, pp)

# df_AvgWeekHrsWrked_ByIndigenous_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_ByIndigenous, pd, np, pp)
# df_AvgWeekHrsWrked_2010_ByIndigenous_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_2010_ByIndigenous, pd, np, pp)
# df_AvgWeekHrsWrked_2013_ByIndigenous_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_2013_ByIndigenous, pd, np, pp)
# df_AvgWeekHrsWrked_2016_ByIndigenous_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_2016_ByIndigenous, pd, np, pp)
# df_AvgWeekHrsWrked_2019_ByIndigenous_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_2019_ByIndigenous, pd, np, pp)

# %% [markdown]
# Filtered by provinces by "Hours Worked"

# %%
# By Hours workee and salaries worked categories by provinces.

# df_Hrs_Wrked_ByAge_Provinces = ProvinceAnalysis(df_Hrs_Wrked_ByAge, pd, np, pp)
# df_Hrs_Wrked_2010_ByAge_Provinces = ProvinceAnalysis(df_Hrs_Wrked_2010_ByAge, pd, np, pp)
df_Hrs_Wrked_2013_ByAge_Provinces = ProvinceAnalysis(df_Hrs_Wrked_2013_ByAge, pd, np, pp)
df_Hrs_Wrked_2016_ByAge_Provinces = ProvinceAnalysis(df_Hrs_Wrked_2016_ByAge, pd, np, pp)
df_Hrs_Wrked_2019_ByAge_Provinces = ProvinceAnalysis(df_Hrs_Wrked_2019_ByAge, pd, np, pp)

# df_Hrs_Wrked_ByGender_Provinces = ProvinceAnalysis(df_Hrs_Wrked_ByGender, pd, np, pp)
# df_Hrs_Wrked_2010_ByGender_Provinces = ProvinceAnalysis(df_Hrs_Wrked_2010_ByGender, pd, np, pp)
df_Hrs_Wrked_2013_ByGender_Provinces = ProvinceAnalysis(df_Hrs_Wrked_2013_ByGender, pd, np, pp)
df_Hrs_Wrked_2016_ByGender_Provinces = ProvinceAnalysis(df_Hrs_Wrked_2016_ByGender, pd, np, pp)
df_Hrs_Wrked_2019_ByGender_Provinces = ProvinceAnalysis(df_Hrs_Wrked_2019_ByGender, pd, np, pp)

# df_Hrs_Wrked_ByEducation_Provinces = ProvinceAnalysis(df_Hrs_Wrked_ByEducation, pd, np, pp)
# df_Hrs_Wrked_2010_ByEducation_Provinces = ProvinceAnalysis(df_Hrs_Wrked_2010_ByEducation, pd, np, pp)
df_Hrs_Wrked_2013_ByEducation_Provinces = ProvinceAnalysis(df_Hrs_Wrked_2013_ByEducation, pd, np, pp)
df_Hrs_Wrked_2016_ByEducation_Provinces = ProvinceAnalysis(df_Hrs_Wrked_2016_ByEducation, pd, np, pp)
df_Hrs_Wrked_2019_ByEducation_Provinces = ProvinceAnalysis(df_Hrs_Wrked_2019_ByEducation, pd, np, pp)

# df_Hrs_Wrked_ByImmigrant_Provinces = ProvinceAnalysis(df_Hrs_Wrked_ByImmigrant, pd, np, pp)
# df_Hrs_Wrked_2010_ByImmigrant_Provinces = ProvinceAnalysis(df_Hrs_Wrked_2010_ByImmigrant, pd, np, pp)
df_Hrs_Wrked_2013_ByImmigrant_Provinces = ProvinceAnalysis(df_Hrs_Wrked_2013_ByImmigrant, pd, np, pp)
df_Hrs_Wrked_2016_ByImmigrant_Provinces = ProvinceAnalysis(df_Hrs_Wrked_2016_ByImmigrant, pd, np, pp)
df_Hrs_Wrked_2019_ByImmigrant_Provinces = ProvinceAnalysis(df_Hrs_Wrked_2019_ByImmigrant, pd, np, pp)

# df_Hrs_Wrked_ByIndigenous_Provinces = ProvinceAnalysis(df_Hrs_Wrked_ByIndigenous, pd, np, pp)
# df_Hrs_Wrked_2010_ByIndigenous_Provinces = ProvinceAnalysis(df_Hrs_Wrked_2010_ByIndigenous, pd, np, pp)
# df_Hrs_Wrked_2013_ByIndigenous_Provinces = ProvinceAnalysis(df_Hrs_Wrked_2013_ByIndigenous, pd, np, pp)
# df_Hrs_Wrked_2016_ByIndigenous_Provinces = ProvinceAnalysis(df_Hrs_Wrked_2016_ByIndigenous, pd, np, pp)
# df_Hrs_Wrked_2019_ByIndigenous_Provinces = ProvinceAnalysis(df_Hrs_Wrked_2019_ByIndigenous, pd, np, pp)


# %% [markdown]
# Filtered by provinces by "Number of jobs"

# %%
# By Number of jobs and salaries worked categories by provinces.

# df_NumOfJob_ByAge_Provinces = ProvinceAnalysis(df_NumOfJob_ByAge, pd, np, pp)
# df_NumOfJob_2010_ByAge_Provinces = ProvinceAnalysis(df_NumOfJob_2010_ByAge, pd, np, pp)
df_NumOfJob_2013_ByAge_Provinces = ProvinceAnalysis(df_NumOfJob_2013_ByAge, pd, np, pp)
df_NumOfJob_2016_ByAge_Provinces = ProvinceAnalysis(df_NumOfJob_2016_ByAge, pd, np, pp)
df_NumOfJob_2019_ByAge_Provinces = ProvinceAnalysis(df_NumOfJob_2019_ByAge, pd, np, pp)

# df_NumOfJob_ByGender_Provinces = ProvinceAnalysis(df_NumOfJob_ByGender, pd, np, pp)
# df_NumOfJob_2010_ByGender_Provinces = ProvinceAnalysis(df_NumOfJob_2010_ByGender, pd, np, pp)
df_NumOfJob_2013_ByGender_Provinces = ProvinceAnalysis(df_NumOfJob_2013_ByGender, pd, np, pp)
df_NumOfJob_2016_ByGender_Provinces = ProvinceAnalysis(df_NumOfJob_2016_ByGender, pd, np, pp)
df_NumOfJob_2019_ByGender_Provinces = ProvinceAnalysis(df_NumOfJob_2019_ByGender, pd, np, pp)

# df_NumOfJob_ByEducation_Provinces = ProvinceAnalysis(df_NumOfJob_ByEducation, pd, np, pp)
# df_NumOfJob_2010_ByEducation_Provinces = ProvinceAnalysis(df_NumOfJob_2010_ByEducation, pd, np, pp)
df_NumOfJob_2013_ByEducation_Provinces = ProvinceAnalysis(df_NumOfJob_2013_ByEducation, pd, np, pp)
df_NumOfJob_2016_ByEducation_Provinces = ProvinceAnalysis(df_NumOfJob_2016_ByEducation, pd, np, pp)
df_NumOfJob_2019_ByEducation_Provinces = ProvinceAnalysis(df_NumOfJob_2019_ByEducation, pd, np, pp)

# df_NumOfJob_ByImmigrant_Provinces = ProvinceAnalysis(df_NumOfJob_ByImmigrant, pd, np, pp)
# df_NumOfJob_2010_ByImmigrant_Provinces = ProvinceAnalysis(df_NumOfJob_2010_ByImmigrant, pd, np, pp)
df_NumOfJob_2013_ByImmigrant_Provinces = ProvinceAnalysis(df_NumOfJob_2013_ByImmigrant, pd, np, pp)
df_NumOfJob_2016_ByImmigrant_Provinces = ProvinceAnalysis(df_NumOfJob_2016_ByImmigrant, pd, np, pp)
df_NumOfJob_2019_ByImmigrant_Provinces = ProvinceAnalysis(df_NumOfJob_2019_ByImmigrant, pd, np, pp)

# df_NumOfJob_ByIndigenous_Provinces = ProvinceAnalysis(df_NumOfJob_ByIndigenous, pd, np, pp)
# df_NumOfJob_2010_ByIndigenous_Provinces = ProvinceAnalysis(df_NumOfJob_2010_ByIndigenous, pd, np, pp)
# df_NumOfJob_2013_ByIndigenous_Provinces = ProvinceAnalysis(df_NumOfJob_2013_ByIndigenous, pd, np, pp)
# df_NumOfJob_2016_ByIndigenous_Provinces = ProvinceAnalysis(df_NumOfJob_2016_ByIndigenous, pd, np, pp)
# df_NumOfJob_2019_ByIndigenous_Provinces = ProvinceAnalysis(df_NumOfJob_2019_ByIndigenous, pd, np, pp)

# %% [markdown]
# Filted by provinces by "Wages and Salaries"

# %%
# By Wages and Salaries worked categories by provinces.

# df_WagesAndSalaries_ByAge_Provinces = ProvinceAnalysis(df_WagesAndSalaries_ByAge, pd, np, pp)
# df_WagesAndSalaries_2010_ByAge_Provinces = ProvinceAnalysis(df_WagesAndSalaries_2010_ByAge, pd, np, pp)
df_WagesAndSalaries_2013_ByAge_Provinces = ProvinceAnalysis(df_WagesAndSalaries_2013_ByAge, pd, np, pp)
df_WagesAndSalaries_2016_ByAge_Provinces = ProvinceAnalysis(df_WagesAndSalaries_2016_ByAge, pd, np, pp)
df_WagesAndSalaries_2019_ByAge_Provinces = ProvinceAnalysis(df_WagesAndSalaries_2019_ByAge, pd, np, pp)

# df_WagesAndSalaries_ByGender_Provinces = ProvinceAnalysis(df_WagesAndSalaries_ByGender, pd, np, pp)
# df_WagesAndSalaries_2010_ByGender_Provinces = ProvinceAnalysis(df_WagesAndSalaries_2010_ByGender, pd, np, pp)
df_WagesAndSalaries_2013_ByGender_Provinces = ProvinceAnalysis(df_WagesAndSalaries_2013_ByGender, pd, np, pp)
df_WagesAndSalaries_2016_ByGender_Provinces = ProvinceAnalysis(df_WagesAndSalaries_2016_ByGender, pd, np, pp)
df_WagesAndSalaries_2019_ByGender_Provinces = ProvinceAnalysis(df_WagesAndSalaries_2019_ByGender, pd, np, pp)

# df_WagesAndSalaries_ByEducation_Provinces = ProvinceAnalysis(df_WagesAndSalaries_ByEducation, pd, np, pp)
# df_WagesAndSalaries_2010_ByEducation_Provinces = ProvinceAnalysis(df_WagesAndSalaries_2010_ByEducation, pd, np, pp)
df_WagesAndSalaries_2013_ByEducation_Provinces = ProvinceAnalysis(df_WagesAndSalaries_2013_ByEducation, pd, np, pp)
df_WagesAndSalaries_2016_ByEducation_Provinces = ProvinceAnalysis(df_WagesAndSalaries_2016_ByEducation, pd, np, pp)
df_WagesAndSalaries_2019_ByEducation_Provinces = ProvinceAnalysis(df_WagesAndSalaries_2019_ByEducation, pd, np, pp)

# df_WagesAndSalaries_ByImmigrant_Provinces = ProvinceAnalysis(df_WagesAndSalaries_ByImmigrant, pd, np, pp)
# df_WagesAndSalaries_2010_ByImmigrant_Provinces = ProvinceAnalysis(df_WagesAndSalaries_2010_ByImmigrant, pd, np, pp)
df_WagesAndSalaries_2013_ByImmigrant_Provinces = ProvinceAnalysis(df_WagesAndSalaries_2013_ByImmigrant, pd, np, pp)
df_WagesAndSalaries_2016_ByImmigrant_Provinces = ProvinceAnalysis(df_WagesAndSalaries_2016_ByImmigrant, pd, np, pp)
df_WagesAndSalaries_2019_ByImmigrant_Provinces = ProvinceAnalysis(df_WagesAndSalaries_2019_ByImmigrant, pd, np, pp)

# df_WagesAndSalaries_ByIndigenous_Provinces = ProvinceAnalysis(df_WagesAndSalaries_ByIndigenous, pd, np, pp)
# df_WagesAndSalaries_2010_ByIndigenous_Provinces = ProvinceAnalysis(df_WagesAndSalaries_2010_ByIndigenous, pd, np, pp)
# df_WagesAndSalaries_2013_ByIndigenous_Provinces = ProvinceAnalysis(df_WagesAndSalaries_2013_ByIndigenous, pd, np, pp)
# df_WagesAndSalaries_2016_ByIndigenous_Provinces = ProvinceAnalysis(df_WagesAndSalaries_2016_ByIndigenous, pd, np, pp)
# df_WagesAndSalaries_2019_ByIndigenous_Provinces = ProvinceAnalysis(df_WagesAndSalaries_2019_ByIndigenous, pd, np, pp)

# %% [markdown]
# After data analysis of the data, the code below can output the result of the analysis.

# %% [markdown]
# Main class for outputting the analysis

# %%
# https://howtodoinjava.com/python-examples/python-print-to-file/


class OutputProvinceAnalysis:

    # Province :
    # -- ['Alberta',  'British Columbia',    'Canada' , 'Manitoba' , 'New Brunswick' 
    # 'Newfoundland and Labrador', 'Northwest Territories' , 'Nova Scotia' , 'Nunavut'
    # 'Ontario' , 'Prince Edward Island', 'Quebec', 'Saskatchewan', 'Yukon']

    def __init__(self, df, PC, yrs, pd, np, pp):

        self.df_output = df
        self.ProCode = PC
        self.YearOutput = yrs

    def OutputResult(self):
        print(str(self.YearOutput))
        self.df_output.outputList(self.ProCode, 20)
        self.df_output.outputAnalysis(self.ProCode)

    def OutputPandaProfiling(self):
        if self.YearOutput == '2010':
            print("Year 2010 is not valid at this moment")
            # self.df_output.outputPandaProfiling(self.ProCode,0,0)
        elif self.YearOutput == '2013':
            self.df_output.outputPandaProfiling(self.ProCode,0,3)
        elif self.YearOutput == '2016':
            self.df_output.outputPandaProfiling(self.ProCode,0,4)
        elif self.YearOutput == '2018':
            self.df_output.outputPandaProfiling(self.ProCode,0,5)
        else:
            print("Error!")

# %% [markdown]
# Filtering only Alberta.

# %% [markdown]
# Only finished "Average annual hours worked".

# %%
# # -- Alberta                     2193966.0   2031.450000   2695.836034  1080
# (Before)
# print("2016 - Overall")
# df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputList(0, 20)
# df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputAnalysis(0)
# print("2016")
# df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputList(0, 20)
# df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputAnalysis(0)
# print("2018")
# df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputList(0, 20)
# df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputAnalysis(0)
# print("2020")
# df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputList(0, 20)
# df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputAnalysis(0)

# print("2016 - Overall")
# df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputList(0, 20)
# df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputAnalysis(0)
# print("2016")
# df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputList(0, 20)
# df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputAnalysis(0)
# print("2018")
# df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputList(0, 20)
# df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputAnalysis(0)
# print("2020")
# df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputList(0, 20)
# df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputAnalysis(0)

# print("2016 - Overall")
# df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputList(0, 20)
# df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputAnalysis(0)
# print("2016")
# df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputList(0, 20)
# df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputAnalysis(0)
# print("2018")
# df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputList(0, 20)
# df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputAnalysis(0)
# print("2020")
# df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputList(0, 20)
# df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputAnalysis(0)

# print("2016 - Overall")
# df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputList(0, 20)
# df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputAnalysis(0)
# print("2016")
# df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputList(0, 20)
# df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputAnalysis(0)
# print("2018")
# df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputList(0, 20)
# df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputAnalysis(0)
# print("2020")
# df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputList(0, 20)
# df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputAnalysis(0)

# %%
# # -- Alberta                     2193966.0   2031.450000   2695.836034  1080
# (After using the class)

ProCode = 0

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByAge_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByAge_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByAge_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByAge_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByGende_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByGender_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByGender_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByGender_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByEducation_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# %% [markdown]
# Panda Profiling for Final Result for Alberta

# %%
# ProCode = 0
# (Before)
# df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputPandaProfiling(ProCode,0,2)
# df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputPandaProfiling(ProCode,0,2)
# df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputPandaProfiling(ProCode,0,2)
# df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,2)

# df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputPandaProfiling(ProCode,0,3)
# df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputPandaProfiling(ProCode,0,3)
# df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputPandaProfiling(ProCode,0,3)
# df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,3)

# df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputPandaProfiling(ProCode,0,4)
# df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputPandaProfiling(ProCode,0,4)
# df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputPandaProfiling(ProCode,0,4)
# df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,4)

# df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputPandaProfiling(ProCode,0,5)
# df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputPandaProfiling(ProCode,0,5)
# df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputPandaProfiling(ProCode,0,5)
# df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,5)

# %%
# After

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByAge_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByAge_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputPandaProfiling()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByAge_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputPandaProfiling()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByAge_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputPandaProfiling()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByGende_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByGender_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputPandaProfiling()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByGender_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputPandaProfiling()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByGender_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputPandaProfiling()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputPandaProfiling()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByEducation_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputPandaProfiling()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputPandaProfiling()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputPandaProfiling()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputPandaProfiling()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputPandaProfiling()

# %% [markdown]
# Filtering only British Columbia.

# %% [markdown]
# Only finished "Average annual hours worked".

# %%
# -- British Columbia            2401296.0   2223.422222   2804.925187  1080

ProCode = 1

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByAge_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByAge_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByAge_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByAge_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByGende_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByGender_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByGender_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByGender_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByEducation_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# %% [markdown]
# Panda Profiling for Final Result for BC

# %%
# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByAge_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByAge_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByAge_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByAge_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByGende_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByGender_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByGender_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByGender_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByEducation_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# %% [markdown]
# Filtering if "GEO" levelled as "Canada" ONLY.

# %% [markdown]
# Only finished "Average annual hours worked".

# %%
# -- Canada                     18252439.0  16900.406481  22232.852533  1080

ProCode = 2 # Canada

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByAge_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByAge_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByAge_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByAge_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByGende_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByGender_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByGender_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByGender_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByEducation_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# %% [markdown]
# Panda Profiling for Final Result for GEO = Canada

# %%
# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByAge_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByAge_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByAge_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByAge_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByGende_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByGender_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByGender_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByGender_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByEducation_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# %% [markdown]
# Filtering only Manitoba.

# %% [markdown]
# Only finished "Average annual hours worked".

# %%
# -- Manitoba                     767802.0    710.927778    915.637659  1080

ProCode = 3

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByAge_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByAge_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByAge_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByAge_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByGende_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByGender_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByGender_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByGender_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByEducation_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# %% [markdown]
# Panda Profiling for Final Result for Manitoba

# %%
# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByAge_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByAge_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByAge_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByAge_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByGende_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByGender_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByGender_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByGender_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByEducation_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# %% [markdown]
# Filtering only New Brunswick.

# %% [markdown]
# Only finished "Average annual hours worked".

# %%
# -- New Brunswick                359320.0    332.703704    530.962762  1080

ProCode = 4

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByAge_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByAge_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByAge_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByAge_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByGende_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByGender_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByGender_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByGender_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByEducation_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# %% [markdown]
# Panda Profiling for Final Result for New Brunswick

# %%
# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByAge_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByAge_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByAge_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByAge_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByGende_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByGender_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByGender_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByGender_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByEducation_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# %% [markdown]
# Filtering only Newfoundland and Labrador.

# %% [markdown]
# Only finished "Average annual hours worked".

# %%
# -- Newfoundland and Labrador    315895.0    306.099806    482.634908  1032

ProCode = 5

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByAge_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByAge_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByAge_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByAge_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByGende_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByGender_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByGender_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByGender_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByEducation_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# %% [markdown]
# Panda Profiling for Final Result for Newfoundland

# %%
# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByAge_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByAge_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByAge_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByAge_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByGende_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByGender_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByGender_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByGender_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByEducation_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# %% [markdown]
# Filtering only Northwest Territories.

# %% [markdown]
# Only finished "Average annual hours worked".

# %%
# -- Northwest Territories         42804.0     41.476744     51.817046  1032

ProCode = 6

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByAge_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByAge_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByAge_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByAge_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByGende_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByGender_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByGender_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByGender_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByEducation_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# %% [markdown]
# Panda Profiling for Final Result for Northwest Territories

# %%
# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByAge_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByAge_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByAge_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByAge_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByGende_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByGender_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByGender_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByGender_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByEducation_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# %% [markdown]
# Filtering only Nova Scotia.

# %% [markdown]
# Only finished "Average annual hours worked".

# %%
# -- Nova Scotia                  531805.0    492.412037    757.119411  1080

ProCode = 7

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByAge_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByAge_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByAge_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByAge_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByGende_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByGender_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByGender_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByGender_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByEducation_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# %% [markdown]
# Panda Profiling for Final Result for Nova Scotia

# %%
# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByAge_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByAge_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByAge_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByAge_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByGende_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByGender_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByGender_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByGender_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByEducation_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# %% [markdown]
# Filtering only Nunavut.

# %% [markdown]
# Only finished "Average annual hours worked".

# %%
# -- Nunavut                       14235.0     15.208333     14.752372   936

ProCode = 8

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByAge_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByAge_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByAge_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByAge_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByGende_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByGender_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByGender_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByGender_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByEducation_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# %% [markdown]
# Panda Profiling for Final Result for Nunavut

# %%
# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByAge_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByAge_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByAge_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByAge_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByGende_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByGender_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByGender_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByGender_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByEducation_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# %% [markdown]
# Filtered by Ontario

# %% [markdown]
# Only finished "Average annual hours worked".

# %%
# -- Ontario                     6601634.0   6112.624074   7594.433779  1080

ProCode = 9

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByAge_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByAge_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByAge_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByAge_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByGende_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByGender_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByGender_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByGender_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByEducation_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# %% [markdown]
# Panda Profiling for Final Result for Ontario

# %%
# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByAge_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByAge_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByAge_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByAge_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByGende_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByGender_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByGender_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByGender_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByEducation_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# %% [markdown]
# Filtering only Prince Edward Island.

# %% [markdown]
# Only finished "Average annual hours worked".

# %%
# -- Prince Edward Island          77931.0     75.514535    121.297367  1032

ProCode = 10

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByAge_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByAge_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByAge_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByAge_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByGende_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByGender_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByGender_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByGender_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByEducation_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# %% [markdown]
# Panda Profiling for Final Result for Prince Edward Island

# %%
# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByAge_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByAge_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByAge_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByAge_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByGende_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByGender_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByGender_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByGender_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByEducation_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# %% [markdown]
# Filtering only Quebec.

# %% [markdown]
# Only finished "Average annual hours worked".

# %%
# -- Quebec                      4271657.0   3955.237963   5580.294544  1080

ProCode = 11

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByAge_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByAge_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByAge_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByAge_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByGende_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByGender_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByGender_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByGender_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByEducation_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# %% [markdown]
# Panda Profiling for Final Result for Quebec

# %%
# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByAge_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByAge_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByAge_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByAge_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByGende_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByGender_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByGender_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByGender_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByEducation_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# %% [markdown]
# Filtering only Saskatchewan.

# %% [markdown]
# Only finished "Average annual hours worked".

# %%
# -- Saskatchewan                 650781.0    602.575000    876.896377  1080

ProCode = 12

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByAge_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByAge_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByAge_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByAge_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByGende_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByGender_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByGender_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByGender_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByEducation_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# %% [markdown]
# Panda Profiling for Final Result for Saskatchewan

# %%
# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByAge_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByAge_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByAge_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByAge_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByGende_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByGender_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByGender_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByGender_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByEducation_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# %% [markdown]
# Filtering only Yukon.

# %% [markdown]
# Only finished "Average annual hours worked".

# %%
# -- Yukon                         16914.0     18.070513     20.188135   936

ProCode = 13

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByAge_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByAge_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByAge_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByAge_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByGende_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByGender_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByGender_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByGender_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByEducation_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces, ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# %% [markdown]
# Panda Profiling for Final Result for Yukon

# %%
# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByAge_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByAge_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByAge_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByAge_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByGende_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByGender_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByGender_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByGender_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByEducation_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# # df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2010_ByEducation_Provinces, ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2013_ByEducation_Provinces, ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces, ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(df_AvgAnnHrsWrk_2019_ByEducation_Provinces, ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# %% [markdown]
# Display all of the indicators, characteristics, and provinces will display too much to analysis.<br />
# Therefore, I made custom code below to display output for speciic province and the indicators<br />
# Characteristics (Age, gender, education, immigrant) still display all of them.<br />
# To use, enter province name (string) and the indicator (in numeric 0-6).<br />

# %%
# https://realpython.com/python-raise-exception/
# https://www.geeksforgeeks.org/check-multiple-conditions-in-if-statement-python/

list_of_province = ['Alberta',  'British Columbia', 'Canada', 'Manitoba', 'New Brunswick', 'Newfoundland and Labrador', 
                    'Northwest Territories' , 'Nova Scotia' , 'Nunavut', 'Ontario' , 
                    'Prince Edward Island', 'Quebec', 'Saskatchewan', 'Yukon']
categorized_province = input('Enter your province name:')
categorized_province = categorized_province.lower()
categorized_province_analysis = "Invalid"
for x in list_of_province:
    if (x.lower() == categorized_province) :
        categorized_province_analysis = x
        break

list_indicator = ["Average annual hours worked",
             "Average annual wages and salaries",
             "Average hourly wage",
             "Average weekly hours worked",
             "Hours Worked", 
             "Number of jobs", 
             "Wages and Salaries"]
categorized_indicator = ""
categorized_indcator_analysis = "Invalid"

if categorized_province_analysis == "Invalid":
    print("Run this code again, this province doesn't exist.")
    print("End of Program")

else:
    print("Enter your indicator attributes, ")
    print("0. Average annual hours worked")
    print("1. Average annual wages and salaries")
    print("2. Average hourly wage")
    print("3. Average weekly hours worked")
    print("4. Hours Worked")
    print("5. Number of jobs")
    print("6. Wages and Salaries")
    categorized_indicator = input('Enter your indicator number:')
    try:
        categorized_indicator = int(categorized_indicator)
    except ValueError:
        if not type(categorized_indicator) is int:
            print("Run this code again, invalid integer")
            print("End of Program")
    try:
        categorized_indicator_analysis = list_indicator[categorized_indicator]
    except IndexError:
        print("Run this code again, invalid range (0-6)")
        print("End of Program")

    if categorized_province_analysis == "Invalid":
        print("End of Program")
    else:
        num = 0
        for x in list_of_province:
            if (categorized_province_analysis == x) :
                ProCode = num
                break
            else:
                num = num + 1
        if categorized_indicator == 0:
            categorized_indicator_analysis = []
            categorized_indicator_analysis.append("") # df_AvgAnnHrsWrk_2010_ByAge_Provinces)
            categorized_indicator_analysis.append(df_AvgAnnHrsWrk_2013_ByAge_Provinces)
            categorized_indicator_analysis.append(df_AvgAnnHrsWrk_2016_ByAge_Provinces)
            categorized_indicator_analysis.append(df_AvgAnnHrsWrk_2019_ByAge_Provinces)
            categorized_indicator_analysis.append("") # df_AvgAnnHrsWrk_2010_ByGender_Provinces)
            categorized_indicator_analysis.append(df_AvgAnnHrsWrk_2013_ByGender_Provinces)
            categorized_indicator_analysis.append(df_AvgAnnHrsWrk_2016_ByGender_Provinces)
            categorized_indicator_analysis.append(df_AvgAnnHrsWrk_2019_ByGender_Provinces)
            categorized_indicator_analysis.append("") # df_AvgAnnHrsWrk_2010_ByEducation_Provinces)
            categorized_indicator_analysis.append(df_AvgAnnHrsWrk_2013_ByEducation_Provinces)
            categorized_indicator_analysis.append(df_AvgAnnHrsWrk_2016_ByEducation_Provinces)
            categorized_indicator_analysis.append(df_AvgAnnHrsWrk_2019_ByEducation_Provinces)
            categorized_indicator_analysis.append("") # df_AvgAnnHrsWrk_2010_ByImmigrant_Provinces)
            categorized_indicator_analysis.append(df_AvgAnnHrsWrk_2013_ByImmigrant_Provinces)
            categorized_indicator_analysis.append(df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces)
            categorized_indicator_analysis.append(df_AvgAnnHrsWrk_2019_ByImmigrant_Provinces)
        elif categorized_indicator == 1:
            categorized_indicator_analysis = []
            categorized_indicator_analysis.append("") # df_AvgAnnWages_2010_ByAge_Provinces)
            categorized_indicator_analysis.append(df_AvgAnnWages_2013_ByAge_Provinces)
            categorized_indicator_analysis.append(df_AvgAnnWages_2016_ByAge_Provinces)
            categorized_indicator_analysis.append(df_AvgAnnWages_2019_ByAge_Provinces)
            categorized_indicator_analysis.append("") # df_AvgAnnWages_2010_ByGender_Provinces)
            categorized_indicator_analysis.append(df_AvgAnnWages_2013_ByGender_Provinces)
            categorized_indicator_analysis.append(df_AvgAnnWages_2016_ByGender_Provinces)
            categorized_indicator_analysis.append(df_AvgAnnWages_2019_ByGender_Provinces)
            categorized_indicator_analysis.append("") # df_AvgAnnWages_2010_ByEducation_Provinces)
            categorized_indicator_analysis.append(df_AvgAnnWages_2013_ByEducation_Provinces)
            categorized_indicator_analysis.append(df_AvgAnnWages_2016_ByEducation_Provinces)
            categorized_indicator_analysis.append(df_AvgAnnWages_2019_ByEducation_Provinces)
            categorized_indicator_analysis.append("") # df_AvgAnnWages_2010_ByImmigrant_Provinces)
            categorized_indicator_analysis.append(df_AvgAnnWages_2013_ByImmigrant_Provinces)
            categorized_indicator_analysis.append(df_AvgAnnWages_2016_ByImmigrant_Provinces)
            categorized_indicator_analysis.append(df_AvgAnnWages_2019_ByImmigrant_Provinces)
        elif categorized_indicator == 2:
            categorized_indicator_analysis = []
            categorized_indicator_analysis.append("") # df_AvgHrsWages_2010_ByAge_Provinces)
            categorized_indicator_analysis.append(df_AvgHrsWages_2013_ByAge_Provinces)
            categorized_indicator_analysis.append(df_AvgHrsWages_2016_ByAge_Provinces)
            categorized_indicator_analysis.append(df_AvgHrsWages_2019_ByAge_Provinces)
            categorized_indicator_analysis.append("") # df_AvgHrsWages_2010_ByGender_Provinces)
            categorized_indicator_analysis.append(df_AvgHrsWages_2013_ByGender_Provinces)
            categorized_indicator_analysis.append(df_AvgHrsWages_2016_ByGender_Provinces)
            categorized_indicator_analysis.append(df_AvgHrsWages_2019_ByGender_Provinces)
            categorized_indicator_analysis.append("") # df_AvgHrsWages_2010_ByEducation_Provinces)
            categorized_indicator_analysis.append(df_AvgHrsWages_2013_ByEducation_Provinces)
            categorized_indicator_analysis.append(df_AvgHrsWages_2016_ByEducation_Provinces)
            categorized_indicator_analysis.append(df_AvgHrsWages_2019_ByEducation_Provinces)
            categorized_indicator_analysis.append("") # df_AvgHrsWages_2010_ByImmigrant_Provinces)
            categorized_indicator_analysis.append(df_AvgHrsWages_2013_ByImmigrant_Provinces)
            categorized_indicator_analysis.append(df_AvgHrsWages_2016_ByImmigrant_Provinces)
            categorized_indicator_analysis.append(df_AvgHrsWages_2019_ByImmigrant_Provinces)
        elif categorized_indicator == 3:
            categorized_indicator_analysis = []
            categorized_indicator_analysis.append("") # df_AvgWeekHrsWrked_2010_ByAge_Provinces)
            categorized_indicator_analysis.append(df_AvgWeekHrsWrked_2013_ByAge_Provinces)
            categorized_indicator_analysis.append(df_AvgWeekHrsWrked_2016_ByAge_Provinces)
            categorized_indicator_analysis.append(df_AvgWeekHrsWrked_2019_ByAge_Provinces)
            categorized_indicator_analysis.append("") # df_AvgWeekHrsWrked_2010_ByGender_Provinces)
            categorized_indicator_analysis.append(df_AvgWeekHrsWrked_2013_ByGender_Provinces)
            categorized_indicator_analysis.append(df_AvgWeekHrsWrked_2016_ByGender_Provinces)
            categorized_indicator_analysis.append(df_AvgWeekHrsWrked_2019_ByGender_Provinces)
            categorized_indicator_analysis.append("") # df_AvgWeekHrsWrked_2010_ByEducation_Provinces)
            categorized_indicator_analysis.append(df_AvgWeekHrsWrked_2013_ByEducation_Provinces)
            categorized_indicator_analysis.append(df_AvgWeekHrsWrked_2016_ByEducation_Provinces)
            categorized_indicator_analysis.append(df_AvgWeekHrsWrked_2019_ByEducation_Provinces)
            categorized_indicator_analysis.append("") # df_AvgWeekHrsWrked_2010_ByImmigrant_Provinces)
            categorized_indicator_analysis.append(df_AvgWeekHrsWrked_2013_ByImmigrant_Provinces)
            categorized_indicator_analysis.append(df_AvgWeekHrsWrked_2016_ByImmigrant_Provinces)
            categorized_indicator_analysis.append(df_AvgWeekHrsWrked_2019_ByImmigrant_Provinces)
        elif categorized_indicator == 4:
            categorized_indicator_analysis = []
            categorized_indicator_analysis.append("") # df_Hrs_Wrked_2010_ByAge_Provinces)
            categorized_indicator_analysis.append(df_Hrs_Wrked_2013_ByAge_Provinces)
            categorized_indicator_analysis.append(df_Hrs_Wrked_2016_ByAge_Provinces)
            categorized_indicator_analysis.append(df_Hrs_Wrked_2019_ByAge_Provinces)
            categorized_indicator_analysis.append("") # df_Hrs_Wrked_2010_ByGender_Provinces)
            categorized_indicator_analysis.append(df_Hrs_Wrked_2013_ByGender_Provinces)
            categorized_indicator_analysis.append(df_Hrs_Wrked_2016_ByGender_Provinces)
            categorized_indicator_analysis.append(df_Hrs_Wrked_2019_ByGender_Provinces)
            categorized_indicator_analysis.append("") # df_Hrs_Wrked_2010_ByEducation_Provinces)
            categorized_indicator_analysis.append(df_Hrs_Wrked_2013_ByEducation_Provinces)
            categorized_indicator_analysis.append(df_Hrs_Wrked_2016_ByEducation_Provinces)
            categorized_indicator_analysis.append(df_Hrs_Wrked_2019_ByEducation_Provinces)
            categorized_indicator_analysis.append("") # df_Hrs_Wrked_2010_ByImmigrant_Provinces)
            categorized_indicator_analysis.append(df_Hrs_Wrked_2013_ByImmigrant_Provinces)
            categorized_indicator_analysis.append(df_Hrs_Wrked_2016_ByImmigrant_Provinces)
            categorized_indicator_analysis.append(df_Hrs_Wrked_2019_ByImmigrant_Provinces)
        elif categorized_indicator == 5:
            categorized_indicator_analysis = []
            categorized_indicator_analysis.append("") # df_NumOfJob_2010_ByAge_Provinces)
            categorized_indicator_analysis.append(df_NumOfJob_2013_ByAge_Provinces)
            categorized_indicator_analysis.append(df_NumOfJob_2016_ByAge_Provinces)
            categorized_indicator_analysis.append(df_NumOfJob_2019_ByAge_Provinces)
            categorized_indicator_analysis.append("") # df_NumOfJob_2010_ByGender_Provinces)
            categorized_indicator_analysis.append(df_NumOfJob_2013_ByGender_Provinces)
            categorized_indicator_analysis.append(df_NumOfJob_2016_ByGender_Provinces)
            categorized_indicator_analysis.append(df_NumOfJob_2019_ByGender_Provinces)
            categorized_indicator_analysis.append("") # df_NumOfJob_2010_ByEducation_Provinces)
            categorized_indicator_analysis.append(df_NumOfJob_2013_ByEducation_Provinces)
            categorized_indicator_analysis.append(df_NumOfJob_2016_ByEducation_Provinces)
            categorized_indicator_analysis.append(df_NumOfJob_2019_ByEducation_Provinces)
            categorized_indicator_analysis.append("") # df_NumOfJob_2010_ByImmigrant_Provinces)
            categorized_indicator_analysis.append(df_NumOfJob_2013_ByImmigrant_Provinces)
            categorized_indicator_analysis.append(df_NumOfJob_2016_ByImmigrant_Provinces)
            categorized_indicator_analysis.append(df_NumOfJob_2019_ByImmigrant_Provinces)
        elif categorized_indicator == 6:
            categorized_indicator_analysis = []
            categorized_indicator_analysis.append("") # df_WagesAndSalaries_2010_ByAge_Provinces)
            categorized_indicator_analysis.append(df_WagesAndSalaries_2013_ByAge_Provinces)
            categorized_indicator_analysis.append(df_WagesAndSalaries_2016_ByAge_Provinces)
            categorized_indicator_analysis.append(df_WagesAndSalaries_2019_ByAge_Provinces)
            categorized_indicator_analysis.append("") # df_WagesAndSalaries_2010_ByGender_Provinces)
            categorized_indicator_analysis.append(df_WagesAndSalaries_2013_ByGender_Provinces)
            categorized_indicator_analysis.append(df_WagesAndSalaries_2016_ByGender_Provinces)
            categorized_indicator_analysis.append(df_WagesAndSalaries_2019_ByGender_Provinces)
            categorized_indicator_analysis.append("") # df_WagesAndSalaries_2010_ByEducation_Provinces)
            categorized_indicator_analysis.append(df_WagesAndSalaries_2013_ByEducation_Provinces)
            categorized_indicator_analysis.append(df_WagesAndSalaries_2016_ByEducation_Provinces)
            categorized_indicator_analysis.append(df_WagesAndSalaries_2019_ByEducation_Provinces)
            categorized_indicator_analysis.append("") # df_WagesAndSalaries_2010_ByImmigrant_Provinces)
            categorized_indicator_analysis.append(df_WagesAndSalaries_2013_ByImmigrant_Provinces)
            categorized_indicator_analysis.append(df_WagesAndSalaries_2016_ByImmigrant_Provinces)
            categorized_indicator_analysis.append(df_WagesAndSalaries_2019_ByImmigrant_Provinces)
        else:
            pass
        print("The province name is "+categorized_province_analysis)
        print("The indicator name is "+list_indicator[categorized_indicator])
        print("From here, the ProCode will be "+str(ProCode))
        print("The array from categorized_indicator_analysis is")
        print(categorized_indicator_analysis)

# %% [markdown]
# Filtering based on ProCode and indicator given above. <br />
# Must run the code above to run this code. <br />

# %%
# This code need code above.

# df_Display_Output_Result = OutputProvinceAnalysis(categorized_indicator_analysis[0], ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(categorized_indicator_analysis[1], ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(categorized_indicator_analysis[2], ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(categorized_indicator_analysis[3], ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(categorized_indicator_analysis[4], ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(categorized_indicator_analysis[5], ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(categorized_indicator_analysis[6], ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(categorized_indicator_analysis[7], ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(categorized_indicator_analysis[8], ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(categorized_indicator_analysis[9], ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(categorized_indicator_analysis[10], ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(categorized_indicator_analysis[11], ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# df_Display_Output_Result = OutputProvinceAnalysis(categorized_indicator_analysis[12], ProCode, "2010", pd, np, pp)
# df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(categorized_indicator_analysis[13], ProCode, "2013", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(categorized_indicator_analysis[14], ProCode, "2016", pd, np, pp)
df_Display_Output_Result.OutputResult()
df_Display_Output_Result = OutputProvinceAnalysis(categorized_indicator_analysis[15], ProCode, "2019", pd, np, pp)
df_Display_Output_Result.OutputResult()

# %% [markdown]
# Panda Profiling based on ProCode and indicator given above. <br />
# Must run the code above to run this code. <br />

# %%
# # df_Display_Output_Result = OutputProvinceAnalysis(categorized_indicator_analysis[0], ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(categorized_indicator_analysis[1], ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(categorized_indicator_analysis[2], ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(categorized_indicator_analysis[3], ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# # df_Display_Output_Result = OutputProvinceAnalysis(categorized_indicator_analysis[4], ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(categorized_indicator_analysis[5], ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(categorized_indicator_analysis[6], ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(categorized_indicator_analysis[7], ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# # df_Display_Output_Result = OutputProvinceAnalysis(categorized_indicator_analysis[8], ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(categorized_indicator_analysis[9], ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(categorized_indicator_analysis[10], ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(categorized_indicator_analysis[11], ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()

# # df_Display_Output_Result = OutputProvinceAnalysis(categorized_indicator_analysis[12], ProCode, "2010", pd, np, pp)
# # df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(categorized_indicator_analysis[13], ProCode, "2013", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(categorized_indicator_analysis[14], ProCode, "2016", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()
# df_Display_Output_Result = OutputProvinceAnalysis(categorized_indicator_analysis[15], ProCode, "2019", pd, np, pp)
# df_Display_Output_Result.OutputPandaProfiling()


