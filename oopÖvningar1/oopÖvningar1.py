# Skapa en klass Matratt
#den ska ha ett namn, pris, typ, antal kalorier
#Typ kan man tänka sig Vegetarisk, Vegansk, Kött
#Skapa upp några lägg i en lista.
#Skriv ut en dagens lunchmeny

class Dish:
    def __init__(self, name, price, typ,calories):
        self.Name= name
        self._Price= price
        self.Typ=typ
        self.Calories=""
    def GetPrice(self):
        if self.Typ=="Vegetarisk":
            return self._Price*0.7
        return self._Price
lunchMenyn=[]
lunchMenyn.append(Dish("pannkakor",89,"Vegetarisk", 10))
lunchMenyn.append(Dish("Hamburgare",99,"kött", 100))
lunchMenyn.append(Dish("Hamburgare",99,"kött", 100))
while True:
    clear()
    for dish in lunchMenyn:
        if dish.Typ=="Vegetarisk":
            print(f"{dish.Name} {dish.Price*7}")
        else:
            print(f"{dish.Name} {dish.Price}")
        
        v=dish.GetPrice()
        printf(v)
