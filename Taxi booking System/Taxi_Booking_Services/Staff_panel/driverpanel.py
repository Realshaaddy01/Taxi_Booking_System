class getset_driver:
    def __init__(self, DID=0, Name=None, Address=None, Email=None, Phone=None, License_num=None, Registration_num=None,
                 Password=None,driver_status=None):
        self.DID = DID
        self.Name = Name
        self.Address = Address
        self.Email = Email
        self.Phone = Phone
        self.License_num = License_num
        self.Registration_num = Registration_num
        self.Password = Password
        self.driver_status=driver_status

    # Getters

    def getDID(self):
        return self.DID

    def getName(self):
        return self.Name

    def getAddress(self):
        return self.Address

    def getEmail(self):
        return self.Email

    def getPhone(self):
        return self.Phone

    def getLicense_num(self):
        return self.License_num

    def getRegistration_num(self):
        return self.Registration_num

    def getPassword(self):
        return self.Password
    def getdriver_status(self):
        return self.driver_status

    # Setters

    def setDID(self, DID):
        self.DID = DID

    def setName(self, Name):
        self.Name = Name

    def setAddress(self, Address):
        self.Address = Address

    def setEmail(self, Email):
        self.Email = Email

    def setPhone(self, Phone):
        self.Phone = Phone

    def setLiscense_num(self, Liscense_num):
        self.License_num = Liscense_num

    def setRegistration_num(self, Registration_num):
        self.Registration_num = Registration_num

    def setPassword(self, Password):
        self.Password = Password

    def setdriver_status(self,driver_status):
        self.driver_status=driver_status

        # str

    def __str__(self):
        return str(
            self.DID) + ", " + self.Name + ", " + self.Address + ", " + self.Email + ", " + self.Phone + ", " + self.License_num + ", " + self.Registration_num + ", " + self.Password+", "+self.driver_status
