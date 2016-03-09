import math

class Vehicle:

    def __init__( self, arrivalTime, endTime, chargeReq, maxRate ):

        # Make sure we dont set out of range parameters

        # Vehicle parameters
        self.arrivalTime        =       arrivalTime
        self.endTime            =       endTime
        self.chargeReq          =       chargeReq
        self.maxRate            =       maxRate
        self.chargeRate         =       0
        self.charged            =       0 

        self.id                 =       None # program will set ID upon initialization

        # Calculated parameters
                                        # want to use one minutes rather than seconds
        self.duration           =       ( self.endTime - self.arrivalTime ).total_seconds() / 60.0 

                                        # assuming charge rate is in kWh/second
                                        # chargeTimeNeeded is in minutes  
        self.chargeTimeNeeded   =       math.ceil( float(self.chargeReq) / (60.0 * self.maxRate) )  
                                          
        self.looseTime          =       self.duration - self.chargeTimeNeeded
        self.laxity             =       self.looseTime / self.duration

       
    # update vehicle laxity 
    def updateLaxity( self, currentTime ):
        timeLeft =  self.duration - (( currentTime - self.arrivalTime ).total_seconds() / 60.0 )
        
        self.chargeTimeNeeded   =       math.ceil(( float(self.chargeReq)- float(self.charged)) / (60.0 * self.maxRate) )  
                                          
        self.looseTime          =       timeLeft - self.chargeTimeNeeded

        # Check for dividing by zero 
        if timeLeft == 0 and self.chargeTimeNeeded > 0:
            pass    #do nothing, just keep previous laxity value
        
        elif timeLeft == 0 and self.chargeTimeNeeded == 0:
            self.laxity         =       0
        
        else:
            self.laxity         =       self.looseTime / timeLeft

    def chargeVehicle( self, rate ):

        if (self.chargeReq - self.charged) <= ( 60.0 * rate ):
                self.charged = self.chargeReq
        else:
            self.charged += ( 60.0 * rate )




