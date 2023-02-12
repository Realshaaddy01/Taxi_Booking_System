class getset_Trip:
    def __init__(self, TID=0, Payment=None, Pickup=None, Dropoff=None, Time=None, Date=None, CID=None, DID=None,booking_status=None):
        self.TID = TID
        self.Payment = Payment
        self.Pickup = Pickup
        self.Dropoff = Dropoff
        self.Time = Time
        self.Date = Date
        self.CID=CID
        self.DID=DID
        self.booking_status=booking_status

    # Getters  '

    def getTID(self):
        return self.TID

    def getPayment(self):
        return self.Payment

    def getPickup(self):
        return self.Pickup

    def getDropoff(self):
        return self.Dropoff

    def getTime(self):
        return self.Time

    def getDate(self):
        return self.Date
    def getCID(self):
        return self.CID
    def getDID(self):
        return self.DID
    def getbooking_status(self):
        return self.booking_status

    # Setters
    def setTID(self,tid):
        self.TID=tid

    def setPayment(self,Payment):
        self.Payment=Payment

    def setPickup(self,Pickup):
        self.Pickup=Pickup

    def setDropoff(self,Dropoff):
        self.Dropoff=Dropoff

    def setTime(self,Time):
        self.Time=Time

    def setDate(self,Date):
        self.Date=Date
    def setCID(self,CID):
        self.CID=CID
    def setDID(self,DID):
        self.DID=DID
    def setbooking_status(self,booking_status):
        self.booking_status=booking_status


        # str

    def __str__(self):
        return str(
            self.TID) + ", " + self.Payment + ", " + self.Pickup + ", " + self.Dropoff + ", " + self.Time + ", " + self.Date+ ", "+self.CID+ ", "+self.DID+", "+self.booking_status
