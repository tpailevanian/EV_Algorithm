import math

class Vehicle:

    def __init__( self, arrivalTime, endTime, chargeReq, maxRate ):

        # Make sure we dont set out of range parameters

        # Vehicle parameters
        self.arrivalTime        =       arrivalTime
        self.endTime            =       endTime
        self.chargeReq          =       chargeReq
        self.maxRate            =       maxRate
        self.chargeRate         =       None
        self.charged            =       0 

        self.id                 =       None # program will set ID upon initialization

        # Calculated parameters
                                        # want to use one minutes rather than seconds
        self.duration           =       ( self.endTime - self.arrivalTime ).total_seconds() / 60.0 

                                        # assuming charge rate is in charge/second
                                        # chargeTimeNeeded is in minutes  
        self.chargeTimeNeeded   =       math.ceil( float(self.chargeReq) / (60.0 * self.maxRate) )  
                                          
        self.looseTime          =       self.duration - self.chargeTimeNeeded
        self.laxity             =       self.looseTime / self.duration

       
    # update vehicle laxity 
    def updateLaxity( self, currentTime ):
        timeLeft =  self.duration - (( currentTime - arrivalTime ).total_seconds() / 60 )
        
        self.chargeTimeNeeded   =       math.ceil(( float(self.chargeReq)- float(self.charged)) / (60.0 * self.maxRate) )  
                                          
        self.looseTime          =       timeLeft - self.chargeTimeNeeded
        self.laxity             =       self.looseTime / timeLeft

        # in case time ends up, we can't divide by 0
        if totalTime == 0:
            self.laxity = 1
        else:
            self.laxity =  looseTime / totalTime

            


