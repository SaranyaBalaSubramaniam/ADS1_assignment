
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''using function to change the values
   to percentage% '''
#function:
def func(pct, allvalues):
    return "{:.1f}%".format(pct)

#Variables:
#DataFrame of Population
df_pop = pd.read_csv("population_csv.csv")
df_pop["Value"] = df_pop["Value"]/100000000
data1 = df_pop[df_pop["Country Name"] == "Euro area"]
data2 = df_pop[df_pop["Country Name"] == "Arab World"]
data3 = df_pop[df_pop["Country Name"] == "East Asia & Pacific"]

#DataFrame of Death
df_DR = pd.read_csv('data_csv.csv', index_col=0)
df_DR = df_DR[df_DR["Year"]==2016]
df_DR = df_DR.loc[['India','Turkey', 'Germany', 'Japan', 'United Kingdom']]

#DataFrame of COVID
df_covid = pd.read_csv("Covid-aggregated_countries_csv.csv")
df_covid = df_covid[df_covid["Date"] == "2021-06-05"]
df_covid = df_covid[df_covid["Recovered"] >1000000]

df_covid.iloc[:,2:] = df_covid.iloc[:,2:]/1000000
df_covid = df_covid.sort_values(by = 'Confirmed', ascending =False)
df_covid = df_covid.iloc[:5,:]


#plottings:
#Line_plotting
plt.rcParams['font.size'] = 18
plt.figure(figsize = (12,7), layout = 'constrained')
plt.plot(data1['Year'], data1['Value'], label = "Euro Area", color = 'Red')
plt.plot(data2['Year'], data2['Value'], label = "Arab", color = 'Black')
plt.plot(data3['Year'], data3['Value'], label = "East Asia & Pacific", color = "DarkGreen")
plt.legend()

#customizing the line plot(labelling, Title given, Background color change, Added Grid)
plt.xlabel('Year')
plt.ylabel('Population in Billions')
plt.title('Population of Specific Regions from 1960 to 2020')
plt.rcParams.update({'axes.facecolor': 'LightGrey'})
plt.grid(True)

#Display the plot
plt.show()
plt.close()

#PieChart_plot
plt.figure(figsize =(14,12),layout = 'constrained')
plt.pie(df_DR["Value"], labels = df_DR.index,autopct = lambda pct: func(pct, df_DR["Value"]))
plt.title('Death Rate Analysis of year 2016')
plt.legend()
plt.show()
plt.close()

#Bar_plot
plt.figure(figsize = (10,7), layout = "constrained")

x = np.arange(len(df_covid['Country']))
width = .15

plt.bar(x - width / 3, df_covid["Confirmed"], width, label="Covid Confirmed Patients", color = 'Red')
plt.bar(x + width / 3, df_covid["Recovered"], width, label="Recovered Patients", color = 'Green')

plt.xticks(x, labels = df_covid["Country"])

plt.rcParams.update({'axes.facecolor': 'LightGrey'})
plt.xlabel('-----COUNTRIES-----')
plt.ylabel('Covid cases in Billions')
plt.title('COVID CASE - 2021')

plt.legend()
plt.show()
plt.close()

