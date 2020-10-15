#3. Vidareutveckla Person
#Skapa en funktion för att få reda på aktuell ålder i hela år (datetime.now.Year –Födelsedatum.Year) 

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

    def getAge(self):
        return datetime.datetime.now().year - self._Birthdate.year

p1=Person("Athina",datetime.date(1987,11,25), "streetgatan 45",675543,"city")

print(p1.getAge())