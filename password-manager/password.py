from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json


# Password Generating 
LETTERS = ["a", "b", "c", "d" , "e" , "f", "g", "h", "i", "j", "k", "l", "m", "n", "o" ,"p", "q" ,"r", "s", "t", "u", "v","w", "x", "y", "z" ] 

CHARACTERS = [":", "!", "<", ">" , "_" ,",", ";" ,"=", "'", "\\", "\"" , "{", "}", "(" , ")", "[", "]", "₹" , "$", "%", "^", "&", "*", "-", "+", "/", "?", "." , "~"]

NUMBERS = ["1", "2", "3", "4", "5", "6", "7" , "8", "9", "0"]

def genarate_pw():
    pw.delete(0, END)
    password_list = []
    t_let = randint(3,10)
    t_char = randint(2,5)
    t_num = randint(2,5)

    for _ in range(t_let):
        password_list.append(choice(LETTERS))

    
    for _ in range(t_char):
        password_list.append(choice(CHARACTERS))
        
    for _ in range(t_num):
        password_list.append(choice(NUMBERS))

    shuffle(password_list)
    
    pswrd = "".join(password_list)
    pw.insert(0, pswrd)
 

        
    


# Data Saving
def saving():

    website= wb.get()
    email= user.get()
    password= pw.get()

    
    
    if website == "" or email== "" or password== "":
        messagebox.showinfo(title="Fill All The Feilds.", message="It seems like, you have left some feilds unfilled. Fill it!")

    elif not "@gmail.com" in email:
        messagebox.showinfo(title="Ooopss!!.", message="Invalid Email!")

    

    else:
        msg = messagebox.askokcancel(title=website, message=f"You entered:\n Website: {website}\n Email/UserId: {email} \n Password: {password}\n Save It ?")
        if msg :
            added_info ={website : {
                "email" : email,
                "password" : password
            }}

            try:
                with open ("Your_Password_Library.json", "r") as doc:
                    # Read the contexts of the file and store it
                    stored_info = json.load(doc)

                    

            except FileNotFoundError:
                with open ("Your_Password_Library.json", "w") as doc:
                    # Storing the data
                    json.dump(added_info, doc, indent=4)

            else:
                # Updating the exsiting file with added info
                stored_info.update(added_info)

                with open ("Your_Password_Library.json", "w") as doc:
                    # Storing the data
                    json.dump(stored_info, doc, indent=4)

            finally:    
                wb.delete(0,END)
                user.delete(0,END)
                pw.delete(0,END)
    



# Searching for the saved websit info
def searching():
    website= wb.get()
    try: 
        with open ("Your_Password_Library.json", "r") as doc:
            # Read the contexts of the file and store it
            data = json.load(doc)
    except FileNotFoundError:
        messagebox.showinfo(title="Ooopss!!.", message="No File Found!")
    
    else:
        if website in data:
            email= data[website]["email"]
            password = data[website]["password"]
            user.insert(0, email)
            pw.insert(0, password)
        else:
            messagebox.showinfo(title="Ooopss!!.", message="Website not Found!")
    

    





window = Tk()
window.title("PassWord Manager")

canvas= Canvas(width=200, height=200)
img= PhotoImage(file="logo.png")
canvas.create_image(150, 150, image= img)
canvas.grid(column=1, row=0)

ins1= Label(text="Website")
ins1.grid(column=0, row=1)
wb = Entry(width=25)
wb.focus()
wb.grid(column=1, row=1)

search= Button(text="Search", width=25, command=searching)
search.grid(column=2, row=1)

ins2= Label(text="Email/UserId")
ins2.grid(column=0, row=2)
user= Entry(width=50)
user.grid(column=1, row=2, columnspan=2)

ins3= Label(text="Password")
ins3.grid(column=0, row=3)
pw= Entry(width=25)
pw.grid(column=1, row=3)

generate= Button(text="Generate Password", width=25, command=genarate_pw)
generate.grid(column=2, row=3)



add= Button(width=50, text="Add", command= saving)
add.grid(column=1, row=4, columnspan=2)







window.mainloop()



