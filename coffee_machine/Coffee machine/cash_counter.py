from kitchen import resources 


class ChashCounter:
    def report(self):
        print(f'''          Profit : {resources["profit"]}''')
    def make_payment(self,drink) :
        required = drink.cost
        coin_dict= {
            '₹1' : 1.00,
            '₹2' : 2.00, 
        }
        print(f"Please pay {required}")
        print("Insert coins: ")
        payment = 0
        for coin in coin_dict:
            payment += int(input(f"How many {coin}")) * coin_dict[coin]
        
        balance = payment - required
        if balance >= 0 :
            resources["profit"] += required
            print(f"Payment is succesful! Here is your change {round(balance , 2)}")
            return True
        else :
            print("Not sufficient coins! Your payment is refunded!")
            return False
             



