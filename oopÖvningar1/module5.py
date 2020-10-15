#5.Kenneln
#Skriv ett program som hanterar ett litet register över hundar som finns på en kennel. För varje
#hund som registreras skall finnas namn, ras, ålder och vikt.
#Programmet skall vara kommandostyrt och fyra olika kommandon skall kunna ges:
#1.Registrera. Användaren får frågor om namn, ras, ålder och vikt för hunden. Ett
#hundobjekt skapas och läggs in i kennel-registret.
#2.Lista. Användaren får en fråga om minsta svanslängd och programmet skriver ut en lista
#på alla hundar hos kenneln som har längre svanslängd än denna minsta angivna (om man
#anger 0 så kommer alltså alla hundar att skrivas ut, anger man 10 så skrivs bara de hundar
#vars svanslängd>=10 ut). Svanslängden för en hund kan räknas ut med den fiffiga
#formeln: svanslängden=åldern*vikten/10. Denna formel gäller för alla hundar UTOM
#taxar. En tax har alltid svanslängden 3.7. Vid utskriften skall alla hundens attribut samt
#svanslängden skrivas ut, t.ex. Fido Pudel 4 år 7 kg svans=2.8 eller Nisse Tax 6 år 8
#kg svans=3.7.
#3.Ta bort. Användaren får en fråga efter namnet på hunden som skall tas bort. Hunden med
#det angivna namnet skall tas bort ur kennel-registret. Om det inte finns någon hund med
#det angivna namnet så skall programmet skriva ut Hund med det namnet fanns ej i
#registret annars skall det skrivas ut Hunden med det angivna namnet är borttagen. Ni
#behöver inte tänka på komplikationen att det kan finnas flera hundar med samma namn.
#4.Avsluta. Programmet avslutas. En tråkig effekt är att när programmet avslutas så
#"försvinner" allt lagrat data (objekt som skapas ligger i primärminnet och finns bara så
#länge programmet körs). Alla registrerade hundar försvinner alltså… så den som hinner –
#SPARA alla hundar i en fil som läses upp vid uppstart 

class Kennel:
    def __init__(self):
        self._dogs=[]

    def addDogtoKennel(self,dog):
        self._dogs.append(dog)

    def getListTaillength(self,min_taillength):
        for i in self._dogs:
            if i.getTailLength()>=min_taillength:
                print(i.getName()," ", i.getRace()," ",i.getAge(),"yrs ",i.getWeight(),"kg ",i.getTailLength())

    def removeDog(self,dog):
        exist=False
        for i in self._dogs:
            if i.getName()==dog:
                self._dogs.remove(i)
                print(f"The dog {dog} has been successfully removed from the kennel")
                exist=True
            else:
                exist=False
        if exist==False:
            print(f"The dog {dog} is not there in the kennel")

class Dog:
    def __init__ (self, name, race, age, weight, tailLength=0.0):
        self._taillength=tailLength
        self._name=name
        self._race=race
        self._age=age
        self._weight=weight

    def getTailLength(self):
        if self._race=="tax":
            return 3.7
        else:
            return (self._age*self._weight/10)

    def getName(self):
        return self._name

    def getRace(self):
        return self._race

    def getAge(self):
        return self._age

    def getWeight(self):
        return self._weight

myKennel=Kennel() 
while True:
    print("1. Register a dog")
    print("2. List dogs based on taillength")
    print("3. Remove a dog")
    print("4. Shut down")
    choice=int(input("What would you like to do: "))
    if choice==1:
        dog=Dog(input("Name of the dog: "),input("Race : "),int(input("Age : ")),float(input("Weight : ")))
        myKennel.addDogtoKennel(dog)
    elif choice ==2:
        min_taillength=float(input("Minimum taillength : "))
        myKennel.getListTaillength(min_taillength)
    elif choice==3:
        myKennel.removeDog(input("Dog that should be removed : "))
    else:
        break

