def calculator(num1, num2, opt):
    if opt == '+':
        print (f"{num1} + {num2} = {num1 + num2}")
        return num1 + num2
    elif opt == '-':
        print (f"{num1} - {num2} = {num1 - num2}")
        return num1 - num2
    elif opt == '*':
        print (f"{num1} * {num2} = {num1 * num2}")
        return num1 * num2
    elif opt == '/':
        print (f"{num1} / {num2} = {num1 / num2}")
        return num1 / num2
    elif opt == '%':
        print (f"{num1} % {num2} = {num1 % num2}")
        return num1 % num2
    else:
        print (f"{num1} UNDEFINED {num2} = 0.0")
        return 0.0
    
msg = 'no'
while msg == 'no':
    print('''
    _____________________
    |  _________________  |
    | |            0.   | |  .----------------.  .----------------.  .----------------.  .----------------. 
    | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
    |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
    | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
    | |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
    | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
    | |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
    | | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
    | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
    | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
    | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
    |_____________________|
    ''')
    done = False
    while not done:
        try:
            num1 = float(input("Entre first number:\n"))
            done = True
        except ValueError:
            print("Invalid number.")

    msg = 'yes'
    result= num1
    while msg == 'yes':
        done = False
        while not done:
            try:
                num2 = float(input("Entre second number:\n"))
                done = True
            except ValueError:
                print("Invalid number.")

        opt= input("Entre operation:\n'+'\n'-'\n'*'\n'/'\n'%'\n")
        result= calculator(result, num2, opt)
        msg= input("Wish to 'CONTINUE'?: type 'yes'\n Wish to 'RESTART'?: type 'no'\n")
    print('\n' * 100)

else: 
    print("Typing Mistake")


        
