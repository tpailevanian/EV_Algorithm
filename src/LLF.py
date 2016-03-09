from operator import attrgetter
from llf_constants import *
from vehicleLists import *
import vehicle

def updateLLF( currentTime, lists ):


	for vehicle in lists.allVehicles:

		if vehicle.arrivalTime == currentTime:
			lists.chargeQueue.append( vehicle )

	if lists.chargeQueue is not None:
		lists.chargeQueue = sorted(lists.chargeQueue, key=attrgetter('laxity'))
	
	demand = 0

	# Reset currently charging list 
	lists.currentlyCharging = [] 

	for vehicle in lists.chargeQueue[:]:

		vehicle.updateLaxity( currentTime )

		#if ((vehicle.chargeReq - vehicle.charged)  <= .00001 ) or \
		if 	(vehicle.endTime == currentTime):

			remove_id = vehicle.id
			lists.doneCharging.append( vehicle )

			try:
				lists.chargeQueue = [item for item in lists.chargeQueue if item.id != remove_id ]
			except ValueError:
				index = -1
	
	for vehicle in lists.chargeQueue:	
		if ( vehicle.maxRate + demand ) <= ( float(max_pwr) / 3600.0 ):
			demand = vehicle.maxRate + demand
			lists.currentlyCharging.append( vehicle )
			vehicle.chargeRate = vehicle.maxRate

	for vehicle in lists.currentlyCharging:
		vehicle.chargeVehicle( vehicle.maxRate )

	print "length of the chargeQueue is %d" %len(lists.chargeQueue)
	print "length of the currentlyCharging is %d" %len(lists.currentlyCharging)
	print "length of the doneCharging is %d" %len(lists.doneCharging)
