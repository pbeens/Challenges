'''
Time To Wake Up
https://github.com/pbeens/ICS-Computer-Studies/blob/master/Challenges/Time%20to%20Wake%20Up.pdf
'''

# Global Vars
goodData = []
months = []
monthly_avg_times = []


# Read in data file
def readData():
    f = open('Time To Wake Up.txt', 'r')
    lines = f.readlines()
    # only keep the lines with hours of 05, 06, 07
    for line in lines:
        hour = getHour(line)
        if hour in ['05', '06', '07']:
            goodData.append(line.strip())


# get all the months and put in the global months list
def getMonths():
    for line in goodData:
        month = line.split()[0]
        if month not in months:
            months.append(month)


# extract the hour from the line
def getHour(line):
    return line.strip().split()[4].split(':')[0]


# extract the minutes from the line
def getMinutes(line):
    return line.strip().split()[4].split(':')[1][:2]


# convert the decimal time format to hh:mm, with leading zero, if necessary
def tidyTime(t):
    # m = minutes, h = hours
    m = str(int((t % int(t)) * 60))
    if len(m) < 2:
        m = "0" + m
    if int(t) < 10:
        h = "0" + str(int(t)) + ":" + m
    else:
        h = str(int(t)) + ":" + m
    return h


# Program starts here
readData()
getMonths()

# iterate through each month, calculating average and printing
for month in months:
    # vars used for determining monthly averages
    numMonths = 0
    hoursSum = 0
    # calculate monthly average for each month
    for line in goodData:
        if str(line).startswith(month):
            numMonths += 1
            hoursSum += int(getHour(line))
            hoursSum += int(getMinutes(line)) / 60
    avgTime = round((hoursSum / numMonths), 2)
    # save the average time to find min and max later
    monthly_avg_times.append(float(avgTime))
    # create the dot leader to be used in the output
    dots = (17 - len(month)) * '.'
    # print the month data
    print(month + dots + tidyTime(avgTime) + 'AM')

# print the min and max months
min_month_index = monthly_avg_times.index(min(monthly_avg_times))
max_month_index = monthly_avg_times.index(max(monthly_avg_times))
print('Earliest month...' + str(months[min_month_index]))
print('Latest month.....' + str(months[max_month_index]))
