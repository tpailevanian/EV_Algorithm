from csvUtil import CSV_Util
from LLF import *
from llf_constants import *
import datetime
import os
import vehicle
from vehicleLists import *

# Create vehicle lists
lists = VehicleLists()

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
	newVehicle.id = i 
	lists.allVehicles.append( newVehicle )

# Simulation takes place in while loop
while (timer_end - timer).total_seconds() > 0.0:
	
	updateLLF( timer, lists)

	timer = timer + datetime.timedelta( 0, sim_time_delta * 60 )
	print timer.strftime("Date: %m/%d/%y Time: %H:%M")

for vehicle in range( numVehicles):

	#csv.exportVehicletoCSV( lists.allVehicles[ vehicle ] )
	csv.exportVehicletoCSV( lists.doneCharging[ vehicle ] )



