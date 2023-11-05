# non-profit-organization

# Process of this analysis
Export csv file into the big dataset.
Filtered some columns/attributes and removed null values that are founded.
Division into different datasets based on the Indicators (There's should be seven datasets)
Division into four different datasets based on the year. Contains three years worth of data (2010-2012, 2013-2015, 2016-2018, 2019-2021)
Division into four different characteristics into four dataasets.
Division based on the GEO, provinces.

# Variable names involve during the analysis

df - Whole dataset without any filtering or division
df_sorted - Whole dataset with any filtering like removing non-important attributes.
df_sorted_na - Whole dataset with removal of the null values inside the dataset.

Division of into new dataset based on Indicator
df_AvgAnnHrsWrk     - Average annual hours worked
df_AvgAnnWages      - Average annual wages and salaries
df_AvgHrsWages      - Average hourly wage
df_AvgWeekHrsWrked  - Average weekly hours worked
df_Hrs_Wrked        - Hours Worked
df_NumOfJob         - Number of jobs
df_WagesAndSalaries - Wages and Salaries

Division of into new datasset based on the GEO/year
df_AvgAnnHrsWrk_2010 -     - Average annual hours worked in 2010
df_AvgAnnHrsWrk_2013       - Average annual hours worked in 2013
df_AvgAnnHrsWrk_2016       - Average annual hours worked in 2016
df_AvgAnnHrsWrk_2019       - Average annual hours worked in 2019
- Not being used anymore
df_AvgAnnHrsWrk_below_2016 - Average annual hours worked below 2016
df_AvgAnnHrsWrk_above_2017 - Average annual hours worked above 2017

Division of into new dataset based on the group of Characteristics
df_WagesAndSalaries_201x_ByAge          - Wages and Salaries in 201x By Age
df_WagesAndSalaries_201x_ByGender       - Wages and Salaries in 201x By Gender Group
df_WagesAndSalaries_201x_ByEducation    - Wages and Salaries in 201x By Education level
df_WagesAndSalaries_201x_ByImmigrant    - Wages and Salaries in 201x By Immigrant level
df_WagesAndSalaries_201x_ByIndigenous   - Wages and Salaries in 201x By Indigenous status

Division of into new dataset based on the provinces
df_AvgAnnHrsWrk_201x_ByAge_Provinces        - Average annual hours worked in 2010 by age group grouped by provinces
df_AvgAnnHrsWrk_201x_ByGender_Provinces     - Average annual hours worked in 2010 by gender grouped by provinces
df_AvgAnnHrsWrk_201x_ByEducation_Provinces  - Average annual hours worked in 2010 by education level grouped by provinces
df_AvgAnnHrsWrk_201x_ByImmigrant_Provinces  -- Average annual hours worked in 2010 by immigrant status  grouped by provinces
df_AvgAnnHrsWrk_201x_ByIndigenous_Provinces - Average annual hours worked in 2010 by indigenous status grouped by provinces

ProvinceAnalysis(df_AvgAnnHrsWrk_201x_ByAge, pd, np, pp) - Create new object using ProvinceAnalysis using datasets and other necessary part.
self.df = Dataset, the dataset that import
self.provinces = array of provinces
self.indicators = array of indicators
self.characteristics = array of characteristics 
self.year = array of years being analysis
self.dfProvinces = array of analysis based of division by provinces, do analysis from the df Dataset

Province [0-13]:
['Alberta', 'BC', 'GEO = Canada' , 'Manitoba' , 'New Brunswick', 'Newfoundland', 'Northwest Territories' , 'Nova Scotia' , 'Nunavut', 'Ontario' , 'PEI', 'Quebec', 'Saskatchewan', 'Yukon']
outputAnalysis(province_id) - Output detail analysis including sum, mean, and skewness.
outputAnalysisSimple(province_id) - Summarized the output details.
outputList(province_id, num) - Output first "num" amount of dataset.
outputPandaProfiling(province_id) - Do Panda profiling for specific provinces in specific year.

OutputProvinceAnalysis(df_AvgAnnHrsWrk_201x_ByAge_Provinces, ProCode, "201x", pd, np, pp) - Create new object using ProvinceAnalysis using dataset and other necessary part.
ProCode is code for the provinces mentions above.
"201x" here is the year of the analysis.
self.df_output - dataset that are analyzing
self.ProCode - province to analysis (in numeric code)
self.YearOutput - year that was analyized (more for panda-profiling)
OutputResult(self) - Display the result that was analyzed.
OutputPandaProfiling(self) - Do Panda Analysis in specific provines
# Contents in this pages
Data_Anlaysis_x - Contain last modified work. Last one is Data_Analysis_v07.
36100651-eng.zip - Contain original dataset employment of non-profit organizations.
data_analysis.ipynb/data_analysis.py - contain technical report in Jupiter Report / Python file.
data_analysis.pdf - contain output of technical report.
