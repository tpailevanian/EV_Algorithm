from csvUtil import CSV_Util
from llf_constants import *
import datetime
import os
import vehicle

# Create lists for keeping track of EVs
allVehicles = []		# contains all the vehicles that have entered the charging station for the day
chargeQueue = [] 		# contains all the vehicles that are charging or need to charge
currentlyCharging = []	# contains all the vehicles that are currently charging
doneCharging = [] 		# contains all the vehicles that have finished charging or have departed

os.chdir("..")
cwd = os.getcwd()
data_path = cwd + '/data'

# Get back to src directory
os.chdir(cwd + '/src')

data_filename = 'SampleData0.csv'

# Create simulation clock
timer = datetime.datetime.strptime('%s %s' % ( simulation_start_date, simulation_start_time ), \
													'%m/%d/%y %H:%M')
timer_end = datetime.datetime.strptime('%s %s' % ( simulation_end_date, simulation_end_time ), \
													'%m/%d/%y %H:%M')

# Setup CSV utility
csv = CSV_Util( data_path, data_filename)

# Add vehicles to the simulation
for i in range( numVehicles ):

	newVehicle = csv.addVehicle()
	allVehicles.append( newVehicle )


# Simulation takes place in while loop
while (timer_end - timer).total_seconds() > 0.0:
	

	timer = timer + datetime.timedelta(0,60)
	print timer.strftime("Date: %m/%d/%y Time: %H:%M")


for vehicle in range( numVehicles):

	csv.exportVehicletoCSV( allVehicles[vehicle] )