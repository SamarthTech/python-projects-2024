MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 50.00
}

def transaction():
    global total
    global MENU
    global resources
    z=False
    if total==MENU[a]["cost"]:
        resources["money"]=resources["money"]+total
        return True
    elif total>MENU[a]["cost"]:
        total=total-MENU[a]["cost"]
        if resources["money"]>=total:
            resources["money"] = resources["money"] - total
            return True
        else:
            print("Not enough money in the coffee machine. Money refunded.")
            return False
    else:
        print("Not enough money for transaction. Money refunded")
        return False

def reduction():
    global resources
    for y in resources:
        if y!="money":
            resources[y]=resources[y]-MENU[a]["ingredients"][y]

def check():
    a1 = 0
    for y in resources:
        if y!="money":
            if resources[y]>=MENU[a]["ingredients"][y]:
                a1=a1+1
            else:
                print(f"Insufficient {y}")
    if a1==3:
        return True
    else:
        return False





a=""
while a!= "off":
    a=input("What would you like? (espresso/latte/cappuccino): ")
    if a=="report":
        for i in resources:
            if i=="coffee":
                print(i.capitalize() + ": " + str(resources[i])+"g" )
            elif i=="money":
                print(i.capitalize() + ": $" + str(resources[i]))
            else:
                print(i.capitalize() + ": " + str(resources[i]) + "ml")
    else:
        for i in MENU:
            if a==i:
                b=check()
                if b==True:
                    print("Insert coins")
                    q=int(input("How many quarters?: "))
                    d=int(input("How many dimes?: "))
                    n=int(input("How many nickels?: "))
                    p=int(input("How many pennies?: "))
                    total= q*0.25 + d*0.10 + n*0.05 + p*0.01
                    c=transaction()
                    if c==True:
                        reduction()
                        print(f"Here is your {a}. Enjoy!")
                        if total>0 and not(total==MENU[a]["cost"]):
                            print(f"Here is your change of ${total}")

