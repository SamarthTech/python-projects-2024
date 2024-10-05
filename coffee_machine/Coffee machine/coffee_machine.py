from kitchen import resources


class CoffeeMachine:
    def report(self):
        print(f'''
        Water : {resources["water"]} ml
        Milk : {resources["milk"]} ml
        Coffee : {resources["coffee"]} gm'''
        )
    
    def is_resource_sufficient(self, drink):
        print("Resource availablity is checking...")
        required = drink.ingrediants
        if resources["coffee"] >= required["coffee"] and resources["milk"] >= required["milk"] and resources["water"] >= required["water"]:
            return True
        elif resources["coffee"] < required["coffee"]:
            print ("Coffee is not available! Sorry!")
            return False
        elif  resources["milk"] < required["milk"]:
            print("Milk is not available! Sorry!")
            return False
        else:
            print  ("Water is not available! Sorry!")
            return False
        
    def make_coffee(self, drink) :
        required = drink.ingrediants
        resources["coffee"] -= required ["coffee"]
        resources["milk"] -= required["milk"]
        resources ["water"] -= required ["water"] 





