import random 

print("Welcome to Tic-Tac-Toe")
print("----------------------")

possibleNumbers=[1,2,3,4,5,6,7,8,9]  
gameBoard = [[1,2,3],[4,5,6],[7,8,9]] 
rows = 3
columns = 3

def printGameBoard():
    for x in range (rows):
        print("\n+---+---+---+")
        print("|",end="")
        for y in range(columns):
            print("",gameBoard[x][y],end=" |")
    print("\n+---+---+---+")

def modifyArray(num,turn):   
    num -= 1
    if(num==0):
        gameBoard[0][0]=turn 
    elif(num==1):
        gameBoard[0][1]=turn 
    elif(num==2):
        gameBoard[0][2]=turn 
    elif(num==3):
        gameBoard[1][0]=turn 
    elif(num==4):
        gameBoard[1][1]=turn 
    elif(num==5):
        gameBoard[1][2]=turn 
    elif(num==6):
        gameBoard[2][0]=turn 
    elif(num==7):
        gameBoard[2][1]=turn 
    elif(num==8):
        gameBoard[2][2]=turn 

def checkForWinner(gameBoard):
    
    
    
    if(gameBoard[0][0]=='X' and gameBoard[0][1]=='X' and gameBoard[0][2]=='X'):
        print("X has won !!!")
        return 'X'
    elif(gameBoard[0][0]=='O' and gameBoard[0][1]=='O' and gameBoard[0][2]=='O'):
        print("O has won !!!")
        return 'O'
    
    
    elif(gameBoard[1][0]=='X' and gameBoard[1][1]=='X' and gameBoard[1][2]=='X'):
        print("X has won !!!")
        return 'X'
    elif(gameBoard[1][0]=='O' and gameBoard[1][1]=='O' and gameBoard[1][2]=='O'):
        print("O has won !!!")
        return 'O'
    
   
    elif(gameBoard[2][0]=='X' and gameBoard[2][1]=='X' and gameBoard[2][2]=='X'):
        print("X has won !!!")
        return 'X'
    elif(gameBoard[2][0]=='O' and gameBoard[2][1]=='O' and gameBoard[2][2]=='O'):
        print("O has won !!!")
        return 'O'

    

    
    elif(gameBoard[0][0]=='X' and gameBoard[1][0]=='X' and gameBoard[2][0]=='X'):
        print("X has won !!!")
        return 'X'
    elif(gameBoard[0][0]=='O' and gameBoard[1][0]=='O' and gameBoard[2][0]=='O'):
        print("O has won !!!")
        return 'O'
    
    
    elif(gameBoard[0][1]=='X' and gameBoard[1][1]=='X' and gameBoard[2][1]=='X'):
        print("X has won !!!")
        return 'X'
    elif(gameBoard[0][1]=='O' and gameBoard[1][1]=='O' and gameBoard[2][1]=='O'):
        print("O has won !!!")
        return 'O'

    
    elif(gameBoard[0][2]=='X' and gameBoard[1][2]=='X' and gameBoard[2][2]=='X'):
        print("X has won !!!")
        return 'X'
    elif(gameBoard[0][2]=='O' and gameBoard[1][2]=='O' and gameBoard[2][2]=='O'):
        print("O has won !!!")
        return 'O'
    
   

    
    elif(gameBoard[0][0]=='X' and gameBoard[1][1]=='X' and gameBoard[2][2]=='X'):
        print("X has won !!!")
        return 'X'
    elif(gameBoard[0][0]=='O' and gameBoard[1][1]=='O' and gameBoard[2][2]=='O'):
        print("O has won !!!")
        return 'O'
    
    
    elif(gameBoard[0][2]=='X' and gameBoard[1][1]=='X' and gameBoard[2][0]=='X'):
        print("X has won !!!")
        return 'X'
    elif(gameBoard[0][2]=='O' and gameBoard[1][1]=='O' and gameBoard[2][0]=='O'):
        print("O has won !!!")
        return 'O'
    
    return None

def isDraw():
    
    return all(isinstance(cell, str) for row in gameBoard for cell in row)

leaveloop = False 
turnCounter = 0  

while(leaveloop == False):

   
    if(turnCounter % 2 ==1):
        printGameBoard()
        numberPicked = int(input("\n Choose a number between 1 to 9:"))
        if (numberPicked>=1 and numberPicked<=9):
            modifyArray(numberPicked,'X')
            possibleNumbers.remove(numberPicked)
        else:
            print("Invalid input , plrase try again")
        turnCounter += 1
         
   
    else:
        while(True):
            cpuChoice = random.choice(possibleNumbers)
            if cpuChoice in possibleNumbers:
                modifyArray(cpuChoice,'O')
                possibleNumbers.remove(cpuChoice)
                turnCounter += 1
                break 


    winner = checkForWinner(gameBoard)
    if winner:
        printGameBoard()
        print(f"\n{winner} has won the game!")
        leaveloop = True  
        break


    if isDraw():
        printGameBoard()
        print("\nIt's a draw!")
        leaveloop = True  
        break

        




