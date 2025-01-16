# Create a program that analyses temperature data collected from multiple weather stations in Australia. 
# The data is stored in multiple CSV files under a temperatures folder
# with each file representing data from one year.

import pandas as pd
import sys
print("Welcome to the WEATHER STATION Data Analyser!")
folderloc = str("C:/Users/User/Documents/temperature_data/")



while True:
    b = str(input("Enter your local address of the temperature_data folder in this format C:/Users/User/Documents/temperature_data/ \n(**must use forward slashes) "))
    if b == "":
        break
    else: 
        folderloc = b  
        try:
            df = pd.read_csv(f"{folderloc}stations_group_1986.csv")
            break
        except FileNotFoundError:
            print('!!Invalid data folder location, please rectify!!')
        

print('\n***Part A: compute seasonal mean temperatures:')
#Create data frame objects for data computation with indexed column
yearsdf = pd.DataFrame({'years': pd.Series(range(1986,2006))})
#Add extra columns for storing seasona mean temp values
l = len(range(1986,2006))
yearsdf['summer'] = [0]*l
yearsdf['autumn'] = [0]*l
yearsdf['winter'] = [0]*l
yearsdf['spring'] = [0]*l
#Extract temp data from csv files
for years in range(1986, 2006):
    df = pd.read_csv(f"{folderloc}stations_group_{years}.csv")
    #identify row index
    yr = yearsdf[yearsdf['years'] == years].index 
    #use inbuilt .mean() function for computation
    yearsdf.iloc[yr, 2] = df[['March', 'April', 'May']].mean().mean()
    yearsdf.iloc[yr, 3] = df[['June', 'July', 'August']].mean().mean()
    yearsdf.iloc[yr, 4] = df[['September', 'October', 'November']].mean().mean()
    #Note extra difficulties with summer season as it bridges consecutive years
    if years == 1986:
        yearsdf.iloc[yr, 1] = df[['January', 'February']].mean().mean()
    else:
        lastdf = pd.read_csv(f"{folderloc}stations_group_{years-1}.csv")
        dec_mean = lastdf['December'].mean() #december values from previous year data
        jan_mean = df['January'].mean()
        feb_mean = df['February'].mean()
        summer = pd.Series([dec_mean, jan_mean, feb_mean])
        yearsdf.iloc[yr, 1] = summer.mean()
print(yearsdf)
#Compile temp data to string
avtempdata = f"The following seasonal average temperatures across all years from all reported stations in DegreesC\n"
avtempdata = avtempdata + f"Summer = {round(yearsdf['summer'].mean(), 2)} Autumn = {round(yearsdf['autumn'].mean(),2)} Winter = {round(yearsdf['winter'].mean(),2)} Spring = {round(yearsdf['spring'].mean(),2)}"
print(avtempdata)
#Save mean seasonal temps to .txt file
with open(f"{folderloc}average_temp.txt", 'w') as file:
    file.write(avtempdata)
print("Data written to average_temp.txt")
#hold program till user 
while True:
    d = input("Press Enter to continue to Part B...")
    if d=="":
            break



print('\n***Part B: compute station with largest temperature range:')
#Create list object with station names for calculated data computation
stationdf = pd.DataFrame({'Station': df['STATION_NAME']})  #Indexes the column
#Add extra collumns for storing highest and lowest temp values
stationdf['highest_temp'] = [0]*112
stationdf['lowest_temp'] = [100]*112
#Create range object for column indexes
import calendar
months = list(calendar.month_name)[1:] 
#Extract temp data from csv files
for years in range(1986, 2006):
    df = pd.read_csv(f"{folderloc}stations_group_{years}.csv")
    #compute each stations yearly max and min, and store if higher or lower than existing max or min
    for station in range(0, 112):
        if (df.iloc[station, 4:16].max()) > (stationdf.iloc[station, 1]):
            stationdf.iloc[station, 1] = (df.iloc[station, 4:16].max())
        if (df.iloc[station, 4:16].min()) < (stationdf.iloc[station, 2]):
            stationdf.iloc[station, 2] = (df.iloc[station, 4:16].min()) 
#Add additional column for temp range vaflues
stationdf['temp_range'] = [0]*112
#Compute the temprange at each station and store
for station in range(0, 112):
    stationdf.iloc[station, 3] = round(stationdf.iloc[station, 1]-stationdf.iloc[station, 2], 2) #range = highest - lowest
print(stationdf)
#Find the largest temprange and its station of occurence
maxtemprange = stationdf['temp_range'].max()
maxtempstation_indexes = stationdf[stationdf['temp_range'] == maxtemprange].index.tolist()
maxtempstation = stationdf.iloc[maxtempstation_indexes[0],0]
#Compile data to string
maxtemprangedata = f"The the largest temperature range seen is {maxtemprange} degreesC, at {maxtempstation} station"
print(maxtemprangedata)
#Save highest and lowest temps to .txt file
with open(f"{folderloc}largest_temp_range_station.txt", 'w') as file:
    file.write(maxtemprangedata)

#pause for user
while True:
    c = input("Press Enter to continue to Part C...")
    if c=="":
            break 



print('\n***PartC: compute warmest and coolest stations, based on the mean of yearly mean temperatures')
#Create object with station names for calculated data storage
df = pd.read_csv(f"{folderloc}stations_group_1986.csv")
stationdf = pd.DataFrame({'Station': df['STATION_NAME']})  #Indexes the column
#Extract year averages from the csv files
for year in range(1986, 2006):
    df = pd.read_csv(f"{folderloc}stations_group_{year}.csv")
    yr_av_list = []
    for station in range(0, 112):
        station_year_av = round((df.iloc[station, 4:16].mean()), 2)
        yr_av_list.append(station_year_av)
    #Append year averages as new columns in dataframe   
    stationdf[str(year)] = yr_av_list
#Compute the all time averge for each station
alltime_av_list = []
for station in range (0,112):
    station_alltime_av = round(stationdf.iloc[station,1:len(range(1986,2006))].mean(), 2)
    alltime_av_list.append(station_alltime_av) 
#Append all time averages as new column in dataframe
stationdf['alltimeAv'] = alltime_av_list
print(stationdf)
#Compute warmest and coolest values
warmest_av_temp = stationdf['alltimeAv'].max()
coolest_av_temp = stationdf['alltimeAv'].min()
#Compute which stations these occured at 
max_indexes = stationdf[stationdf['alltimeAv'] == warmest_av_temp].index.tolist()
min_indexes = stationdf[stationdf['alltimeAv'] == coolest_av_temp].index.tolist()
#Saved data to to warmest&coolest.txt file. Note the for loops required incase of multiple stations with same av temps
with open(f"{folderloc}warmest_and_coolest_station.txt", 'w') as file:
    for i in range(0,len(max_indexes)):
        warmesttempstation = stationdf.iloc[max_indexes[i],0]
        #Compile data to string
        if i ==0:
            warmstationdata = f"The warmest all time Station average temperature is {warmest_av_temp} degreesC, at {warmesttempstation} station"
        else:
            warmstationdata = f" and at {warmesttempstation}"
        file.write(warmstationdata)
    for j in range(0,len(min_indexes)):
        coolesttempstation = stationdf.iloc[min_indexes[j],0]
        #Compile data to string
        if j ==0:
            coolstationdata = f"\nThe coolest all time Station average temperature is {coolest_av_temp} degreesC, at {coolesttempstation} station"
        else:
            coolstationdata = f" and at {coolesttempstation}"
        file.write(coolstationdata)
print(warmstationdata)
print(coolstationdata)      
print("Data written to warmest_and_coolest_station.txt")

while True:
    c = input("Press Enter to exit...")
    if c=="":
            sys.exit()