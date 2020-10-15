# Skapa en klass, Person. Vi ska hålla reda på personens
#Födelsedatum
#Namn
#GatuAdress
#PostNummer
#Postort
#Skapa en constructor! En person har alltid ett födelsedatum eller hur!
#Allt det andra behöver den inte ha...kan sättas senare "i livet"
#Vilka funktioner:
#- Namnge
#- BytAdress
#I koden skapar du upp två personer. Du och en kompis. Sätt addresser för er två.
#Skriv kod så att den ena flyttar in hos den andra!


import datetime

class Person:
    def __init__(self, Namn, Födelsedatum, streetaddress="",postnumber="",postort=""):
        self._Name=Namn
        self._Birthdate=Födelsedatum
        self._streetaddress=streetaddress
        self._postnumber=postnumber
        self._postort=postort

    def setName(Namn):
        self._Name=Namn

    def getAddress(self):
        return self._streetaddress

    def getPostnumber(self):
        return self._postnumber

    def getPlace(self):
        return self._postort

    def changeAddress(self,streetaddress, pincode, place):
        self._streetaddress=streetaddress
        self._postnumber=pincode
        self._postort=place

p1=Person("Athina",datetime.date(1987,11,25))
p2=Person("George",datetime.date(1984,4,30),"gatustreet 23", 678544,"City")
print(p2.getAddress())

p2.changeAddress(p1.getAddress(),p1.getPostnumber(),p1.getPlace())

print(p2.getAddress())



