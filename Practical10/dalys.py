#general function: to read the DALYs data from a csv file and perform some operations on it
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#change the directory
os.chdir("C:/cygwin64/home/Stat9/IBI1_2024-2025/IBI1_2024-25/Practical10")
#read the given file
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
#showing the third column for the first 10 rows
print(dalys_data.iloc[0:10,2])
#state what was the 10th year with DALYs data recorded in Afghanistan
print("The 10th year with DALYs data recorded in Afghanistan is: ", dalys_data.iloc[9,2])
#creat a Boolean for those data which year is 1990
Column=dalys_data["Year"]==1990
#use this Boolean to get the DALYs we want
print(dalys_data.loc[Column,"DALYs"])

#find the DALYs data for the United Kingdom and France
#and store the data in two variables:DALYs and Year
uk = dalys_data.loc[dalys_data.Entity=="United Kingdom", ["DALYs", "Year"]]
fr = dalys_data.loc[dalys_data.Entity=="France", ["DALYs", "Year"]]
#calculate the mean of DALYs for the United Kingdom and France
uk_mean = uk["DALYs"].mean()
fr_mean = fr["DALYs"].mean()
#compare the mean of DALYs for the United Kingdom and France
if uk_mean > fr_mean:
    print("The United Kingdom has a higher mean of DALYs.")
elif uk_mean < fr_mean:
    print("France has a higher mean of DALYs.")
#plot the DALYs data for the United Kingdom
plt.plot(uk.Year, uk.DALYs, 'b+')
plt.show()

