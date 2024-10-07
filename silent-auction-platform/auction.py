print("WELCOME TO SILENT AUCTION PLATFORM !!!")

store_datas={}

def check_data():
    msg = "yes"
    while msg == "yes":
        name= input("What's Your Name?: ").capitalize()
        try:
            bid = int(input("Make Your Bid: "))
        except ValueError:
            print("Invalid Input! Bid Should To Be In Numbers. \n Try Again")
            continue

        store_datas[name]=bid
        msg= input("Anyone Left?: \n if yes type 'yes' otherwise type 'no' \n [Any other inputs will close the platform.]: ")
        print('\n' * 100)

check_data()

finish = False
while not finish:
    win=0
    winner= ""
    is_draw = False
    draw = []
    for name in store_datas:
        if win < store_datas[name]:
            win= store_datas[name]
            winner= name
            is_draw = False
        elif win == store_datas[name]:
            is_draw= True
            draw.append(name)

    if is_draw:
        store_datas={}
        draw_between = ""
        for any in draw:
            draw_between += f"{any} , "
        draw_between += f"and {winner}"
        draw.append(winner)

        print(f"Its Draw Between {draw_between} with {win} bid.")
        print(f"The Auction Window Will Reopen Only For Them. No Other Can Participate.")
        
        for name in draw:
            print(f"{name}, It's Your Turn!")
            bid= int(input("Make Your Bid?: "))
            store_datas[name]=bid
            print('\n' * 100)
    else:
        finish = True

print(f"{winner} won the auction with {win} bid.")
    
