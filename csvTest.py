import csv
import os
import datetime


f = open('SampleData0.csv', 'rU')
sampleData = csv.reader(f, delimiter=',', quotechar='\n')

EV_Data = []

parameters = next(sampleData)

for row in sampleData:
	start_time = datetime.datetime.strptime(row[1], "%m/%d/%y %H:%M")
	duration = datetime.datetime.strptime(row[5], '%H:%M:%S')
	charge_time = datetime.datetime.strptime(row[6], '%H:%M:%S')
	energy_needed = float(row[7])

	#print start_time
	#print duration
	#print charge_time
	EV_Data.append([start_time, duration.time(), charge_time.time(), energy_needed])

#print EV_Data[0]
#print EV_Data[1]

path = os.getcwd()
logPath = path + '/Logs'


os.chdir(logPath)


filename = datetime.datetime.now().strftime('%Y.%m.%d_%H.%M_LOG.csv')

logfile = open(filename, 'w')
logwriter = csv.writer(logfile, delimiter=',', quotechar='\n')

logwriter.writerow(EV_Data[0])
logwriter.writerow(EV_Data[1])

os.chdir(path)


f.close()
logfile.close()


