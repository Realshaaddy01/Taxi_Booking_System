class getset_Cust:
    def __init__(self, CID=0, Name=None, Address=None, Email=None, Phone=None, Age=None, Password=None):
        self.CID = CID
        self.Name = Name
        self.Address = Address
        self.Email = Email
        self.Phone = Phone
        self.Age = Age
        self.Password = Password

    # Getters

    def getCID(self):
        return self.CID

    def getName(self):
        return self.Name

    def getAddress(self):
        return self.Address

    def getEmail(self):
        return self.Email

    def getPhone(self):
        return self.Phone

    def getAge(self):
        return self.Age

    def getPassword(self):
        return self.Password

    # Setters

    def setCID(self, CID):
        self.CID = CID

    def setName(self, Name):
        self.Name = Name

    def setAddress(self, Address):
        self.Address = Address

    def setEmail(self, Email):
        self.Email = Email

    def setPhone(self, Phone):
        self.Phone = Phone

    def setAge(self, Age):
        self.Age = Age

    def setPassword(self, Password):
        self.Password = Password

        # str

    def __str__(self):
        return str(
            self.CID) + ", " + self.Name + ", " + self.Address + ", " + self.Email + ", " + self.Phone + ", " + ", " + self.Age + ", " + ", " + self.Password
