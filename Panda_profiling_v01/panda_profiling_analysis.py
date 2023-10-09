# Panda profiling file

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import ydata_profiling as pp                # panda_profiling repo renamed into ydata_profiling
from ydata_profiling import ProfileReport   # panda_profiling repo renamed into ydata_profiling
import seaborn as sns
import warnings
import os


warnings.filterwarnings('ignore')

df = pd.read_csv('36100651.csv') # Importing csv files

print(df.info())
print(df.head(10))
print(df.describe())

pp = ProfileReport(df)
pp_df = pp.to_html()

f = open("df_NoMod.html", "a")  # Expert into html file without modifying any columns in dataset.
f.write(pp_df)
f.close()

# Removing unnecessary columns that does not required for the analysis.
df_sorted = df[['REF_DATE','GEO','Sector','Characteristics','Indicators','UOM','SCALAR_FACTOR','VALUE']]
print(df_sorted.head(20))

print(df_sorted.info())
print(df_sorted.describe())

pp_sorted = ProfileReport(df_sorted)
pp_df_sorted = pp_sorted.to_html()

f = open("df_Sorted.html", "a") # Expert modifying data into html file.
f.write(pp_df_sorted)
f.close()

# Source used to code the file. #
# https://www.w3schools.com/python/python_file_write.asp
# https://community.incorta.com/t5/data-schemas-knowledgebase/generate-profile-reports-using-pandas-profiling-package-within/ta-p/1436
# https://www.analyticsvidhya.com/blog/2021/06/generate-reports-using-pandas-profiling-deploy-using-streamlit/
# https://www.kaggle.com/code/frtgnn/simple-profiling-eda-using-pandas-profiling
# https://www.geeksforgeeks.org/pandas-profiling-in-python/
