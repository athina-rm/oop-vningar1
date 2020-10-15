import os
import time
import re


class TodaysMenu:
    def __init__(self, name, price, typee, calories):
        self._Name = name
        self._Price = price
        self._Type = typee
        self._Calories = calories

    def GetTodaysSpecial(self):
        if self._Type == "Veg":
            return self._Price * 0.6
            
        else:

            return self._Price

    def __repr__(self): #GET THE BUNCH!
        return self._Name, self._Price, self._Type, self._Calories


lunchMenu = []
while True:
    for i in range(3):
        userInputToSplit = input(" \n\n\n\nInput Name of dish , Price , Type , Calories  ")


        userInput = re.findall(r"(?<![\"=\w])(?:[^\W_]+)(?![\"=\w])",userInputToSplit)




        print(userInput)
        

        def validate_number(s):
            try:
                return int(s)
            except (ValueError, TypeError):
                return s

        userInput = [validate_number(s) for s in userInput]
        name = userInput[0]
        price = userInput[1]
        typee = userInput[2]
        calories = userInput[3]

        lunchMenu.append(TodaysMenu(name, price, typee, calories))


    while True:
        for dish in lunchMenu:
            v = dish.GetTodaysSpecial()
            
            print(f"\nLunch Special ! {dish._Name} Only : {v}")
            
            
            #print([TodaysMenu])

            
        break
    input("\n\nPress any key to continue ")
