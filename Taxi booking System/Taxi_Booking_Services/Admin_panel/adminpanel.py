class getset_admin:
    def __init__(self, AID=0, Name=None, Address=None, Email=None, Phone=None,Password=None):
        self.AID = AID
        self.Name = Name
        self.Address = Address
        self.Email = Email
        self.Phone = Phone
        self.Password = Password

    # Getters
    def getDID(self):
        return self.AID

    def getName(self):
        return self.Name

    def getAddress(self):
        return self.Address

    def getEmail(self):
        return self.Email

    def getPhone(self):
        return self.Phone


    def getPassword(self):
        return self.Password

    # Setters

    def setDID(self, DID):
        self.AID = DID

    def setName(self, Name):
        self.Name = Name

    def setAddress(self, Address):
        self.Address = Address

    def setEmail(self, Email):
        self.Email = Email

    def setPhone(self, Phone):
        self.Phone = Phone

    def setPassword(self, Password):
        self.Password = Password

        # str

    def __str__(self):
        return str(
            self.AID) + ", " + self.Name + ", " + self.Address + ", " + self.Email + ", " + self.Phone + ", "  + self.Password
