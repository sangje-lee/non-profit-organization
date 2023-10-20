# %% [markdown]
# ## Data analysis
# Based on year of 2017, 2019, and 2021. 
# Plus, division between before 2016 and after 2017.

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
# Filter only the essential part of the dataset.

# %%
print("Grab the only the essential part of database.")
df_sorted = df[['REF_DATE','GEO','Sector','Characteristics','Indicators','UOM','SCALAR_FACTOR','VALUE']]
print(df_sorted.head(20))

print(df_sorted.info())
grouped = df_sorted.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.size]))

# %% [markdown]
# Notice there is missing value in this dataset.

# %%
print("Original database null counter")
print(df.isnull().sum())
print("\n Modified dataset null counter.")
print(df_sorted.isnull().sum())

# %% [markdown]
# Code for dropping missing dataset,

# %%
df_sorted_na = df_sorted.dropna()

# %% [markdown]
# Check now if there's still a missing dataset

# %%
print("Modified dataset modification after removing missing value and it's total counter")
print(df_sorted_na.isnull().sum())
print(df_sorted_na.head(20))

print(df_sorted_na.info())
grouped = df_sorted_na.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.size]))

# %%
print(df_sorted_na.info())
grouped = df_sorted_na.groupby(['Indicators'])
print(grouped['VALUE'].agg([np.size]))

# %% [markdown]
# Panda Profiling for original dataset,

# %%
# https://medium.com/analytics-vidhya/pandas-profiling-5ecd0b977ecd

pp = ProfileReport(df, title="Pandas Profiling Report")
pp_df = pp.to_html()

f = open("df_NoMod.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

# %% [markdown]
# Panda Profiling for modified dataset,

# %%
pp_sorted = ProfileReport(df_sorted, title="Pandas Profiling Report with Columns Sorted")
pp_df_sorted = pp_sorted.to_html()

f = open("df_Sorted.html", "a") # Expert modifying data into html file.
f.write(pp_df_sorted)
f.close()

# %% [markdown]
# Panda Profiling for removed dataset,

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
# Average annual hours worked from sorted dataset.

# %%
# Average annual hours worked        15120
print("\nAverage annual hours worked")
df_AvgAnnHrsWrk = df_sorted_na.loc[
    (df_sorted_na['Indicators'] == 'Average annual hours worked')
]
grouped = df_AvgAnnHrsWrk.groupby(['GEO'])
print(grouped['VALUE'].agg([np.sum, np.mean, np.std, np.size]))
print("The total number of this one is ",len(df_AvgAnnHrsWrk.index))

# %%
# Average annual hours worked        15120 (With missing value)
print("\nAverage annual hours worked")
df_sorted_ann_hours_worked_with_na = df_sorted.loc[
    (df_sorted['Indicators'] == 'Average annual hours worked')
]
grouped = df_sorted_ann_hours_worked_with_na .groupby(['GEO'])
print(grouped['VALUE'].agg([np.sum, np.mean, np.std, np.size]))
print("The total number of this one is ",len(df_sorted_ann_hours_worked_with_na .index))

# %% [markdown]
# Panda Profiling only for "Average annual hours worked"

# %%
pp = ProfileReport(df_AvgAnnHrsWrk, title="Average annual hours worked")
pp_df = pp.to_html()

f = open("Average annual hours worked.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

# %%
# With missing value

pp = ProfileReport(df_sorted_ann_hours_worked_with_na, title="Pandas Profiling Report with missing value")
pp_df = pp.to_html()

f = open("Average annual hours worked.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

# %% [markdown]
# Grabbing the data preivous from 2015 for "Average annual hours worked"

# %%
print("Grabbing the data previous from 2015.")
df_AvgAnnHrsWrk_below_2015 = df_AvgAnnHrsWrk.loc[
    (df_AvgAnnHrsWrk['REF_DATE'] == 2010) |
    (df_AvgAnnHrsWrk['REF_DATE'] == 2011) |
    (df_AvgAnnHrsWrk['REF_DATE'] == 2012) |
    (df_AvgAnnHrsWrk['REF_DATE'] == 2013) |
    (df_AvgAnnHrsWrk['REF_DATE'] == 2014) |
    (df_AvgAnnHrsWrk['REF_DATE'] == 2015)
]
print(df_AvgAnnHrsWrk_below_2015.head(20))
print(df_AvgAnnHrsWrk_below_2015.info())
grouped = df_AvgAnnHrsWrk_below_2015.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgAnnHrsWrk_below_2015.index))

# %% [markdown]
# Grabbing the data above from 2017 and up for "Average annual hours worked"

# %%
print("Grabbing the data above 2016.")
df_AvgAnnHrsWrk_above_2016 = df_AvgAnnHrsWrk.loc[
    (df_AvgAnnHrsWrk['REF_DATE'] == 2016) |
    (df_AvgAnnHrsWrk['REF_DATE'] == 2017) |
    (df_AvgAnnHrsWrk['REF_DATE'] == 2018) |
    (df_AvgAnnHrsWrk['REF_DATE'] == 2019) |
    (df_AvgAnnHrsWrk['REF_DATE'] == 2020) |
    (df_AvgAnnHrsWrk['REF_DATE'] == 2021)
]
print(df_AvgAnnHrsWrk_above_2016.head(20))
print(df_AvgAnnHrsWrk_above_2016.info())
grouped = df_AvgAnnHrsWrk_above_2016.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgAnnHrsWrk_above_2016.index))

# %% [markdown]
# Grabbing the data below 2016 and above from 2017 with missing value.

# %%
print("Grabbing the data previous from 2016. (With missing value)")
df_na_below_2015_year = df_sorted_ann_hours_worked_with_na.loc[
    (df_sorted_ann_hours_worked_with_na['REF_DATE'] == 2010) |
    (df_sorted_ann_hours_worked_with_na['REF_DATE'] == 2011) |
    (df_sorted_ann_hours_worked_with_na['REF_DATE'] == 2012) |
    (df_sorted_ann_hours_worked_with_na['REF_DATE'] == 2013) |
    (df_sorted_ann_hours_worked_with_na['REF_DATE'] == 2014) |
    (df_sorted_ann_hours_worked_with_na['REF_DATE'] == 2015)
]
print(df_na_below_2015_year.head(20))
print(df_na_below_2015_year.info())
grouped = df_na_below_2015_year.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_na_below_2015_year.index))

print("Grabbing the data from 2017, 2019, and 2021.")
df_na_above_2016_year = df_sorted_ann_hours_worked_with_na.loc[
    (df_sorted_ann_hours_worked_with_na['REF_DATE'] == 2016) |
    (df_sorted_ann_hours_worked_with_na['REF_DATE'] == 2017) |
    (df_sorted_ann_hours_worked_with_na['REF_DATE'] == 2018) |
    (df_sorted_ann_hours_worked_with_na['REF_DATE'] == 2019) |
    (df_sorted_ann_hours_worked_with_na['REF_DATE'] == 2020) |
    (df_sorted_ann_hours_worked_with_na['REF_DATE'] == 2021)
]
print(df_na_above_2016_year.head(20))
print(df_na_above_2016_year.info())
grouped = df_na_above_2016_year.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_na_above_2016_year.index))

# %% [markdown]
# Panda Profiling only for "Average annual hours worked" before 2016 and after 2017.

# %%
pp = ProfileReport(df_AvgAnnHrsWrk_below_2015, title="Average annual hours worked before 2015")
pp_df = pp.to_html()

f = open("Average annual hours worked below 2015.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

pp = ProfileReport(df_AvgAnnHrsWrk_above_2016, title="Average annual hours worked after 2016")
pp_df = pp.to_html()

f = open("Average annual hours worked above 2016.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

# %% [markdown]
# Panda Profiling only for "Average annual wages and salaries" before 2016 and after 2017 with missing value.

# %%
pp = ProfileReport(df_na_below_2015_year, title="Average annual hours worked with na before 2015")
pp_df = pp.to_html()

f = open("Average annual hours worked below 2016 - with na.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

pp = ProfileReport(df_na_above_2016_year, title="Average annual hours worked with na above 2016")
pp_df = pp.to_html()

f = open("Average annual hours worked above 2017 - with na.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

# %% [markdown]
# Average annual wages and salaries from sorted dataset.

# %% [markdown]
# No more collecting data including missing value.

# %%
# Average annual wages and salaries  15120
print("\nAverage annual wages and salaries")
df_AvgAnnWages = df_sorted_na.loc[
    (df_sorted_na['Indicators'] == 'Average annual wages and salaries')
]
grouped = df_AvgAnnWages.groupby(['GEO'])
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
# Grabbing the data preivous from 2016 for "Average annual wages and salaries"

# %%
print("Grabbing the data previous from 2016.")
df_AvgAnnWages_below_2015 = df_AvgAnnWages.loc[
    (df_AvgAnnWages['REF_DATE'] == 2010) |
    (df_AvgAnnWages['REF_DATE'] == 2011) |
    (df_AvgAnnWages['REF_DATE'] == 2012) |
    (df_AvgAnnWages['REF_DATE'] == 2013) |
    (df_AvgAnnWages['REF_DATE'] == 2014) |
    (df_AvgAnnWages['REF_DATE'] == 2015)
]
print(df_AvgAnnWages_below_2015.head(20))
print(df_AvgAnnWages_below_2015.info())
grouped = df_AvgAnnWages_below_2015.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgAnnWages_below_2015.index))

# %% [markdown]
# Grabbing the data above from 2017 and up for "Average annual wages and salaries"

# %%
print("Grabbing the data from 2017, 2019, and 2021.")
df_AvgAnnWages_above_2016 = df_AvgAnnWages.loc[
    (df_AvgAnnWages['REF_DATE'] == 2016) |
    (df_AvgAnnWages['REF_DATE'] == 2017) |
    (df_AvgAnnWages['REF_DATE'] == 2018) |
    (df_AvgAnnWages['REF_DATE'] == 2019) |
    (df_AvgAnnWages['REF_DATE'] == 2020) |
    (df_AvgAnnWages['REF_DATE'] == 2021)
]
print(df_AvgAnnWages_above_2016.head(20))
print(df_AvgAnnWages_above_2016.info())
grouped = df_AvgAnnWages_above_2016.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgAnnWages_above_2016.index))

# %% [markdown]
# Panda Profiling only for "Average annual wages and salaries" before 2016 and after 2017.

# %%
pp = ProfileReport(df_AvgAnnWages_below_2015, title="Average annual wages and salaries below 2015")
pp_df = pp.to_html()

f = open("Average annual wages and salaries below 2015.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

pp = ProfileReport(df_AvgAnnWages_above_2016, title="Average annual wages and salaries after 2016")
pp_df = pp.to_html()

f = open("Average annual wages and salaries above 2016.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

# %% [markdown]
# Average hourly wage from sorted dataset.

# %%
# Average hourly wage                15120
print("\nAverage hourly wage")
df_AvgHrsWages = df_sorted_na.loc[
    (df_sorted_na['Indicators'] == 'Average hourly wage')
]
grouped = df_AvgHrsWages.groupby(['GEO'])
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
# Grabbing the data preivous from 2016 for "Average hourly wages"

# %%
print("Grabbing the data previous from 2016.")
df_AvgHrsWages_below_2015 = df_AvgHrsWages.loc[
    (df_AvgHrsWages['REF_DATE'] == 2010) |
    (df_AvgHrsWages['REF_DATE'] == 2011) |
    (df_AvgHrsWages['REF_DATE'] == 2012) |
    (df_AvgHrsWages['REF_DATE'] == 2013) |
    (df_AvgHrsWages['REF_DATE'] == 2014) |
    (df_AvgHrsWages['REF_DATE'] == 2015)
]
print(df_AvgHrsWages_below_2015.head(20))
print(df_AvgHrsWages_below_2015.info())
grouped = df_AvgHrsWages_below_2015.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgHrsWages_below_2015.index))

# %% [markdown]
# Grabbing the data above from 2017 and up for "Average hourly wages"

# %%
print("Grabbing the data from 2017, 2019, and 2021.")
df_AvgHrsWages_above_2016 = df_AvgHrsWages.loc[
    (df_AvgHrsWages['REF_DATE'] == 2016) |
    (df_AvgHrsWages['REF_DATE'] == 2017) |
    (df_AvgHrsWages['REF_DATE'] == 2018) |
    (df_AvgHrsWages['REF_DATE'] == 2019) |
    (df_AvgHrsWages['REF_DATE'] == 2020) |
    (df_AvgHrsWages['REF_DATE'] == 2021)
]
print(df_AvgHrsWages_above_2016.head(20))
print(df_AvgHrsWages_above_2016.info())
grouped = df_AvgHrsWages_above_2016.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgHrsWages_above_2016.index))

# %% [markdown]
# Panda Profiling only for "Average hourly wages" before 2016 and after 2017.

# %%
pp = ProfileReport(df_AvgHrsWages_below_2015, title="Average hourly wage before 2015")
pp_df = pp.to_html()

f = open("Average hourly wages below 2015.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

pp = ProfileReport(df_AvgHrsWages_above_2016, title="Average hourly wage afer 2016")
pp_df = pp.to_html()

f = open("Average hourly wages above 2016.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

# %% [markdown]
# Average weekly hours worked from sorted dataset.

# %%
# Average weekly hours worked        15120
print("\nAverage weekly hours worked")
df_AvgWeekHrsWrked = df_sorted_na.loc[
    (df_sorted_na['Indicators'] == 'Average weekly hours worked')
]
grouped = df_AvgWeekHrsWrked.groupby(['GEO'])
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
# Grabbing the data preivous from 2016 for "Average weekly hours worked"

# %%
print("Grabbing the data previous from 2016.")
df_AvgWeekHrsWrked_below_2015 = df_AvgWeekHrsWrked.loc[
    (df_AvgWeekHrsWrked['REF_DATE'] == 2010) |
    (df_AvgWeekHrsWrked['REF_DATE'] == 2011) |
    (df_AvgWeekHrsWrked['REF_DATE'] == 2012) |
    (df_AvgWeekHrsWrked['REF_DATE'] == 2013) |
    (df_AvgWeekHrsWrked['REF_DATE'] == 2014) |
    (df_AvgWeekHrsWrked['REF_DATE'] == 2015)
]
print(df_AvgWeekHrsWrked_below_2015.head(20))
print(df_AvgWeekHrsWrked_below_2015.info())
grouped = df_AvgWeekHrsWrked_below_2015.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgWeekHrsWrked_below_2015.index))

# %% [markdown]
# Grabbing the data above from 2017 and up for "Average weekly hours worked"

# %%
print("Grabbing the data from 2017, 2019, and 2021.")
df_AvgWeekHrsWrked_above_2016 = df_AvgWeekHrsWrked.loc[
    (df_AvgWeekHrsWrked['REF_DATE'] == 2016) |
    (df_AvgWeekHrsWrked['REF_DATE'] == 2017) |
    (df_AvgWeekHrsWrked['REF_DATE'] == 2018) |
    (df_AvgWeekHrsWrked['REF_DATE'] == 2019) |
    (df_AvgWeekHrsWrked['REF_DATE'] == 2020) |
    (df_AvgWeekHrsWrked['REF_DATE'] == 2021)
]
print(df_AvgWeekHrsWrked_above_2016.head(20))
print(df_AvgWeekHrsWrked_above_2016.info())
grouped = df_AvgWeekHrsWrked_above_2016.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgWeekHrsWrked_above_2016.index))

# %% [markdown]
# Panda Profiling only for "Average weekly hours worked" before 2016 and after 2017.

# %%
pp = ProfileReport(df_AvgWeekHrsWrked_below_2015, title="Average weekly hours worked before 2015")
pp_df = pp.to_html()

f = open("Average weekly hours worked below 2015.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

pp = ProfileReport(df_AvgWeekHrsWrked_above_2016, title="Average weekly hours worked after 2016")
pp_df = pp.to_html()

f = open("Average weekly hours worked above 2016.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

# %% [markdown]
# Hours worked from sorted dataset.

# %%
# Hours worked                       15120
print("\nHours worked")
df_Hrs_Wrked = df_sorted_na.loc[
    (df_sorted_na['Indicators'] == 'Hours worked')
]
grouped = df_Hrs_Wrked.groupby(['GEO'])
print(grouped['VALUE'].agg([np.sum, np.mean, np.std, np.size]))
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
# Grabbing the data preivous from 2016 for "hours worked"

# %%
print("Grabbing the data previous from 2016.")
df_Hrs_Wrked_below_2015 = df_Hrs_Wrked.loc[
    (df_Hrs_Wrked['REF_DATE'] == 2010) |
    (df_Hrs_Wrked['REF_DATE'] == 2011) |
    (df_Hrs_Wrked['REF_DATE'] == 2012) |
    (df_Hrs_Wrked['REF_DATE'] == 2013) |
    (df_Hrs_Wrked['REF_DATE'] == 2014) |
    (df_Hrs_Wrked['REF_DATE'] == 2015)
]
print(df_Hrs_Wrked_below_2015.head(20))
print(df_Hrs_Wrked_below_2015.info())
grouped = df_Hrs_Wrked_below_2015.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_Hrs_Wrked_below_2015.index))

# %% [markdown]
# Grabbing the data above from 2017 and up for "hours worked"

# %%
print("Grabbing the data from 2016 above")
df_Hrs_Wrked_above_2016 = df_Hrs_Wrked.loc[
    (df_Hrs_Wrked['REF_DATE'] == 2016) |
    (df_Hrs_Wrked['REF_DATE'] == 2017) |
    (df_Hrs_Wrked['REF_DATE'] == 2018) |
    (df_Hrs_Wrked['REF_DATE'] == 2019) |
    (df_Hrs_Wrked['REF_DATE'] == 2020) |
    (df_Hrs_Wrked['REF_DATE'] == 2021)
]
print(df_Hrs_Wrked_above_2016.head(20))
print(df_Hrs_Wrked_above_2016.info())
grouped = df_Hrs_Wrked_above_2016.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_Hrs_Wrked_above_2016.index))

# %% [markdown]
# Panda Profiling only for "hours worked" before 2016 and after 2017.

# %%
pp = ProfileReport(df_Hrs_Wrked_below_2015, title="Hours Worked below 2015")
pp_df = pp.to_html()

f = open("Hours worked below 2015.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

pp = ProfileReport(df_Hrs_Wrked_above_2016, title="Hours Worked after 2016")
pp_df = pp.to_html()

f = open("Hours worked above 2016.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

# %% [markdown]
# Number of jobs from sorted dataset.

# %%
# Number of jobs                     15120
print("\nNumber of jobs")
df_NumOfJob = df_sorted_na.loc[
    (df_sorted_na['Indicators'] == 'Number of jobs')
]
grouped = df_NumOfJob.groupby(['GEO'])
print(grouped['VALUE'].agg([np.sum, np.mean, np.std, np.size]))
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
# Grabbing the data preivous from 2016 for "Number of the jobs"

# %%
print("Grabbing the data previous from 2016.")
df_NumOfJob_below_2015 = df_NumOfJob.loc[
    (df_NumOfJob['REF_DATE'] == 2010) |
    (df_NumOfJob['REF_DATE'] == 2011) |
    (df_NumOfJob['REF_DATE'] == 2012) |
    (df_NumOfJob['REF_DATE'] == 2013) |
    (df_NumOfJob['REF_DATE'] == 2014) |
    (df_NumOfJob['REF_DATE'] == 2015)
]
print(df_NumOfJob_below_2015.head(20))
print(df_NumOfJob_below_2015.info())
grouped = df_NumOfJob_below_2015.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_NumOfJob_below_2015.index))

# %% [markdown]
# Grabbing the data above from 2017 and up for "Number of the jobs"

# %%
print("Grabbing the data from above 2016.")
df_NumOfJob_above_2016 = df_NumOfJob.loc[
    (df_NumOfJob['REF_DATE'] == 2016) |
    (df_NumOfJob['REF_DATE'] == 2017) |
    (df_NumOfJob['REF_DATE'] == 2018) |
    (df_NumOfJob['REF_DATE'] == 2019) |
    (df_NumOfJob['REF_DATE'] == 2020) |
    (df_NumOfJob['REF_DATE'] == 2021)
]
print(df_NumOfJob_above_2016.head(20))
print(df_NumOfJob_above_2016.info())
grouped = df_NumOfJob_above_2016.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_NumOfJob_above_2016.index))

# %% [markdown]
# Panda Profiling only for "Number of the jobs" before 2016 and after 2017.

# %%
pp = ProfileReport(df_NumOfJob_below_2015, title="Number of jobs before 2015")
pp_df = pp.to_html()

f = open("Number of jobs below 2015.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

pp = ProfileReport(df_NumOfJob_above_2016, title="Number of jobs after 2016")
pp_df = pp.to_html()

f = open("Number of jobs above 2016.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

# %% [markdown]
# Wages and salaries from sorted dataset.

# %%
# Wages and salaries                 15120
print("\nWages and salaries")
df_WagesAndSalaries = df_sorted_na.loc[
    (df_sorted_na['Indicators'] == 'Wages and salaries')
]
grouped = df_WagesAndSalaries.groupby(['GEO'])
print(grouped['VALUE'].agg([np.sum, np.mean, np.std, np.size]))
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
# Grabbing the data preivous from 2016 for "Wages and Salaries"

# %%
print("Grabbing the data previous from 2015.")
df_WagesAndSalaries_below_2015 = df_WagesAndSalaries.loc[
    (df_WagesAndSalaries['REF_DATE'] == 2010) |
    (df_WagesAndSalaries['REF_DATE'] == 2011) |
    (df_WagesAndSalaries['REF_DATE'] == 2012) |
    (df_WagesAndSalaries['REF_DATE'] == 2013) |
    (df_WagesAndSalaries['REF_DATE'] == 2014) |
    (df_WagesAndSalaries['REF_DATE'] == 2015)
]
print(df_WagesAndSalaries_below_2015.head(20))
print(df_WagesAndSalaries_below_2015.info())
grouped = df_WagesAndSalaries_below_2015.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_WagesAndSalaries_below_2015.index))

# %% [markdown]
# Grabbing the data above from 2017 and up for "Wages and Salaries"

# %%
print("Grabbing the data from above 2016.")
df_WagesAndSalaries_above_2016 = df_WagesAndSalaries.loc[
    (df_WagesAndSalaries['REF_DATE'] == 2016) |
    (df_WagesAndSalaries['REF_DATE'] == 2017) |
    (df_WagesAndSalaries['REF_DATE'] == 2018) |
    (df_WagesAndSalaries['REF_DATE'] == 2019) |
    (df_WagesAndSalaries['REF_DATE'] == 2020) |
    (df_WagesAndSalaries['REF_DATE'] == 2021)
]
print(df_WagesAndSalaries_above_2016.head(20))
print(df_WagesAndSalaries_above_2016.info())
grouped = df_WagesAndSalaries_above_2016.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_WagesAndSalaries_above_2016.index))

# %% [markdown]
# Panda Profiling only for "Wages and Salaries" before 2016 and after 2017.

# %%
pp = ProfileReport(df_WagesAndSalaries_below_2015, title="Wages and Salaries before 2015")
pp_df = pp.to_html()

f = open("Wages and salaries below 2015.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

pp = ProfileReport(df_WagesAndSalaries_above_2016, title="Wages and Salaries after 2016")
pp_df = pp.to_html()

f = open("Wages and salaries above 2016.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

# %%
print("For next step, proceed with dividing data with 2016-2017, 2018-2019, 2020-2021\n",
      "This part was originally divide 2017, 2019, and 2021.\n",
      "Plan changed because too complex coding.")

# %% [markdown]
# Grabbing the year (REF_DATE) from 2017, 2019, and 2021 individually for "Average annual hours worked".

# %%
print("Grabbing the data from 2017, 2019, and 2021.")
df_AvgAnnHrsWrk_2016 = df_AvgAnnHrsWrk_above_2016.loc[
    (df_AvgAnnHrsWrk_above_2016['REF_DATE'] == 2016) |
    (df_AvgAnnHrsWrk_above_2016['REF_DATE'] == 2017)
]

df_AvgAnnHrsWrk_2018 = df_AvgAnnHrsWrk_above_2016.loc[
    (df_AvgAnnHrsWrk_above_2016['REF_DATE'] == 2018) |
    (df_AvgAnnHrsWrk_above_2016['REF_DATE'] == 2019)
]

df_AvgAnnHrsWrk_2020 = df_AvgAnnHrsWrk_above_2016.loc[
    (df_AvgAnnHrsWrk_above_2016['REF_DATE'] == 2020) |
    (df_AvgAnnHrsWrk_above_2016['REF_DATE'] == 2021)
]

grouped = df_AvgAnnHrsWrk_2016.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

grouped = df_AvgAnnHrsWrk_2018.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

grouped = df_AvgAnnHrsWrk_2020.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

# %% [markdown]
# Panda Profiling for year 2017, 2019, and 2021 for "Average annual hours worked".

# %%
pp = ProfileReport(df_AvgAnnHrsWrk_2016, title="Average annual hours worked 2016")
pp_df = pp.to_html()

f = open("Average annual hours worked 2016.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

pp = ProfileReport(df_AvgAnnHrsWrk_2018, title="Average annual hours worked 2018")
pp_df = pp.to_html()

f = open("Average annual hours worked 2018.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

pp = ProfileReport(df_AvgAnnHrsWrk_2020, title="Average annual hours worked 2020")
pp_df = pp.to_html()

f = open("Average annual hours worked 2020.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

# %% [markdown]
# Grabbing the year (REF_DATE) from 2017, 2019, and 2021 individually for "Average annual wages and salaries".

# %%
print("Grabbing the data from 2017, 2019, and 2021.")
df_AvgAnnWages_2016 = df_AvgAnnWages_above_2016.loc[
    (df_AvgAnnWages_above_2016['REF_DATE'] == 2016) |
    (df_AvgAnnWages_above_2016['REF_DATE'] == 2017)
]

df_AvgAnnWages_2018 = df_AvgAnnWages_above_2016.loc[
    (df_AvgAnnWages_above_2016['REF_DATE'] == 2018) |
    (df_AvgAnnWages_above_2016['REF_DATE'] == 2019)
]

df_AvgAnnWages_2020 = df_AvgAnnWages_above_2016.loc[
    (df_AvgAnnWages_above_2016['REF_DATE'] == 2020) |
    (df_AvgAnnWages_above_2016['REF_DATE'] == 2021)
]

grouped = df_AvgAnnWages_2016.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

grouped = df_AvgAnnWages_2018.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

grouped = df_AvgAnnWages_2020.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

# %% [markdown]
# Panda Profiling for year 2017, 2019, and 2021 for "Average annual wages and salaries".

# %%
pp = ProfileReport(df_AvgAnnWages_2016, title="Average annual wages and salaries 2016")
pp_df = pp.to_html()

f = open("Average annual wages and salaries 2016.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

pp = ProfileReport(df_AvgAnnWages_2018, title="Average annual wages and salaries 2018")
pp_df = pp.to_html()

f = open("Average annual wages and salaries 2018.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

pp = ProfileReport(df_AvgAnnWages_2020, title="Average annual wages and salaries 2020")
pp_df = pp.to_html()

f = open("Average annual wages and salaries 2020.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

# %% [markdown]
# Grabbing the year (REF_DATE) from 2017, 2019, and 2021 individually for "Average hourly wages".

# %%
print("Grabbing the data from 2017, 2019, and 2021.")
df_AvgHrsWages_2016 = df_AvgHrsWages_above_2016.loc[
    (df_AvgHrsWages_above_2016['REF_DATE'] == 2016) |
    (df_AvgHrsWages_above_2016['REF_DATE'] == 2017)
]

df_AvgHrsWages_2018 = df_AvgHrsWages_above_2016.loc[
    (df_AvgHrsWages_above_2016['REF_DATE'] == 2018) |
    (df_AvgHrsWages_above_2016['REF_DATE'] == 2019)
]

df_AvgHrsWages_2020 = df_AvgHrsWages_above_2016.loc[
    (df_AvgHrsWages_above_2016['REF_DATE'] == 2020) |
    (df_AvgHrsWages_above_2016['REF_DATE'] == 2021)
]

grouped = df_AvgHrsWages_2016.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

grouped = df_AvgHrsWages_2018.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

grouped = df_AvgHrsWages_2020.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

# %% [markdown]
# Panda Profiling for year 2017, 2019, and 2021 for "Average hourly wages".

# %%
pp = ProfileReport(df_AvgHrsWages_2016, title="Average hourly wage 2016")
pp_df = pp.to_html()

f = open("Average hourly wages 2016.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

pp = ProfileReport(df_AvgHrsWages_2018, title="Average hourly wage 2018")
pp_df = pp.to_html()

f = open("Average hourly wages 2018.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

pp = ProfileReport(df_AvgHrsWages_2020, title="Average hourly wage 2020")
pp_df = pp.to_html()

f = open("Average hourly wages 2020.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

# %% [markdown]
# Grabbing the year (REF_DATE) from 2017, 2019, and 2021 individually for "Average weekly hours worked".

# %%
print("Grabbing the data from 2017, 2019, and 2021.")
df_AvgWeekHrsWrked_2016 = df_AvgWeekHrsWrked_above_2016.loc[
    (df_AvgWeekHrsWrked_above_2016['REF_DATE'] == 2016) |
    (df_AvgWeekHrsWrked_above_2016['REF_DATE'] == 2017)
]

df_AvgWeekHrsWrked_2018 = df_AvgWeekHrsWrked_above_2016.loc[
    (df_AvgWeekHrsWrked_above_2016['REF_DATE'] == 2018) |
    (df_AvgWeekHrsWrked_above_2016['REF_DATE'] == 2019)
]

df_AvgWeekHrsWrked_2020 = df_AvgWeekHrsWrked_above_2016.loc[
    (df_AvgWeekHrsWrked_above_2016['REF_DATE'] == 2020) |
    (df_AvgWeekHrsWrked_above_2016['REF_DATE'] == 2021)
]

grouped = df_AvgWeekHrsWrked_2016.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

grouped = df_AvgWeekHrsWrked_2018.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

grouped = df_AvgWeekHrsWrked_2020.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

# %% [markdown]
# Panda Profiling for year 2017, 2019, and 2021 for "Average weekly hours worked".

# %%
pp = ProfileReport(df_AvgWeekHrsWrked_2016, title="Average weekly hours worked 2016")
pp_df = pp.to_html()

f = open("Average weekly hours worked 2016.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

pp = ProfileReport(df_AvgWeekHrsWrked_2018, title="Average weekly hours worked 2018")
pp_df = pp.to_html()

f = open("Average weekly hours worked 2018.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

pp = ProfileReport(df_AvgWeekHrsWrked_2020, title="Average weekly hours worked 2020")
pp_df = pp.to_html()

f = open("Average weekly hours worked 2020.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

# %% [markdown]
# Grabbing the year (REF_DATE) from 2017, 2019, and 2021 individually for "hours worked".

# %%
print("Grabbing the data from 2017, 2019, and 2021.")
df_Hrs_Wrked_2016 = df_Hrs_Wrked_above_2016.loc[
    (df_Hrs_Wrked_above_2016['REF_DATE'] == 2016) |
    (df_Hrs_Wrked_above_2016['REF_DATE'] == 2017)
]

df_Hrs_Wrked_2018 = df_Hrs_Wrked_above_2016.loc[
    (df_Hrs_Wrked_above_2016['REF_DATE'] == 2018) |
    (df_Hrs_Wrked_above_2016['REF_DATE'] == 2019)
]

df_Hrs_Wrked_2020 = df_Hrs_Wrked_above_2016.loc[
    (df_Hrs_Wrked_above_2016['REF_DATE'] == 2020) |
    (df_Hrs_Wrked_above_2016['REF_DATE'] == 2021)
]

grouped = df_Hrs_Wrked_2016.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

grouped = df_Hrs_Wrked_2018.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

grouped = df_Hrs_Wrked_2020.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

# %% [markdown]
# Panda Profiling for year 2017, 2019, and 2021 for "hours worked".

# %%
pp = ProfileReport(df_Hrs_Wrked_2016, title="Hours Worked 2016")
pp_df = pp.to_html()

f = open("Hours worked 2016.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

pp = ProfileReport(df_Hrs_Wrked_2018, title="Hours Worked 2018")
pp_df = pp.to_html()

f = open("Hours worked 2018.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

pp = ProfileReport(df_Hrs_Wrked_2020, title="Hours Worked 2020")
pp_df = pp.to_html()

f = open("Hours worked 2020.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

# %% [markdown]
# Grabbing the year (REF_DATE) from 2017, 2019, and 2021 individually for "Number of jobs".

# %%
print("Grabbing the data from 2017, 2019, and 2021.")
df_NumOfJob_2016 = df_NumOfJob_above_2016.loc[
    (df_NumOfJob_above_2016['REF_DATE'] == 2016) |
    (df_NumOfJob_above_2016['REF_DATE'] == 2017)
]

df_NumOfJob_2018 = df_NumOfJob_above_2016.loc[
    (df_NumOfJob_above_2016['REF_DATE'] == 2018) |
    (df_NumOfJob_above_2016['REF_DATE'] == 2019)
]

df_NumOfJob_2020 = df_NumOfJob_above_2016.loc[
    (df_NumOfJob_above_2016['REF_DATE'] == 2020) |
    (df_NumOfJob_above_2016['REF_DATE'] == 2021)
]

grouped = df_NumOfJob_2016.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

grouped = df_NumOfJob_2018.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

grouped = df_NumOfJob_2020.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

# %% [markdown]
# Panda Profiling for year 2017, 2019, and 2021 for "Number of jobs".

# %%
pp = ProfileReport(df_NumOfJob_2016, title="Number of jobs 2016")
pp_df = pp.to_html()

f = open("Number of jobs 2016.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

pp = ProfileReport(df_NumOfJob_2018, title="Number of jobs 2018")
pp_df = pp.to_html()

f = open("Number of jobs 2018.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

pp = ProfileReport(df_NumOfJob_2020, title="Number of jobs 2020")
pp_df = pp.to_html()

f = open("Number of jobs 2020.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

# %% [markdown]
# Grabbing the year (REF_DATE) from 2017, 2019, and 2021 individually for "Wages and Salaries".

# %%
print("Grabbing the data from 2017, 2019, and 2021.")
df_WagesAndSalaries_2016 = df_WagesAndSalaries_above_2016.loc[
    (df_WagesAndSalaries_above_2016['REF_DATE'] == 2016) |
    (df_WagesAndSalaries_above_2016['REF_DATE'] == 2017)
]

df_WagesAndSalaries_2018 = df_WagesAndSalaries_above_2016.loc[
    (df_WagesAndSalaries_above_2016['REF_DATE'] == 2018) |
    (df_WagesAndSalaries_above_2016['REF_DATE'] == 2019)
]

df_WagesAndSalaries_2020 = df_WagesAndSalaries_above_2016.loc[
    (df_WagesAndSalaries_above_2016['REF_DATE'] == 2020) |
    (df_WagesAndSalaries_above_2016['REF_DATE'] == 2021)
]

grouped = df_WagesAndSalaries_2016.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

grouped = df_WagesAndSalaries_2018.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

grouped = df_WagesAndSalaries_2020.groupby(['REF_DATE'])
print(grouped['VALUE'].agg([np.sum, np.size]))

# %% [markdown]
# Panda Profiling for year 2017, 2019, and 2021 for "Wages and Salaries".

# %%
pp = ProfileReport(df_WagesAndSalaries_2016, title="Wages and Salaries 2016")
pp_df = pp.to_html()

f = open("Wages and Salaries 2016.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

pp = ProfileReport(df_WagesAndSalaries_2018, title="Wages and Salaries 2018")
pp_df = pp.to_html()

f = open("Wages and Salaries 2018.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

pp = ProfileReport(df_WagesAndSalaries_2020, title="Wages and Salaries 2020")
pp_df = pp.to_html()

f = open("Wages and Salaries 2020.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

# %%
print("For next step, I was originally wanted to proceeded with \n",
      "Divide the data into province and territorial and then divide into\n",
      "Sub categorical, like age group. I have decided to scrap the plan\n",
      "It is taking longer to do analysis and could bring more confusion")

# %% [markdown]
# Filtered for "Average annual hours worked" by following: "Age group", "Gender level", "Education level", "Immigration status", and "Aboriginal status".

# %%
# # Whole Dataset inside Average Annual Hours Worked

# print("\nAge group in Alberta")
# df_AvgAnnHrsWrk_ByAge = df_AvgAnnHrsWrk.loc[
#     (df_AvgAnnHrsWrk['Characteristics'] == '15 to 24 years') |
#     (df_AvgAnnHrsWrk['Characteristics'] == '25 to 34 years') |
#     (df_AvgAnnHrsWrk['Characteristics'] == '35 to 44 years') |
#     (df_AvgAnnHrsWrk['Characteristics'] == '45 to 54 years') |
#     (df_AvgAnnHrsWrk['Characteristics'] == '55 to 64 years') |
#     (df_AvgAnnHrsWrk['Characteristics'] == '65 years old and over')]
# print(df_AvgAnnHrsWrk_ByAge.head(20))
# grouped = df_AvgAnnHrsWrk_ByAge.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnHrsWrk_ByAge.index))

# print("\nGender group in Alberta")
# df_AvgAnnHrsWrk_ByGender = df_AvgAnnHrsWrk.loc[
#     (df_AvgAnnHrsWrk['Characteristics'] == 'Female employees') |
#     (df_AvgAnnHrsWrk['Characteristics'] == 'Male employees')
# ]
# print(df_AvgAnnHrsWrk_ByGender.head(20))
# grouped = df_AvgAnnHrsWrk_ByGender.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnHrsWrk_ByGender.index))

# print("\nEducation group in Alberta")
# df_AvgAnnHrsWrk_ByEducation = df_AvgAnnHrsWrk.loc[
#     (df_AvgAnnHrsWrk['Characteristics'] == 'High school diploma and less') |
#     (df_AvgAnnHrsWrk['Characteristics'] == 'Trade certificate') |
#     (df_AvgAnnHrsWrk['Characteristics'] == 'University degree and higher')
# ]
# print(df_AvgAnnHrsWrk_ByEducation.head(20))
# grouped = df_AvgAnnHrsWrk_ByEducation.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnHrsWrk_ByEducation.index))

# print("\nImmigrant group in Alberta")
# df_AvgAnnHrsWrk_ByImmigrant = df_AvgAnnHrsWrk.loc[
#     (df_AvgAnnHrsWrk['Characteristics'] == 'Immigrant employees') |
#     (df_AvgAnnHrsWrk['Characteristics'] == 'Non-immigrant employees')
# ]
# print(df_AvgAnnHrsWrk_ByImmigrant.head(20))
# grouped = df_AvgAnnHrsWrk_ByImmigrant.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnHrsWrk_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgAnnHrk_ByIndigenous = df_AvgAnnHrsWrk.loc[
#     (df_AvgAnnHrsWrk['Characteristics'] == 'Indigenous identity employees') |
#     (df_AvgAnnHrsWrk['Characteristics'] == 'Non-indigenous identity employees')
# ]
# print(df_AvgAnnHrk_ByIndigenous.head(20))
# grouped = df_AvgAnnHrk_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnHrk_ByIndigenous.index))

# %%
# # Dataset year is below 2016 inside Average Annual Hours Worked

# print("\nAge group in Alberta")
# df_AvgAnnHrsWrk_below_2016_ByAge = df_AvgAnnHrsWrk_below_2016.loc[
#     (df_AvgAnnHrsWrk_below_2016['Characteristics'] == '15 to 24 years') |
#     (df_AvgAnnHrsWrk_below_2016['Characteristics'] == '25 to 34 years') |
#     (df_AvgAnnHrsWrk_below_2016['Characteristics'] == '35 to 44 years') |
#     (df_AvgAnnHrsWrk_below_2016['Characteristics'] == '45 to 54 years') |
#     (df_AvgAnnHrsWrk_below_2016['Characteristics'] == '55 to 64 years') |
#     (df_AvgAnnHrsWrk_below_2016['Characteristics'] == '65 years old and over')]
# print(df_AvgAnnHrsWrk_below_2016_ByAge.head(20))
# grouped = df_AvgAnnHrsWrk_below_2016_ByAge.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnHrsWrk_below_2016_ByAge.index))

# print("\nGender group in Alberta")
# df_AvgAnnHrsWrk_below_2016_ByGender = df_AvgAnnHrsWrk_below_2016.loc[
#     (df_AvgAnnHrsWrk_below_2016['Characteristics'] == 'Female employees') |
#     (df_AvgAnnHrsWrk_below_2016['Characteristics'] == 'Male employees')
# ]
# print(df_AvgAnnHrsWrk_below_2016_ByGender.head(20))
# grouped = df_AvgAnnHrsWrk_below_2016_ByGender.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnHrsWrk_below_2016_ByGender.index))

# print("\nEducation group in Alberta")
# df_AvgAnnHrsWrk_below_2016_ByEducation = df_AvgAnnHrsWrk_below_2016.loc[
#     (df_AvgAnnHrsWrk_below_2016['Characteristics'] == 'High school diploma and less') |
#     (df_AvgAnnHrsWrk_below_2016['Characteristics'] == 'Trade certificate') |
#     (df_AvgAnnHrsWrk_below_2016['Characteristics'] == 'University degree and higher')
# ]
# print(df_AvgAnnHrsWrk_below_2016_ByEducation.head(20))
# grouped = df_AvgAnnHrsWrk_below_2016_ByEducation.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnHrsWrk_below_2016_ByEducation.index))

# print("\nImmigrant group in Alberta")
# df_AvgAnnHrsWrk_below_2016_ByImmigrant = df_AvgAnnHrsWrk_below_2016.loc[
#     (df_AvgAnnHrsWrk_below_2016['Characteristics'] == 'Immigrant employees') |
#     (df_AvgAnnHrsWrk_below_2016['Characteristics'] == 'Non-immigrant employees')
# ]
# print(df_AvgAnnHrsWrk_below_2016_ByImmigrant.head(20))
# grouped = df_AvgAnnHrsWrk_below_2016_ByImmigrant.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnHrsWrk_below_2016_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgAnnHrsWrk_below_2016_ByIndigenous = df_AvgAnnHrsWrk_below_2016.loc[
#     (df_AvgAnnHrsWrk_below_2016['Characteristics'] == 'Indigenous identity employees') |
#     (df_AvgAnnHrsWrk_below_2016['Characteristics'] == 'Non-indigenous identity employees')
# ]
# print(df_AvgAnnHrsWrk_below_2016_ByIndigenous.head(20))
# grouped = df_AvgAnnHrsWrk_below_2016_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnHrsWrk_below_2016_ByIndigenous.index))

# %%
# Dataset year is above 2017 inside Average Annual Hours Worked

# https://medium.com/@atanudan/kurtosis-skew-function-in-pandas-aa63d72e20de
# https://towardsdatascience.com/learning-pandas-profiling-fc533336edc7
# https://jakevdp.github.io/PythonDataScienceHandbook/02.04-computation-on-arrays-aggregates.html
# https://medium.com/@pritul.dave/everything-about-moments-skewness-and-kurtosis-using-python-numpy-df305a193e46

print("\nAge group in Alberta")
df_AvgAnnHrsWrk_above_2016_ByAge = df_AvgAnnHrsWrk_above_2016.loc[
    (df_AvgAnnHrsWrk_above_2016['Characteristics'] == '15 to 24 years') |
    (df_AvgAnnHrsWrk_above_2016['Characteristics'] == '25 to 34 years') |
    (df_AvgAnnHrsWrk_above_2016['Characteristics'] == '35 to 44 years') |
    (df_AvgAnnHrsWrk_above_2016['Characteristics'] == '45 to 54 years') |
    (df_AvgAnnHrsWrk_above_2016['Characteristics'] == '55 to 64 years') |
    (df_AvgAnnHrsWrk_above_2016['Characteristics'] == '65 years old and over')]
print(df_AvgAnnHrsWrk_above_2016_ByAge.head(20))
grouped = df_AvgAnnHrsWrk_above_2016_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("Total size : ",len(df_AvgAnnHrsWrk_above_2016_ByAge.index))

print("\nGender group in Alberta")
df_AvgAnnHrsWrk_above_2016_ByGender = df_AvgAnnHrsWrk_above_2016.loc[
    (df_AvgAnnHrsWrk_above_2016['Characteristics'] == 'Female employees') |
    (df_AvgAnnHrsWrk_above_2016['Characteristics'] == 'Male employees')
]
print(df_AvgAnnHrsWrk_above_2016_ByGender.head(20))
grouped = df_AvgAnnHrsWrk_above_2016_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("Total size : ",len(df_AvgAnnHrsWrk_above_2016_ByGender.index))

print("\nEducation group in Alberta")
df_AvgAnnHrsWrk_above_2016_ByEducation = df_AvgAnnHrsWrk_above_2016.loc[
    (df_AvgAnnHrsWrk_above_2016['Characteristics'] == 'High school diploma and less') |
    (df_AvgAnnHrsWrk_above_2016['Characteristics'] == 'Trade certificate') |
    (df_AvgAnnHrsWrk_above_2016['Characteristics'] == 'University degree and higher')
]
print(df_AvgAnnHrsWrk_above_2016_ByEducation.head(20))
grouped = df_AvgAnnHrsWrk_above_2016_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("Total size : ",len(df_AvgAnnHrsWrk_above_2016_ByEducation.index))

print("\nImmigrant group in Alberta")
df_AvgAnnHrsWrk_above_2016_ByImmigrant = df_AvgAnnHrsWrk_above_2016.loc[
    (df_AvgAnnHrsWrk_above_2016['Characteristics'] == 'Immigrant employees') |
    (df_AvgAnnHrsWrk_above_2016['Characteristics'] == 'Non-immigrant employees')
]
print(df_AvgAnnHrsWrk_above_2016_ByImmigrant.head(20))
grouped = df_AvgAnnHrsWrk_above_2016_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("Total size : ",len(df_AvgAnnHrsWrk_above_2016_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgAnnHrsWrk_above_2016_ByIndigenous = df_AvgAnnHrsWrk_above_2016.loc[
#     (df_AvgAnnHrsWrk_above_2016['Characteristics'] == 'Indigenous identity employees') |
#     (df_AvgAnnHrsWrk_above_2016['Characteristics'] == 'Non-indigenous identity employees')
# ]
# print(df_AvgAnnHrsWrk_above_2016_ByIndigenous.head(20))
# grouped = df_AvgAnnHrsWrk_above_2016_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.mean, np.size]))
# print("The total number of this one is ",len(df_AvgAnnHrsWrk_above_2016_ByIndigenous.index))

# %%
# Dataset year in 2017 inside Average Annual Hours Worked

print("\nAge group in Alberta")
df_AvgAnnHrsWrk_2016_ByAge = df_AvgAnnHrsWrk_2016.loc[
    (df_AvgAnnHrsWrk_2016['Characteristics'] == '15 to 24 years') |
    (df_AvgAnnHrsWrk_2016['Characteristics'] == '25 to 34 years') |
    (df_AvgAnnHrsWrk_2016['Characteristics'] == '35 to 44 years') |
    (df_AvgAnnHrsWrk_2016['Characteristics'] == '45 to 54 years') |
    (df_AvgAnnHrsWrk_2016['Characteristics'] == '55 to 64 years') |
    (df_AvgAnnHrsWrk_2016['Characteristics'] == '65 years old and over')]
print(df_AvgAnnHrsWrk_2016_ByAge.head(20))
grouped = df_AvgAnnHrsWrk_2016_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("Total size : ",len(df_AvgAnnHrsWrk_2016_ByAge.index))

print("\nGender group in Alberta")
df_AvgAnnHrsWrk_2016_ByGender = df_AvgAnnHrsWrk_2016.loc[
    (df_AvgAnnHrsWrk_2016['Characteristics'] == 'Female employees') |
    (df_AvgAnnHrsWrk_2016['Characteristics'] == 'Male employees')
]
print(df_AvgAnnHrsWrk_2016_ByGender.head(20))
grouped = df_AvgAnnHrsWrk_2016_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("Total size : ",len(df_AvgAnnHrsWrk_2016_ByGender.index))

print("\nEducation group in Alberta")
df_AvgAnnHrsWrk_2016_ByEducation = df_AvgAnnHrsWrk_2016.loc[
    (df_AvgAnnHrsWrk_2016['Characteristics'] == 'High school diploma and less') |
    (df_AvgAnnHrsWrk_2016['Characteristics'] == 'Trade certificate') |
    (df_AvgAnnHrsWrk_2016['Characteristics'] == 'University degree and higher')
]
print(df_AvgAnnHrsWrk_2016_ByEducation.head(20))
grouped = df_AvgAnnHrsWrk_2016_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("Total size : ",len(df_AvgAnnHrsWrk_2016_ByEducation.index))

print("\nImmigrant group in Alberta")
df_AvgAnnHrsWrk_2016_ByImmigrant = df_AvgAnnHrsWrk_2016.loc[
    (df_AvgAnnHrsWrk_2016['Characteristics'] == 'Immigrant employees') |
    (df_AvgAnnHrsWrk_2016['Characteristics'] == 'Non-immigrant employees')
]
print(df_AvgAnnHrsWrk_2016_ByImmigrant.head(20))
grouped = df_AvgAnnHrsWrk_2016_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("Total size : ",len(df_AvgAnnHrsWrk_2016_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgAnnHrk_2017_ByIndigenous = df_AvgAnnHrsWrk_2016.loc[
#     (df_AvgAnnHrsWrk_2016['Characteristics'] == 'Indigenous identity employees') |
#     (df_AvgAnnHrsWrk_2016['Characteristics'] == 'Non-indigenous identity employees')
# ]
# print(df_AvgAnnHrk_2017_ByIndigenous.head(20))
# grouped = df_AvgAnnHrk_2017_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnHrk_2017_ByIndigenous.index))

# %%
# Dataset year in 2019 inside Average Annual Hours Worked

print("\nAge group in Alberta")
df_AvgAnnHrsWrk_2018_ByAge = df_AvgAnnHrsWrk_2018.loc[
    (df_AvgAnnHrsWrk_2018['Characteristics'] == '15 to 24 years') |
    (df_AvgAnnHrsWrk_2018['Characteristics'] == '25 to 34 years') |
    (df_AvgAnnHrsWrk_2018['Characteristics'] == '35 to 44 years') |
    (df_AvgAnnHrsWrk_2018['Characteristics'] == '45 to 54 years') |
    (df_AvgAnnHrsWrk_2018['Characteristics'] == '55 to 64 years') |
    (df_AvgAnnHrsWrk_2018['Characteristics'] == '65 years old and over')]
print(df_AvgAnnHrsWrk_2018_ByAge.head(20))
grouped = df_AvgAnnHrsWrk_2018_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("Total size : ",len(df_AvgAnnHrsWrk_2018_ByAge.index))

print("\nGender group in Alberta")
df_AvgAnnHrsWrk_2018_ByGender = df_AvgAnnHrsWrk_2018.loc[
    (df_AvgAnnHrsWrk_2018['Characteristics'] == 'Female employees') |
    (df_AvgAnnHrsWrk_2018['Characteristics'] == 'Male employees')
]
print(df_AvgAnnHrsWrk_2018_ByGender.head(20))
grouped = df_AvgAnnHrsWrk_2018_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("Total size : ",len(df_AvgAnnHrsWrk_2018_ByGender.index))

print("\nEducation group in Alberta")
df_AvgAnnHrsWrk_2018_ByEducation = df_AvgAnnHrsWrk_2018.loc[
    (df_AvgAnnHrsWrk_2018['Characteristics'] == 'High school diploma and less') |
    (df_AvgAnnHrsWrk_2018['Characteristics'] == 'Trade certificate') |
    (df_AvgAnnHrsWrk_2018['Characteristics'] == 'University degree and higher')
]
print(df_AvgAnnHrsWrk_2018_ByEducation.head(20))
grouped = df_AvgAnnHrsWrk_2018_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("Total size : ",len(df_AvgAnnHrsWrk_2018_ByEducation.index))

print("\nImmigrant group in Alberta")
df_AvgAnnHrsWrk_2018_ByImmigrant = df_AvgAnnHrsWrk_2018.loc[
    (df_AvgAnnHrsWrk_2018['Characteristics'] == 'Immigrant employees') |
    (df_AvgAnnHrsWrk_2018['Characteristics'] == 'Non-immigrant employees')
]
print(df_AvgAnnHrsWrk_2018_ByImmigrant.head(20))
grouped = df_AvgAnnHrsWrk_2018_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("Total size : ",len(df_AvgAnnHrsWrk_2018_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgAnnHrk_2017_ByIndigenous = df_AvgAnnHrsWrk_2018.loc[
#     (df_AvgAnnHrsWrk_2018['Characteristics'] == 'Indigenous identity employees') |
#     (df_AvgAnnHrsWrk_2018['Characteristics'] == 'Non-indigenous identity employees')
# ]
# print(df_AvgAnnHrk_2017_ByIndigenous.head(20))
# grouped = df_AvgAnnHrk_2017_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnHrk_2017_ByIndigenous.index))

# %%
# Dataset year in 2020 inside Average Annual Hours Worked

print("\nAge group in Alberta")
df_AvgAnnHrsWrk_2020_ByAge = df_AvgAnnHrsWrk_2020.loc[
    (df_AvgAnnHrsWrk_2020['Characteristics'] == '15 to 24 years') |
    (df_AvgAnnHrsWrk_2020['Characteristics'] == '25 to 34 years') |
    (df_AvgAnnHrsWrk_2020['Characteristics'] == '35 to 44 years') |
    (df_AvgAnnHrsWrk_2020['Characteristics'] == '45 to 54 years') |
    (df_AvgAnnHrsWrk_2020['Characteristics'] == '55 to 64 years') |
    (df_AvgAnnHrsWrk_2020['Characteristics'] == '65 years old and over')]
print(df_AvgAnnHrsWrk_2020_ByAge.head(20))
grouped = df_AvgAnnHrsWrk_2020_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("Total size : ",len(df_AvgAnnHrsWrk_2020_ByAge.index))

print("\nGender group in Alberta")
df_AvgAnnHrsWrk_2020_ByGender = df_AvgAnnHrsWrk_2020.loc[
    (df_AvgAnnHrsWrk_2020['Characteristics'] == 'Female employees') |
    (df_AvgAnnHrsWrk_2020['Characteristics'] == 'Male employees')
]
print(df_AvgAnnHrsWrk_2020_ByGender.head(20))
grouped = df_AvgAnnHrsWrk_2020_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("Total size : ",len(df_AvgAnnHrsWrk_2020_ByGender.index))

print("\nEducation group in Alberta")
df_AvgAnnHrsWrk_2020_ByEducation = df_AvgAnnHrsWrk_2020.loc[
    (df_AvgAnnHrsWrk_2020['Characteristics'] == 'High school diploma and less') |
    (df_AvgAnnHrsWrk_2020['Characteristics'] == 'Trade certificate') |
    (df_AvgAnnHrsWrk_2020['Characteristics'] == 'University degree and higher')
]
print(df_AvgAnnHrsWrk_2020_ByEducation.head(20))
grouped = df_AvgAnnHrsWrk_2020_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("Total size : ",len(df_AvgAnnHrsWrk_2020_ByEducation.index))

print("\nImmigrant group in Alberta")
df_AvgAnnHrsWrk_2020_ByImmigrant = df_AvgAnnHrsWrk_2020.loc[
    (df_AvgAnnHrsWrk_2020['Characteristics'] == 'Immigrant employees') |
    (df_AvgAnnHrsWrk_2020['Characteristics'] == 'Non-immigrant employees')
]
print(df_AvgAnnHrsWrk_2020_ByImmigrant.head(20))
grouped = df_AvgAnnHrsWrk_2020_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("Total size : ",len(df_AvgAnnHrsWrk_2020_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgAnnHrk_2017_ByIndigenous = df_AvgAnnHrsWrk_2020.loc[
#     (df_AvgAnnHrsWrk_2020['Characteristics'] == 'Indigenous identity employees') |
#     (df_AvgAnnHrsWrk_2020['Characteristics'] == 'Non-indigenous identity employees')
# ]
# print(df_AvgAnnHrk_2017_ByIndigenous.head(20))
# grouped = df_AvgAnnHrk_2017_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnHrk_2017_ByIndigenous.index))

# %% [markdown]
# Filtered for "Average annual wages and salaries" by following: "Age group", "Gender level", "Education level", "Immigration status", and "Aboriginal status".

# %%
# # Whole Dataset inside Average annual wages and salaries
# print("\nAge group in Alberta")
# df_AvgAnnWages_ByAge = df_AvgAnnWages.loc[
#     (df_AvgAnnWages['Characteristics'] == '15 to 24 years') |
#     (df_AvgAnnWages['Characteristics'] == '25 to 34 years') |
#     (df_AvgAnnWages['Characteristics'] == '35 to 44 years') |
#     (df_AvgAnnWages['Characteristics'] == '45 to 54 years') |
#     (df_AvgAnnWages['Characteristics'] == '55 to 64 years') |
#     (df_AvgAnnWages['Characteristics'] == '65 years old and over')]
# print(df_AvgAnnWages_ByAge.head(20))
# grouped = df_AvgAnnWages_ByAge.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnWages_ByAge.index))

# print("\nGender group in Alberta")
# df_AvgAnnWages_ByGender = df_AvgAnnWages.loc[
#     (df_AvgAnnWages['Characteristics'] == 'Female employees') |
#     (df_AvgAnnWages['Characteristics'] == 'Male employees')
# ]
# print(df_AvgAnnWages_ByGender.head(20))
# grouped = df_AvgAnnWages_ByGender.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnWages_ByGender.index))

# print("\nEducation group in Alberta")
# df_AvgAnnWages_ByEducation = df_AvgAnnWages.loc[
#     (df_AvgAnnWages['Characteristics'] == 'High school diploma and less') |
#     (df_AvgAnnWages['Characteristics'] == 'Trade certificate') |
#     (df_AvgAnnWages['Characteristics'] == 'University degree and higher')
# ]
# print(df_AvgAnnWages_ByEducation.head(20))
# grouped = df_AvgAnnWages_ByEducation.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnWages_ByEducation.index))

# print("\nImmigrant group in Alberta")
# df_AvgAnnWages_ByImmigrant = df_AvgAnnWages.loc[
#     (df_AvgAnnWages['Characteristics'] == 'Immigrant employees') |
#     (df_AvgAnnWages['Characteristics'] == 'Non-immigrant employees')
# ]
# print(df_AvgAnnWages_ByImmigrant.head(20))
# grouped = df_AvgAnnWages_ByImmigrant.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnWages_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgAnnHrk_ByIndigenous = df_AvgAnnWages.loc[
#     (df_AvgAnnWages['Characteristics'] == 'Indigenous identity employees') |
#     (df_AvgAnnWages['Characteristics'] == 'Non-indigenous identity employees')
# ]
# print(df_AvgAnnHrk_ByIndigenous.head(20))
# grouped = df_AvgAnnHrk_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnHrk_ByIndigenous.index))

# %%
# # Dataset year below year 2016 inside Average annual wages and salaries

# print("\nAge group in Alberta")
# df_AvgAnnWages_below_2016_ByAge = df_AvgAnnWages_below_2016.loc[
#     (df_AvgAnnWages_below_2016['Characteristics'] == '15 to 24 years') |
#     (df_AvgAnnWages_below_2016['Characteristics'] == '25 to 34 years') |
#     (df_AvgAnnWages_below_2016['Characteristics'] == '35 to 44 years') |
#     (df_AvgAnnWages_below_2016['Characteristics'] == '45 to 54 years') |
#     (df_AvgAnnWages_below_2016['Characteristics'] == '55 to 64 years') |
#     (df_AvgAnnWages_below_2016['Characteristics'] == '65 years old and over')]
# print(df_AvgAnnWages_below_2016_ByAge.head(20))
# grouped = df_AvgAnnWages_below_2016_ByAge.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnWages_below_2016_ByAge.index))

# print("\nGender group in Alberta")
# df_AvgAnnWages_below_2016_ByGender = df_AvgAnnWages_below_2016.loc[
#     (df_AvgAnnWages_below_2016['Characteristics'] == 'Female employees') |
#     (df_AvgAnnWages_below_2016['Characteristics'] == 'Male employees')
# ]
# print(df_AvgAnnWages_below_2016_ByGender.head(20))
# grouped = df_AvgAnnWages_below_2016_ByGender.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnWages_below_2016_ByGender.index))

# print("\nEducation group in Alberta")
# df_AvgAnnWages_below_2016_ByEducation = df_AvgAnnWages_below_2016.loc[
#     (df_AvgAnnWages_below_2016['Characteristics'] == 'High school diploma and less') |
#     (df_AvgAnnWages_below_2016['Characteristics'] == 'Trade certificate') |
#     (df_AvgAnnWages_below_2016['Characteristics'] == 'University degree and higher')
# ]
# print(df_AvgAnnWages_below_2016_ByEducation.head(20))
# grouped = df_AvgAnnWages_below_2016_ByEducation.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnWages_below_2016_ByEducation.index))

# print("\nImmigrant group in Alberta")
# df_AvgAnnWages_below_2016_ByImmigrant = df_AvgAnnWages_below_2016.loc[
#     (df_AvgAnnWages_below_2016['Characteristics'] == 'Immigrant employees') |
#     (df_AvgAnnWages_below_2016['Characteristics'] == 'Non-immigrant employees')
# ]
# print(df_AvgAnnWages_below_2016_ByImmigrant.head(20))
# grouped = df_AvgAnnWages_below_2016_ByImmigrant.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnWages_below_2016_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgAnnHrk_ByIndigenous = df_AvgAnnWages_below_2016.loc[
#     (df_AvgAnnWages_below_2016['Characteristics'] == 'Indigenous identity employees') |
#     (df_AvgAnnWages_below_2016['Characteristics'] == 'Non-indigenous identity employees')
# ]
# print(df_AvgAnnHrk_ByIndigenous.head(20))
# grouped = df_AvgAnnHrk_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnHrk_ByIndigenous.index))

# %%
# Dataset year above year of 2017 inside Average annual wages and salaries

print("\nAge group in Alberta")
df_AvgAnnWages_above_2016_ByAge = df_AvgAnnWages_above_2016.loc[
    (df_AvgAnnWages_above_2016['Characteristics'] == '15 to 24 years') |
    (df_AvgAnnWages_above_2016['Characteristics'] == '25 to 34 years') |
    (df_AvgAnnWages_above_2016['Characteristics'] == '35 to 44 years') |
    (df_AvgAnnWages_above_2016['Characteristics'] == '45 to 54 years') |
    (df_AvgAnnWages_above_2016['Characteristics'] == '55 to 64 years') |
    (df_AvgAnnWages_above_2016['Characteristics'] == '65 years old and over')]
print(df_AvgAnnWages_above_2016_ByAge.head(20))
grouped = df_AvgAnnWages_above_2016_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgAnnWages_above_2016_ByAge.index))

print("\nGender group in Alberta")
df_AvgAnnWages_above_2016_ByGender = df_AvgAnnWages_above_2016.loc[
    (df_AvgAnnWages_above_2016['Characteristics'] == 'Female employees') |
    (df_AvgAnnWages_above_2016['Characteristics'] == 'Male employees')
]
print(df_AvgAnnWages_above_2016_ByGender.head(20))
grouped = df_AvgAnnWages_above_2016_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgAnnWages_above_2016_ByGender.index))

print("\nEducation group in Alberta")
df_AvgAnnWages_above_2016_ByEducation = df_AvgAnnWages_above_2016.loc[
    (df_AvgAnnWages_above_2016['Characteristics'] == 'High school diploma and less') |
    (df_AvgAnnWages_above_2016['Characteristics'] == 'Trade certificate') |
    (df_AvgAnnWages_above_2016['Characteristics'] == 'University degree and higher')
]
print(df_AvgAnnWages_above_2016_ByEducation.head(20))
grouped = df_AvgAnnWages_above_2016_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgAnnWages_above_2016_ByEducation.index))

print("\nImmigrant group in Alberta")
df_AvgAnnWages_above_2016_ByImmigrant = df_AvgAnnWages_above_2016.loc[
    (df_AvgAnnWages_above_2016['Characteristics'] == 'Immigrant employees') |
    (df_AvgAnnWages_above_2016['Characteristics'] == 'Non-immigrant employees')
]
print(df_AvgAnnWages_above_2016_ByImmigrant.head(20))
grouped = df_AvgAnnWages_above_2016_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgAnnWages_above_2016_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgAnnWages_above_2016_ByIndigenous = df_AvgAnnWages_above_2016.loc[
#     (df_AvgAnnWages_above_2016['Characteristics'] == 'Indigenous identity employees') |
#     (df_AvgAnnWages_above_2016['Characteristics'] == 'Non-indigenous identity employees')
# ]
# print(df_AvgAnnWages_above_2016_ByIndigenous.head(20))
# grouped = df_AvgAnnWages_above_2016_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnWages_above_2016_ByIndigenous.index))

# %%
# Dataset year in 2017 inside Average annual wages and salaries

print("\nAge group in Alberta")
df_AvgAnnWages_2016_ByAge = df_AvgAnnWages_2016.loc[
    (df_AvgAnnWages_2016['Characteristics'] == '15 to 24 years') |
    (df_AvgAnnWages_2016['Characteristics'] == '25 to 34 years') |
    (df_AvgAnnWages_2016['Characteristics'] == '35 to 44 years') |
    (df_AvgAnnWages_2016['Characteristics'] == '45 to 54 years') |
    (df_AvgAnnWages_2016['Characteristics'] == '55 to 64 years') |
    (df_AvgAnnWages_2016['Characteristics'] == '65 years old and over')]
print(df_AvgAnnWages_2016_ByAge.head(20))
grouped = df_AvgAnnWages_2016_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgAnnWages_2016_ByAge.index))

print("\nGender group in Alberta")
df_AvgAnnWages_2016_ByGender = df_AvgAnnWages_2016.loc[
    (df_AvgAnnWages_2016['Characteristics'] == 'Female employees') |
    (df_AvgAnnWages_2016['Characteristics'] == 'Male employees')
]
print(df_AvgAnnWages_2016_ByGender.head(20))
grouped = df_AvgAnnWages_2016_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgAnnWages_2016_ByGender.index))

print("\nEducation group in Alberta")
df_AvgAnnWages_2016_ByEducation = df_AvgAnnWages_2016.loc[
    (df_AvgAnnWages_2016['Characteristics'] == 'High school diploma and less') |
    (df_AvgAnnWages_2016['Characteristics'] == 'Trade certificate') |
    (df_AvgAnnWages_2016['Characteristics'] == 'University degree and higher')
]
print(df_AvgAnnWages_2016_ByEducation.head(20))
grouped = df_AvgAnnWages_2016_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgAnnWages_2016_ByEducation.index))

print("\nImmigrant group in Alberta")
df_AvgAnnWages_2016_ByImmigrant = df_AvgAnnWages_2016.loc[
    (df_AvgAnnWages_2016['Characteristics'] == 'Immigrant employees') |
    (df_AvgAnnWages_2016['Characteristics'] == 'Non-immigrant employees')
]
print(df_AvgAnnWages_2016_ByImmigrant.head(20))
grouped = df_AvgAnnWages_2016_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgAnnWages_2016_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgAnnHrk_ByIndigenous = df_AvgAnnWages_2016.loc[
#     (df_AvgAnnWages_2016['Characteristics'] == 'Indigenous identity employees') |
#     (df_AvgAnnWages_2016['Characteristics'] == 'Non-indigenous identity employees')
# ]
# print(df_AvgAnnHrk_ByIndigenous.head(20))
# grouped = df_AvgAnnHrk_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnHrk_ByIndigenous.index))

# %%
# Dataset year in 2019 inside Average annual wages and salaries

print("\nAge group in Alberta")
df_AvgAnnWages_2018_ByAge = df_AvgAnnWages_2018.loc[
    (df_AvgAnnWages_2018['Characteristics'] == '15 to 24 years') |
    (df_AvgAnnWages_2018['Characteristics'] == '25 to 34 years') |
    (df_AvgAnnWages_2018['Characteristics'] == '35 to 44 years') |
    (df_AvgAnnWages_2018['Characteristics'] == '45 to 54 years') |
    (df_AvgAnnWages_2018['Characteristics'] == '55 to 64 years') |
    (df_AvgAnnWages_2018['Characteristics'] == '65 years old and over')]
print(df_AvgAnnWages_2018_ByAge.head(20))
grouped = df_AvgAnnWages_2018_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgAnnWages_2018_ByAge.index))

print("\nGender group in Alberta")
df_AvgAnnWages_2018_ByGender = df_AvgAnnWages_2018.loc[
    (df_AvgAnnWages_2018['Characteristics'] == 'Female employees') |
    (df_AvgAnnWages_2018['Characteristics'] == 'Male employees')
]
print(df_AvgAnnWages_2018_ByGender.head(20))
grouped = df_AvgAnnWages_2018_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgAnnWages_2018_ByGender.index))

print("\nEducation group in Alberta")
df_AvgAnnWages_2018_ByEducation = df_AvgAnnWages_2018.loc[
    (df_AvgAnnWages_2018['Characteristics'] == 'High school diploma and less') |
    (df_AvgAnnWages_2018['Characteristics'] == 'Trade certificate') |
    (df_AvgAnnWages_2018['Characteristics'] == 'University degree and higher')
]
print(df_AvgAnnWages_2018_ByEducation.head(20))
grouped = df_AvgAnnWages_2018_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgAnnWages_2018_ByEducation.index))

print("\nImmigrant group in Alberta")
df_AvgAnnWages_2018_ByImmigrant = df_AvgAnnWages_2018.loc[
    (df_AvgAnnWages_2018['Characteristics'] == 'Immigrant employees') |
    (df_AvgAnnWages_2018['Characteristics'] == 'Non-immigrant employees')
]
print(df_AvgAnnWages_2018_ByImmigrant.head(20))
grouped = df_AvgAnnWages_2018_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgAnnWages_2018_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgAnnHrk_ByIndigenous = df_AvgAnnWages_2018.loc[
#     (df_AvgAnnWages_2018['Characteristics'] == 'Indigenous identity employees') |
#     (df_AvgAnnWages_2018['Characteristics'] == 'Non-indigenous identity employees')
# ]
# print(df_AvgAnnHrk_ByIndigenous.head(20))
# grouped = df_AvgAnnHrk_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnHrk_ByIndigenous.index))

# %%
# Dataset year in 2021 inside Average annual wages and salaries

print("\nAge group in Alberta")
df_AvgAnnWages_2020_ByAge = df_AvgAnnWages_2020.loc[
    (df_AvgAnnWages_2020['Characteristics'] == '15 to 24 years') |
    (df_AvgAnnWages_2020['Characteristics'] == '25 to 34 years') |
    (df_AvgAnnWages_2020['Characteristics'] == '35 to 44 years') |
    (df_AvgAnnWages_2020['Characteristics'] == '45 to 54 years') |
    (df_AvgAnnWages_2020['Characteristics'] == '55 to 64 years') |
    (df_AvgAnnWages_2020['Characteristics'] == '65 years old and over')]
print(df_AvgAnnWages_2020_ByAge.head(20))
grouped = df_AvgAnnWages_2020_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgAnnWages_2020_ByAge.index))

print("\nGender group in Alberta")
df_AvgAnnWages_2020_ByGender = df_AvgAnnWages_2020.loc[
    (df_AvgAnnWages_2020['Characteristics'] == 'Female employees') |
    (df_AvgAnnWages_2020['Characteristics'] == 'Male employees')
]
print(df_AvgAnnWages_2020_ByGender.head(20))
grouped = df_AvgAnnWages_2020_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgAnnWages_2020_ByGender.index))

print("\nEducation group in Alberta")
df_AvgAnnWages_2020_ByEducation = df_AvgAnnWages_2020.loc[
    (df_AvgAnnWages_2020['Characteristics'] == 'High school diploma and less') |
    (df_AvgAnnWages_2020['Characteristics'] == 'Trade certificate') |
    (df_AvgAnnWages_2020['Characteristics'] == 'University degree and higher')
]
print(df_AvgAnnWages_2020_ByEducation.head(20))
grouped = df_AvgAnnWages_2020_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgAnnWages_2020_ByEducation.index))

print("\nImmigrant group in Alberta")
df_AvgAnnWages_2020_ByImmigrant = df_AvgAnnWages_2020.loc[
    (df_AvgAnnWages_2020['Characteristics'] == 'Immigrant employees') |
    (df_AvgAnnWages_2020['Characteristics'] == 'Non-immigrant employees')
]
print(df_AvgAnnWages_2020_ByImmigrant.head(20))
grouped = df_AvgAnnWages_2020_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgAnnWages_2020_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgAnnHrk_ByIndigenous = df_AvgAnnWages_2020.loc[
#     (df_AvgAnnWages_2020['Characteristics'] == 'Indigenous identity employees') |
#     (df_AvgAnnWages_2020['Characteristics'] == 'Non-indigenous identity employees')
# ]
# print(df_AvgAnnHrk_ByIndigenous.head(20))
# grouped = df_AvgAnnHrk_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnHrk_ByIndigenous.index))

# %% [markdown]
# Filtered for "Average hourly wage" by following: "Age group", "Gender level", "Education level", "Immigration status", and "Aboriginal status".

# %%
# # Whole Dataset inside "Average hourly wage"

# print("\nAge group in Alberta")
# df_AvgHrsWages_ByAge = df_AvgHrsWages.loc[
#     (df_AvgHrsWages['Characteristics'] == '15 to 24 years') |
#     (df_AvgHrsWages['Characteristics'] == '25 to 34 years') |
#     (df_AvgHrsWages['Characteristics'] == '35 to 44 years') |
#     (df_AvgHrsWages['Characteristics'] == '45 to 54 years') |
#     (df_AvgHrsWages['Characteristics'] == '55 to 64 years') |
#     (df_AvgHrsWages['Characteristics'] == '65 years old and over')]
# print(df_AvgHrsWages_ByAge.head(20))
# grouped = df_AvgHrsWages_ByAge.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgHrsWages_ByAge.index))

# print("\nGender group in Alberta")
# df_AvgHrsWages_ByGender = df_AvgHrsWages.loc[
#     (df_AvgHrsWages['Characteristics'] == 'Female employees') |
#     (df_AvgHrsWages['Characteristics'] == 'Male employees')
# ]
# print(df_AvgHrsWages_ByGender.head(20))
# grouped = df_AvgHrsWages_ByGender.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgHrsWages_ByGender.index))

# print("\nEducation group in Alberta")
# df_AvgHrsWages_ByEducation = df_AvgHrsWages.loc[
#     (df_AvgHrsWages['Characteristics'] == 'High school diploma and less') |
#     (df_AvgHrsWages['Characteristics'] == 'Trade certificate') |
#     (df_AvgHrsWages['Characteristics'] == 'University degree and higher')
# ]
# print(df_AvgHrsWages_ByEducation.head(20))
# grouped = df_AvgHrsWages_ByEducation.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgHrsWages_ByEducation.index))

# print("\nImmigrant group in Alberta")
# df_AvgHrsWages_ByImmigrant = df_AvgHrsWages.loc[
#     (df_AvgHrsWages['Characteristics'] == 'Immigrant employees') |
#     (df_AvgHrsWages['Characteristics'] == 'Non-immigrant employees')
# ]
# print(df_AvgHrsWages_ByImmigrant.head(20))
# grouped = df_AvgHrsWages_ByImmigrant.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgHrsWages_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgAnnHrk_ByIndigenous = df_AvgHrsWages.loc[
#     (df_AvgHrsWages['Characteristics'] == 'Indigenous identity employees') |
#     (df_AvgHrsWages['Characteristics'] == 'Non-indigenous identity employees')
# ]
# print(df_AvgAnnHrk_ByIndigenous.head(20))
# grouped = df_AvgAnnHrk_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnHrk_ByIndigenous.index))

# %%
# # Dataset year below year 2016 inside "Average hourly wage"

# print("\nAge group in Alberta")
# df_AvgHrsWages_below_2016_ByAge = df_AvgHrsWages_below_2016.loc[
#     (df_AvgHrsWages_below_2016['Characteristics'] == '15 to 24 years') |
#     (df_AvgHrsWages_below_2016['Characteristics'] == '25 to 34 years') |
#     (df_AvgHrsWages_below_2016['Characteristics'] == '35 to 44 years') |
#     (df_AvgHrsWages_below_2016['Characteristics'] == '45 to 54 years') |
#     (df_AvgHrsWages_below_2016['Characteristics'] == '55 to 64 years') |
#     (df_AvgHrsWages_below_2016['Characteristics'] == '65 years old and over')]
# print(df_AvgHrsWages_below_2016_ByAge.head(20))
# grouped = df_AvgHrsWages_below_2016_ByAge.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgHrsWages_below_2016_ByAge.index))

# print("\nGender group in Alberta")
# df_AvgHrsWages_below_2016_ByGender = df_AvgHrsWages_below_2016.loc[
#     (df_AvgHrsWages_below_2016['Characteristics'] == 'Female employees') |
#     (df_AvgHrsWages_below_2016['Characteristics'] == 'Male employees')
# ]
# print(df_AvgHrsWages_below_2016_ByGender.head(20))
# grouped = df_AvgHrsWages_below_2016_ByGender.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgHrsWages_below_2016_ByGender.index))

# print("\nEducation group in Alberta")
# df_AvgHrsWages_below_2016_ByEducation = df_AvgHrsWages_below_2016.loc[
#     (df_AvgHrsWages_below_2016['Characteristics'] == 'High school diploma and less') |
#     (df_AvgHrsWages_below_2016['Characteristics'] == 'Trade certificate') |
#     (df_AvgHrsWages_below_2016['Characteristics'] == 'University degree and higher')
# ]
# print(df_AvgHrsWages_below_2016_ByEducation.head(20))
# grouped = df_AvgHrsWages_below_2016_ByEducation.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgHrsWages_below_2016_ByEducation.index))

# print("\nImmigrant group in Alberta")
# df_AvgHrsWages_below_2016_ByImmigrant = df_AvgHrsWages_below_2016.loc[
#     (df_AvgHrsWages_below_2016['Characteristics'] == 'Immigrant employees') |
#     (df_AvgHrsWages_below_2016['Characteristics'] == 'Non-immigrant employees')
# ]
# print(df_AvgHrsWages_below_2016_ByImmigrant.head(20))
# grouped = df_AvgHrsWages_below_2016_ByImmigrant.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgHrsWages_below_2016_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgAnnHrk_ByIndigenous = df_AvgHrsWages_below_2016.loc[
#     (df_AvgHrsWages_below_2016['Characteristics'] == 'Indigenous identity employees') |
#     (df_AvgHrsWages_below_2016['Characteristics'] == 'Non-indigenous identity employees')
# ]
# print(df_AvgAnnHrk_ByIndigenous.head(20))
# grouped = df_AvgAnnHrk_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnHrk_ByIndigenous.index))

# %%
# Dataset year above year of 2017 inside "Average hourly wage"

print("\nAge group in Alberta")
df_AvgHrsWages_above_2016_ByAge = df_AvgHrsWages_above_2016.loc[
    (df_AvgHrsWages_above_2016['Characteristics'] == '15 to 24 years') |
    (df_AvgHrsWages_above_2016['Characteristics'] == '25 to 34 years') |
    (df_AvgHrsWages_above_2016['Characteristics'] == '35 to 44 years') |
    (df_AvgHrsWages_above_2016['Characteristics'] == '45 to 54 years') |
    (df_AvgHrsWages_above_2016['Characteristics'] == '55 to 64 years') |
    (df_AvgHrsWages_above_2016['Characteristics'] == '65 years old and over')]
print(df_AvgHrsWages_above_2016_ByAge.head(20))
grouped = df_AvgHrsWages_above_2016_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgHrsWages_above_2016_ByAge.index))

print("\nGender group in Alberta")
df_AvgHrsWages_above_2016_ByGender = df_AvgHrsWages_above_2016.loc[
    (df_AvgHrsWages_above_2016['Characteristics'] == 'Female employees') |
    (df_AvgHrsWages_above_2016['Characteristics'] == 'Male employees')
]
print(df_AvgHrsWages_above_2016_ByGender.head(20))
grouped = df_AvgHrsWages_above_2016_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgHrsWages_above_2016_ByGender.index))

print("\nEducation group in Alberta")
df_AvgHrsWages_above_2016_ByEducation = df_AvgHrsWages_above_2016.loc[
    (df_AvgHrsWages_above_2016['Characteristics'] == 'High school diploma and less') |
    (df_AvgHrsWages_above_2016['Characteristics'] == 'Trade certificate') |
    (df_AvgHrsWages_above_2016['Characteristics'] == 'University degree and higher')
]
print(df_AvgHrsWages_above_2016_ByEducation.head(20))
grouped = df_AvgHrsWages_above_2016_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgHrsWages_above_2016_ByEducation.index))

print("\nImmigrant group in Alberta")
df_AvgHrsWages_above_2016_ByImmigrant = df_AvgHrsWages_above_2016.loc[
    (df_AvgHrsWages_above_2016['Characteristics'] == 'Immigrant employees') |
    (df_AvgHrsWages_above_2016['Characteristics'] == 'Non-immigrant employees')
]
print(df_AvgHrsWages_above_2016_ByImmigrant.head(20))
grouped = df_AvgHrsWages_above_2016_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgHrsWages_above_2016_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgHrsWages_above_2016_ByIndigenous = df_AvgHrsWages_above_2016.loc[
#     (df_AvgHrsWages_above_2016['Characteristics'] == 'Indigenous identity employees') |
#     (df_AvgHrsWages_above_2016['Characteristics'] == 'Non-indigenous identity employees')
# ]
# print(df_AvgHrsWages_above_2016_ByIndigenous.head(20))
# grouped = df_AvgHrsWages_above_2016_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgHrsWages_above_2016_ByIndigenous.index))

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
print(df_AvgHrsWages_2016_ByAge.head(20))
grouped = df_AvgHrsWages_2016_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgHrsWages_2016_ByAge.index))

print("\nGender group in Alberta")
df_AvgHrsWages_2016_ByGender = df_AvgHrsWages_2016.loc[
    (df_AvgHrsWages_2016['Characteristics'] == 'Female employees') |
    (df_AvgHrsWages_2016['Characteristics'] == 'Male employees')
]
print(df_AvgHrsWages_2016_ByGender.head(20))
grouped = df_AvgHrsWages_2016_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgHrsWages_2016_ByGender.index))

print("\nEducation group in Alberta")
df_AvgHrsWages_2016_ByEducation = df_AvgHrsWages_2016.loc[
    (df_AvgHrsWages_2016['Characteristics'] == 'High school diploma and less') |
    (df_AvgHrsWages_2016['Characteristics'] == 'Trade certificate') |
    (df_AvgHrsWages_2016['Characteristics'] == 'University degree and higher')
]
print(df_AvgHrsWages_2016_ByEducation.head(20))
grouped = df_AvgHrsWages_2016_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgHrsWages_2016_ByEducation.index))

print("\nImmigrant group in Alberta")
df_AvgHrsWages_2016_ByImmigrant = df_AvgHrsWages_2016.loc[
    (df_AvgHrsWages_2016['Characteristics'] == 'Immigrant employees') |
    (df_AvgHrsWages_2016['Characteristics'] == 'Non-immigrant employees')
]
print(df_AvgHrsWages_2016_ByImmigrant.head(20))
grouped = df_AvgHrsWages_2016_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgHrsWages_2016_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgAnnHrk_ByIndigenous = df_AvgHrsWages_2016.loc[
#     (df_AvgHrsWages_2016['Characteristics'] == 'Indigenous identity employees') |
#     (df_AvgHrsWages_2016['Characteristics'] == 'Non-indigenous identity employees')
# ]
# print(df_AvgAnnHrk_ByIndigenous.head(20))
# grouped = df_AvgAnnHrk_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnHrk_ByIndigenous.index))

# %%
# Dataset year in 2019 inside "Average hourly wage"

print("\nAge group in Alberta")
df_AvgHrsWages_2018_ByAge = df_AvgHrsWages_2018.loc[
    (df_AvgHrsWages_2018['Characteristics'] == '15 to 24 years') |
    (df_AvgHrsWages_2018['Characteristics'] == '25 to 34 years') |
    (df_AvgHrsWages_2018['Characteristics'] == '35 to 44 years') |
    (df_AvgHrsWages_2018['Characteristics'] == '45 to 54 years') |
    (df_AvgHrsWages_2018['Characteristics'] == '55 to 64 years') |
    (df_AvgHrsWages_2018['Characteristics'] == '65 years old and over')]
print(df_AvgHrsWages_2018_ByAge.head(20))
grouped = df_AvgHrsWages_2018_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgHrsWages_2018_ByAge.index))

print("\nGender group in Alberta")
df_AvgHrsWages_2018_ByGender = df_AvgHrsWages_2018.loc[
    (df_AvgHrsWages_2018['Characteristics'] == 'Female employees') |
    (df_AvgHrsWages_2018['Characteristics'] == 'Male employees')
]
print(df_AvgHrsWages_2018_ByGender.head(20))
grouped = df_AvgHrsWages_2018_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgHrsWages_2018_ByGender.index))

print("\nEducation group in Alberta")
df_AvgHrsWages_2018_ByEducation = df_AvgHrsWages_2018.loc[
    (df_AvgHrsWages_2018['Characteristics'] == 'High school diploma and less') |
    (df_AvgHrsWages_2018['Characteristics'] == 'Trade certificate') |
    (df_AvgHrsWages_2018['Characteristics'] == 'University degree and higher')
]
print(df_AvgHrsWages_2018_ByEducation.head(20))
grouped = df_AvgHrsWages_2018_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgHrsWages_2018_ByEducation.index))

print("\nImmigrant group in Alberta")
df_AvgHrsWages_2018_ByImmigrant = df_AvgHrsWages_2018.loc[
    (df_AvgHrsWages_2018['Characteristics'] == 'Immigrant employees') |
    (df_AvgHrsWages_2018['Characteristics'] == 'Non-immigrant employees')
]
print(df_AvgHrsWages_2018_ByImmigrant.head(20))
grouped = df_AvgHrsWages_2018_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgHrsWages_2018_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgAnnHrk_ByIndigenous = df_AvgHrsWages_2018.loc[
#     (df_AvgHrsWages_2018['Characteristics'] == 'Indigenous identity employees') |
#     (df_AvgHrsWages_2018['Characteristics'] == 'Non-indigenous identity employees')
# ]
# print(df_AvgAnnHrk_ByIndigenous.head(20))
# grouped = df_AvgAnnHrk_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnHrk_ByIndigenous.index))

# %%
# Dataset year in 2021 inside "Average hourly wage"

print("\nAge group in Alberta")
df_AvgHrsWages_2020_ByAge = df_AvgHrsWages_2020.loc[
    (df_AvgHrsWages_2020['Characteristics'] == '15 to 24 years') |
    (df_AvgHrsWages_2020['Characteristics'] == '25 to 34 years') |
    (df_AvgHrsWages_2020['Characteristics'] == '35 to 44 years') |
    (df_AvgHrsWages_2020['Characteristics'] == '45 to 54 years') |
    (df_AvgHrsWages_2020['Characteristics'] == '55 to 64 years') |
    (df_AvgHrsWages_2020['Characteristics'] == '65 years old and over')]
print(df_AvgHrsWages_2020_ByAge.head(20))
grouped = df_AvgHrsWages_2020_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgHrsWages_2020_ByAge.index))

print("\nGender group in Alberta")
df_AvgHrsWages_2020_ByGender = df_AvgHrsWages_2020.loc[
    (df_AvgHrsWages_2020['Characteristics'] == 'Female employees') |
    (df_AvgHrsWages_2020['Characteristics'] == 'Male employees')
]
print(df_AvgHrsWages_2020_ByGender.head(20))
grouped = df_AvgHrsWages_2020_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgHrsWages_2020_ByGender.index))

print("\nEducation group in Alberta")
df_AvgHrsWages_2020_ByEducation = df_AvgHrsWages_2020.loc[
    (df_AvgHrsWages_2020['Characteristics'] == 'High school diploma and less') |
    (df_AvgHrsWages_2020['Characteristics'] == 'Trade certificate') |
    (df_AvgHrsWages_2020['Characteristics'] == 'University degree and higher')
]
print(df_AvgHrsWages_2020_ByEducation.head(20))
grouped = df_AvgHrsWages_2020_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgHrsWages_2020_ByEducation.index))

print("\nImmigrant group in Alberta")
df_AvgHrsWages_2020_ByImmigrant = df_AvgHrsWages_2020.loc[
    (df_AvgHrsWages_2020['Characteristics'] == 'Immigrant employees') |
    (df_AvgHrsWages_2020['Characteristics'] == 'Non-immigrant employees')
]
print(df_AvgHrsWages_2020_ByImmigrant.head(20))
grouped = df_AvgHrsWages_2020_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgHrsWages_2020_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgAnnHrk_ByIndigenous = df_AvgHrsWages_2020.loc[
#     (df_AvgHrsWages_2020['Characteristics'] == 'Indigenous identity employees') |
#     (df_AvgHrsWages_2020['Characteristics'] == 'Non-indigenous identity employees')
# ]
# print(df_AvgAnnHrk_ByIndigenous.head(20))
# grouped = df_AvgAnnHrk_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnHrk_ByIndigenous.index))

# %% [markdown]
# Filtered for "Average weekly hours worked" by following: "Age group", "Gender level", "Education level", "Immigration status", and "Aboriginal status".

# %%
# # Whole Dataset inside "Average weekly hours worked"

# print("\nAge group in Alberta")
# df_AvgWeekHrsWrked_ByAge = df_AvgWeekHrsWrked.loc[
#     (df_AvgWeekHrsWrked['Characteristics'] == '15 to 24 years') |
#     (df_AvgWeekHrsWrked['Characteristics'] == '25 to 34 years') |
#     (df_AvgWeekHrsWrked['Characteristics'] == '35 to 44 years') |
#     (df_AvgWeekHrsWrked['Characteristics'] == '45 to 54 years') |
#     (df_AvgWeekHrsWrked['Characteristics'] == '55 to 64 years') |
#     (df_AvgWeekHrsWrked['Characteristics'] == '65 years old and over')]
# print(df_AvgWeekHrsWrked_ByAge.head(20))
# grouped = df_AvgWeekHrsWrked_ByAge.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgWeekHrsWrked_ByAge.index))

# print("\nGender group in Alberta")
# df_AvgWeekHrsWrked_ByGender = df_AvgWeekHrsWrked.loc[
#     (df_AvgWeekHrsWrked['Characteristics'] == 'Female employees') |
#     (df_AvgWeekHrsWrked['Characteristics'] == 'Male employees')
# ]
# print(df_AvgWeekHrsWrked_ByGender.head(20))
# grouped = df_AvgWeekHrsWrked_ByGender.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgWeekHrsWrked_ByGender.index))

# print("\nEducation group in Alberta")
# df_AvgWeekHrsWrked_ByEducation = df_AvgWeekHrsWrked.loc[
#     (df_AvgWeekHrsWrked['Characteristics'] == 'High school diploma and less') |
#     (df_AvgWeekHrsWrked['Characteristics'] == 'Trade certificate') |
#     (df_AvgWeekHrsWrked['Characteristics'] == 'University degree and higher')
# ]
# print(df_AvgWeekHrsWrked_ByEducation.head(20))
# grouped = df_AvgWeekHrsWrked_ByEducation.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgWeekHrsWrked_ByEducation.index))

# print("\nImmigrant group in Alberta")
# df_AvgWeekHrsWrked_ByImmigrant = df_AvgWeekHrsWrked.loc[
#     (df_AvgWeekHrsWrked['Characteristics'] == 'Immigrant employees') |
#     (df_AvgWeekHrsWrked['Characteristics'] == 'Non-immigrant employees')
# ]
# print(df_AvgWeekHrsWrked_ByImmigrant.head(20))
# grouped = df_AvgWeekHrsWrked_ByImmigrant.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgWeekHrsWrked_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgAnnHrk_ByIndigenous = df_AvgWeekHrsWrked.loc[
#     (df_AvgWeekHrsWrked['Characteristics'] == 'Indigenous identity employees') |
#     (df_AvgWeekHrsWrked['Characteristics'] == 'Non-indigenous identity employees')
# ]
# print(df_AvgAnnHrk_ByIndigenous.head(20))
# grouped = df_AvgAnnHrk_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnHrk_ByIndigenous.index))

# %%
# # Dataset year below year 2016 inside "Average weekly hours worked"

# print("\nAge group in Alberta")
# df_AvgWeekHrsWrked_below_2016_ByAge = df_AvgWeekHrsWrked_below_2016.loc[
#     (df_AvgWeekHrsWrked_below_2016['Characteristics'] == '15 to 24 years') |
#     (df_AvgWeekHrsWrked_below_2016['Characteristics'] == '25 to 34 years') |
#     (df_AvgWeekHrsWrked_below_2016['Characteristics'] == '35 to 44 years') |
#     (df_AvgWeekHrsWrked_below_2016['Characteristics'] == '45 to 54 years') |
#     (df_AvgWeekHrsWrked_below_2016['Characteristics'] == '55 to 64 years') |
#     (df_AvgWeekHrsWrked_below_2016['Characteristics'] == '65 years old and over')]
# print(df_AvgWeekHrsWrked_below_2016_ByAge.head(20))
# grouped = df_AvgWeekHrsWrked_below_2016_ByAge.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgWeekHrsWrked_below_2016_ByAge.index))

# print("\nGender group in Alberta")
# df_AvgWeekHrsWrked_below_2016_ByGender = df_AvgWeekHrsWrked_below_2016.loc[
#     (df_AvgWeekHrsWrked_below_2016['Characteristics'] == 'Female employees') |
#     (df_AvgWeekHrsWrked_below_2016['Characteristics'] == 'Male employees')
# ]
# print(df_AvgWeekHrsWrked_below_2016_ByGender.head(20))
# grouped = df_AvgWeekHrsWrked_below_2016_ByGender.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgWeekHrsWrked_below_2016_ByGender.index))

# print("\nEducation group in Alberta")
# df_AvgWeekHrsWrked_below_2016_ByEducation = df_AvgWeekHrsWrked_below_2016.loc[
#     (df_AvgWeekHrsWrked_below_2016['Characteristics'] == 'High school diploma and less') |
#     (df_AvgWeekHrsWrked_below_2016['Characteristics'] == 'Trade certificate') |
#     (df_AvgWeekHrsWrked_below_2016['Characteristics'] == 'University degree and higher')
# ]
# print(df_AvgWeekHrsWrked_below_2016_ByEducation.head(20))
# grouped = df_AvgWeekHrsWrked_below_2016_ByEducation.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgWeekHrsWrked_below_2016_ByEducation.index))

# print("\nImmigrant group in Alberta")
# df_AvgWeekHrsWrked_below_2016_ByImmigrant = df_AvgWeekHrsWrked_below_2016.loc[
#     (df_AvgWeekHrsWrked_below_2016['Characteristics'] == 'Immigrant employees') |
#     (df_AvgWeekHrsWrked_below_2016['Characteristics'] == 'Non-immigrant employees')
# ]
# print(df_AvgWeekHrsWrked_below_2016_ByImmigrant.head(20))
# grouped = df_AvgWeekHrsWrked_below_2016_ByImmigrant.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgWeekHrsWrked_below_2016_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgAnnHrk_ByIndigenous = df_AvgWeekHrsWrked_below_2016.loc[
#     (df_AvgWeekHrsWrked_below_2016['Characteristics'] == 'Indigenous identity employees') |
#     (df_AvgWeekHrsWrked_below_2016['Characteristics'] == 'Non-indigenous identity employees')
# ]
# print(df_AvgAnnHrk_ByIndigenous.head(20))
# grouped = df_AvgAnnHrk_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnHrk_ByIndigenous.index))

# %%
# Dataset year above year of 2017 inside "Average weekly hours worked"

print("\nAge group in Alberta")
df_AvgWeekHrsWrked_above_2016_ByAge = df_AvgWeekHrsWrked_above_2016.loc[
    (df_AvgWeekHrsWrked_above_2016['Characteristics'] == '15 to 24 years') |
    (df_AvgWeekHrsWrked_above_2016['Characteristics'] == '25 to 34 years') |
    (df_AvgWeekHrsWrked_above_2016['Characteristics'] == '35 to 44 years') |
    (df_AvgWeekHrsWrked_above_2016['Characteristics'] == '45 to 54 years') |
    (df_AvgWeekHrsWrked_above_2016['Characteristics'] == '55 to 64 years') |
    (df_AvgWeekHrsWrked_above_2016['Characteristics'] == '65 years old and over')]
print(df_AvgWeekHrsWrked_above_2016_ByAge.head(20))
grouped = df_AvgWeekHrsWrked_above_2016_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgWeekHrsWrked_above_2016_ByAge.index))

print("\nGender group in Alberta")
df_AvgWeekHrsWrked_above_2016_ByGender = df_AvgWeekHrsWrked_above_2016.loc[
    (df_AvgWeekHrsWrked_above_2016['Characteristics'] == 'Female employees') |
    (df_AvgWeekHrsWrked_above_2016['Characteristics'] == 'Male employees')
]
print(df_AvgWeekHrsWrked_above_2016_ByGender.head(20))
grouped = df_AvgWeekHrsWrked_above_2016_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgWeekHrsWrked_above_2016_ByGender.index))

print("\nEducation group in Alberta")
df_AvgWeekHrsWrked_above_2016_ByEducation = df_AvgWeekHrsWrked_above_2016.loc[
    (df_AvgWeekHrsWrked_above_2016['Characteristics'] == 'High school diploma and less') |
    (df_AvgWeekHrsWrked_above_2016['Characteristics'] == 'Trade certificate') |
    (df_AvgWeekHrsWrked_above_2016['Characteristics'] == 'University degree and higher')
]
print(df_AvgWeekHrsWrked_above_2016_ByEducation.head(20))
grouped = df_AvgWeekHrsWrked_above_2016_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgWeekHrsWrked_above_2016_ByEducation.index))

print("\nImmigrant group in Alberta")
df_AvgWeekHrsWrked_above_2016_ByImmigrant = df_AvgWeekHrsWrked_above_2016.loc[
    (df_AvgWeekHrsWrked_above_2016['Characteristics'] == 'Immigrant employees') |
    (df_AvgWeekHrsWrked_above_2016['Characteristics'] == 'Non-immigrant employees')
]
print(df_AvgWeekHrsWrked_above_2016_ByImmigrant.head(20))
grouped = df_AvgWeekHrsWrked_above_2016_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgWeekHrsWrked_above_2016_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgWeekHrsWrked_above_2016_ByIndigenous = df_AvgWeekHrsWrked_above_2016.loc[
#     (df_AvgWeekHrsWrked_above_2016['Characteristics'] == 'Indigenous identity employees') |
#     (df_AvgWeekHrsWrked_above_2016['Characteristics'] == 'Non-indigenous identity employees')
# ]
# print(df_AvgWeekHrsWrked_above_2016_ByIndigenous.head(20))
# grouped = df_AvgWeekHrsWrked_above_2016_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgWeekHrsWrked_above_2016_ByIndigenous.index))

# %%
# Dataset year in 2017 inside "Average weekly hours worked"

print("\nAge group in Alberta")
df_AvgWeekHrsWrked_2016_ByAge = df_AvgWeekHrsWrked_2016.loc[
    (df_AvgWeekHrsWrked_2016['Characteristics'] == '15 to 24 years') |
    (df_AvgWeekHrsWrked_2016['Characteristics'] == '25 to 34 years') |
    (df_AvgWeekHrsWrked_2016['Characteristics'] == '35 to 44 years') |
    (df_AvgWeekHrsWrked_2016['Characteristics'] == '45 to 54 years') |
    (df_AvgWeekHrsWrked_2016['Characteristics'] == '55 to 64 years') |
    (df_AvgWeekHrsWrked_2016['Characteristics'] == '65 years old and over')]
print(df_AvgWeekHrsWrked_2016_ByAge.head(20))
grouped = df_AvgWeekHrsWrked_2016_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgWeekHrsWrked_2016_ByAge.index))

print("\nGender group in Alberta")
df_AvgWeekHrsWrked_2016_ByGender = df_AvgWeekHrsWrked_2016.loc[
    (df_AvgWeekHrsWrked_2016['Characteristics'] == 'Female employees') |
    (df_AvgWeekHrsWrked_2016['Characteristics'] == 'Male employees')
]
print(df_AvgWeekHrsWrked_2016_ByGender.head(20))
grouped = df_AvgWeekHrsWrked_2016_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgWeekHrsWrked_2016_ByGender.index))

print("\nEducation group in Alberta")
df_AvgWeekHrsWrked_2016_ByEducation = df_AvgWeekHrsWrked_2016.loc[
    (df_AvgWeekHrsWrked_2016['Characteristics'] == 'High school diploma and less') |
    (df_AvgWeekHrsWrked_2016['Characteristics'] == 'Trade certificate') |
    (df_AvgWeekHrsWrked_2016['Characteristics'] == 'University degree and higher')
]
print(df_AvgWeekHrsWrked_2016_ByEducation.head(20))
grouped = df_AvgWeekHrsWrked_2016_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgWeekHrsWrked_2016_ByEducation.index))

print("\nImmigrant group in Alberta")
df_AvgWeekHrsWrked_2016_ByImmigrant = df_AvgWeekHrsWrked_2016.loc[
    (df_AvgWeekHrsWrked_2016['Characteristics'] == 'Immigrant employees') |
    (df_AvgWeekHrsWrked_2016['Characteristics'] == 'Non-immigrant employees')
]
print(df_AvgWeekHrsWrked_2016_ByImmigrant.head(20))
grouped = df_AvgWeekHrsWrked_2016_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgWeekHrsWrked_2016_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgAnnHrk_ByIndigenous = df_AvgWeekHrsWrked_2016.loc[
#     (df_AvgWeekHrsWrked_2016['Characteristics'] == 'Indigenous identity employees') |
#     (df_AvgWeekHrsWrked_2016['Characteristics'] == 'Non-indigenous identity employees')
# ]
# print(df_AvgAnnHrk_ByIndigenous.head(20))
# grouped = df_AvgAnnHrk_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnHrk_ByIndigenous.index))

# %%
# Dataset year in 2019 inside "Average weekly hours worked"

print("\nAge group in Alberta")
df_AvgWeekHrsWrked_2018_ByAge = df_AvgWeekHrsWrked_2018.loc[
    (df_AvgWeekHrsWrked_2018['Characteristics'] == '15 to 24 years') |
    (df_AvgWeekHrsWrked_2018['Characteristics'] == '25 to 34 years') |
    (df_AvgWeekHrsWrked_2018['Characteristics'] == '35 to 44 years') |
    (df_AvgWeekHrsWrked_2018['Characteristics'] == '45 to 54 years') |
    (df_AvgWeekHrsWrked_2018['Characteristics'] == '55 to 64 years') |
    (df_AvgWeekHrsWrked_2018['Characteristics'] == '65 years old and over')]
print(df_AvgWeekHrsWrked_2018_ByAge.head(20))
grouped = df_AvgWeekHrsWrked_2018_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgWeekHrsWrked_2018_ByAge.index))

print("\nGender group in Alberta")
df_AvgWeekHrsWrked_2018_ByGender = df_AvgWeekHrsWrked_2018.loc[
    (df_AvgWeekHrsWrked_2018['Characteristics'] == 'Female employees') |
    (df_AvgWeekHrsWrked_2018['Characteristics'] == 'Male employees')
]
print(df_AvgWeekHrsWrked_2018_ByGender.head(20))
grouped = df_AvgWeekHrsWrked_2018_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgWeekHrsWrked_2018_ByGender.index))

print("\nEducation group in Alberta")
df_AvgWeekHrsWrked_2018_ByEducation = df_AvgWeekHrsWrked_2018.loc[
    (df_AvgWeekHrsWrked_2018['Characteristics'] == 'High school diploma and less') |
    (df_AvgWeekHrsWrked_2018['Characteristics'] == 'Trade certificate') |
    (df_AvgWeekHrsWrked_2018['Characteristics'] == 'University degree and higher')
]
print(df_AvgWeekHrsWrked_2018_ByEducation.head(20))
grouped = df_AvgWeekHrsWrked_2018_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgWeekHrsWrked_2018_ByEducation.index))

print("\nImmigrant group in Alberta")
df_AvgWeekHrsWrked_2018_ByImmigrant = df_AvgWeekHrsWrked_2018.loc[
    (df_AvgWeekHrsWrked_2018['Characteristics'] == 'Immigrant employees') |
    (df_AvgWeekHrsWrked_2018['Characteristics'] == 'Non-immigrant employees')
]
print(df_AvgWeekHrsWrked_2018_ByImmigrant.head(20))
grouped = df_AvgWeekHrsWrked_2018_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgWeekHrsWrked_2018_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgAnnHrk_ByIndigenous = df_AvgWeekHrsWrked_2018.loc[
#     (df_AvgWeekHrsWrked_2018['Characteristics'] == 'Indigenous identity employees') |
#     (df_AvgWeekHrsWrked_2018['Characteristics'] == 'Non-indigenous identity employees')
# ]
# print(df_AvgAnnHrk_ByIndigenous.head(20))
# grouped = df_AvgAnnHrk_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnHrk_ByIndigenous.index))

# %%
# Dataset year in 2021 inside "Average weekly hours worked"

print("\nAge group in Alberta")
df_AvgWeekHrsWrked_2020_ByAge = df_AvgWeekHrsWrked_2020.loc[
    (df_AvgWeekHrsWrked_2020['Characteristics'] == '15 to 24 years') |
    (df_AvgWeekHrsWrked_2020['Characteristics'] == '25 to 34 years') |
    (df_AvgWeekHrsWrked_2020['Characteristics'] == '35 to 44 years') |
    (df_AvgWeekHrsWrked_2020['Characteristics'] == '45 to 54 years') |
    (df_AvgWeekHrsWrked_2020['Characteristics'] == '55 to 64 years') |
    (df_AvgWeekHrsWrked_2020['Characteristics'] == '65 years old and over')]
print(df_AvgWeekHrsWrked_2020_ByAge.head(20))
grouped = df_AvgWeekHrsWrked_2020_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgWeekHrsWrked_2020_ByAge.index))

print("\nGender group in Alberta")
df_AvgWeekHrsWrked_2020_ByGender = df_AvgWeekHrsWrked_2020.loc[
    (df_AvgWeekHrsWrked_2020['Characteristics'] == 'Female employees') |
    (df_AvgWeekHrsWrked_2020['Characteristics'] == 'Male employees')
]
print(df_AvgWeekHrsWrked_2020_ByGender.head(20))
grouped = df_AvgWeekHrsWrked_2020_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgWeekHrsWrked_2020_ByGender.index))

print("\nEducation group in Alberta")
df_AvgWeekHrsWrked_2020_ByEducation = df_AvgWeekHrsWrked_2020.loc[
    (df_AvgWeekHrsWrked_2020['Characteristics'] == 'High school diploma and less') |
    (df_AvgWeekHrsWrked_2020['Characteristics'] == 'Trade certificate') |
    (df_AvgWeekHrsWrked_2020['Characteristics'] == 'University degree and higher')
]
print(df_AvgWeekHrsWrked_2020_ByEducation.head(20))
grouped = df_AvgWeekHrsWrked_2020_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgWeekHrsWrked_2020_ByEducation.index))

print("\nImmigrant group in Alberta")
df_AvgWeekHrsWrked_2020_ByImmigrant = df_AvgWeekHrsWrked_2020.loc[
    (df_AvgWeekHrsWrked_2020['Characteristics'] == 'Immigrant employees') |
    (df_AvgWeekHrsWrked_2020['Characteristics'] == 'Non-immigrant employees')
]
print(df_AvgWeekHrsWrked_2020_ByImmigrant.head(20))
grouped = df_AvgWeekHrsWrked_2020_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgWeekHrsWrked_2020_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgAnnHrk_ByIndigenous = df_AvgWeekHrsWrked_2020.loc[
#     (df_AvgWeekHrsWrked_2020['Characteristics'] == 'Indigenous identity employees') |
#     (df_AvgWeekHrsWrked_2020['Characteristics'] == 'Non-indigenous identity employees')
# ]
# print(df_AvgAnnHrk_ByIndigenous.head(20))
# grouped = df_AvgAnnHrk_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnHrk_ByIndigenous.index))

# %% [markdown]
# Filtered for "Hours worked" by following: "Age group", "Gender level", "Education level", "Immigration status", and "Aboriginal status".
# 

# %%
# # Whole Dataset inside "Hours Worked"
# print("\nAge group in Alberta")
# df_Hrs_Wrked_ByAge = df_Hrs_Wrked.loc[
#     (df_Hrs_Wrked['Characteristics'] == '15 to 24 years') |
#     (df_Hrs_Wrked['Characteristics'] == '25 to 34 years') |
#     (df_Hrs_Wrked['Characteristics'] == '35 to 44 years') |
#     (df_Hrs_Wrked['Characteristics'] == '45 to 54 years') |
#     (df_Hrs_Wrked['Characteristics'] == '55 to 64 years') |
#     (df_Hrs_Wrked['Characteristics'] == '65 years old and over')]
# print(df_Hrs_Wrked_ByAge.head(20))
# grouped = df_Hrs_Wrked_ByAge.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_Hrs_Wrked_ByAge.index))

# print("\nGender group in Alberta")
# df_Hrs_Wrked_ByGender = df_Hrs_Wrked.loc[
#     (df_Hrs_Wrked['Characteristics'] == 'Female employees') |
#     (df_Hrs_Wrked['Characteristics'] == 'Male employees')
# ]
# print(df_Hrs_Wrked_ByGender.head(20))
# grouped = df_Hrs_Wrked_ByGender.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_Hrs_Wrked_ByGender.index))

# print("\nEducation group in Alberta")
# df_Hrs_Wrked_ByEducation = df_Hrs_Wrked.loc[
#     (df_Hrs_Wrked['Characteristics'] == 'High school diploma and less') |
#     (df_Hrs_Wrked['Characteristics'] == 'Trade certificate') |
#     (df_Hrs_Wrked['Characteristics'] == 'University degree and higher')
# ]
# print(df_Hrs_Wrked_ByEducation.head(20))
# grouped = df_Hrs_Wrked_ByEducation.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_Hrs_Wrked_ByEducation.index))

# print("\nImmigrant group in Alberta")
# df_Hrs_Wrked_ByImmigrant = df_Hrs_Wrked.loc[
#     (df_Hrs_Wrked['Characteristics'] == 'Immigrant employees') |
#     (df_Hrs_Wrked['Characteristics'] == 'Non-immigrant employees')
# ]
# print(df_Hrs_Wrked_ByImmigrant.head(20))
# grouped = df_Hrs_Wrked_ByImmigrant.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_Hrs_Wrked_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgAnnHrk_ByIndigenous = df_Hrs_Wrked.loc[
#     (df_Hrs_Wrked['Characteristics'] == 'Indigenous identity employees') |
#     (df_Hrs_Wrked['Characteristics'] == 'Non-indigenous identity employees')
# ]
# print(df_AvgAnnHrk_ByIndigenous.head(20))
# grouped = df_AvgAnnHrk_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnHrk_ByIndigenous.index))

# %%
# # Dataset year below year 2016 inside "Hours Worked"
# print("\nAge group in Alberta")
# df_Hrs_Wrked_below_2016_ByAge = df_Hrs_Wrked_below_2016.loc[
#     (df_Hrs_Wrked_below_2016['Characteristics'] == '15 to 24 years') |
#     (df_Hrs_Wrked_below_2016['Characteristics'] == '25 to 34 years') |
#     (df_Hrs_Wrked_below_2016['Characteristics'] == '35 to 44 years') |
#     (df_Hrs_Wrked_below_2016['Characteristics'] == '45 to 54 years') |
#     (df_Hrs_Wrked_below_2016['Characteristics'] == '55 to 64 years') |
#     (df_Hrs_Wrked_below_2016['Characteristics'] == '65 years old and over')]
# print(df_Hrs_Wrked_below_2016_ByAge.head(20))
# grouped = df_Hrs_Wrked_below_2016_ByAge.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_Hrs_Wrked_below_2016_ByAge.index))

# print("\nGender group in Alberta")
# df_Hrs_Wrked_below_2016_ByGender = df_Hrs_Wrked_below_2016.loc[
#     (df_Hrs_Wrked_below_2016['Characteristics'] == 'Female employees') |
#     (df_Hrs_Wrked_below_2016['Characteristics'] == 'Male employees')
# ]
# print(df_Hrs_Wrked_below_2016_ByGender.head(20))
# grouped = df_Hrs_Wrked_below_2016_ByGender.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_Hrs_Wrked_below_2016_ByGender.index))

# print("\nEducation group in Alberta")
# df_Hrs_Wrked_below_2016_ByEducation = df_Hrs_Wrked_below_2016.loc[
#     (df_Hrs_Wrked_below_2016['Characteristics'] == 'High school diploma and less') |
#     (df_Hrs_Wrked_below_2016['Characteristics'] == 'Trade certificate') |
#     (df_Hrs_Wrked_below_2016['Characteristics'] == 'University degree and higher')
# ]
# print(df_Hrs_Wrked_below_2016_ByEducation.head(20))
# grouped = df_Hrs_Wrked_below_2016_ByEducation.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_Hrs_Wrked_below_2016_ByEducation.index))

# print("\nImmigrant group in Alberta")
# df_Hrs_Wrked_below_2016_ByImmigrant = df_Hrs_Wrked_below_2016.loc[
#     (df_Hrs_Wrked_below_2016['Characteristics'] == 'Immigrant employees') |
#     (df_Hrs_Wrked_below_2016['Characteristics'] == 'Non-immigrant employees')
# ]
# print(df_Hrs_Wrked_below_2016_ByImmigrant.head(20))
# grouped = df_Hrs_Wrked_below_2016_ByImmigrant.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_Hrs_Wrked_below_2016_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgAnnHrk_ByIndigenous = df_Hrs_Wrked_below_2016.loc[
#     (df_Hrs_Wrked_below_2016['Characteristics'] == 'Indigenous identity employees') |
#     (df_Hrs_Wrked_below_2016['Characteristics'] == 'Non-indigenous identity employees')
# ]
# print(df_AvgAnnHrk_ByIndigenous.head(20))
# grouped = df_AvgAnnHrk_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnHrk_ByIndigenous.index))

# %%
# Dataset year above year of 2017 inside "Hours Worked"

print("\nAge group in Alberta")
df_Hrs_Wrked_above_2016_ByAge = df_Hrs_Wrked_above_2016.loc[
    (df_Hrs_Wrked_above_2016['Characteristics'] == '15 to 24 years') |
    (df_Hrs_Wrked_above_2016['Characteristics'] == '25 to 34 years') |
    (df_Hrs_Wrked_above_2016['Characteristics'] == '35 to 44 years') |
    (df_Hrs_Wrked_above_2016['Characteristics'] == '45 to 54 years') |
    (df_Hrs_Wrked_above_2016['Characteristics'] == '55 to 64 years') |
    (df_Hrs_Wrked_above_2016['Characteristics'] == '65 years old and over')]
print(df_Hrs_Wrked_above_2016_ByAge.head(20))
grouped = df_Hrs_Wrked_above_2016_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_Hrs_Wrked_above_2016_ByAge.index))

print("\nGender group in Alberta")
df_Hrs_Wrked_above_2016_ByGender = df_Hrs_Wrked_above_2016.loc[
    (df_Hrs_Wrked_above_2016['Characteristics'] == 'Female employees') |
    (df_Hrs_Wrked_above_2016['Characteristics'] == 'Male employees')
]
print(df_Hrs_Wrked_above_2016_ByGender.head(20))
grouped = df_Hrs_Wrked_above_2016_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_Hrs_Wrked_above_2016_ByGender.index))

print("\nEducation group in Alberta")
df_Hrs_Wrked_above_2016_ByEducation = df_Hrs_Wrked_above_2016.loc[
    (df_Hrs_Wrked_above_2016['Characteristics'] == 'High school diploma and less') |
    (df_Hrs_Wrked_above_2016['Characteristics'] == 'Trade certificate') |
    (df_Hrs_Wrked_above_2016['Characteristics'] == 'University degree and higher')
]
print(df_Hrs_Wrked_above_2016_ByEducation.head(20))
grouped = df_Hrs_Wrked_above_2016_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_Hrs_Wrked_above_2016_ByEducation.index))

print("\nImmigrant group in Alberta")
df_Hrs_Wrked_above_2016_ByImmigrant = df_Hrs_Wrked_above_2016.loc[
    (df_Hrs_Wrked_above_2016['Characteristics'] == 'Immigrant employees') |
    (df_Hrs_Wrked_above_2016['Characteristics'] == 'Non-immigrant employees')
]
print(df_Hrs_Wrked_above_2016_ByImmigrant.head(20))
grouped = df_Hrs_Wrked_above_2016_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_Hrs_Wrked_above_2016_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_Hrs_Wrked_above_2016_ByIndigenous = df_Hrs_Wrked_above_2016.loc[
#     (df_Hrs_Wrked_above_2016['Characteristics'] == 'Indigenous identity employees') |
#     (df_Hrs_Wrked_above_2016['Characteristics'] == 'Non-indigenous identity employees')
# ]
# print(df_Hrs_Wrked_above_2016_ByIndigenous.head(20))
# grouped = df_Hrs_Wrked_above_2016_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_Hrs_Wrked_above_2016_ByIndigenous.index))

# %%
# Dataset year in 2017 inside "Hours Worked"

print("\nAge group in Alberta")
df_Hrs_Wrked_2016_ByAge = df_Hrs_Wrked_2016.loc[
    (df_Hrs_Wrked_2016['Characteristics'] == '15 to 24 years') |
    (df_Hrs_Wrked_2016['Characteristics'] == '25 to 34 years') |
    (df_Hrs_Wrked_2016['Characteristics'] == '35 to 44 years') |
    (df_Hrs_Wrked_2016['Characteristics'] == '45 to 54 years') |
    (df_Hrs_Wrked_2016['Characteristics'] == '55 to 64 years') |
    (df_Hrs_Wrked_2016['Characteristics'] == '65 years old and over')]
print(df_Hrs_Wrked_2016_ByAge.head(20))
grouped = df_Hrs_Wrked_2016_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_Hrs_Wrked_2016_ByAge.index))

print("\nGender group in Alberta")
df_Hrs_Wrked_2016_ByGender = df_Hrs_Wrked_2016.loc[
    (df_Hrs_Wrked_2016['Characteristics'] == 'Female employees') |
    (df_Hrs_Wrked_2016['Characteristics'] == 'Male employees')
]
print(df_Hrs_Wrked_2016_ByGender.head(20))
grouped = df_Hrs_Wrked_2016_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_Hrs_Wrked_2016_ByGender.index))

print("\nEducation group in Alberta")
df_Hrs_Wrked_2016_ByEducation = df_Hrs_Wrked_2016.loc[
    (df_Hrs_Wrked_2016['Characteristics'] == 'High school diploma and less') |
    (df_Hrs_Wrked_2016['Characteristics'] == 'Trade certificate') |
    (df_Hrs_Wrked_2016['Characteristics'] == 'University degree and higher')
]
print(df_Hrs_Wrked_2016_ByEducation.head(20))
grouped = df_Hrs_Wrked_2016_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_Hrs_Wrked_2016_ByEducation.index))

print("\nImmigrant group in Alberta")
df_Hrs_Wrked_2016_ByImmigrant = df_Hrs_Wrked_2016.loc[
    (df_Hrs_Wrked_2016['Characteristics'] == 'Immigrant employees') |
    (df_Hrs_Wrked_2016['Characteristics'] == 'Non-immigrant employees')
]
print(df_Hrs_Wrked_2016_ByImmigrant.head(20))
grouped = df_Hrs_Wrked_2016_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_Hrs_Wrked_2016_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgAnnHrk_ByIndigenous = df_Hrs_Wrked_2016.loc[
#     (df_Hrs_Wrked_2016['Characteristics'] == 'Indigenous identity employees') |
#     (df_Hrs_Wrked_2016['Characteristics'] == 'Non-indigenous identity employees')
# ]
# print(df_AvgAnnHrk_ByIndigenous.head(20))
# grouped = df_AvgAnnHrk_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnHrk_ByIndigenous.index))

# %%
# Dataset year in 2019 inside "Hour Worked"

print("\nAge group in Alberta")
df_Hrs_Wrked_2018_ByAge = df_Hrs_Wrked_2018.loc[
    (df_Hrs_Wrked_2018['Characteristics'] == '15 to 24 years') |
    (df_Hrs_Wrked_2018['Characteristics'] == '25 to 34 years') |
    (df_Hrs_Wrked_2018['Characteristics'] == '35 to 44 years') |
    (df_Hrs_Wrked_2018['Characteristics'] == '45 to 54 years') |
    (df_Hrs_Wrked_2018['Characteristics'] == '55 to 64 years') |
    (df_Hrs_Wrked_2018['Characteristics'] == '65 years old and over')]
print(df_Hrs_Wrked_2018_ByAge.head(20))
grouped = df_Hrs_Wrked_2018_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_Hrs_Wrked_2018_ByAge.index))

print("\nGender group in Alberta")
df_Hrs_Wrked_2018_ByGender = df_Hrs_Wrked_2018.loc[
    (df_Hrs_Wrked_2018['Characteristics'] == 'Female employees') |
    (df_Hrs_Wrked_2018['Characteristics'] == 'Male employees')
]
print(df_Hrs_Wrked_2018_ByGender.head(20))
grouped = df_Hrs_Wrked_2018_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_Hrs_Wrked_2018_ByGender.index))

print("\nEducation group in Alberta")
df_Hrs_Wrked_2018_ByEducation = df_Hrs_Wrked_2018.loc[
    (df_Hrs_Wrked_2018['Characteristics'] == 'High school diploma and less') |
    (df_Hrs_Wrked_2018['Characteristics'] == 'Trade certificate') |
    (df_Hrs_Wrked_2018['Characteristics'] == 'University degree and higher')
]
print(df_Hrs_Wrked_2018_ByEducation.head(20))
grouped = df_Hrs_Wrked_2018_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_Hrs_Wrked_2018_ByEducation.index))

print("\nImmigrant group in Alberta")
df_Hrs_Wrked_2018_ByImmigrant = df_Hrs_Wrked_2018.loc[
    (df_Hrs_Wrked_2018['Characteristics'] == 'Immigrant employees') |
    (df_Hrs_Wrked_2018['Characteristics'] == 'Non-immigrant employees')
]
print(df_Hrs_Wrked_2018_ByImmigrant.head(20))
grouped = df_Hrs_Wrked_2018_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_Hrs_Wrked_2018_ByImmigrant.index))

print("\nIndigenous group in Alberta")
df_AvgAnnHrk_ByIndigenous = df_Hrs_Wrked_2018.loc[
    (df_Hrs_Wrked_2018['Characteristics'] == 'Indigenous identity employees') |
    (df_Hrs_Wrked_2018['Characteristics'] == 'Non-indigenous identity employees')
]
print(df_AvgAnnHrk_ByIndigenous.head(20))
grouped = df_AvgAnnHrk_ByIndigenous.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgAnnHrk_ByIndigenous.index))


# %%
# Dataset year in 2021 inside "Hour Worked"

print("\nAge group in Alberta")
df_Hrs_Wrked_2020_ByAge = df_Hrs_Wrked_2020.loc[
    (df_Hrs_Wrked_2020['Characteristics'] == '15 to 24 years') |
    (df_Hrs_Wrked_2020['Characteristics'] == '25 to 34 years') |
    (df_Hrs_Wrked_2020['Characteristics'] == '35 to 44 years') |
    (df_Hrs_Wrked_2020['Characteristics'] == '45 to 54 years') |
    (df_Hrs_Wrked_2020['Characteristics'] == '55 to 64 years') |
    (df_Hrs_Wrked_2020['Characteristics'] == '65 years old and over')]
print(df_Hrs_Wrked_2020_ByAge.head(20))
grouped = df_Hrs_Wrked_2020_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_Hrs_Wrked_2020_ByAge.index))

print("\nGender group in Alberta")
df_Hrs_Wrked_2020_ByGender = df_Hrs_Wrked_2020.loc[
    (df_Hrs_Wrked_2020['Characteristics'] == 'Female employees') |
    (df_Hrs_Wrked_2020['Characteristics'] == 'Male employees')
]
print(df_Hrs_Wrked_2020_ByGender.head(20))
grouped = df_Hrs_Wrked_2020_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_Hrs_Wrked_2020_ByGender.index))

print("\nEducation group in Alberta")
df_Hrs_Wrked_2020_ByEducation = df_Hrs_Wrked_2020.loc[
    (df_Hrs_Wrked_2020['Characteristics'] == 'High school diploma and less') |
    (df_Hrs_Wrked_2020['Characteristics'] == 'Trade certificate') |
    (df_Hrs_Wrked_2020['Characteristics'] == 'University degree and higher')
]
print(df_Hrs_Wrked_2020_ByEducation.head(20))
grouped = df_Hrs_Wrked_2020_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_Hrs_Wrked_2020_ByEducation.index))

print("\nImmigrant group in Alberta")
df_Hrs_Wrked_2020_ByImmigrant = df_Hrs_Wrked_2020.loc[
    (df_Hrs_Wrked_2020['Characteristics'] == 'Immigrant employees') |
    (df_Hrs_Wrked_2020['Characteristics'] == 'Non-immigrant employees')
]
print(df_Hrs_Wrked_2020_ByImmigrant.head(20))
grouped = df_Hrs_Wrked_2020_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_Hrs_Wrked_2020_ByImmigrant.index))

print("\nIndigenous group in Alberta")
df_AvgAnnHrk_ByIndigenous = df_Hrs_Wrked_2020.loc[
    (df_Hrs_Wrked_2020['Characteristics'] == 'Indigenous identity employees') |
    (df_Hrs_Wrked_2020['Characteristics'] == 'Non-indigenous identity employees')
]
print(df_AvgAnnHrk_ByIndigenous.head(20))
grouped = df_AvgAnnHrk_ByIndigenous.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_AvgAnnHrk_ByIndigenous.index))

# %% [markdown]
# Filtered for "Number of jobs" by following: "Age group", "Gender level", "Education level", "Immigration status", and "Aboriginal status".

# %%
# # Whole Dataset inside "Number of jobs"

# print("\nAge group in Alberta")
# df_NumOfJob_ByAge = df_NumOfJob.loc[
#     (df_NumOfJob['Characteristics'] == '15 to 24 years') |
#     (df_NumOfJob['Characteristics'] == '25 to 34 years') |
#     (df_NumOfJob['Characteristics'] == '35 to 44 years') |
#     (df_NumOfJob['Characteristics'] == '45 to 54 years') |
#     (df_NumOfJob['Characteristics'] == '55 to 64 years') |
#     (df_NumOfJob['Characteristics'] == '65 years old and over')]
# print(df_NumOfJob_ByAge.head(20))
# grouped = df_NumOfJob_ByAge.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_NumOfJob_ByAge.index))

# print("\nGender group in Alberta")
# df_NumOfJob_ByGender = df_NumOfJob.loc[
#     (df_NumOfJob['Characteristics'] == 'Female employees') |
#     (df_NumOfJob['Characteristics'] == 'Male employees')
# ]
# print(df_NumOfJob_ByGender.head(20))
# grouped = df_NumOfJob_ByGender.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_NumOfJob_ByGender.index))

# print("\nEducation group in Alberta")
# df_NumOfJob_ByEducation = df_NumOfJob.loc[
#     (df_NumOfJob['Characteristics'] == 'High school diploma and less') |
#     (df_NumOfJob['Characteristics'] == 'Trade certificate') |
#     (df_NumOfJob['Characteristics'] == 'University degree and higher')
# ]
# print(df_NumOfJob_ByEducation.head(20))
# grouped = df_NumOfJob_ByEducation.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_NumOfJob_ByEducation.index))

# print("\nImmigrant group in Alberta")
# df_NumOfJob_ByImmigrant = df_NumOfJob.loc[
#     (df_NumOfJob['Characteristics'] == 'Immigrant employees') |
#     (df_NumOfJob['Characteristics'] == 'Non-immigrant employees')
# ]
# print(df_NumOfJob_ByImmigrant.head(20))
# grouped = df_NumOfJob_ByImmigrant.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_NumOfJob_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgAnnHrk_ByIndigenous = df_NumOfJob.loc[
#     (df_NumOfJob['Characteristics'] == 'Indigenous identity employees') |
#     (df_NumOfJob['Characteristics'] == 'Non-indigenous identity employees')
# ]
# print(df_AvgAnnHrk_ByIndigenous.head(20))
# grouped = df_AvgAnnHrk_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnHrk_ByIndigenous.index))

# %%
# # Dataset year below year 2016 inside "Number of jobs"

# print("\nAge group in Alberta")
# df_NumOfJob_below_2016_ByAge = df_NumOfJob_below_2016.loc[
#     (df_NumOfJob_below_2016['Characteristics'] == '15 to 24 years') |
#     (df_NumOfJob_below_2016['Characteristics'] == '25 to 34 years') |
#     (df_NumOfJob_below_2016['Characteristics'] == '35 to 44 years') |
#     (df_NumOfJob_below_2016['Characteristics'] == '45 to 54 years') |
#     (df_NumOfJob_below_2016['Characteristics'] == '55 to 64 years') |
#     (df_NumOfJob_below_2016['Characteristics'] == '65 years old and over')]
# print(df_NumOfJob_below_2016_ByAge.head(20))
# grouped = df_NumOfJob_below_2016_ByAge.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_NumOfJob_below_2016_ByAge.index))

# print("\nGender group in Alberta")
# df_NumOfJob_below_2016_ByGender = df_NumOfJob_below_2016.loc[
#     (df_NumOfJob_below_2016['Characteristics'] == 'Female employees') |
#     (df_NumOfJob_below_2016['Characteristics'] == 'Male employees')
# ]
# print(df_NumOfJob_below_2016_ByGender.head(20))
# grouped = df_NumOfJob_below_2016_ByGender.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_NumOfJob_below_2016_ByGender.index))

# print("\nEducation group in Alberta")
# df_NumOfJob_below_2016_ByEducation = df_NumOfJob_below_2016.loc[
#     (df_NumOfJob_below_2016['Characteristics'] == 'High school diploma and less') |
#     (df_NumOfJob_below_2016['Characteristics'] == 'Trade certificate') |
#     (df_NumOfJob_below_2016['Characteristics'] == 'University degree and higher')
# ]
# print(df_NumOfJob_below_2016_ByEducation.head(20))
# grouped = df_NumOfJob_below_2016_ByEducation.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_NumOfJob_below_2016_ByEducation.index))

# print("\nImmigrant group in Alberta")
# df_NumOfJob_below_2016_ByImmigrant = df_NumOfJob_below_2016.loc[
#     (df_NumOfJob_below_2016['Characteristics'] == 'Immigrant employees') |
#     (df_NumOfJob_below_2016['Characteristics'] == 'Non-immigrant employees')
# ]
# print(df_NumOfJob_below_2016_ByImmigrant.head(20))
# grouped = df_NumOfJob_below_2016_ByImmigrant.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_NumOfJob_below_2016_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgAnnHrk_ByIndigenous = df_NumOfJob_below_2016.loc[
#     (df_NumOfJob_below_2016['Characteristics'] == 'Indigenous identity employees') |
#     (df_NumOfJob_below_2016['Characteristics'] == 'Non-indigenous identity employees')
# ]
# print(df_AvgAnnHrk_ByIndigenous.head(20))
# grouped = df_AvgAnnHrk_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnHrk_ByIndigenous.index))

# %%
# Dataset year above year of 2017 inside "Number of jobs"

print("\nAge group in Alberta")
df_NumOfJob_above_2016_ByAge = df_NumOfJob_above_2016.loc[
    (df_NumOfJob_above_2016['Characteristics'] == '15 to 24 years') |
    (df_NumOfJob_above_2016['Characteristics'] == '25 to 34 years') |
    (df_NumOfJob_above_2016['Characteristics'] == '35 to 44 years') |
    (df_NumOfJob_above_2016['Characteristics'] == '45 to 54 years') |
    (df_NumOfJob_above_2016['Characteristics'] == '55 to 64 years') |
    (df_NumOfJob_above_2016['Characteristics'] == '65 years old and over')]
print(df_NumOfJob_above_2016_ByAge.head(20))
grouped = df_NumOfJob_above_2016_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_NumOfJob_above_2016_ByAge.index))

print("\nGender group in Alberta")
df_NumOfJob_above_2016_ByGender = df_NumOfJob_above_2016.loc[
    (df_NumOfJob_above_2016['Characteristics'] == 'Female employees') |
    (df_NumOfJob_above_2016['Characteristics'] == 'Male employees')
]
print(df_NumOfJob_above_2016_ByGender.head(20))
grouped = df_NumOfJob_above_2016_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_NumOfJob_above_2016_ByGender.index))

print("\nEducation group in Alberta")
df_NumOfJob_above_2016_ByEducation = df_NumOfJob_above_2016.loc[
    (df_NumOfJob_above_2016['Characteristics'] == 'High school diploma and less') |
    (df_NumOfJob_above_2016['Characteristics'] == 'Trade certificate') |
    (df_NumOfJob_above_2016['Characteristics'] == 'University degree and higher')
]
print(df_NumOfJob_above_2016_ByEducation.head(20))
grouped = df_NumOfJob_above_2016_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_NumOfJob_above_2016_ByEducation.index))

print("\nImmigrant group in Alberta")
df_NumOfJob_above_2016_ByImmigrant = df_NumOfJob_above_2016.loc[
    (df_NumOfJob_above_2016['Characteristics'] == 'Immigrant employees') |
    (df_NumOfJob_above_2016['Characteristics'] == 'Non-immigrant employees')
]
print(df_NumOfJob_above_2016_ByImmigrant.head(20))
grouped = df_NumOfJob_above_2016_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_NumOfJob_above_2016_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_NumOfJob_above_2016_ByIndigenous = df_NumOfJob_above_2016.loc[
#     (df_NumOfJob_above_2016['Characteristics'] == 'Indigenous identity employees') |
#     (df_NumOfJob_above_2016['Characteristics'] == 'Non-indigenous identity employees')
# ]
# print(df_NumOfJob_above_2016_ByIndigenous.head(20))
# grouped = df_NumOfJob_above_2016_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_NumOfJob_above_2016_ByIndigenous.index))

# %%
# Dataset year in 2017 inside "Number of jobs"

print("\nAge group in Alberta")
df_NumOfJob_2016_ByAge = df_NumOfJob_2016.loc[
    (df_NumOfJob_2016['Characteristics'] == '15 to 24 years') |
    (df_NumOfJob_2016['Characteristics'] == '25 to 34 years') |
    (df_NumOfJob_2016['Characteristics'] == '35 to 44 years') |
    (df_NumOfJob_2016['Characteristics'] == '45 to 54 years') |
    (df_NumOfJob_2016['Characteristics'] == '55 to 64 years') |
    (df_NumOfJob_2016['Characteristics'] == '65 years old and over')]
print(df_NumOfJob_2016_ByAge.head(20))
grouped = df_NumOfJob_2016_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_NumOfJob_2016_ByAge.index))

print("\nGender group in Alberta")
df_NumOfJob_2016_ByGender = df_NumOfJob_2016.loc[
    (df_NumOfJob_2016['Characteristics'] == 'Female employees') |
    (df_NumOfJob_2016['Characteristics'] == 'Male employees')
]
print(df_NumOfJob_2016_ByGender.head(20))
grouped = df_NumOfJob_2016_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_NumOfJob_2016_ByGender.index))

print("\nEducation group in Alberta")
df_NumOfJob_2016_ByEducation = df_NumOfJob_2016.loc[
    (df_NumOfJob_2016['Characteristics'] == 'High school diploma and less') |
    (df_NumOfJob_2016['Characteristics'] == 'Trade certificate') |
    (df_NumOfJob_2016['Characteristics'] == 'University degree and higher')
]
print(df_NumOfJob_2016_ByEducation.head(20))
grouped = df_NumOfJob_2016_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_NumOfJob_2016_ByEducation.index))

print("\nImmigrant group in Alberta")
df_NumOfJob_2016_ByImmigrant = df_NumOfJob_2016.loc[
    (df_NumOfJob_2016['Characteristics'] == 'Immigrant employees') |
    (df_NumOfJob_2016['Characteristics'] == 'Non-immigrant employees')
]
print(df_NumOfJob_2016_ByImmigrant.head(20))
grouped = df_NumOfJob_2016_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_NumOfJob_2016_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgAnnHrk_ByIndigenous = df_NumOfJob_2016.loc[
#     (df_NumOfJob_2016['Characteristics'] == 'Indigenous identity employees') |
#     (df_NumOfJob_2016['Characteristics'] == 'Non-indigenous identity employees')
# ]
# print(df_AvgAnnHrk_ByIndigenous.head(20))
# grouped = df_AvgAnnHrk_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnHrk_ByIndigenous.index))

# %%
# Dataset year in 2019 inside "Number of jobs"

print("\nAge group in Alberta")
df_NumOfJob_2018_ByAge = df_NumOfJob_2018.loc[
    (df_NumOfJob_2018['Characteristics'] == '15 to 24 years') |
    (df_NumOfJob_2018['Characteristics'] == '25 to 34 years') |
    (df_NumOfJob_2018['Characteristics'] == '35 to 44 years') |
    (df_NumOfJob_2018['Characteristics'] == '45 to 54 years') |
    (df_NumOfJob_2018['Characteristics'] == '55 to 64 years') |
    (df_NumOfJob_2018['Characteristics'] == '65 years old and over')]
print(df_NumOfJob_2018_ByAge.head(20))
grouped = df_NumOfJob_2018_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_NumOfJob_2018_ByAge.index))

print("\nGender group in Alberta")
df_NumOfJob_2018_ByGender = df_NumOfJob_2018.loc[
    (df_NumOfJob_2018['Characteristics'] == 'Female employees') |
    (df_NumOfJob_2018['Characteristics'] == 'Male employees')
]
print(df_NumOfJob_2018_ByGender.head(20))
grouped = df_NumOfJob_2018_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_NumOfJob_2018_ByGender.index))

print("\nEducation group in Alberta")
df_NumOfJob_2018_ByEducation = df_NumOfJob_2018.loc[
    (df_NumOfJob_2018['Characteristics'] == 'High school diploma and less') |
    (df_NumOfJob_2018['Characteristics'] == 'Trade certificate') |
    (df_NumOfJob_2018['Characteristics'] == 'University degree and higher')
]
print(df_NumOfJob_2018_ByEducation.head(20))
grouped = df_NumOfJob_2018_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_NumOfJob_2018_ByEducation.index))

print("\nImmigrant group in Alberta")
df_NumOfJob_2018_ByImmigrant = df_NumOfJob_2018.loc[
    (df_NumOfJob_2018['Characteristics'] == 'Immigrant employees') |
    (df_NumOfJob_2018['Characteristics'] == 'Non-immigrant employees')
]
print(df_NumOfJob_2018_ByImmigrant.head(20))
grouped = df_NumOfJob_2018_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_NumOfJob_2018_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgAnnHrk_ByIndigenous = df_NumOfJob_2018.loc[
#     (df_NumOfJob_2018['Characteristics'] == 'Indigenous identity employees') |
#     (df_NumOfJob_2018['Characteristics'] == 'Non-indigenous identity employees')
# ]
# print(df_AvgAnnHrk_ByIndigenous.head(20))
# grouped = df_AvgAnnHrk_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnHrk_ByIndigenous.index))

# %%
# Dataset year in 2021 inside "Number of jobs"

print("\nAge group in Alberta")
df_NumOfJob_2020_ByAge = df_NumOfJob_2020.loc[
    (df_NumOfJob_2020['Characteristics'] == '15 to 24 years') |
    (df_NumOfJob_2020['Characteristics'] == '25 to 34 years') |
    (df_NumOfJob_2020['Characteristics'] == '35 to 44 years') |
    (df_NumOfJob_2020['Characteristics'] == '45 to 54 years') |
    (df_NumOfJob_2020['Characteristics'] == '55 to 64 years') |
    (df_NumOfJob_2020['Characteristics'] == '65 years old and over')]
print(df_NumOfJob_2020_ByAge.head(20))
grouped = df_NumOfJob_2020_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_NumOfJob_2020_ByAge.index))

print("\nGender group in Alberta")
df_NumOfJob_2020_ByGender = df_NumOfJob_2020.loc[
    (df_NumOfJob_2020['Characteristics'] == 'Female employees') |
    (df_NumOfJob_2020['Characteristics'] == 'Male employees')
]
print(df_NumOfJob_2020_ByGender.head(20))
grouped = df_NumOfJob_2020_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_NumOfJob_2020_ByGender.index))

print("\nEducation group in Alberta")
df_NumOfJob_2020_ByEducation = df_NumOfJob_2020.loc[
    (df_NumOfJob_2020['Characteristics'] == 'High school diploma and less') |
    (df_NumOfJob_2020['Characteristics'] == 'Trade certificate') |
    (df_NumOfJob_2020['Characteristics'] == 'University degree and higher')
]
print(df_NumOfJob_2020_ByEducation.head(20))
grouped = df_NumOfJob_2020_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_NumOfJob_2020_ByEducation.index))

print("\nImmigrant group in Alberta")
df_NumOfJob_2020_ByImmigrant = df_NumOfJob_2020.loc[
    (df_NumOfJob_2020['Characteristics'] == 'Immigrant employees') |
    (df_NumOfJob_2020['Characteristics'] == 'Non-immigrant employees')
]
print(df_NumOfJob_2020_ByImmigrant.head(20))
grouped = df_NumOfJob_2020_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_NumOfJob_2020_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgAnnHrk_ByIndigenous = df_NumOfJob_2020.loc[
#     (df_NumOfJob_2020['Characteristics'] == 'Indigenous identity employees') |
#     (df_NumOfJob_2020['Characteristics'] == 'Non-indigenous identity employees')
# ]
# print(df_AvgAnnHrk_ByIndigenous.head(20))
# grouped = df_AvgAnnHrk_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnHrk_ByIndigenous.index))

# %% [markdown]
# Filtered for "Wages and Salaries" by following: "Age group", "Gender level", "Education level", "Immigration status", and "Aboriginal status".

# %%
# # Whole Dataset inside "Wages and Salaries"

# print("\nAge group in Alberta")
# df_WagesAndSalaries_ByAge = df_WagesAndSalaries.loc[
#     (df_WagesAndSalaries['Characteristics'] == '15 to 24 years') |
#     (df_WagesAndSalaries['Characteristics'] == '25 to 34 years') |
#     (df_WagesAndSalaries['Characteristics'] == '35 to 44 years') |
#     (df_WagesAndSalaries['Characteristics'] == '45 to 54 years') |
#     (df_WagesAndSalaries['Characteristics'] == '55 to 64 years') |
#     (df_WagesAndSalaries['Characteristics'] == '65 years old and over')]
# print(df_WagesAndSalaries_ByAge.head(20))
# grouped = df_WagesAndSalaries_ByAge.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_WagesAndSalaries_ByAge.index))

# print("\nGender group in Alberta")
# df_WagesAndSalaries_ByGender = df_WagesAndSalaries.loc[
#     (df_WagesAndSalaries['Characteristics'] == 'Female employees') |
#     (df_WagesAndSalaries['Characteristics'] == 'Male employees')
# ]
# print(df_WagesAndSalaries_ByGender.head(20))
# grouped = df_WagesAndSalaries_ByGender.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_WagesAndSalaries_ByGender.index))

# print("\nEducation group in Alberta")
# df_WagesAndSalaries_ByEducation = df_WagesAndSalaries.loc[
#     (df_WagesAndSalaries['Characteristics'] == 'High school diploma and less') |
#     (df_WagesAndSalaries['Characteristics'] == 'Trade certificate') |
#     (df_WagesAndSalaries['Characteristics'] == 'University degree and higher')
# ]
# print(df_WagesAndSalaries_ByEducation.head(20))
# grouped = df_WagesAndSalaries_ByEducation.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_WagesAndSalaries_ByEducation.index))

# print("\nImmigrant group in Alberta")
# df_WagesAndSalaries_ByImmigrant = df_WagesAndSalaries.loc[
#     (df_WagesAndSalaries['Characteristics'] == 'Immigrant employees') |
#     (df_WagesAndSalaries['Characteristics'] == 'Non-immigrant employees')
# ]
# print(df_WagesAndSalaries_ByImmigrant.head(20))
# grouped = df_WagesAndSalaries_ByImmigrant.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_WagesAndSalaries_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgAnnHrk_ByIndigenous = df_WagesAndSalaries.loc[
#     (df_WagesAndSalaries['Characteristics'] == 'Indigenous identity employees') |
#     (df_WagesAndSalaries['Characteristics'] == 'Non-indigenous identity employees')
# ]
# print(df_AvgAnnHrk_ByIndigenous.head(20))
# grouped = df_AvgAnnHrk_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnHrk_ByIndigenous.index))

# %%
# # Dataset year below year 2016 inside "Wages and Salaries"

# print("\nAge group in Alberta")
# df_WagesAndSalaries_below_2016_ByAge = df_WagesAndSalaries_below_2016.loc[
#     (df_WagesAndSalaries_below_2016['Characteristics'] == '15 to 24 years') |
#     (df_WagesAndSalaries_below_2016['Characteristics'] == '25 to 34 years') |
#     (df_WagesAndSalaries_below_2016['Characteristics'] == '35 to 44 years') |
#     (df_WagesAndSalaries_below_2016['Characteristics'] == '45 to 54 years') |
#     (df_WagesAndSalaries_below_2016['Characteristics'] == '55 to 64 years') |
#     (df_WagesAndSalaries_below_2016['Characteristics'] == '65 years old and over')]
# print(df_WagesAndSalaries_below_2016_ByAge.head(20))
# grouped = df_WagesAndSalaries_below_2016_ByAge.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_WagesAndSalaries_below_2016_ByAge.index))

# print("\nGender group in Alberta")
# df_WagesAndSalaries_below_2016_ByGender = df_WagesAndSalaries_below_2016.loc[
#     (df_WagesAndSalaries_below_2016['Characteristics'] == 'Female employees') |
#     (df_WagesAndSalaries_below_2016['Characteristics'] == 'Male employees')
# ]
# print(df_WagesAndSalaries_below_2016_ByGender.head(20))
# grouped = df_WagesAndSalaries_below_2016_ByGender.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_WagesAndSalaries_below_2016_ByGender.index))

# print("\nEducation group in Alberta")
# df_WagesAndSalaries_below_2016_ByEducation = df_WagesAndSalaries_below_2016.loc[
#     (df_WagesAndSalaries_below_2016['Characteristics'] == 'High school diploma and less') |
#     (df_WagesAndSalaries_below_2016['Characteristics'] == 'Trade certificate') |
#     (df_WagesAndSalaries_below_2016['Characteristics'] == 'University degree and higher')
# ]
# print(df_WagesAndSalaries_below_2016_ByEducation.head(20))
# grouped = df_WagesAndSalaries_below_2016_ByEducation.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_WagesAndSalaries_below_2016_ByEducation.index))

# print("\nImmigrant group in Alberta")
# df_WagesAndSalaries_below_2016_ByImmigrant = df_WagesAndSalaries_below_2016.loc[
#     (df_WagesAndSalaries_below_2016['Characteristics'] == 'Immigrant employees') |
#     (df_WagesAndSalaries_below_2016['Characteristics'] == 'Non-immigrant employees')
# ]
# print(df_WagesAndSalaries_below_2016_ByImmigrant.head(20))
# grouped = df_WagesAndSalaries_below_2016_ByImmigrant.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_WagesAndSalaries_below_2016_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_AvgAnnHrk_ByIndigenous = df_WagesAndSalaries_below_2016.loc[
#     (df_WagesAndSalaries_below_2016['Characteristics'] == 'Indigenous identity employees') |
#     (df_WagesAndSalaries_below_2016['Characteristics'] == 'Non-indigenous identity employees')
# ]
# print(df_AvgAnnHrk_ByIndigenous.head(20))
# grouped = df_AvgAnnHrk_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_AvgAnnHrk_ByIndigenous.index))

# %%
# Dataset year above year of 2017 inside "Wages and Salaries"

print("\nAge group in Alberta")
df_WagesAndSalaries_above_2016_ByAge = df_WagesAndSalaries_above_2016.loc[
    (df_WagesAndSalaries_above_2016['Characteristics'] == '15 to 24 years') |
    (df_WagesAndSalaries_above_2016['Characteristics'] == '25 to 34 years') |
    (df_WagesAndSalaries_above_2016['Characteristics'] == '35 to 44 years') |
    (df_WagesAndSalaries_above_2016['Characteristics'] == '45 to 54 years') |
    (df_WagesAndSalaries_above_2016['Characteristics'] == '55 to 64 years') |
    (df_WagesAndSalaries_above_2016['Characteristics'] == '65 years old and over')]
print(df_WagesAndSalaries_above_2016_ByAge.head(20))
grouped = df_WagesAndSalaries_above_2016_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_WagesAndSalaries_above_2016_ByAge.index))

print("\nGender group in Alberta")
df_WagesAndSalaries_above_2016_ByGender = df_WagesAndSalaries_above_2016.loc[
    (df_WagesAndSalaries_above_2016['Characteristics'] == 'Female employees') |
    (df_WagesAndSalaries_above_2016['Characteristics'] == 'Male employees')
]
print(df_WagesAndSalaries_above_2016_ByGender.head(20))
grouped = df_WagesAndSalaries_above_2016_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_WagesAndSalaries_above_2016_ByGender.index))

print("\nEducation group in Alberta")
df_WagesAndSalaries_above_2016_ByEducation = df_WagesAndSalaries_above_2016.loc[
    (df_WagesAndSalaries_above_2016['Characteristics'] == 'High school diploma and less') |
    (df_WagesAndSalaries_above_2016['Characteristics'] == 'Trade certificate') |
    (df_WagesAndSalaries_above_2016['Characteristics'] == 'University degree and higher')
]
print(df_WagesAndSalaries_above_2016_ByEducation.head(20))
grouped = df_WagesAndSalaries_above_2016_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_WagesAndSalaries_above_2016_ByEducation.index))

print("\nImmigrant group in Alberta")
df_WagesAndSalaries_above_2016_ByImmigrant = df_WagesAndSalaries_above_2016.loc[
    (df_WagesAndSalaries_above_2016['Characteristics'] == 'Immigrant employees') |
    (df_WagesAndSalaries_above_2016['Characteristics'] == 'Non-immigrant employees')
]
print(df_WagesAndSalaries_above_2016_ByImmigrant.head(20))
grouped = df_WagesAndSalaries_above_2016_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_WagesAndSalaries_above_2016_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_WagesAndSalaries_above_2016_ByIndigenous = df_WagesAndSalaries_above_2016.loc[
#     (df_WagesAndSalaries_above_2016['Characteristics'] == 'Indigenous identity employees') |
#     (df_WagesAndSalaries_above_2016['Characteristics'] == 'Non-indigenous identity employees')
# ]
# print(df_WagesAndSalaries_above_2016_ByIndigenous.head(20))
# grouped = df_WagesAndSalaries_above_2016_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_WagesAndSalaries_above_2016_ByIndigenous.index))

# %%
# Dataset year in 2017 inside "Wages and Salaries"

print("\nAge group in Alberta")
df_WagesAndSalaries_2016_ByAge = df_WagesAndSalaries_2016.loc[
    (df_WagesAndSalaries_2016['Characteristics'] == '15 to 24 years') |
    (df_WagesAndSalaries_2016['Characteristics'] == '25 to 34 years') |
    (df_WagesAndSalaries_2016['Characteristics'] == '35 to 44 years') |
    (df_WagesAndSalaries_2016['Characteristics'] == '45 to 54 years') |
    (df_WagesAndSalaries_2016['Characteristics'] == '55 to 64 years') |
    (df_WagesAndSalaries_2016['Characteristics'] == '65 years old and over')]
print(df_WagesAndSalaries_2016_ByAge.head(20))
grouped = df_WagesAndSalaries_2016_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_WagesAndSalaries_2016_ByAge.index))

print("\nGender group in Alberta")
df_WagesAndSalaries_2016_ByGender = df_WagesAndSalaries_2016.loc[
    (df_WagesAndSalaries_2016['Characteristics'] == 'Female employees') |
    (df_WagesAndSalaries_2016['Characteristics'] == 'Male employees')
]
print(df_WagesAndSalaries_2016_ByGender.head(20))
grouped = df_WagesAndSalaries_2016_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_WagesAndSalaries_2016_ByGender.index))

print("\nEducation group in Alberta")
df_WagesAndSalaries_2016_ByEducation = df_WagesAndSalaries_2016.loc[
    (df_WagesAndSalaries_2016['Characteristics'] == 'High school diploma and less') |
    (df_WagesAndSalaries_2016['Characteristics'] == 'Trade certificate') |
    (df_WagesAndSalaries_2016['Characteristics'] == 'University degree and higher')
]
print(df_WagesAndSalaries_2016_ByEducation.head(20))
grouped = df_WagesAndSalaries_2016_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_WagesAndSalaries_2016_ByEducation.index))

print("\nImmigrant group in Alberta")
df_WagesAndSalaries_2016_ByImmigrant = df_WagesAndSalaries_2016.loc[
    (df_WagesAndSalaries_2016['Characteristics'] == 'Immigrant employees') |
    (df_WagesAndSalaries_2016['Characteristics'] == 'Non-immigrant employees')
]
print(df_WagesAndSalaries_2016_ByImmigrant.head(20))
grouped = df_WagesAndSalaries_2016_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_WagesAndSalaries_2016_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_WagesAndSalaries_2016_ByIndigenous = df_WagesAndSalaries_2016.loc[
#     (df_WagesAndSalaries_2016['Characteristics'] == 'Indigenous identity employees') |
#     (df_WagesAndSalaries_2016['Characteristics'] == 'Non-indigenous identity employees')
# ]
# print(df_WagesAndSalaries_2016_ByIndigenous.head(20))
# grouped = df_WagesAndSalaries_2016_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_WagesAndSalaries_2016_ByIndigenous.index))


# %%
# Dataset year in 2019 inside "Wages and Salaries"

print("\nAge group in Alberta")
df_WagesAndSalaries_2018_ByAge = df_WagesAndSalaries_2018.loc[
    (df_WagesAndSalaries_2018['Characteristics'] == '15 to 24 years') |
    (df_WagesAndSalaries_2018['Characteristics'] == '25 to 34 years') |
    (df_WagesAndSalaries_2018['Characteristics'] == '35 to 44 years') |
    (df_WagesAndSalaries_2018['Characteristics'] == '45 to 54 years') |
    (df_WagesAndSalaries_2018['Characteristics'] == '55 to 64 years') |
    (df_WagesAndSalaries_2018['Characteristics'] == '65 years old and over')]
print(df_WagesAndSalaries_2018_ByAge.head(20))
grouped = df_WagesAndSalaries_2018_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_WagesAndSalaries_2018_ByAge.index))

print("\nGender group in Alberta")
df_WagesAndSalaries_2018_ByGender = df_WagesAndSalaries_2018.loc[
    (df_WagesAndSalaries_2018['Characteristics'] == 'Female employees') |
    (df_WagesAndSalaries_2018['Characteristics'] == 'Male employees')
]
print(df_WagesAndSalaries_2018_ByGender.head(20))
grouped = df_WagesAndSalaries_2018_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_WagesAndSalaries_2018_ByGender.index))

print("\nEducation group in Alberta")
df_WagesAndSalaries_2018_ByEducation = df_WagesAndSalaries_2018.loc[
    (df_WagesAndSalaries_2018['Characteristics'] == 'High school diploma and less') |
    (df_WagesAndSalaries_2018['Characteristics'] == 'Trade certificate') |
    (df_WagesAndSalaries_2018['Characteristics'] == 'University degree and higher')
]
print(df_WagesAndSalaries_2018_ByEducation.head(20))
grouped = df_WagesAndSalaries_2018_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_WagesAndSalaries_2018_ByEducation.index))

print("\nImmigrant group in Alberta")
df_WagesAndSalaries_2018_ByImmigrant = df_WagesAndSalaries_2018.loc[
    (df_WagesAndSalaries_2018['Characteristics'] == 'Immigrant employees') |
    (df_WagesAndSalaries_2018['Characteristics'] == 'Non-immigrant employees')
]
print(df_WagesAndSalaries_2018_ByImmigrant.head(20))
grouped = df_WagesAndSalaries_2018_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_WagesAndSalaries_2018_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_WagesAndSalaries_2018_ByIndigenous = df_WagesAndSalaries_2018.loc[
#     (df_WagesAndSalaries_2018['Characteristics'] == 'Indigenous identity employees') |
#     (df_WagesAndSalaries_2018['Characteristics'] == 'Non-indigenous identity employees')
# ]
# print(df_WagesAndSalaries_2018_ByIndigenous.head(20))
# grouped = df_WagesAndSalaries_2018_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_WagesAndSalaries_2018_ByIndigenous.index))


# %%
# Dataset year in 2021 inside "Wages and Salaries"

print("\nAge group in Alberta")
df_WagesAndSalaries_2020_ByAge = df_WagesAndSalaries_2020.loc[
    (df_WagesAndSalaries_2020['Characteristics'] == '15 to 24 years') |
    (df_WagesAndSalaries_2020['Characteristics'] == '25 to 34 years') |
    (df_WagesAndSalaries_2020['Characteristics'] == '35 to 44 years') |
    (df_WagesAndSalaries_2020['Characteristics'] == '45 to 54 years') |
    (df_WagesAndSalaries_2020['Characteristics'] == '55 to 64 years') |
    (df_WagesAndSalaries_2020['Characteristics'] == '65 years old and over')]
print(df_WagesAndSalaries_2020_ByAge.head(20))
grouped = df_WagesAndSalaries_2020_ByAge.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_WagesAndSalaries_2020_ByAge.index))

print("\nGender group in Alberta")
df_WagesAndSalaries_2020_ByGender = df_WagesAndSalaries_2020.loc[
    (df_WagesAndSalaries_2020['Characteristics'] == 'Female employees') |
    (df_WagesAndSalaries_2020['Characteristics'] == 'Male employees')
]
print(df_WagesAndSalaries_2020_ByGender.head(20))
grouped = df_WagesAndSalaries_2020_ByGender.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_WagesAndSalaries_2020_ByGender.index))

print("\nEducation group in Alberta")
df_WagesAndSalaries_2020_ByEducation = df_WagesAndSalaries_2020.loc[
    (df_WagesAndSalaries_2020['Characteristics'] == 'High school diploma and less') |
    (df_WagesAndSalaries_2020['Characteristics'] == 'Trade certificate') |
    (df_WagesAndSalaries_2020['Characteristics'] == 'University degree and higher')
]
print(df_WagesAndSalaries_2020_ByEducation.head(20))
grouped = df_WagesAndSalaries_2020_ByEducation.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_WagesAndSalaries_2020_ByEducation.index))

print("\nImmigrant group in Alberta")
df_WagesAndSalaries_2020_ByImmigrant = df_WagesAndSalaries_2020.loc[
    (df_WagesAndSalaries_2020['Characteristics'] == 'Immigrant employees') |
    (df_WagesAndSalaries_2020['Characteristics'] == 'Non-immigrant employees')
]
print(df_WagesAndSalaries_2020_ByImmigrant.head(20))
grouped = df_WagesAndSalaries_2020_ByImmigrant.groupby(['Characteristics'])
print(grouped['VALUE'].agg([np.sum, np.size]))
print("The total number of this one is ",len(df_WagesAndSalaries_2020_ByImmigrant.index))

# print("\nIndigenous group in Alberta")
# df_WagesAndSalaries_2020_ByIndigenous = df_WagesAndSalaries_2020.loc[
#     (df_WagesAndSalaries_2020['Characteristics'] == 'Indigenous identity employees') |
#     (df_WagesAndSalaries_2020['Characteristics'] == 'Non-indigenous identity employees')
# ]
# print(df_WagesAndSalaries_2020_ByIndigenous.head(20))
# grouped = df_WagesAndSalaries_2020_ByIndigenous.groupby(['Characteristics'])
# print(grouped['VALUE'].agg([np.sum, np.size]))
# print("The total number of this one is ",len(df_WagesAndSalaries_2020_ByIndigenous.index))

# %% [markdown]
# Final output for Average annual hours worked

# %%
dfa_Target_To_Analysis = [df_AvgAnnHrsWrk_above_2016_ByAge, df_AvgAnnHrsWrk_above_2016_ByEducation, df_AvgAnnHrsWrk_above_2016_ByEducation, df_AvgAnnHrsWrk_above_2016_ByImmigrant]
for df_Target_To_Analysis in dfa_Target_To_Analysis:
      grouped = df_Target_To_Analysis.groupby(['Characteristics'])
      print("Year of above 2016")
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
dfa_Target_To_Analysis = [df_AvgAnnHrsWrk_2018_ByAge, df_AvgAnnHrsWrk_2018_ByEducation, df_AvgAnnHrsWrk_2018_ByEducation, df_AvgAnnHrsWrk_2018_ByImmigrant]
for df_Target_To_Analysis in dfa_Target_To_Analysis:
      grouped = df_Target_To_Analysis.groupby(['Characteristics'])
      print("Year of 2018")
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
dfa_Target_To_Analysis = [df_AvgAnnHrsWrk_2020_ByAge, df_AvgAnnHrsWrk_2020_ByEducation, df_AvgAnnHrsWrk_2020_ByEducation, df_AvgAnnHrsWrk_2020_ByImmigrant]
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
dfa_Target_To_Analysis = [df_AvgAnnWages_above_2016_ByAge, df_AvgAnnWages_above_2016_ByEducation, df_AvgAnnWages_above_2016_ByEducation, df_AvgAnnWages_above_2016_ByImmigrant]
for df_Target_To_Analysis in dfa_Target_To_Analysis:
      grouped = df_Target_To_Analysis.groupby(['Characteristics'])
      print("Year of above 2016")
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
dfa_Target_To_Analysis = [df_AvgAnnWages_2018_ByAge, df_AvgAnnWages_2018_ByEducation, df_AvgAnnWages_2018_ByEducation, df_AvgAnnWages_2018_ByImmigrant]
for df_Target_To_Analysis in dfa_Target_To_Analysis:
      grouped = df_Target_To_Analysis.groupby(['Characteristics'])
      print("Year of 2018")
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
dfa_Target_To_Analysis = [df_AvgAnnWages_2020_ByAge, df_AvgAnnWages_2020_ByEducation, df_AvgAnnWages_2020_ByEducation, df_AvgAnnWages_2020_ByImmigrant]
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
dfa_Target_To_Analysis = [df_AvgHrsWages_above_2016_ByAge, df_AvgHrsWages_above_2016_ByEducation, df_AvgHrsWages_above_2016_ByEducation, df_AvgHrsWages_above_2016_ByImmigrant]
for df_Target_To_Analysis in dfa_Target_To_Analysis:
      grouped = df_Target_To_Analysis.groupby(['Characteristics'])
      print("Year of above 2016")
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
dfa_Target_To_Analysis = [df_AvgHrsWages_2018_ByAge, df_AvgHrsWages_2018_ByEducation, df_AvgHrsWages_2018_ByEducation, df_AvgHrsWages_2018_ByImmigrant]
for df_Target_To_Analysis in dfa_Target_To_Analysis:
      grouped = df_Target_To_Analysis.groupby(['Characteristics'])
      print("Year of 2018")
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
dfa_Target_To_Analysis = [df_AvgHrsWages_2020_ByAge, df_AvgHrsWages_2020_ByEducation, df_AvgHrsWages_2020_ByEducation, df_AvgHrsWages_2020_ByImmigrant]
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
# Final output for "Average weekly hours worked"

# %%
dfa_Target_To_Analysis = [df_AvgWeekHrsWrked_above_2016_ByAge, df_AvgWeekHrsWrked_above_2016_ByEducation, df_AvgWeekHrsWrked_above_2016_ByEducation, df_AvgWeekHrsWrked_above_2016_ByImmigrant]
for df_Target_To_Analysis in dfa_Target_To_Analysis:
      grouped = df_Target_To_Analysis.groupby(['Characteristics'])
      print("Year of above 2016")
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
dfa_Target_To_Analysis = [df_AvgWeekHrsWrked_2018_ByAge, df_AvgWeekHrsWrked_2018_ByEducation, df_AvgWeekHrsWrked_2018_ByEducation, df_AvgWeekHrsWrked_2018_ByImmigrant]
for df_Target_To_Analysis in dfa_Target_To_Analysis:
      grouped = df_Target_To_Analysis.groupby(['Characteristics'])
      print("Year of 2018")
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
dfa_Target_To_Analysis = [df_AvgWeekHrsWrked_2020_ByAge, df_AvgWeekHrsWrked_2020_ByEducation, df_AvgWeekHrsWrked_2020_ByEducation, df_AvgWeekHrsWrked_2020_ByImmigrant]
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
# Final output for "Hours Worked"

# %%
dfa_Target_To_Analysis = [df_Hrs_Wrked_above_2016_ByAge, df_Hrs_Wrked_above_2016_ByEducation, df_Hrs_Wrked_above_2016_ByEducation, df_Hrs_Wrked_above_2016_ByImmigrant]
for df_Target_To_Analysis in dfa_Target_To_Analysis:
      grouped = df_Target_To_Analysis.groupby(['Characteristics'])
      print("Year of above 2016")
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
dfa_Target_To_Analysis = [df_Hrs_Wrked_2018_ByAge, df_Hrs_Wrked_2018_ByEducation, df_Hrs_Wrked_2018_ByEducation, df_Hrs_Wrked_2018_ByImmigrant]
for df_Target_To_Analysis in dfa_Target_To_Analysis:
      grouped = df_Target_To_Analysis.groupby(['Characteristics'])
      print("Year of 2018")
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
dfa_Target_To_Analysis = [df_Hrs_Wrked_2020_ByAge, df_Hrs_Wrked_2020_ByEducation, df_Hrs_Wrked_2020_ByEducation, df_Hrs_Wrked_2020_ByImmigrant]
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
# Final output for "Number of jobs"

# %%
dfa_Target_To_Analysis = [df_NumOfJob_above_2016_ByAge, df_NumOfJob_above_2016_ByEducation, df_NumOfJob_above_2016_ByEducation, df_NumOfJob_above_2016_ByImmigrant]
for df_Target_To_Analysis in dfa_Target_To_Analysis:
      grouped = df_Target_To_Analysis.groupby(['Characteristics'])
      print("Year of above 2016")
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
dfa_Target_To_Analysis = [df_NumOfJob_2018_ByAge, df_NumOfJob_2018_ByEducation, df_NumOfJob_2018_ByEducation, df_NumOfJob_2018_ByImmigrant]
for df_Target_To_Analysis in dfa_Target_To_Analysis:
      grouped = df_Target_To_Analysis.groupby(['Characteristics'])
      print("Year of 2018")
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
dfa_Target_To_Analysis = [df_NumOfJob_2020_ByAge, df_NumOfJob_2020_ByEducation, df_NumOfJob_2020_ByEducation, df_NumOfJob_2020_ByImmigrant]
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
# Final output for "Wages and Salaries"

# %%
dfa_Target_To_Analysis = [df_WagesAndSalaries_above_2016_ByAge, df_WagesAndSalaries_above_2016_ByEducation, df_WagesAndSalaries_above_2016_ByEducation, df_WagesAndSalaries_above_2016_ByImmigrant]
for df_Target_To_Analysis in dfa_Target_To_Analysis:
      grouped = df_Target_To_Analysis.groupby(['Characteristics'])
      print("Year of above 2016")
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
dfa_Target_To_Analysis = [df_WagesAndSalaries_2018_ByAge, df_WagesAndSalaries_2018_ByEducation, df_WagesAndSalaries_2018_ByEducation, df_WagesAndSalaries_2018_ByImmigrant]
for df_Target_To_Analysis in dfa_Target_To_Analysis:
      grouped = df_Target_To_Analysis.groupby(['Characteristics'])
      print("Year of 2018")
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
dfa_Target_To_Analysis = [df_WagesAndSalaries_2020_ByAge, df_WagesAndSalaries_2020_ByEducation, df_WagesAndSalaries_2020_ByEducation, df_WagesAndSalaries_2020_ByImmigrant]
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
        self.pd = pd
        self.np = np
        self.pp = pp
        self.df_ByProvince = []
        for x in self.province:
            df_sorted = df.loc[df['GEO'] == x]
            self.df_ByProvince.append(df_sorted)
        # self.df_sorted = df.loc[df['GEO'] == province]

    def outputProvince(self, province_id):
        print(self.province[province_id])

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
        # grouped = self.df_sorted.groupby(['Characteristics'])
        grouped = self.df_ByProvince[province_id].groupby(['Characteristics'])
        print(grouped['VALUE'].agg([self.np.sum, self.np.mean, self.np.size]))

    def outputList(self, province_id, num):
        print("\nGrab the dataset only in " + str(self.province[province_id]))
        print(self.df_ByProvince[province_id].head(num))
        print(self.df_ByProvince[province_id].info())

    def outputPandaProfiling(self, province_id, indicator_id, type_id):

        indicator = ["Average annual hours worked",
                    "Average annual wages and salaries",
                    "Average hourly wage",
                    "Average weekly hours worked",
                    "Hours Worked",
                    "Number of jobs",
                    "Wages and Salaries"]
        
        type = ["",
                "below 2015",
                "above 2016",
                "2016",
                "2018",
                "2020"]

        fileName = str(indicator[indicator_id]) + " " + str(type[type_id]) + " in " + str(self.province[province_id]) + ".html"
        

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
# df_AvgAnnHrsWrk_below_2016_ByAge_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_below_2016_ByAge, pd, np, pp)
df_AvgAnnHrsWrk_above_2016_ByAge_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_above_2016_ByAge, pd, np, pp)
df_AvgAnnHrsWrk_2016_ByAge_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByAge, pd, np, pp)
df_AvgAnnHrsWrk_2018_ByAge_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_2018_ByAge, pd, np, pp)
df_AvgAnnHrsWrk_2020_ByAge_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_2020_ByAge, pd, np, pp)

# df_AvgAnnHrsWrk_ByGender_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_ByGender, pd, np, pp)
# df_AvgAnnHrsWrk_below_2016_ByGender_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_below_2016_ByGender, pd, np, pp)
df_AvgAnnHrsWrk_above_2016_ByGender_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_above_2016_ByGender, pd, np, pp)
df_AvgAnnHrsWrk_2016_ByGender_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByGender, pd, np, pp)
df_AvgAnnHrsWrk_2018_ByGender_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_2018_ByGender, pd, np, pp)
df_AvgAnnHrsWrk_2020_ByGender_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_2020_ByGender, pd, np, pp)

# df_AvgAnnHrsWrk_ByEducation_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_ByEducation, pd, np, pp)
# df_AvgAnnHrsWrk_below_2016_ByEducation_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_below_2016_ByEducation, pd, np, pp)
df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_above_2016_ByEducation, pd, np, pp)
df_AvgAnnHrsWrk_2016_ByEducation_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByEducation, pd, np, pp)
df_AvgAnnHrsWrk_2018_ByEducation_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_2018_ByEducation, pd, np, pp)
df_AvgAnnHrsWrk_2020_ByEducation_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_2020_ByEducation, pd, np, pp)

# df_AvgAnnHrsWrk_ByImmigrant_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_ByImmigrant, pd, np, pp)
# df_AvgAnnHrsWrk_below_2016_ByImmigrant_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_below_2016_ByImmigrant, pd, np, pp)
df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_above_2016_ByImmigrant, pd, np, pp)
df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByImmigrant, pd, np, pp)
df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_2018_ByImmigrant, pd, np, pp)
df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_2020_ByImmigrant, pd, np, pp)

# df_AvgAnnHrsWrk_ByIndigenous_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_ByIndigenous, pd, np, pp)
# df_AvgAnnHrsWrk_below_2016_ByIndigenous_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_below_2016_ByIndigenous, pd, np, pp)
# df_AvgAnnHrsWrk_above_2016_ByIndigenous_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_above_2017_ByIndigenous, pd, np, pp)
# df_AvgAnnHrsWrk_2016_ByIndigenous_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_2016_ByIndigenous, pd, np, pp)
# df_AvgAnnHrsWrk_2018_ByIndigenous_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_2018_ByIndigenous, pd, np, pp)
# df_AvgAnnHrsWrk_2020_ByIndigenous_Provinces = ProvinceAnalysis(df_AvgAnnHrsWrk_2020_ByIndigenous, pd, np, pp)

# %% [markdown]
# Filtered by provinces by "Average wages and salaries"

# %%
# By Average annual wages and salaries worked categories by provinces.

# df_AvgAnnWages_ByAge_Provinces = ProvinceAnalysis(df_AvgAnnWages_ByAge, pd, np, pp)
# df_AvgAnnWages_below_2016_ByAge_Provinces = ProvinceAnalysis(df_AvgAnnWages_below_2016_ByAge, pd, np, pp)
df_AvgAnnWages_above_2016_ByAge_Provinces = ProvinceAnalysis(df_AvgAnnWages_above_2016_ByAge, pd, np, pp)
df_AvgAnnWages_2016_ByAge_Provinces = ProvinceAnalysis(df_AvgAnnWages_2016_ByAge, pd, np, pp)
df_AvgAnnWages_2018_ByAge_Provinces = ProvinceAnalysis(df_AvgAnnWages_2018_ByAge, pd, np, pp)
df_AvgAnnWages_2020_ByAge_Provinces = ProvinceAnalysis(df_AvgAnnWages_2020_ByAge, pd, np, pp)

# df_AvgAnnWages_ByGender_Provinces = ProvinceAnalysis(df_AvgAnnWages_ByGender, pd, np, pp)
# df_AvgAnnWages_below_2016_ByGender_Provinces = ProvinceAnalysis(df_AvgAnnWages_below_2016_ByGender, pd, np, pp)
df_AvgAnnWages_above_2016_ByGender_Provinces = ProvinceAnalysis(df_AvgAnnWages_above_2016_ByGender, pd, np, pp)
df_AvgAnnWages_2016_ByGender_Provinces = ProvinceAnalysis(df_AvgAnnWages_2016_ByGender, pd, np, pp)
df_AvgAnnWages_2018_ByGender_Provinces = ProvinceAnalysis(df_AvgAnnWages_2018_ByGender, pd, np, pp)
df_AvgAnnWages_2020_ByGender_Provinces = ProvinceAnalysis(df_AvgAnnWages_2020_ByGender, pd, np, pp)

# df_AvgAnnWages_ByEducation_Provinces = ProvinceAnalysis(df_AvgAnnWages_ByEducation, pd, np, pp)
# df_AvgAnnWages_below_2016_ByEducation_Provinces = ProvinceAnalysis(df_AvgAnnWages_below_2016_ByEducation, pd, np, pp)
# df_AvgAnnWages_above_2016_ByEducation_Provinces = ProvinceAnalysis(df_AvgAnnWages_above_2016_ByEducation, pd, np, pp)
df_AvgAnnWages_2016_ByEducation_Provinces = ProvinceAnalysis(df_AvgAnnWages_2016_ByEducation, pd, np, pp)
df_AvgAnnWages_2018_ByEducation_Provinces = ProvinceAnalysis(df_AvgAnnWages_2018_ByEducation, pd, np, pp)
df_AvgAnnWages_2020_ByEducation_Provinces = ProvinceAnalysis(df_AvgAnnWages_2020_ByEducation, pd, np, pp)

# df_AvgAnnWages_ByImmigrant_Provinces = ProvinceAnalysis(df_AvgAnnWages_ByImmigrant, pd, np, pp)
# df_AvgAnnWages_below_2016_ByImmigrant_Provinces = ProvinceAnalysis(df_AvgAnnWages_below_2016_ByImmigrant, pd, np, pp)
df_AvgAnnWages_above_2016_ByImmigrant_Provinces = ProvinceAnalysis(df_AvgAnnWages_above_2016_ByImmigrant, pd, np, pp)
df_AvgAnnWages_2016_ByImmigrant_Provinces = ProvinceAnalysis(df_AvgAnnWages_2016_ByImmigrant, pd, np, pp)
df_AvgAnnWages_2018_ByImmigrant_Provinces = ProvinceAnalysis(df_AvgAnnWages_2018_ByImmigrant, pd, np, pp)
df_AvgAnnWages_2020_ByImmigrant_Provinces = ProvinceAnalysis(df_AvgAnnWages_2020_ByImmigrant, pd, np, pp)

# df_AvgAnnWages_ByIndigenous_Provinces = ProvinceAnalysis(df_AvgAnnWages_ByIndigenous, pd, np, pp)
# df_AvgAnnWages_below_2016_ByIndigenous_Provinces = ProvinceAnalysis(df_AvgAnnWages_below_2016_ByIndigenous, pd, np, pp)
# df_AvgAnnWages_above_2017_ByIndigenous_Provinces = ProvinceAnalysis(df_AvgAnnWages_above_2017_ByIndigenous, pd, np, pp)
# df_AvgAnnWages_2017_ByIndigenous_Provinces = ProvinceAnalysis(df_AvgAnnWages_2017_ByIndigenous, pd, np, pp)
# df_AvgAnnWages_2019_ByIndigenous_Provinces = ProvinceAnalysis(df_AvgAnnWages_2019_ByIndigenous, pd, np, pp)
# df_AvgAnnWages_2021_ByIndigenous_Provinces = ProvinceAnalysis(df_AvgAnnWages_2021_ByIndigenous, pd, np, pp)

# %% [markdown]
# Filtered by provinces by "Average hourly wage"

# %%
# By Average hourly wages and salaries worked categories by provinces.

# df_AvgHrsWages_ByAge_Provinces = ProvinceAnalysis(df_AvgHrsWages_ByAge, pd, np, pp)
# df_AvgHrsWages_below_2016_ByAge_Provinces = ProvinceAnalysis(df_AvgHrsWages_below_2016_ByAge, pd, np, pp)
df_AvgHrsWages_above_2016_ByAge_Provinces = ProvinceAnalysis(df_AvgHrsWages_above_2016_ByAge, pd, np, pp)
df_AvgHrsWages_2016_ByAge_Provinces = ProvinceAnalysis(df_AvgHrsWages_2016_ByAge, pd, np, pp)
df_AvgHrsWages_2018_ByAge_Provinces = ProvinceAnalysis(df_AvgHrsWages_2018_ByAge, pd, np, pp)
df_AvgHrsWages_2020_ByAge_Provinces = ProvinceAnalysis(df_AvgHrsWages_2020_ByAge, pd, np, pp)

# df_AvgHrsWages_ByGender_Provinces = ProvinceAnalysis(df_AvgHrsWages_ByGender, pd, np, pp)
# df_AvgHrsWages_below_2016_ByGender_Provinces = ProvinceAnalysis(df_AvgHrsWages_below_2016_ByGender, pd, np, pp)
df_AvgHrsWages_above_2016_ByGender_Provinces = ProvinceAnalysis(df_AvgHrsWages_above_2016_ByGender, pd, np, pp)
df_AvgHrsWages_2016_ByGender_Provinces = ProvinceAnalysis(df_AvgHrsWages_2016_ByGender, pd, np, pp)
df_AvgHrsWages_2018_ByGender_Provinces = ProvinceAnalysis(df_AvgHrsWages_2018_ByGender, pd, np, pp)
df_AvgHrsWages_2020_ByGender_Provinces = ProvinceAnalysis(df_AvgHrsWages_2020_ByGender, pd, np, pp)

# df_AvgHrsWages_ByEducation_Provinces = ProvinceAnalysis(df_AvgHrsWages_ByEducation, pd, np, pp)
# df_AvgHrsWages_below_2016_ByEducation_Provinces = ProvinceAnalysis(df_AvgHrsWages_below_2016_ByEducation, pd, np, pp)
df_AvgHrsWages_above_2016_ByEducation_Provinces = ProvinceAnalysis(df_AvgHrsWages_above_2016_ByEducation, pd, np, pp)
df_AvgHrsWages_2016_ByEducation_Provinces = ProvinceAnalysis(df_AvgHrsWages_2016_ByEducation, pd, np, pp)
df_AvgHrsWages_2018_ByEducation_Provinces = ProvinceAnalysis(df_AvgHrsWages_2018_ByEducation, pd, np, pp)
df_AvgHrsWages_2020_ByEducation_Provinces = ProvinceAnalysis(df_AvgHrsWages_2020_ByEducation, pd, np, pp)

# df_AvgHrsWages_ByImmigrant_Provinces = ProvinceAnalysis(df_AvgHrsWages_ByImmigrant, pd, np, pp)
# df_AvgHrsWages_below_2016_ByImmigrant_Provinces = ProvinceAnalysis(df_AvgHrsWages_below_2016_ByImmigrant, pd, np, pp)
df_AvgHrsWages_above_2016_ByImmigrant_Provinces = ProvinceAnalysis(df_AvgHrsWages_above_2016_ByImmigrant, pd, np, pp)
df_AvgHrsWages_2016_ByImmigrant_Provinces = ProvinceAnalysis(df_AvgHrsWages_2016_ByImmigrant, pd, np, pp)
df_AvgHrsWages_2018_ByImmigrant_Provinces = ProvinceAnalysis(df_AvgHrsWages_2018_ByImmigrant, pd, np, pp)
df_AvgHrsWages_2020_ByImmigrant_Provinces = ProvinceAnalysis(df_AvgHrsWages_2020_ByImmigrant, pd, np, pp)

# df_AvgHrsWages_ByIndigenous_Provinces = ProvinceAnalysis(df_AvgHrsWages_ByIndigenous, pd, np, pp)
# df_AvgHrsWages_below_2016_ByIndigenous_Provinces = ProvinceAnalysis(df_AvgHrsWages_below_2016_ByIndigenous, pd, np, pp)
# df_AvgHrsWages_above_2017_ByIndigenous_Provinces = ProvinceAnalysis(df_AvgHrsWages_above_2017_ByIndigenous, pd, np, pp)
# # df_AvgHrsWages_2017_ByIndigenous_Provinces = ProvinceAnalysis(df_AvgHrsWages_2017_ByIndigenous, pd, np, pp)
# # df_AvgHrsWages_2019_ByIndigenous_Provinces = ProvinceAnalysis(df_AvgHrsWages_2019_ByIndigenous, pd, np, pp)
# df_AvgHrsWages_2021_ByIndigenous_Provinces = ProvinceAnalysis(df_AvgHrsWages_2021_ByIndigenous, pd, np, pp)

# %% [markdown]
# Filtered by provinces by "Average weekly hours worked"

# %%
# By Average annual wages and salaries worked categories by provinces.

# df_AvgWeekHrsWrked_ByAge_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_ByAge, pd, np, pp)
# df_AvgWeekHrsWrked_below_2016_ByAge_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_below_2016_ByAge, pd, np, pp)
df_AvgWeekHrsWrked_above_2016_ByAge_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_above_2016_ByAge, pd, np, pp)
df_AvgWeekHrsWrked_2016_ByAge_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_2016_ByAge, pd, np, pp)
df_AvgWeekHrsWrked_2018_ByAge_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_2018_ByAge, pd, np, pp)
df_AvgWeekHrsWrked_2020_ByAge_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_2020_ByAge, pd, np, pp)

# df_AvgWeekHrsWrked_ByGender_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_ByGender, pd, np, pp)
# df_AvgWeekHrsWrked_below_2016_ByGender_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_below_2016_ByGender, pd, np, pp)
df_AvgWeekHrsWrked_above_2016_ByGender_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_above_2016_ByGender, pd, np, pp)
df_AvgWeekHrsWrked_2016_ByGender_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_2016_ByGender, pd, np, pp)
df_AvgWeekHrsWrked_2018_ByGender_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_2018_ByGender, pd, np, pp)
df_AvgWeekHrsWrked_2020_ByGender_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_2020_ByGender, pd, np, pp)

# df_AvgWeekHrsWrked_ByEducation_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_ByEducation, pd, np, pp)
# df_AvgWeekHrsWrked_below_2016_ByEducation_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_below_2016_ByEducation, pd, np, pp)
df_AvgWeekHrsWrked_above_2016_ByEducation_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_above_2016_ByEducation, pd, np, pp)
df_AvgWeekHrsWrked_2016_ByEducation_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_2016_ByEducation, pd, np, pp)
df_AvgWeekHrsWrked_2018_ByEducation_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_2018_ByEducation, pd, np, pp)
df_AvgWeekHrsWrked_2020_ByEducation_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_2020_ByEducation, pd, np, pp)

# df_AvgWeekHrsWrked_ByImmigrant_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_ByImmigrant, pd, np, pp)
# df_AvgWeekHrsWrked_below_2016_ByImmigrant_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_below_2016_ByImmigrant, pd, np, pp)
df_AvgWeekHrsWrked_above_2016_ByImmigrant_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_above_2016_ByImmigrant, pd, np, pp)
df_AvgWeekHrsWrked_2016_ByImmigrant_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_2016_ByImmigrant, pd, np, pp)
df_AvgWeekHrsWrked_2018_ByImmigrant_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_2018_ByImmigrant, pd, np, pp)
df_AvgWeekHrsWrked_2020_ByImmigrant_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_2020_ByImmigrant, pd, np, pp)

# # df_AvgWeekHrsWrked_ByIndigenous_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_ByIndigenous, pd, np, pp)
# df_AvgWeekHrsWrked_below_2016_ByIndigenous_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_below_2016_ByIndigenous, pd, np, pp)
# df_AvgWeekHrsWrked_above_2017_ByIndigenous_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_above_2017_ByIndigenous, pd, np, pp)
# # df_AvgWeekHrsWrked_2017_ByIndigenous_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_2017_ByIndigenous, pd, np, pp)
# # df_AvgWeekHrsWrked_2019_ByIndigenous_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_2019_ByIndigenous, pd, np, pp)
# df_AvgWeekHrsWrked_2021_ByIndigenous_Provinces = ProvinceAnalysis(df_AvgWeekHrsWrked_2021_ByIndigenous, pd, np, pp)

# %% [markdown]
# Filtered by provinces by "Hours Worked"

# %%
# By Hours workee and salaries worked categories by provinces.

# df_Hrs_Wrked_ByAge_Provinces = ProvinceAnalysis(df_Hrs_Wrked_ByAge, pd, np, pp)
# df_Hrs_Wrked_below_2016_ByAge_Provinces = ProvinceAnalysis(df_Hrs_Wrked_below_2016_ByAge, pd, np, pp)
df_Hrs_Wrked_above_2016_ByAge_Provinces = ProvinceAnalysis(df_Hrs_Wrked_above_2016_ByAge, pd, np, pp)
df_Hrs_Wrked_2016_ByAge_Provinces = ProvinceAnalysis(df_Hrs_Wrked_2016_ByAge, pd, np, pp)
df_Hrs_Wrked_2018_ByAge_Provinces = ProvinceAnalysis(df_Hrs_Wrked_2018_ByAge, pd, np, pp)
df_Hrs_Wrked_2020_ByAge_Provinces = ProvinceAnalysis(df_Hrs_Wrked_2020_ByAge, pd, np, pp)

# df_Hrs_Wrked_ByGender_Provinces = ProvinceAnalysis(df_Hrs_Wrked_ByGender, pd, np, pp)
# df_Hrs_Wrked_below_2016_ByGender_Provinces = ProvinceAnalysis(df_Hrs_Wrked_below_2016_ByGender, pd, np, pp)
df_Hrs_Wrked_above_2016_ByGender_Provinces = ProvinceAnalysis(df_Hrs_Wrked_above_2016_ByGender, pd, np, pp)
df_Hrs_Wrked_2016_ByGender_Provinces = ProvinceAnalysis(df_Hrs_Wrked_2016_ByGender, pd, np, pp)
df_Hrs_Wrked_2018_ByGender_Provinces = ProvinceAnalysis(df_Hrs_Wrked_2018_ByGender, pd, np, pp)
df_Hrs_Wrked_2020_ByGender_Provinces = ProvinceAnalysis(df_Hrs_Wrked_2020_ByGender, pd, np, pp)

# df_Hrs_Wrked_ByEducation_Provinces = ProvinceAnalysis(df_Hrs_Wrked_ByEducation, pd, np, pp)
# df_Hrs_Wrked_below_2016_ByEducation_Provinces = ProvinceAnalysis(df_Hrs_Wrked_below_2016_ByEducation, pd, np, pp)
# df_Hrs_Wrked_above_2016_ByEducation_Provinces = ProvinceAnalysis(df_Hrs_Wrked_above_2016_ByEducation, pd, np, pp)
df_Hrs_Wrked_2016_ByEducation_Provinces = ProvinceAnalysis(df_Hrs_Wrked_2016_ByEducation, pd, np, pp)
df_Hrs_Wrked_2018_ByEducation_Provinces = ProvinceAnalysis(df_Hrs_Wrked_2018_ByEducation, pd, np, pp)
df_Hrs_Wrked_2020_ByEducation_Provinces = ProvinceAnalysis(df_Hrs_Wrked_2020_ByEducation, pd, np, pp)

# df_Hrs_Wrked_ByImmigrant_Provinces = ProvinceAnalysis(df_Hrs_Wrked_ByImmigrant, pd, np, pp)
# df_Hrs_Wrked_below_2016_ByImmigrant_Provinces = ProvinceAnalysis(df_Hrs_Wrked_below_2016_ByImmigrant, pd, np, pp)
df_Hrs_Wrked_above_2016_ByImmigrant_Provinces = ProvinceAnalysis(df_Hrs_Wrked_above_2016_ByImmigrant, pd, np, pp)
df_Hrs_Wrked_2016_ByImmigrant_Provinces = ProvinceAnalysis(df_Hrs_Wrked_2016_ByImmigrant, pd, np, pp)
df_Hrs_Wrked_2018_ByImmigrant_Provinces = ProvinceAnalysis(df_Hrs_Wrked_2018_ByImmigrant, pd, np, pp)
df_Hrs_Wrked_2020_ByImmigrant_Provinces = ProvinceAnalysis(df_Hrs_Wrked_2020_ByImmigrant, pd, np, pp)

# df_Hrs_Wrked_ByIndigenous_Provinces = ProvinceAnalysis(df_Hrs_Wrked_ByIndigenous, pd, np, pp)
# df_Hrs_Wrked_below_2016_ByIndigenous_Provinces = ProvinceAnalysis(df_Hrs_Wrked_below_2016_ByIndigenous, pd, np, pp)
# df_Hrs_Wrked_above_2017_ByIndigenous_Provinces = ProvinceAnalysis(df_Hrs_Wrked_above_2017_ByIndigenous, pd, np, pp)
# # df_Hrs_Wrked_2017_ByIndigenous_Provinces = ProvinceAnalysis(df_Hrs_Wrked_2017_ByIndigenous, pd, np, pp)
# # df_Hrs_Wrked_2019_ByIndigenous_Provinces = ProvinceAnalysis(df_Hrs_Wrked_2019_ByIndigenous, pd, np, pp)
# df_Hrs_Wrked_2021_ByIndigenous_Provinces = ProvinceAnalysis(df_Hrs_Wrked_2021_ByIndigenous, pd, np, pp)


# %% [markdown]
# Filtered by provinces by "Number of jobs"

# %%
# By Number of jobs and salaries worked categories by provinces.

# df_NumOfJob_ByAge_Provinces = ProvinceAnalysis(df_NumOfJob_ByAge, pd, np, pp)
# df_NumOfJob_below_2016_ByAge_Provinces = ProvinceAnalysis(df_NumOfJob_below_2016_ByAge, pd, np, pp)
df_NumOfJob_above_2016_ByAge_Provinces = ProvinceAnalysis(df_NumOfJob_above_2016_ByAge, pd, np, pp)
df_NumOfJob_2016_ByAge_Provinces = ProvinceAnalysis(df_NumOfJob_2016_ByAge, pd, np, pp)
df_NumOfJob_2018_ByAge_Provinces = ProvinceAnalysis(df_NumOfJob_2018_ByAge, pd, np, pp)
df_NumOfJob_2020_ByAge_Provinces = ProvinceAnalysis(df_NumOfJob_2020_ByAge, pd, np, pp)

# df_NumOfJob_ByGender_Provinces = ProvinceAnalysis(df_NumOfJob_ByGender, pd, np, pp)
# df_NumOfJob_below_2016_ByGender_Provinces = ProvinceAnalysis(df_NumOfJob_below_2016_ByGender, pd, np, pp)
df_NumOfJob_above_2016_ByGender_Provinces = ProvinceAnalysis(df_NumOfJob_above_2016_ByGender, pd, np, pp)
df_NumOfJob_2016_ByGender_Provinces = ProvinceAnalysis(df_NumOfJob_2016_ByGender, pd, np, pp)
df_NumOfJob_2018_ByGender_Provinces = ProvinceAnalysis(df_NumOfJob_2018_ByGender, pd, np, pp)
df_NumOfJob_2020_ByGender_Provinces = ProvinceAnalysis(df_NumOfJob_2020_ByGender, pd, np, pp)

# df_NumOfJob_ByEducation_Provinces = ProvinceAnalysis(df_NumOfJob_ByEducation, pd, np, pp)
# df_NumOfJob_below_2016_ByEducation_Provinces = ProvinceAnalysis(df_NumOfJob_below_2016_ByEducation, pd, np, pp)
df_NumOfJob_above_2016_ByEducation_Provinces = ProvinceAnalysis(df_NumOfJob_above_2016_ByEducation, pd, np, pp)
df_NumOfJob_2016_ByEducation_Provinces = ProvinceAnalysis(df_NumOfJob_2016_ByEducation, pd, np, pp)
df_NumOfJob_2018_ByEducation_Provinces = ProvinceAnalysis(df_NumOfJob_2018_ByEducation, pd, np, pp)
df_NumOfJob_2020_ByEducation_Provinces = ProvinceAnalysis(df_NumOfJob_2020_ByEducation, pd, np, pp)

# df_NumOfJob_ByImmigrant_Provinces = ProvinceAnalysis(df_NumOfJob_ByImmigrant, pd, np, pp)
# df_NumOfJob_below_2016_ByImmigrant_Provinces = ProvinceAnalysis(df_NumOfJob_below_2016_ByImmigrant, pd, np, pp)
df_NumOfJob_above_2016_ByImmigrant_Provinces = ProvinceAnalysis(df_NumOfJob_above_2016_ByImmigrant, pd, np, pp)
df_NumOfJob_2016_ByImmigrant_Provinces = ProvinceAnalysis(df_NumOfJob_2016_ByImmigrant, pd, np, pp)
df_NumOfJob_2018_ByImmigrant_Provinces = ProvinceAnalysis(df_NumOfJob_2018_ByImmigrant, pd, np, pp)
df_NumOfJob_2020_ByImmigrant_Provinces = ProvinceAnalysis(df_NumOfJob_2020_ByImmigrant, pd, np, pp)

# # df_NumOfJob_ByIndigenous_Provinces = ProvinceAnalysis(df_NumOfJob_ByIndigenous, pd, np, pp)
# df_NumOfJob_below_2016_ByIndigenous_Provinces = ProvinceAnalysis(df_NumOfJob_below_2016_ByIndigenous, pd, np, pp)
# df_NumOfJob_above_2017_ByIndigenous_Provinces = ProvinceAnalysis(df_NumOfJob_above_2017_ByIndigenous, pd, np, pp)
# # df_NumOfJob_2017_ByIndigenous_Provinces = ProvinceAnalysis(df_NumOfJob_2017_ByIndigenous, pd, np, pp)
# # df_NumOfJob_2019_ByIndigenous_Provinces = ProvinceAnalysis(df_NumOfJob_2019_ByIndigenous, pd, np, pp)
# df_NumOfJob_2021_ByIndigenous_Provinces = ProvinceAnalysis(df_NumOfJob_2021_ByIndigenous, pd, np, pp)

# %% [markdown]
# Filted by provinces by "Wages and Salaries"

# %%
# By Wages and Salaries worked categories by provinces.

# df_WagesAndSalaries_ByAge_Provinces = ProvinceAnalysis(df_WagesAndSalaries_ByAge, pd, np, pp)
# df_WagesAndSalaries_below_2016_ByAge_Provinces = ProvinceAnalysis(df_WagesAndSalaries_below_2016_ByAge, pd, np, pp)
df_WagesAndSalaries_above_2016_ByAge_Provinces = ProvinceAnalysis(df_WagesAndSalaries_above_2016_ByAge, pd, np, pp)
df_WagesAndSalaries_2016_ByAge_Provinces = ProvinceAnalysis(df_WagesAndSalaries_2016_ByAge, pd, np, pp)
df_WagesAndSalaries_2018_ByAge_Provinces = ProvinceAnalysis(df_WagesAndSalaries_2018_ByAge, pd, np, pp)
df_WagesAndSalaries_2020_ByAge_Provinces = ProvinceAnalysis(df_WagesAndSalaries_2020_ByAge, pd, np, pp)

# df_WagesAndSalaries_ByGender_Provinces = ProvinceAnalysis(df_WagesAndSalaries_ByGender, pd, np, pp)
# df_WagesAndSalaries_below_2016_ByGender_Provinces = ProvinceAnalysis(df_WagesAndSalaries_below_2016_ByGender, pd, np, pp)
df_WagesAndSalaries_above_2016_ByGender_Provinces = ProvinceAnalysis(df_WagesAndSalaries_above_2016_ByGender, pd, np, pp)
df_WagesAndSalaries_2016_ByGender_Provinces = ProvinceAnalysis(df_WagesAndSalaries_2016_ByGender, pd, np, pp)
df_WagesAndSalaries_2018_ByGender_Provinces = ProvinceAnalysis(df_WagesAndSalaries_2018_ByGender, pd, np, pp)
df_WagesAndSalaries_2020_ByGender_Provinces = ProvinceAnalysis(df_WagesAndSalaries_2020_ByGender, pd, np, pp)

# df_WagesAndSalaries_ByEducation_Provinces = ProvinceAnalysis(df_WagesAndSalaries_ByEducation, pd, np, pp)
# df_WagesAndSalaries_below_2016_ByEducation_Provinces = ProvinceAnalysis(df_WagesAndSalaries_below_2016_ByEducation, pd, np, pp)
df_WagesAndSalaries_above_2016_ByEducation_Provinces = ProvinceAnalysis(df_WagesAndSalaries_above_2016_ByEducation, pd, np, pp)
df_WagesAndSalaries_2016_ByEducation_Provinces = ProvinceAnalysis(df_WagesAndSalaries_2016_ByEducation, pd, np, pp)
df_WagesAndSalaries_2018_ByEducation_Provinces = ProvinceAnalysis(df_WagesAndSalaries_2018_ByEducation, pd, np, pp)
df_WagesAndSalaries_2020_ByEducation_Provinces = ProvinceAnalysis(df_WagesAndSalaries_2020_ByEducation, pd, np, pp)

# df_WagesAndSalaries_ByImmigrant_Provinces = ProvinceAnalysis(df_WagesAndSalaries_ByImmigrant, pd, np, pp)
# df_WagesAndSalaries_below_2016_ByImmigrant_Provinces = ProvinceAnalysis(df_WagesAndSalaries_below_2016_ByImmigrant, pd, np, pp)
df_WagesAndSalaries_above_2016_ByImmigrant_Provinces = ProvinceAnalysis(df_WagesAndSalaries_above_2016_ByImmigrant, pd, np, pp)
df_WagesAndSalaries_2016_ByImmigrant_Provinces = ProvinceAnalysis(df_WagesAndSalaries_2016_ByImmigrant, pd, np, pp)
df_WagesAndSalaries_2018_ByImmigrant_Provinces = ProvinceAnalysis(df_WagesAndSalaries_2018_ByImmigrant, pd, np, pp)
df_WagesAndSalaries_2020_ByImmigrant_Provinces = ProvinceAnalysis(df_WagesAndSalaries_2020_ByImmigrant, pd, np, pp)

# df_WagesAndSalaries_ByIndigenous_Provinces = ProvinceAnalysis(df_WagesAndSalaries_ByIndigenous, pd, np, pp)
# df_WagesAndSalaries_below_2016_ByIndigenous_Provinces = ProvinceAnalysis(df_WagesAndSalaries_below_2016_ByIndigenous, pd, np, pp)
# df_WagesAndSalaries_above_2017_ByIndigenous_Provinces = ProvinceAnalysis(df_WagesAndSalaries_above_2017_ByIndigenous, pd, np, pp)
# # df_WagesAndSalaries_2017_ByIndigenous_Provinces = ProvinceAnalysis(df_WagesAndSalaries_2017_ByIndigenous, pd, np, pp)
# # df_WagesAndSalaries_2019_ByIndigenous_Provinces = ProvinceAnalysis(df_WagesAndSalaries_2019_ByIndigenous, pd, np, pp)
# df_WagesAndSalaries_2021_ByIndigenous_Provinces = ProvinceAnalysis(df_WagesAndSalaries_2021_ByIndigenous, pd, np, pp)

# %% [markdown]
# Filtering only Alberta.

# %% [markdown]
# Only finished "Average annual hours worked".

# %%
# # -- Alberta                     2193966.0   2031.450000   2695.836034  1080

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
# -- Alberta                     2193966.0   2031.450000   2695.836034  1080
ProCode = 0

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputAnalysis(ProCode)

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputAnalysis(ProCode)

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputAnalysis(ProCode)

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputAnalysis(ProCode)

# %% [markdown]
# Panda Profiling for Final Result for Alberta

# %%
ProCode = 0

df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputPandaProfiling(ProCode,0,2)
df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputPandaProfiling(ProCode,0,2)
df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputPandaProfiling(ProCode,0,2)
df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,2)

df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputPandaProfiling(ProCode,0,3)
df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputPandaProfiling(ProCode,0,3)
df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputPandaProfiling(ProCode,0,3)
df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,3)

df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputPandaProfiling(ProCode,0,4)
df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputPandaProfiling(ProCode,0,4)
df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputPandaProfiling(ProCode,0,4)
df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,4)

df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputPandaProfiling(ProCode,0,5)
df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputPandaProfiling(ProCode,0,5)
df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputPandaProfiling(ProCode,0,5)
df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,5)

# %% [markdown]
# Filtering only British Columbia.

# %% [markdown]
# Only finished "Average annual hours worked".

# %%
# -- British Columbia            2401296.0   2223.422222   2804.925187  1080

ProCode = 1

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputAnalysis(ProCode)

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputAnalysis(ProCode)

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputAnalysis(ProCode)

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputAnalysis(ProCode)

# %% [markdown]
# Panda Profiling for Final Result for BC

# %%
ProCode = 1

df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputPandaProfiling(ProCode,0,2)
df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputPandaProfiling(ProCode,0,2)
df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputPandaProfiling(ProCode,0,2)
df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,2)

df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputPandaProfiling(ProCode,0,3)
df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputPandaProfiling(ProCode,0,3)
df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputPandaProfiling(ProCode,0,3)
df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,3)

df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputPandaProfiling(ProCode,0,4)
df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputPandaProfiling(ProCode,0,4)
df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputPandaProfiling(ProCode,0,4)
df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,4)

df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputPandaProfiling(ProCode,0,5)
df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputPandaProfiling(ProCode,0,5)
df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputPandaProfiling(ProCode,0,5)
df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,5)

# %% [markdown]
# Filtering if "GEO" levelled as "Canada" ONLY.

# %% [markdown]
# Only finished "Average annual hours worked".

# %%
# -- Canada                     18252439.0  16900.406481  22232.852533  1080

ProCode = 2 # Canada

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputAnalysis(ProCode)

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputAnalysis(ProCode)

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputAnalysis(ProCode)

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputAnalysis(ProCode)

# %% [markdown]
# Panda Profiling for Final Result for GEO = Canada

# %%
ProCode = 2

df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputPandaProfiling(ProCode,0,2)
df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputPandaProfiling(ProCode,0,2)
df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputPandaProfiling(ProCode,0,2)
df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,2)

df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputPandaProfiling(ProCode,0,3)
df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputPandaProfiling(ProCode,0,3)
df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputPandaProfiling(ProCode,0,3)
df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,3)

df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputPandaProfiling(ProCode,0,4)
df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputPandaProfiling(ProCode,0,4)
df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputPandaProfiling(ProCode,0,4)
df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,4)

df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputPandaProfiling(ProCode,0,5)
df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputPandaProfiling(ProCode,0,5)
df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputPandaProfiling(ProCode,0,5)
df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,5)

# %% [markdown]
# Filtering only Manitoba.

# %% [markdown]
# Only finished "Average annual hours worked".

# %%
# -- Manitoba                     767802.0    710.927778    915.637659  1080

ProCode = 3

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputAnalysis(ProCode)

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputAnalysis(ProCode)

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputAnalysis(ProCode)

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputAnalysis(ProCode)

# %% [markdown]
# Panda Profiling for Final Result for Manitoba

# %%
ProCode = 3

df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputPandaProfiling(ProCode,0,2)
df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputPandaProfiling(ProCode,0,2)
df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputPandaProfiling(ProCode,0,2)
df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,2)

df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputPandaProfiling(ProCode,0,3)
df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputPandaProfiling(ProCode,0,3)
df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputPandaProfiling(ProCode,0,3)
df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,3)

df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputPandaProfiling(ProCode,0,4)
df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputPandaProfiling(ProCode,0,4)
df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputPandaProfiling(ProCode,0,4)
df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,4)

df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputPandaProfiling(ProCode,0,5)
df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputPandaProfiling(ProCode,0,5)
df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputPandaProfiling(ProCode,0,5)
df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,5)

# %% [markdown]
# Filtering only New Brunswick.

# %% [markdown]
# Only finished "Average annual hours worked".

# %%
# -- New Brunswick                359320.0    332.703704    530.962762  1080

ProCode = 4

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputAnalysis(ProCode)

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputAnalysis(ProCode)

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputAnalysis(ProCode)

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputAnalysis(ProCode)

# %% [markdown]
# Panda Profiling for Final Result for New Brunswick

# %%
ProCode = 4

df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputPandaProfiling(ProCode,0,2)
df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputPandaProfiling(ProCode,0,2)
df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputPandaProfiling(ProCode,0,2)
df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,2)

df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputPandaProfiling(ProCode,0,3)
df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputPandaProfiling(ProCode,0,3)
df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputPandaProfiling(ProCode,0,3)
df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,3)

df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputPandaProfiling(ProCode,0,4)
df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputPandaProfiling(ProCode,0,4)
df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputPandaProfiling(ProCode,0,4)
df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,4)

df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputPandaProfiling(ProCode,0,5)
df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputPandaProfiling(ProCode,0,5)
df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputPandaProfiling(ProCode,0,5)
df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,5)

# %% [markdown]
# Filtering only Newfoundland and Labrador.

# %% [markdown]
# Only finished "Average annual hours worked".

# %%
# -- Newfoundland and Labrador    315895.0    306.099806    482.634908  1032

ProCode = 5

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputAnalysis(ProCode)

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputAnalysis(ProCode)

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputAnalysis(ProCode)

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputAnalysis(ProCode)

# %% [markdown]
# Panda Profiling for Final Result for Newfoundland

# %%
ProCode = 5

df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputPandaProfiling(ProCode,0,2)
df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputPandaProfiling(ProCode,0,2)
df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputPandaProfiling(ProCode,0,2)
df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,2)

df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputPandaProfiling(ProCode,0,3)
df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputPandaProfiling(ProCode,0,3)
df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputPandaProfiling(ProCode,0,3)
df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,3)

df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputPandaProfiling(ProCode,0,4)
df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputPandaProfiling(ProCode,0,4)
df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputPandaProfiling(ProCode,0,4)
df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,4)

df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputPandaProfiling(ProCode,0,5)
df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputPandaProfiling(ProCode,0,5)
df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputPandaProfiling(ProCode,0,5)
df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,5)

# %% [markdown]
# Filtering only Northwest Territories.

# %% [markdown]
# Only finished "Average annual hours worked".

# %%
# -- Northwest Territories         42804.0     41.476744     51.817046  1032

ProCode = 6

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputAnalysis(ProCode)

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputAnalysis(ProCode)

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputAnalysis(ProCode)

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputAnalysis(ProCode)

# %% [markdown]
# Panda Profiling for Final Result for Northwest Territories

# %%
ProCode = 6

df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputPandaProfiling(ProCode,0,2)
df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputPandaProfiling(ProCode,0,2)
df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputPandaProfiling(ProCode,0,2)
df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,2)

df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputPandaProfiling(ProCode,0,3)
df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputPandaProfiling(ProCode,0,3)
df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputPandaProfiling(ProCode,0,3)
df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,3)

df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputPandaProfiling(ProCode,0,4)
df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputPandaProfiling(ProCode,0,4)
df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputPandaProfiling(ProCode,0,4)
df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,4)

df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputPandaProfiling(ProCode,0,5)
df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputPandaProfiling(ProCode,0,5)
df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputPandaProfiling(ProCode,0,5)
df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,5)

# %% [markdown]
# Filtering only Nova Scotia.

# %% [markdown]
# Only finished "Average annual hours worked".

# %%
# -- Nova Scotia                  531805.0    492.412037    757.119411  1080

ProCode = 7

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputAnalysis(ProCode)

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputAnalysis(ProCode)

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputAnalysis(ProCode)

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputAnalysis(ProCode)

# %% [markdown]
# Panda Profiling for Final Result for Nova Scotia

# %%
ProCode = 7

df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputPandaProfiling(ProCode,0,2)
df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputPandaProfiling(ProCode,0,2)
df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputPandaProfiling(ProCode,0,2)
df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,2)

df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputPandaProfiling(ProCode,0,3)
df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputPandaProfiling(ProCode,0,3)
df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputPandaProfiling(ProCode,0,3)
df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,3)

df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputPandaProfiling(ProCode,0,4)
df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputPandaProfiling(ProCode,0,4)
df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputPandaProfiling(ProCode,0,4)
df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,4)

df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputPandaProfiling(ProCode,0,5)
df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputPandaProfiling(ProCode,0,5)
df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputPandaProfiling(ProCode,0,5)
df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,5)

# %% [markdown]
# Filtering only Nunavut.

# %% [markdown]
# Only finished "Average annual hours worked".

# %%
# -- Nunavut                       14235.0     15.208333     14.752372   936

ProCode = 8

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputAnalysis(ProCode)

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputAnalysis(ProCode)

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputAnalysis(ProCode)

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputAnalysis(ProCode)

# %% [markdown]
# Panda Profiling for Final Result for Nunavut

# %%
ProCode = 8

df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputPandaProfiling(ProCode,0,2)
df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputPandaProfiling(ProCode,0,2)
df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputPandaProfiling(ProCode,0,2)
df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,2)

df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputPandaProfiling(ProCode,0,3)
df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputPandaProfiling(ProCode,0,3)
df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputPandaProfiling(ProCode,0,3)
df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,3)

df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputPandaProfiling(ProCode,0,4)
df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputPandaProfiling(ProCode,0,4)
df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputPandaProfiling(ProCode,0,4)
df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,4)

df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputPandaProfiling(ProCode,0,5)
df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputPandaProfiling(ProCode,0,5)
df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputPandaProfiling(ProCode,0,5)
df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,5)

# %% [markdown]
# Filtered by Ontario

# %% [markdown]
# Only finished "Average annual hours worked".

# %%
# -- Ontario                     6601634.0   6112.624074   7594.433779  1080

ProCode = 9

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputAnalysis(ProCode)

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputAnalysis(ProCode)

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputAnalysis(ProCode)

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputAnalysis(ProCode)

# %% [markdown]
# Panda Profiling for Final Result for Ontario

# %%
ProCode = 9

df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputPandaProfiling(ProCode,0,2)
df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputPandaProfiling(ProCode,0,2)
df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputPandaProfiling(ProCode,0,2)
df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,2)

df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputPandaProfiling(ProCode,0,3)
df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputPandaProfiling(ProCode,0,3)
df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputPandaProfiling(ProCode,0,3)
df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,3)

df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputPandaProfiling(ProCode,0,4)
df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputPandaProfiling(ProCode,0,4)
df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputPandaProfiling(ProCode,0,4)
df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,4)

df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputPandaProfiling(ProCode,0,5)
df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputPandaProfiling(ProCode,0,5)
df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputPandaProfiling(ProCode,0,5)
df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,5)

# %% [markdown]
# Filtering only Prince Edward Island.

# %% [markdown]
# Only finished "Average annual hours worked".

# %%
# -- Prince Edward Island          77931.0     75.514535    121.297367  1032

ProCode = 10

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputAnalysis(ProCode)

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputAnalysis(ProCode)

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputAnalysis(ProCode)

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputAnalysis(ProCode)

# %% [markdown]
# Panda Profiling for Final Result for Alberta

# %%
ProCode = 10

df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputPandaProfiling(ProCode,0,2)
df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputPandaProfiling(ProCode,0,2)
df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputPandaProfiling(ProCode,0,2)
df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,2)

df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputPandaProfiling(ProCode,0,3)
df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputPandaProfiling(ProCode,0,3)
df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputPandaProfiling(ProCode,0,3)
df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,3)

df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputPandaProfiling(ProCode,0,4)
df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputPandaProfiling(ProCode,0,4)
df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputPandaProfiling(ProCode,0,4)
df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,4)

df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputPandaProfiling(ProCode,0,5)
df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputPandaProfiling(ProCode,0,5)
df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputPandaProfiling(ProCode,0,5)
df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,5)

# %% [markdown]
# Filtering only Quebec.

# %% [markdown]
# Only finished "Average annual hours worked".

# %%
# -- Quebec                      4271657.0   3955.237963   5580.294544  1080

ProCode = 11

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputAnalysis(ProCode)

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputAnalysis(ProCode)

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputAnalysis(ProCode)

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputAnalysis(ProCode)

# %% [markdown]
# Panda Profiling for Final Result for Quebec

# %%
ProCode = 11

df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputPandaProfiling(ProCode,0,2)
df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputPandaProfiling(ProCode,0,2)
df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputPandaProfiling(ProCode,0,2)
df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,2)

df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputPandaProfiling(ProCode,0,3)
df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputPandaProfiling(ProCode,0,3)
df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputPandaProfiling(ProCode,0,3)
df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,3)

df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputPandaProfiling(ProCode,0,4)
df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputPandaProfiling(ProCode,0,4)
df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputPandaProfiling(ProCode,0,4)
df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,4)

df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputPandaProfiling(ProCode,0,5)
df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputPandaProfiling(ProCode,0,5)
df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputPandaProfiling(ProCode,0,5)
df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,5)

# %% [markdown]
# Filtering only Saskatchewan.

# %% [markdown]
# Only finished "Average annual hours worked".

# %%
# -- Saskatchewan                 650781.0    602.575000    876.896377  1080

ProCode = 12

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputAnalysis(ProCode)

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputAnalysis(ProCode)

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputAnalysis(ProCode)

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputAnalysis(ProCode)

# %% [markdown]
# Panda Profiling for Final Result for Saskatchewan

# %%
ProCode = 12

df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputPandaProfiling(ProCode,0,2)
df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputPandaProfiling(ProCode,0,2)
df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputPandaProfiling(ProCode,0,2)
df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,2)

df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputPandaProfiling(ProCode,0,3)
df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputPandaProfiling(ProCode,0,3)
df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputPandaProfiling(ProCode,0,3)
df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,3)

df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputPandaProfiling(ProCode,0,4)
df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputPandaProfiling(ProCode,0,4)
df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputPandaProfiling(ProCode,0,4)
df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,4)

df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputPandaProfiling(ProCode,0,5)
df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputPandaProfiling(ProCode,0,5)
df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputPandaProfiling(ProCode,0,5)
df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,5)

# %% [markdown]
# Filtering only Yukon.

# %% [markdown]
# Only finished "Average annual hours worked".

# %%
# -- Yukon                         16914.0     18.070513     20.188135   936

ProCode = 13

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputAnalysis(ProCode)

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputAnalysis(ProCode)

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputAnalysis(ProCode)

print("2016 - Overall")
df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputAnalysis(ProCode)
print("2016")
df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputAnalysis(ProCode)
print("2018")
df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputAnalysis(ProCode)
print("2020")
df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputList(ProCode, 20)
df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputAnalysis(ProCode)

# %% [markdown]
# Panda Profiling for Final Result for Yukon

# %%
ProCode = 13

df_AvgAnnHrsWrk_above_2016_ByAge_Provinces.outputPandaProfiling(ProCode,0,2)
df_AvgAnnHrsWrk_above_2016_ByGender_Provinces.outputPandaProfiling(ProCode,0,2)
df_AvgAnnHrsWrk_above_2016_ByEducation_Provinces.outputPandaProfiling(ProCode,0,2)
df_AvgAnnHrsWrk_above_2016_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,2)

df_AvgAnnHrsWrk_2016_ByAge_Provinces.outputPandaProfiling(ProCode,0,3)
df_AvgAnnHrsWrk_2016_ByGender_Provinces.outputPandaProfiling(ProCode,0,3)
df_AvgAnnHrsWrk_2016_ByEducation_Provinces.outputPandaProfiling(ProCode,0,3)
df_AvgAnnHrsWrk_2016_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,3)

df_AvgAnnHrsWrk_2018_ByAge_Provinces.outputPandaProfiling(ProCode,0,4)
df_AvgAnnHrsWrk_2018_ByGender_Provinces.outputPandaProfiling(ProCode,0,4)
df_AvgAnnHrsWrk_2018_ByEducation_Provinces.outputPandaProfiling(ProCode,0,4)
df_AvgAnnHrsWrk_2018_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,4)

df_AvgAnnHrsWrk_2020_ByAge_Provinces.outputPandaProfiling(ProCode,0,5)
df_AvgAnnHrsWrk_2020_ByGender_Provinces.outputPandaProfiling(ProCode,0,5)
df_AvgAnnHrsWrk_2020_ByEducation_Provinces.outputPandaProfiling(ProCode,0,5)
df_AvgAnnHrsWrk_2020_ByImmigrant_Provinces.outputPandaProfiling(ProCode,0,5)


