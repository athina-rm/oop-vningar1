##
#class Person:
#    def __init__(self, birthDate):
#        self._Name= ""
#        self._BirthDate= birthDate
#        self._StreetAddress=""
#        self._PostalCode=0
#        self._City= ""
#    def SetName (self,name):
#        #validera
#        self._Name=name
#    def ChangeAddress (self, street,pin, place):
#        self._StreetAddress=street
#        self._PostalCode=pin
#        self._City= place




#def Moveinto(self, minNyaSambo):
#    self.ChangeAddress(minNyaSambo.GetStreetAddress(), minnyaSambo.GetPostalCode(),
#                       minNyaSambo.GetCity())

#dat=datetime.datetime (1972,8,3)

#stefan= Person(dat)
#stefan.SetName ("Stefan")
#fru= Person(dat)

#1. Skapa en klass Matratt
#den ska ha ett namn, pris, typ, antal kalorier
#Typ kan man tänka sig Vegetarisk, Vegansk, Kött
#Skapa upp några lägg i en lista.
#Skriv ut en dagens lunchmeny!

class Dish:
    def __init__(self,name,price,foodtype,calories):
        self._name=name
        self._price=price
        self._foodtype=foodtype
        self._calories=calories

    def GetName(self):
        return self._name

    def getPrice(self):
        return (self._price)

lunchMenyn=[]
lunchMenyn.append(Dish("pannkakor",89,"Vegetarisk", 10))
lunchMenyn.append(Dish("Hamburgare",99,"kött", 100))
lunchMenyn.append(Dish("Tofuburgare",99,"Vegan", 80))

for mat in lunchMenyn:
    print(mat.GetName(), mat.getPrice())






