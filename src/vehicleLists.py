
class VehicleLists:

    def __init__( self, algorithm ):

        # Vehicle Lists
        self.allVehicles = []  # contains all the vehicles that have 
                                        #   entered the charging station for the day
        self.chargeQueue = []  # contains all the vehicles that are charging 
                                        #   or need to charge
        self.currentlyCharging = []  # contains all the vehicles that 
                                                    #   are currently charging
        self.doneCharging = []    # contains all the vehicles that have 
                                            #   finished charging or have departed
        self.algorithm_type = algorithm # contains the algorithm used for the lists

        self.demand = 0         # Initialize power demand to 0



       
    