import vehicle

allVehicles = []

def updateLLF():

	chargeQueue = []
	doneCharging = []
	currentlyCharging = []


	for vehicle in currentlyCharging:

		# add charge to the vehicle
        if vehicle is not None:
            vehicle.currentCharge += ( vehicle.chargeRate ) * 60.0 # charge rate is in charge/second

    for i, vehicle in enumerate( allVehicles ):
    	if vehicle is not None:

    		if vehicle.currentCharge >= chargeNeeded:

    			allVehicles.stopCharging(i) 	# vehicle is done charging so stop
    												#	stop including it in the calculation
    			chargeQueue.remove(vehicle)

    			doneCharging.append[vehicle.id]	# keep track of vehicles that are done charging
			
			# Make sure the station does not draw too much power
			totChrgRate = 0
			for vehicle in chargingQueue:
				if vehicle.chargeRate + totChrgRate < totPwr:
					currentlyCharging.append[(vehicle.id, vehicle.laxity)]
					totChrgRate += vehicle.chargeRate

def onArrival(vehicle):

	allVehicles.append[vehicle]
	vehicle.id = length(allVehicles)

	sorted(chargingQueue, )

