from coffee_machine import CoffeeMachine
from menu import Menu
from cash_counter import ChashCounter

finish = False
while not finish:
    command = input("What do you want? (latte, cappuccino, espresso): ").lower()
    order = Menu()
    my_machine = CoffeeMachine()
    my_counter = ChashCounter()

    drink = order.find_drink(command)
    if drink:
        if my_machine.is_resource_sufficient(drink) and my_counter.make_payment(drink):
            my_machine.make_coffee(drink)
            print("Your order is ready! ☕ Please get it")
        else:
            continue

    else:
        if command == "report":
            my_machine.report()
            my_counter.report()
        elif command == "off": 
            finish = True
            print("\n" * 100)
        else:
            print("Typing Error")
    
        
    

    

