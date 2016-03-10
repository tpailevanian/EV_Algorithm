from csvUtil import CSV_Util
from LLF import *
from IC import *
from sim_constants import *
from vehicleLists import *
from simulationData import *
from simFuncs import *
import datetime
import os
import vehicle
import copy

# Create vehicle lists
llf_lists = VehicleLists( 'llf' )	# Lists for the LLF simulation
ic_lists = VehicleLists( 'ic' )	# Lists for the Instant Charging simulation
sim_data = SimulationData()		# List of simulation data

os.chdir("..")
cwd = os.getcwd()
data_path = cwd + '/data'

# Get back to src directory
os.chdir(cwd + '/src')

# Create simulation clock
timer = datetime.datetime.strptime('%s %s' % ( simulation_start_date, simulation_start_time ), \
													'%m/%d/%y %H:%M')
timer_end = datetime.datetime.strptime('%s %s' % ( simulation_end_date, simulation_end_time ), \
													'%m/%d/%y %H:%M')

# Setup CSV utility
data = CSV_Util( data_path, data_filename)

# Add vehicles to the simulation
for i in range( numVehicles ):

	newVehicle = data.addVehicle()
	newVehicle.id = i 
	llf_lists.allVehicles.append( copy.deepcopy( newVehicle ))
	ic_lists.allVehicles.append( copy.deepcopy( newVehicle ))

# Simulation takes place in while loop
while (timer_end - timer).total_seconds() > 0.0:
	
	updateIC( timer, ic_lists )
	updateLLF( timer, llf_lists )
	
	sim_data.time.append( timer )
	sim_data.llf_demand.append( llf_lists.demand )
	sim_data.llf_avg_laxity.append( averageLaxity(llf_lists) )
	sim_data.ic_demand.append( ic_lists.demand )
	sim_data.ic_avg_laxity.append( averageLaxity(ic_lists) )
	
	
	
	timer = timer + datetime.timedelta( 0, 60 )
	print timer.strftime("Date: %m/%d/%y Time: %H:%M")

# FOR DEBUG
#print len(llf_lists.allVehicles)
#print len(llf_lists.doneCharging)
#print len(ic_lists.allVehicles)
#print len(ic_lists.doneCharging)

for vehicle in range( numVehicles ):

	#data.exportVehicletoCSV( llf_lists.allVehicles[ vehicle ] )
	data.exportVehicletoCSV( llf_lists.doneCharging[ vehicle ] )
	#data.exportVehicletoCSV( ic_lists.allVehicles[ vehicle ] )
	data.exportVehicletoCSV( ic_lists.doneCharging[ vehicle ] )

# Finished with simulation so log data and generate plots
data.exportSimtoCSV( sim_data )
plotPower( sim_data, data.getLogPath() )
plotLaxity( sim_data, data.getLogPath() )




