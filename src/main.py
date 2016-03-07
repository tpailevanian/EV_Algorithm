from csvUtil import CSV_Util
import datetime
import math
import os
import vehicle

VehicleList = []
numVehicles = 9

os.chdir("..")
cwd = os.getcwd()
data_path = cwd + '/data'

# Get back to src directory
os.chdir(cwd + '/src')




data_filename = 'SampleData0.csv'

csv = CSV_Util( data_path, data_filename)

for i in range(numVehicles):

	newVehicle = csv.addVehicle()
	VehicleList.append( newVehicle )

for vehicle in range(numVehicles):

	csv.exportVehicletoCSV( VehicleList[vehicle] )