#Tuple of fruits
class Problem10():
    def __init__(self,fruitsList):
        self.fruitsList = fruitsList

    #printing fruit names in capital letters
    def fruitNames(self):
        capitalizedFruits=[names[0].upper() for names in self.fruitsList]
        print(capitalizedFruits)

    #print fruit names whose cost is less than 0.50
    def cheapFruits(self):
        cheapFruits = [names[0] for names in self.fruitsList if names[1] < 0.50 ]
        print(cheapFruits)

    #printing fruit details with highest number of fruits
    def highestFruits(self):
        highestFruits = max(self.fruitsList, key=lambda fruit:fruit[2])
        print(highestFruits)

    #printing the sorted list with sorting based on cost*number of fruits in descending order
    def sortedFruits(self):
        print(sorted(self.fruitsList, key=lambda fruit:fruit[1]*fruit[2],reverse=True))

fruitsList= [('banana', 0.45,6), ('jackfruit', 4.55, 2), ('kiwi', 0.15, 23)]
obj=Problem10(fruitsList)
obj.fruitNames()
obj.cheapFruits()
obj.highestFruits()
obj.sortedFruits()


