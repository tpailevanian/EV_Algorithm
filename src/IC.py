from operator import attrgetter
from sim_constants import *
from vehicleLists import *
import vehicle

def updateIC( currentTime, lists ):


	for vehicle in lists.allVehicles:

		if vehicle.arrivalTime == currentTime:

			lists.chargeQueue.append( vehicle )

	# Reset currently charging list 
	lists.currentlyCharging = [] 

	for vehicle in lists.chargeQueue[:]:

		vehicle.updateLaxity( currentTime )

		if ((vehicle.chargeReq - vehicle.charged)  <= .00001 ) or \
		 	(vehicle.endTime == currentTime):

			remove_id = vehicle.id
			lists.doneCharging.append( vehicle )

			try:
				lists.chargeQueue = [item for item in lists.chargeQueue if item.id != remove_id ]
			except ValueError:
				index = -1

	# Initialize the demand for this time instance
	demand = 0

	for vehicle in lists.chargeQueue:
		rate = vehicle.maxRate
		demand += rate
		vehicle.chargeRate = rate
		vehicle.chargeVehicle( rate )

	lists.demand = demand * 3600

	# FOR DEBUG
	#print "length of the chargeQueue is %d" %len(lists.chargeQueue)
	#print "length of the currentlyCharging is %d" %len(lists.currentlyCharging)
	#print "length of the doneCharging is %d" %len(lists.doneCharging)

def averageLaxity( lists ):

	averageLaxity = 0

	for vehicle in lists.chargeQueue:
		averageLaxity += vehicle.laxity 

	return averageLaxity / len( lists.chargeQueue )


