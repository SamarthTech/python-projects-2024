requirments = {
    "latte" : {
        "coffee": 15,
        "water" : 10,
        "milk": 4,
        "price": 3.51
    },

    "cappuccino" : {
        "coffee": 5,
        "water" : 5,
        "milk": 10,
        "price": 2.42
    },

    "espresso" : {
        "coffee": 15,
        "water" : 5,
        "milk" : 0,
        "price" : 1.55
    }
}

class MenuItem:
    def __init__(self, name, drink):
        self.name = name
        self.cost = drink["price"]
        water = drink["water"]
        coffee = drink["coffee"]
        milk = drink["milk"]
        self.ingrediants = {"water" : water, "coffee": coffee, "milk": milk}

class Menu:
    def find_drink(self,name):
        if name in requirments:
            drink = requirments[name]
            return MenuItem(name , drink)
        else:
            return None
    
