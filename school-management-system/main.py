import tkinter as tk
from tkinter import messagebox
import sqlite3
con = sqlite3.connect("testdata.db")
cur = con.cursor()

window = tk.Tk()
window.geometry("450x300")
window.configure(bg = '#897C78')
window.title("Hariyana Vidya Mandir")

# the label for Username 
name_label = tk.Label(window, text = "Username :",font=("Helvetica",14,"bold"),fg = '#18120F',bg = '#FDD4B8')
name_label.place(x = 40,y = 60)  
    
# the label for Password  
password_label = tk.Label(window,text = "Password :",font=("Helvetica",14,"bold"),fg = '#18120F',bg = '#FDD4B8')
password_label.place(x = 40,y = 110)  

# Username input box
name_entry = tk.Entry(window,width = 20,font=("Helvetica",14))
name_entry.place(x = 170,y = 60)  

#Password input box   
password_entry = tk.Entry(window,width = 20,font=("Helvetica",14),show = '*')
password_entry.place(x = 170,y = 110)  

#Radio button for choosing 1 of 3 options
radio = tk.IntVar()

head_checkbox = tk.Radiobutton(window,text = "Principal",variable = radio,value = 1,width = 10,
                                  font=("Helvetica",12,"bold"),bg = '#897C78',fg = '#18120F',activebackground = '#897C78')
head_checkbox.place(x = 40,y = 160)

teacher_checkbox = tk.Radiobutton(window,text = "Teacher",variable = radio,value = 2,width = 10,
                                  font=("Helvetica",12,"bold"),bg = '#897C78',fg = '#18120F',activebackground = '#897C78')
teacher_checkbox.place(x = 168,y = 160)

student_checkbox = tk.Radiobutton(window,text = "Student",width = 10,variable = radio,value = 3,
                                  font=("Helvetica",12,"bold"),bg = '#897C78',fg = '#18120F',activebackground = '#897C78')
student_checkbox.place(x = 278,y = 160)

login_button = tk.Button(window,text = "LOG IN",width = 20,font=("Helvetica",14,"bold"),bg = '#C7A196',
                         activebackground = '#FDD4B8',command = lambda:logincommand(name_entry.get(),password_entry.get()))
login_button.place(x = 108,y = 210)


def logincommand(name_enter,password_enter):
        # For student login
        if(radio.get()==3):
            cur.execute("SELECT username FROM StudentData")
            a = cur.fetchall()
            count=0
            for i in range(0,len(a)):
                if(a[i][0]==name_enter):
                    count = 0
                    break
                count=count+1
            # Checking if the username exists
            if(count!=0):
                messagebox.showerror('Incorrect Password','Your Username or Password was Incorrect.Try Again')
            cur.execute("SELECT password FROM StudentData WHERE username='"+name_enter+"'")
            # Checking if the password is correct
            if(password_enter==cur.fetchone()[0]):
                newwindow = tk.Toplevel(window)

                newwindow.geometry("800x700")
                newwindow.configure(bg = '#583830')

                newwindow.title("Hariyana Vidya Mandir")

                loginas_label = tk.Label(newwindow, text = "Logged in as Student",width = 100,justify = tk.LEFT,anchor = tk.NW,
                         font = ("PT Sans",20,"bold"),bg = '#FDD4B8')
                loginas_label.place(x = 0,y = 0)

                # Displaying the labels at their proper positions
                class Heads:
                    def __init__(self,text,width,x,y):
                        self.text = text
                        self.width = width
                        self.x = x
                        self.y = y
        
                        self.label = tk.Label(newwindow,text = self.text,width = self.width,font = ("Cambria",14,"bold"),justify = tk.LEFT,
                              anchor = tk.NW,fg = '#18120F',bg = '#C7A196')
                        self.label.place(x = self.x,y = self.y)

                # Displaying the data of the student
                class Values:
                    def __init__(self,text,width,x,y):
                        self.text = text
                        self.width = width
                        self.x = x
                        self.y = y
        
                        cur.execute("SELECT " + self.text + " FROM StudentData WHERE username='"+name_enter+"' AND password='"+password_enter+"'")
                        self.text_var = tk.StringVar()
                        self.text_var.set(cur.fetchone())
                        if(self.text=='photo'):
                            self.label = tk.Label(newwindow,textvariable = self.text_var,width = self.width,height = 9,
                                  fg = '#18120F',bg = '#FDD4B8')
                            self.label.place(x = self.x,y = self.y)
                        elif(self.text=='addr'):
                            self.label = tk.Label(newwindow,textvariable = self.text_var,width = self.width,font = ("Cambria",14),
                                  justify = tk.LEFT,wraplength = 600,anchor = tk.NW,fg = '#18120F',bg = '#FDD4B8')
                            self.label.place(x = self.x,y = self.y)
                        else:    
                            self.label = tk.Label(newwindow,textvariable = self.text_var,width = self.width,font = ("Cambria",14),
                                  justify = tk.LEFT,anchor = tk.NW,fg = '#18120F',bg = '#FDD4B8')
                            self.label.place(x = self.x,y = self.y)

                blank_label = tk.Label(newwindow,width = 59,font = ("Cambria",14),fg = '#18120F',bg = '#FDD4B8')
                blank_label.place(x = 105,y = 310)
                blank_label = tk.Label(newwindow,width = 59,font = ("Cambria",14),fg = '#18120F',bg = '#FDD4B8')
                blank_label.place(x = 105,y = 335)
                blank_label = tk.Label(newwindow,width = 49,font = ("Cambria",14),fg = '#18120F',bg = '#FDD4B8')
                blank_label.place(x = 205,y = 610)
                blank_label = tk.Label(newwindow,width = 49,font = ("Cambria",14),fg = '#18120F',bg = '#FDD4B8')
                blank_label.place(x = 205,y = 630)

                name = Heads('First Name:',12,10,70)
                name1 = Values('name',12,155,70)
                lname = Heads('Last Name:',13,295,70)
                lname1 = Values('lname',12,450,70)
                fname = Heads('Middle Name:',12,10,125)
                fname1 = Values('fname',12,155,125)
                mname = Heads("Mother's Name:",13,295,125)
                mname1 = Values('mname',12,450,125)
                dob = Heads('Date of Birth:',12,10,180)
                dob1 = Values('dob',12,155,180)
                bplace = Heads('Birth Place:',12,295,180)
                bplace1 = Values('bplace',13,440,180)
                photo = Values('photo',15,590,70)
                nation = Heads('Nationality:',10,10,235)
                nation1 = Values('nation',7,134,235)
                relig = Heads("Religion:",10,232,235)
                relig1 = Values('relig',12,357,235)
                caste = Heads("Caste:",6,505,235)
                caste1 = Values('caste',11,585,235)
                addr = Heads("Address:",7,10,290)
                addr1 = Values('addr',59,105,290)
                mno = Heads('Mobile No.:',10,10,390)
                mno1 = Values('mno',20,134,390)
                hei = Heads("Height:",8,362,390)
                hei1 = Values('hei',5,467,390)
                wei = Heads("Weight:",7,552,390)
                wei1 = Values('wei',5,645,390)
                adno = Heads("Aadhaar Card No.:",16,10,440)
                adno1 = Values('adno',16,200,440)
                grno = Heads("General Registration No.:",21,385,440)
                grno1 = Values('gno',6,635,440)
                doa = Heads("Date of Admission in School:",23,10,490)
                doa1 = Values('doa',11,275,490)
                std = Heads("Standard:",9,410,490)
                std1 = Values('std',5,525,490)
                div = Heads("Div:",5,595,490)
                div1 = Values('div',3,665,490)
                ctname = Heads("Class Teacher's Name:",18,10,540)
                ctname1 = Values('ctname',12,220,540)
                hcolor = Heads("House Colour:",11,357,540)
                hcolor1 = Values('hcolor',8,489,540)
                rno = Heads("Roll No.:",7,587,540)
                rno1 = Values('rno',2,676,540)
                ctsc = Heads("Teacher's Remarks:",16,10,590)
                ctsc1 = Values('trem',49,205,590)
                # Back Button
                back = tk.Button(newwindow,text = "Back",command = newwindow.destroy,anchor = tk.NW,fg = '#18120F',bg = '#C7A196',
                                 font = ("Cambria",10,"bold"),justify = tk.LEFT)
                back.place(x = 10, y = 670)
                newwindow.mainloop()

            # If password is incorrect
            else:
                messagebox.showerror('Incorrect Password','Your Username or Password was Incorrect.Try Again')

        # For Teacher login
        if(radio.get()==2):
            cur.execute("SELECT username FROM TeacherData")
            a = cur.fetchall()
            count=0
            for i in range(0,len(a)):
                if(a[i][0]==name_enter):
                    count = 0
                    break
                count=count+1
            if(count!=0):
                messagebox.showerror('Incorrect Password','Your Username or Password was Incorrect.Try Again')
            cur.execute("SELECT password FROM TeacherData WHERE username='"+name_enter+"'")
            if(password_enter==cur.fetchone()[0]):
                newwindow1 = tk.Toplevel(window)
                newwindow1.geometry("770x700")
                newwindow1.configure(bg = '#583830')

                newwindow1.title("S.V.D.D. School")

                loginas_label = tk.Label(newwindow1, text = "Logged in as Teacher",width = 100,justify = tk.LEFT,anchor = tk.NW,
                         font = ("PT Sans",20,"bold"),bg = '#FDD4B8')
                loginas_label.place(x = 0,y = 0)

                class Heads:
                    def __init__(self,text,width,x,y):
                        self.text = text
                        self.width = width
                        self.x = x
                        self.y = y
                        
                        
                        self.label = tk.Label(newwindow1,text = self.text,width = self.width,font = ("Cambria",14,"bold"),justify = tk.LEFT,
                              anchor = tk.NW,fg = '#18120F',bg = '#C7A196')
                        self.label.place(x = self.x,y = self.y)

                class Values:
                    def __init__(self,text,width,x,y):
                        self.text = text
                        self.width = width
                        self.x = x
                        self.y = y
        
                        cur.execute("SELECT " + self.text + " FROM TeacherData WHERE username='"+name_enter+"' AND password='"+password_enter+"'")
                        self.text_var = tk.StringVar()
                        self.text_var.set(cur.fetchone())
                        if(self.text=='photo'):
                            self.label = tk.Label(newwindow1,textvariable = self.text_var,width = self.width,height = 9,
                                  fg = '#18120F',bg = '#FDD4B8')
                            self.label.place(x = self.x,y = self.y)
                        elif(self.text=='addr'):
                            self.label = tk.Label(newwindow1,textvariable = self.text_var,width = self.width,font = ("Cambria",14),
                                  justify = tk.LEFT,wraplength = 600,anchor = tk.NW,fg = '#18120F',bg = '#FDD4B8')
                            self.label.place(x = self.x,y = self.y)
                        elif(self.text=='tfor'):
                            self.label = tk.Label(newwindow1,textvariable = self.text_var,width = self.width,font = ("Cambria",14),
                                  justify = tk.LEFT,wraplength = 550,anchor = tk.NW,fg = '#18120F',bg = '#FDD4B8')
                            self.label.place(x = self.x,y = self.y)
                        else:    
                            self.label = tk.Label(newwindow1,textvariable = self.text_var,width = self.width,font = ("Cambria",14),
                                  justify = tk.LEFT,anchor = tk.NW,fg = '#18120F',bg = '#FDD4B8')
                            self.label.place(x = self.x,y = self.y)

                blank_label = tk.Label(newwindow1,width = 59,font = ("Cambria",14),fg = '#18120F',bg = '#FDD4B8')
                blank_label.place(x = 105,y = 310)
                blank_label = tk.Label(newwindow1,width = 59,font = ("Cambria",14),fg = '#18120F',bg = '#FDD4B8')
                blank_label.place(x = 105,y = 335)
                blank_label = tk.Label(newwindow1,width = 54,font = ("Cambria",14),fg = '#18120F',bg = '#FDD4B8')
                blank_label.place(x = 155,y = 565)

                name = Heads('First Name:',12,10,70)
                name1 = Values('name',12,155,70)
                lname = Heads('Last Name:',13,295,70)
                lname1 = Values('lname',12,450,70)
                fname = Heads('Middle Name:',12,10,125)
                fname1 = Values('fname',12,155,125)
                mname = Heads("Mother's Name:",13,295,125)
                mname1 = Values('mname',12,450,125)
                dob = Heads('Date of Birth:',12,10,180)
                dob1 = Values('dob',12,155,180)
                bplace = Heads('Birth Place:',12,295,180)
                bplace1 = Values('bplace',13,440,180)
                photo = Values('photo',15,590,70)
                nation = Heads('Nationality:',10,10,235)
                nation1 = Values('nation',7,134,235)
                relig = Heads("Religion:",10,232,235)
                relig1 = Values('relig',12,357,235)
                caste = Heads("Caste:",6,505,235)
                caste1 = Values('caste',11,585,235)
                addr = Heads("Address:",7,10,290)
                addr1 = Values('addr',59,105,290)
                mno = Heads('Mobile No.:',10,10,390)
                mno1 = Values('mno',20,134,390)
                adno = Heads("Aadhaar Card No.:",15,365,390)
                adno1 = Values('adno',15,545,390)
                trno = Heads("Teacher's Registration No.:",23,10,440)
                trno1 = Values('trno',6,280,440)
                ctfc = Heads("Class Teacher for Class:",20,378,440)
                ctfc1 = Values('ctfc',8,615,440)
                staught = Heads("Subjects Taught:",15,10,490)
                staught1 = Values('staught',50,195,490)
                taught = Heads("Teacher For:",11,10,540)
                taught1 = Values('tfor',54,155,540)
                
                # Method for adding new student
                def addnew():
                    newwindow6 = tk.Toplevel(newwindow1)

                    newwindow6.geometry("1000x1000")
                    newwindow6.configure(bg = '#583830')

                    newwindow6.title("S.V.D.D. School")

                    loginas_label = tk.Label(newwindow6, text = "Logged in as Teacher",width = 100,justify = tk.LEFT,anchor = tk.NW,
                         font = ("PT Sans",20,"bold"),bg = '#FDD4B8')
                    loginas_label.place(x = 0,y = 0)
                    
                    def added(name1,lname1,fname1,mname1,dob1,bplace1,nation1,relig1,caste1,addr1,mno1,hei1,wei1,adno1,grno1,doa1,std1,div1,ctname1,hcolor1,rno1,ctsc1,photo1,username1,password1):
                        cur.execute("INSERT INTO StudentData VALUES('"+name1+"','"+lname1+"','"+fname1+"','"+mname1+"','"+dob1+"','"+bplace1+"','"+nation1+"','"+relig1+"','"+caste1+"','"+addr1+"','"+mno1+"','"+hei1+"','"+wei1+"','"+adno1+"','"+grno1+"','"+doa1+"','"+std1+"','"+div1+"','"+ctname1+"','"+hcolor1+"','"+rno1+"','"+ctsc1+"','"+photo1+"','"+username1+"','"+password1+"')")
                        con.commit()
                        messagebox.showinfo("Successful!","New Student Details Added Successfully")

                    class Heads:
                        def __init__(self,text,width,x,y):
                            self.text = text
                            self.width = width
                            self.x = x
                            self.y = y
        
                            self.label = tk.Label(newwindow6,text = self.text,width = self.width,font = ("Cambria",14,"bold"),justify = tk.LEFT,
                              anchor = tk.NW,fg = '#18120F',bg = '#C7A196')
                            self.label.place(x = self.x,y = self.y)

                    class Values:
                        def __init__(self,width,x,y):
                            self.width = width
                            self.x = x
                            self.y = y
        
                            self.enter = tk.Entry(newwindow6,width = self.width,font = ("Cambria",14),
                              fg = '#18120F',bg = '#FDD4B8')
                            self.enter.place(x = self.x,y = self.y)
                        def ret(self):
                            return self.enter.get()
                    
                    name = Heads('First Name:',12,10,70)
                    name1 = Values(12,155,70)
                    lname = Heads('Last Name:',13,295,70)
                    lname1 = Values(12,450,70)
                    fname = Heads('Middle Name:',12,10,125)
                    fname1 = Values(12,155,125)
                    mname = Heads("Mother's Name:",13,295,125)
                    mname1 = Values(12,450,125)
                    dob = Heads('Date of Birth:',12,10,180)
                    dob1 = Values(12,155,180)
                    bplace = Heads('Birth Place:',12,295,180)
                    bplace1 = Values(13,440,180)
                    nation = Heads('Nationality:',10,10,235)
                    nation1 = Values(7,134,235)
                    relig = Heads("Religion:",10,232,235)
                    relig1 = Values(12,357,235)
                    caste = Heads("Caste:",6,505,235)
                    caste1 = Values(11,585,235)
                    addr = Heads("Address:",7,10,290)
                    addr1 = tk.Text(newwindow6,width = 54,font = ("Cambria",14),height = 3,
                              fg = '#18120F',bg = '#FDD4B8')
                    addr1.place(x = 108,y = 290)
                    mno = Heads('Mobile No.:',10,10,390)
                    mno1 = Values(20,134,390)
                    hei = Heads("Height:",8,362,390)
                    hei1 = Values(5,467,390)
                    wei = Heads("Weight:",7,552,390)
                    wei1 = Values(5,645,390)
                    adno = Heads("Aadhaar Card No.:",16,10,440)
                    adno1 = Values(16,200,440)
                    grno = Heads("General Registration No.:",21,385,440)
                    grno1 = Values(6,635,440)
                    doa = Heads("Date of Admission in School:",23,10,490)
                    doa1 = Values(11,275,490)
                    std = Heads("Standard:",9,410,490)
                    std1 = Values(5,525,490)
                    div = Heads("Div:",5,595,490)
                    div1 = Values(3,665,490)
                    ctname = Heads("Class Teacher's Name:",18,10,540)
                    ctname1 = Values(12,220,540)
                    hcolor = Heads("House Colour:",11,357,540)
                    hcolor1 = Values(8,489,540)
                    rno = Heads("Roll No.:",7,587,540)
                    rno1 = Values(2,676,540)
                    ctsc = Heads("Teacher's Remarks:",16,10,590)
                    ctsc1 = tk.Text(newwindow6,width = 44,font = ("Cambria",14),height = 3,
                              fg = '#18120F',bg = '#FDD4B8')
                    ctsc1.place(x = 210,y = 590)
                    username = Heads("Username:",10,600,125)
                    username1 = Values(15,720,125)
                    password = Heads("Password:",10,600,180)
                    password1 = Values(15,720,180)
                    photo = Heads("Photo:",10,600,70)
                    photo1 = Values(15,720,70)
                    back = tk.Button(newwindow6,text = "Back",command = newwindow6.destroy,anchor = tk.NW,fg = '#18120F',bg = '#C7A196',
                                 font = ("Cambria",10,"bold"),justify = tk.LEFT)
                    back.place(x = 10, y = 680)
                    enter1 = tk.Button(newwindow6,text = "Enter",command = lambda:added(name1.ret(),lname1.ret(),fname1.ret(),mname1.ret(),dob1.ret(),bplace1.ret(),nation1.ret(),relig1.ret(),caste1.ret(),addr1.get("1.0","end-1c"),mno1.ret(),hei1.ret(),wei1.ret(),adno1.ret(),grno1.ret(),doa1.ret(),std1.ret(),div1.ret(),ctname1.ret(),hcolor1.ret(),rno1.ret(),ctsc1.get("1.0","end-1c"),photo1.ret(),username1.ret(),password1.ret()),
                                       anchor = tk.NW,fg = '#18120F',bg = '#C7A196',
                                 font = ("Cambria",10,"bold"),justify = tk.LEFT)
                    enter1.place(x = 500, y = 680)
                    newwindow6.mainloop()

                # Method for Editing Student Information  
                def eedit():
                    newwindow3 = tk.Toplevel(newwindow1)
                    newwindow3.geometry('700x800')
                    newwindow3.configure(bg = '#583830')
                    newwindow3.title("S.V.D.D. School")
                    loginas_label = tk.Label(newwindow3, text = "Logged in as Teacher",width = 100,justify = tk.LEFT,anchor = tk.NW,
                         font = ("PT Sans",20,"bold"),bg = '#FDD4B8')
                    loginas_label.place(x = 0,y = 0)
                    drop = tk.Listbox(newwindow3,width = 22,height = 22,fg = '#18120F',bg = '#FDD4B8')
                    drop.insert(1,'First Name')
                    drop.insert(2,'Last Name')
                    drop.insert(3,'Middle Name')
                    drop.insert(4,'Mother\'s Name')
                    drop.insert(5,'Date of Birth')
                    drop.insert(6,'Birth Place')
                    drop.insert(7,'Nationality')
                    drop.insert(8,'Religion')
                    drop.insert(9,'Caste')
                    drop.insert(10,'Address')
                    drop.insert(11,'Mobile No.')
                    drop.insert(12,'Height')
                    drop.insert(13,'Weight')
                    drop.insert(14,'Aadhaar Card No.')
                    drop.insert(15,'General Registration No.')
                    drop.insert(16,'Date of Admission')
                    drop.insert(17,'Standard')
                    drop.insert(18,'Division')
                    drop.insert(19,'Class Teacher\'s Name')
                    drop.insert(20,'House Colour')
                    drop.insert(21,'Roll No.')
                    drop.insert(22,'Teacher\'s Remarks')
                    drop.place(x = 20,y = 80)

                    # After selecting value to edit
                    def getElement():
                        selection = drop.curselection()
                        try:
                            index = selection[0]
                            value = drop.get(index)
                            a.set(value)
                            ent = tk.Label(newwindow3,text = "Enter Student's First Name:",width = 22,anchor = tk.NW,
                                       fg = '#18120F',bg = '#C7A196',font = ("Cambria",14,"bold"),justify = tk.LEFT)
                            ent.place(x = 200,y = 150)
                            ent1 = tk.Entry(newwindow3,width = 15,font = ("Cambria",14))
                            ent1.place(x = 470,y = 150)
                            ent2 = tk.Label(newwindow3,text = "Enter Student's Gen. Reg. No.:",width = 23,anchor = tk.NW,
                                        fg = '#18120F',bg = '#C7A196',font = ("Cambria",14,"bold"),justify = tk.LEFT)
                            ent2.place(x = 200,y = 200)
                            ent3 = tk.Entry(newwindow3,width = 15,font = ("Cambria",14))
                            ent3.place(x = 470,y = 200)
                            x = tk.Label(newwindow3,textvariable = a,anchor = tk.NW,fg = '#18120F',bg = '#C7A196',
                                    font = ("Cambria",14,"bold"),justify = tk.LEFT)
                            x.place(x = 200,y = 250)
                            y = tk.Text(newwindow3,width = 40,height = 4,font = ("Cambria",14))
                            y.place(x = 200, y = 300)
                            back = tk.Button(newwindow3,text = "Back",command = newwindow3.destroy,anchor = tk.NW,fg = '#18120F',bg = '#C7A196',
                                  font = ("Cambria",14,"bold"),justify = tk.LEFT)
                            back.place(x = 550, y = 450)
                            dict1 = {"First Name":"name","Last Name":"lname","Middle Name":"fname","Mother's Name":"mname","Date of Birth":"dob",
                                "Birth Place":"bplace","Nationality":"nation","Religion":"relig","Caste":"caste","Address":"addr",
                                 "Mobile No.":"mno","Height":"hei","Weight":"wei","Aadhaar Card No.":"ano","General Registration No.":"gno",
                                 "Date of Admission":"doa","Standard":"std","Division":"div","Class Teacher's Name":"ctname","House Colour":"hcolor",
                                 "Roll No.":"rno","Teacher's Remarks":"trem"}         
                            
                            # Update button in edit student info
                            def update(b,name_ent,grno_ent,upda_ent):
                                cur.execute("UPDATE StudentData SET "+b+"='"+upda_ent+"' WHERE name='"+name_ent+"' AND gno='"+grno_ent+"'")
                                con.commit()
                                messagebox.showinfo('Updated','Updated Successfully')
                            def getval(val):
                                for key in dict1.keys():
                                    if key==val:
                                        return dict1[key]  
                            
                            d = getval(a.get())
                                
                            upda = tk.Button(newwindow3,text = 'UPDATE',command = lambda:update(d,ent1.get(),ent3.get(),y.get("1.0","end-1c")),
                                         anchor = tk.NW,fg = '#18120F',bg = '#C7A196',font = ("Cambria",14,"bold"),justify = tk.LEFT)
                            upda.place(x = 200,y = 450)
                        
                        # If any option is not selected
                        except IndexError:
                            messagebox.showerror("Error","Please select an option")
                    a = tk.StringVar()
                    m = tk.Button(newwindow3,text = "Enter",command = getElement,anchor = tk.NW,fg = '#18120F',bg = '#C7A196',
                                 font = ("Cambria",14,"bold"),justify = tk.LEFT)
                    m.place(x = 200,y = 80)
                    
                    newwindow3.mainloop()

                # Edit student info button
                edit = tk.Button(newwindow1,text = 'Edit Student Info',anchor = tk.NW,fg = '#18120F',bg = '#C7A196',
                                 font = ("Cambria",10,"bold"),justify = tk.LEFT,command = eedit)
                edit.place(x = 588,y = 640)
                
                # Back button
                back = tk.Button(newwindow1,text = "Back",command = newwindow1.destroy,anchor = tk.NW,fg = '#18120F',bg = '#C7A196',
                                 font = ("Cambria",10,"bold"),justify = tk.LEFT)
                back.place(x = 10, y = 640)

                # Add new student button
                new = tk.Button(newwindow1,text = "Add New Student",command = addnew,anchor = tk.NW,fg = '#18120F',bg = '#C7A196',
                                 font = ("Cambria",10,"bold"),justify = tk.LEFT)
                new.place(x = 300, y = 640)
                newwindow1.mainloop()

            # If password is incorrect
            else:
                messagebox.showerror('Incorrect Password','Your Username or Password was Incorrect.Try Again') 
        
        # For Principal login
        if(radio.get()==1):
            cur.execute("SELECT username FROM PrincipalData")
            a = cur.fetchall()
            count=0
            for i in range(0,len(a)):
                if(a[i][0]==name_enter):
                    count = 0
                    break
                count=count+1
            if(count!=0):
                messagebox.showerror('Incorrect Password','Your Username or Password was Incorrect.Try Again')
            cur.execute("SELECT password FROM PrincipalData WHERE username='"+name_enter+"'")
            if(password_enter==cur.fetchone()[0]):
                newwindow2 = tk.Toplevel(window)
                newwindow2.geometry("770x700")
                newwindow2.configure(bg = '#583830')

                newwindow2.title("Hariyana Vidya Mandir")

                loginas_label = tk.Label(newwindow2, text = "Logged in as Principal",width = 100,justify = tk.LEFT,anchor = tk.NW,
                         font = ("PT Sans",20,"bold"),bg = '#FDD4B8')
                loginas_label.place(x = 0,y = 0)

                class Heads:
                    def __init__(self,text,width,x,y):
                        self.text = text
                        self.width = width
                        self.x = x
                        self.y = y
        
                        self.label = tk.Label(newwindow2,text = self.text,width = self.width,font = ("Cambria",14,"bold"),justify = tk.LEFT,
                            anchor = tk.NW,fg = '#18120F',bg = '#C7A196')
                        self.label.place(x = self.x,y = self.y)

                class Values:
                    def __init__(self,text,width,x,y):
                        self.text = text
                        self.width = width
                        self.x = x
                        self.y = y
        
                        cur.execute("SELECT " + self.text + " FROM PrincipalData WHERE username='"+name_enter+"' AND password='"+password_enter+"'")
                        self.text_var = tk.StringVar()
                        self.text_var.set(cur.fetchone())
                        if(self.text=='photo'):
                            self.label = tk.Label(newwindow2,textvariable = self.text_var,width = self.width,height = 9,
                                  fg = '#18120F',bg = '#FDD4B8')
                            self.label.place(x = self.x,y = self.y)
                        elif(self.text=='addr'):
                            self.label = tk.Label(newwindow2,textvariable = self.text_var,width = self.width,font = ("Cambria",14),
                                  justify = tk.LEFT,wraplength = 600,anchor = tk.NW,fg = '#18120F',bg = '#FDD4B8')
                            self.label.place(x = self.x,y = self.y)
                        elif(self.text=='tfor'):
                            self.label = tk.Label(newwindow2,textvariable = self.text_var,width = self.width,font = ("Cambria",14),
                                  justify = tk.LEFT,wraplength = 550,anchor = tk.NW,fg = '#18120F',bg = '#FDD4B8')
                            self.label.place(x = self.x,y = self.y)
                        else:    
                            self.label = tk.Label(newwindow2,textvariable = self.text_var,width = self.width,font = ("Cambria",14),
                                  justify = tk.LEFT,anchor = tk.NW,fg = '#18120F',bg = '#FDD4B8')
                            self.label.place(x = self.x,y = self.y)

                blank_label = tk.Label(newwindow2,width = 59,font = ("Cambria",14),fg = '#18120F',bg = '#FDD4B8')
                blank_label.place(x = 105,y = 310)
                blank_label = tk.Label(newwindow2,width = 59,font = ("Cambria",14),fg = '#18120F',bg = '#FDD4B8')
                blank_label.place(x = 105,y = 335)
                blank_label = tk.Label(newwindow2,width = 54,font = ("Cambria",14),fg = '#18120F',bg = '#FDD4B8')
                blank_label.place(x = 155,y = 560)

                name = Heads('First Name:',12,10,70)
                name1 = Values('name',12,155,70)
                lname = Heads('Last Name:',13,295,70)
                lname1 = Values('lname',12,450,70)
                fname = Heads('Middle Name:',12,10,125)
                fname1 = Values('fname',12,155,125)
                mname = Heads("Mother's Name:",13,295,125)
                mname1 = Values('mname',12,450,125)
                dob = Heads('Date of Birth:',12,10,180)
                dob1 = Values('dob',12,155,180)
                bplace = Heads('Birth Place:',12,295,180)
                bplace1 = Values('bplace',13,440,180)
                photo = Values('photo',15,590,70)
                nation = Heads('Nationality:',10,10,235)
                nation1 = Values('nation',7,134,235)
                relig = Heads("Religion:",10,232,235)
                relig1 = Values('relig',12,357,235)
                caste = Heads("Caste:",6,505,235)
                caste1 = Values('caste',11,585,235)
                addr = Heads("Address:",7,10,290)
                addr1 = Values('addr',59,105,290)
                mno = Heads('Mobile No.:',9,10,390)
                mno1 = Values('mno',23,120,390)
                adno = Heads("Aadhaar Card No.:",15,365,390)
                adno1 = Values('adno',15,545,390)
                trno = Heads("Teacher's Registration No.:",23,10,440)
                trno1 = Values('trno',6,280,440)
                ctfc = Heads("Position:",10,372,440)
                ctfc1 = Values('pos',19,505,440)
                staught = Heads("Subjects Taught:",15,10,490)
                staught1 = Values('staught',50,195,490)
                taught = Heads("Teacher For:",11,10,540)
                taught1 = Values('tfor',54,155,540)
                
                # Method for adding new teacher
                def addnew():
                    newwindow6 = tk.Toplevel(newwindow2)

                    newwindow6.geometry("1000x1000")
                    newwindow6.configure(bg = '#583830')

                    newwindow6.title("Hariyana Vidya Mandir")

                    loginas_label = tk.Label(newwindow6, text = "Logged in as Principal",width = 100,justify = tk.LEFT,anchor = tk.NW,
                         font = ("PT Sans",20,"bold"),bg = '#FDD4B8')
                    loginas_label.place(x = 0,y = 0)
                    
                    def added(name1,lname1,fname1,mname1,dob1,bplace1,nation1,relig1,caste1,addr1,mno1,adno1,grno1,ctfc1,staught1,tfor1,photo1,username1,password1):
                        cur.execute("INSERT INTO TeacherData VALUES('"+name1+"','"+lname1+"','"+fname1+"','"+mname1+"','"+dob1+"','"+bplace1+"','"+nation1+"','"+relig1+"','"+caste1+"','"+addr1+"','"+mno1+"','"+adno1+"','"+grno1+"','"+ctfc1+"','"+staught1+"','"+photo1+"','"+username1+"','"+password1+"','"+tfor1+"')")
                        con.commit()
                        messagebox.showinfo("Successful!","New Teacher Details Added Successfully")

                    class Heads:
                        def __init__(self,text,width,x,y):
                            self.text = text
                            self.width = width
                            self.x = x
                            self.y = y
        
                            self.label = tk.Label(newwindow6,text = self.text,width = self.width,font = ("Cambria",14,"bold"),justify = tk.LEFT,
                              anchor = tk.NW,fg = '#18120F',bg = '#C7A196')
                            self.label.place(x = self.x,y = self.y)

                    class Values:
                        def __init__(self,width,x,y):
                            self.width = width
                            self.x = x
                            self.y = y
        
                            self.enter = tk.Entry(newwindow6,width = self.width,font = ("Cambria",14),
                              fg = '#18120F',bg = '#FDD4B8')
                            self.enter.place(x = self.x,y = self.y)
                        def ret(self):
                            return self.enter.get()
                    
                    name = Heads('First Name:',12,10,70)
                    name1 = Values(12,155,70)
                    lname = Heads('Last Name:',13,295,70)
                    lname1 = Values(12,450,70)
                    fname = Heads('Middle Name:',12,10,125)
                    fname1 = Values(12,155,125)
                    mname = Heads("Mother's Name:",13,295,125)
                    mname1 = Values(12,450,125)
                    dob = Heads('Date of Birth:',12,10,180)
                    dob1 = Values(12,155,180)
                    bplace = Heads('Birth Place:',12,295,180)
                    bplace1 = Values(13,440,180)
                    nation = Heads('Nationality:',10,10,235)
                    nation1 = Values(7,134,235)
                    relig = Heads("Religion:",10,232,235)
                    relig1 = Values(12,357,235)
                    caste = Heads("Caste:",6,505,235)
                    caste1 = Values(11,585,235)
                    addr = Heads("Address:",7,10,290)
                    addr1 = tk.Text(newwindow6,width = 55,font = ("Cambria",14),height = 3,
                              fg = '#18120F',bg = '#FDD4B8')
                    addr1.place(x = 108,y = 290)
                    mno = Heads('Mobile No.:',10,10,390)
                    mno1 = Values(20,134,390)
                    adno = Heads("Aadhaar Card No.:",15,365,390)
                    adno1 = Values(15,545,390)
                    trno = Heads("Teacher's Registration No.:",23,10,440)
                    trno1 = Values(6,280,440)
                    ctfc = Heads("Class Teacher for Class:",20,378,440)
                    ctfc1 = Values(9,615,440)
                    staught = Heads("Subjects Taught:",15,10,490)
                    staught1 = Values(47,195,490)
                    taught = Heads("Teacher For:",11,10,540)
                    taught1 = tk.Text(newwindow6,width = 51,font = ("Cambria",14),height = 2,
                              fg = '#18120F',bg = '#FDD4B8')
                    taught1.place(x = 148,y = 540)
                    username = Heads("Username:",10,600,125)
                    username1 = Values(15,720,125)
                    password = Heads("Password:",10,600,180)
                    password1 = Values(15,720,180)
                    photo = Heads("Photo:",10,600,70)
                    photo1 = Values(15,720,70)
                    
                    back = tk.Button(newwindow6,text = "Back",command = newwindow6.destroy,anchor = tk.NW,fg = '#18120F',bg = '#C7A196',
                                 font = ("Cambria",10,"bold"),justify = tk.LEFT)
                    back.place(x = 10, y = 640)
                    enter1 = tk.Button(newwindow6,text = "Enter",command = lambda:added(name1.ret(),lname1.ret(),fname1.ret(),mname1.ret(),dob1.ret(),bplace1.ret(),nation1.ret(),relig1.ret(),caste1.ret(),addr1.get("1.0","end-1c"),mno1.ret(),adno1.ret(),trno1.ret(),ctfc1.ret(),staught1.ret(),taught1.get("1.0","end-1c"),photo1.ret(),username1.ret(),password1.ret()),
                                       anchor = tk.NW,fg = '#18120F',bg = '#C7A196',
                                 font = ("Cambria",10,"bold"),justify = tk.LEFT)
                    enter1.place(x = 500, y = 640)
                    newwindow6.mainloop()

                # Method for editing teacher information
                def eedit1():
                    newwindow4 = tk.Toplevel(newwindow2)
                    newwindow4.geometry('700x800')
                    newwindow4.configure(bg = '#583830')
                    newwindow4.title("Hariyana Vidya Mandir")
                    loginas_label = tk.Label(newwindow4, text = "Logged in as Principal",width = 100,justify = tk.LEFT,anchor = tk.NW,
                             font = ("PT Sans",20,"bold"),bg = '#FDD4B8')
                    loginas_label.place(x = 0,y = 0)
                    drop = tk.Listbox(newwindow4,width = 23,height = 16,fg = '#18120F',bg = '#FDD4B8')
                    drop.insert(1,'First Name')
                    drop.insert(2,'Last Name')
                    drop.insert(3,'Middle Name')
                    drop.insert(4,'Mother\'s Name')
                    drop.insert(5,'Date of Birth')
                    drop.insert(6,'Birth Place')
                    drop.insert(7,'Nationality')
                    drop.insert(8,'Religion')
                    drop.insert(9,'Caste')
                    drop.insert(10,'Address')
                    drop.insert(11,'Mobile No.')
                    drop.insert(12,'Aadhaar Card No.')
                    drop.insert(13,'General Registration No.')
                    drop.insert(14,'Class Teacher for Class')
                    drop.insert(15,'Subjects Taught')
                    drop.insert(16,'Teacher for')
                    drop.place(x = 20,y = 80)
                    
                    
                    def getElement():
                        selection = drop.curselection()
                        try:
                            index = selection[0]
                            value = drop.get(index)
                            a.set(value)
                            ent = tk.Label(newwindow4,text = "Enter Teacher's Frist Name:",width = 22,anchor = tk.NW,
                                       fg = '#18120F',bg = '#C7A196',font = ("Cambria",14,"bold"),justify = tk.LEFT)
                            ent.place(x = 200,y = 150)
                            ent1 = tk.Entry(newwindow4,width = 15,font = ("Cambria",14))
                            ent1.place(x = 470,y = 150)
                            ent2 = tk.Label(newwindow4,text = "Enter Teacher's Reg. No.:",width = 22,anchor = tk.NW,
                                        fg = '#18120F',bg = '#C7A196',font = ("Cambria",14,"bold"),justify = tk.LEFT)
                            ent2.place(x = 200,y = 200)
                            ent3 = tk.Entry(newwindow4,width = 15,font = ("Cambria",14))
                            ent3.place(x = 470,y = 200)
                            x = tk.Label(newwindow4,textvariable = a,anchor = tk.NW,fg = '#18120F',bg = '#C7A196',
                                    font = ("Cambria",14,"bold"),justify = tk.LEFT)
                            x.place(x = 200,y = 250)
                            y = tk.Text(newwindow4,width = 40,height = 4,font = ("Cambria",14))
                            y.place(x = 200, y = 300)
                            back = tk.Button(newwindow4,text = "Back",command = newwindow4.destroy,anchor = tk.NW,fg = '#18120F',bg = '#C7A196',
                                 font = ("Cambria",14,"bold"),justify = tk.LEFT)
                            back.place(x = 550, y = 450)
                            dict1 = { "First Name":"name","Last Name":"lname","Middle Name":"fname","Mother's Name":"mname","Date of Birth":"dob",
                                "Birth Place":"bplace","Nationality":"nation","Religion":"relig","Caste":"caste","Address":"addr",
                                 "Mobile No.":"mno","Aadhaar Card No.":"ano","Teacher's Registration No.":"trno",
                                 "Class Teacher for Class":"ctfc","Subjects Taught":"staught","Teacher for":"tfor" }
                                       
                            if a.get() in dict1.keys():
                                c = a.get()
                                b = dict1[c]
                            def update(b,name_ent,grno_ent,upda_ent):
                                cur.execute("UPDATE TeacherData SET "+b+"='"+upda_ent+"' WHERE name='"+name_ent+"' AND trno='"+grno_ent+"'")
                                con.commit()
                                messagebox.showinfo('Updated','Updated Successfully')
                            upda = tk.Button(newwindow4,text = 'UPDATE',command = lambda:update(b,ent1.get(),ent3.get(),y.get("1.0","end-1c")),
                                         anchor = tk.NW,fg = '#18120F',bg = '#C7A196',font = ("Cambria",14,"bold"),justify = tk.LEFT)
                            upda.place(x = 200,y = 450)
                        except IndexError:
                            messagebox.showerror("Error","Please select an option")
                        
                    a = tk.StringVar()
                    m = tk.Button(newwindow4,text = "Enter",command = getElement,anchor = tk.NW,fg = '#18120F',bg = '#C7A196',
                                 font = ("Cambria",14,"bold"),justify = tk.LEFT)
                    m.place(x = 200,y = 80)
                    newwindow4.mainloop()
                
                # Edit teacher info button
                edit1 = tk.Button(newwindow2,text = 'Edit Teacher Info',anchor = tk.NW,fg = '#18120F',bg = '#C7A196',
                                 font = ("Cambria",10,"bold"),justify = tk.LEFT,command = eedit1)
                edit1.place(x = 588,y = 640)

                # Back button
                back = tk.Button(newwindow2,text = "Back",command = newwindow2.destroy,anchor = tk.NW,fg = '#18120F',bg = '#C7A196',
                                 font = ("Cambria",10,"bold"),justify = tk.LEFT)
                back.place(x = 10, y = 640)

                # Adding new teacher button
                new = tk.Button(newwindow2,text = "Add New Teacher",command = addnew,anchor = tk.NW,fg = '#18120F',bg = '#C7A196',
                                 font = ("Cambria",10,"bold"),justify = tk.LEFT)
                new.place(x = 170, y = 640)

                # Method for editing personal information
                def eedit2():
                    newwindow5 = tk.Toplevel(newwindow2)
                    newwindow5.geometry('700x800')
                    newwindow5.configure(bg = '#583830')
                    newwindow5.title("Hariyana Vidya Mandir")
                    loginas_label = tk.Label(newwindow5, text = "Logged in as Principal",width = 100,justify = tk.LEFT,anchor = tk.NW,
                             font = ("PT Sans",20,"bold"),bg = '#FDD4B8')
                    loginas_label.place(x = 0,y = 0)
                    drop = tk.Listbox(newwindow5,width = 23,height = 16,fg = '#18120F',bg = '#FDD4B8')
                    drop.insert(1,'First Name')
                    drop.insert(2,'Last Name')
                    drop.insert(3,'Middle Name')
                    drop.insert(4,'Mother\'s Name')
                    drop.insert(5,'Date of Birth')
                    drop.insert(6,'Birth Place')
                    drop.insert(7,'Nationality')
                    drop.insert(8,'Religion')
                    drop.insert(9,'Caste')
                    drop.insert(10,'Address')
                    drop.insert(11,'Mobile No.')
                    drop.insert(12,'Aadhaar Card No.')
                    drop.insert(13,'General Registration No.')
                    drop.insert(14,'Position')
                    drop.insert(15,'Subjects Taught')
                    drop.insert(16,'Teacher for')
                    drop.place(x = 20,y = 80)
                    
                    
                    def getElement1():
                        selection = drop.curselection()
                        try:
                            index = selection[0]
                            value = drop.get(index)
                            a.set(value)
                            ent = tk.Label(newwindow5,text = "Enter Your First Name:",width = 22,anchor = tk.NW,
                                       fg = '#18120F',bg = '#C7A196',font = ("Cambria",14,"bold"),justify = tk.LEFT)
                            ent.place(x = 200,y = 150)
                            ent1 = tk.Entry(newwindow5,width = 15,font = ("Cambria",14))
                            ent1.place(x = 470,y = 150)
                            ent2 = tk.Label(newwindow5,text = "Enter Your Reg. No.:",width = 22,anchor = tk.NW,
                                        fg = '#18120F',bg = '#C7A196',font = ("Cambria",14,"bold"),justify = tk.LEFT)
                            ent2.place(x = 200,y = 200)
                            ent3 = tk.Entry(newwindow5,width = 15,font = ("Cambria",14))
                            ent3.place(x = 470,y = 200)
                            x = tk.Label(newwindow5,textvariable = a,anchor = tk.NW,fg = '#18120F',bg = '#C7A196',
                                    font = ("Cambria",14,"bold"),justify = tk.LEFT)
                            x.place(x = 200,y = 250)
                            y = tk.Text(newwindow5,width = 40,height = 4,font = ("Cambria",14))
                            y.place(x = 200, y = 300)
                            back = tk.Button(newwindow5,text = "Back",command = newwindow5.destroy,anchor = tk.NW,fg = '#18120F',bg = '#C7A196',
                                 font = ("Cambria",14,"bold"),justify = tk.LEFT)
                            back.place(x = 550, y = 450)
                            dict2 = {"First Name":"name","Last Name":"lname","Middle Name":"fname","Mother's Name":"mname","Date of Birth":"dob",
                                "Birth Place":"bplace","Nationality":"nation","Religion":"relig","Caste":"caste","Address":"addr",
                                 "Mobile No.":"mno","Aadhaar Card No.":"adno","Teacher's Registration No.":"trno",
                                 "Position":"pos","Subjects Taught":"staught","Teacher for":"tfor"}
                            
                            
                            if a.get() in dict2.keys():
                                c = a.get()
                                d = dict2[c]
                                                        
                            def update1(b,name_ent,grno_ent,upda_ent):
                                cur.execute("UPDATE PrincipalData SET "+b+"='"+upda_ent+"' WHERE name='"+name_ent+"' AND trno='"+grno_ent+"'")
                                con.commit()
                                messagebox.showinfo('Updated','Updated Successfully')
                                
                            upda = tk.Button(newwindow5,text = 'UPDATE',command = lambda:update1(d,ent1.get(),ent3.get(),y.get("1.0","end-1c")),
                                         anchor = tk.NW,fg = '#18120F',bg = '#C7A196',font = ("Cambria",14,"bold"),justify = tk.LEFT)
                            upda.place(x = 200,y = 450)

                        except IndexError:
                            messagebox.showerror("Error","Please select an option")
                        
                    a = tk.StringVar()
                    m = tk.Button(newwindow5,text = "Enter",command = getElement1,anchor = tk.NW,fg = '#18120F',bg = '#C7A196',
                                 font = ("Cambria",14,"bold"),justify = tk.LEFT)
                    m.place(x = 200,y = 80)
                    newwindow5.mainloop()
                    
                # Editing personal information button
                edit1 = tk.Button(newwindow2,text = 'Edit Personal Info',anchor = tk.NW,fg = '#18120F',bg = '#C7A196',
                                 font = ("Cambria",10,"bold"),justify = tk.LEFT,command = eedit2)
                edit1.place(x = 350,y = 640)
                newwindow2.mainloop() 
            # If password is incorrect  
            else:
                messagebox.showerror('Incorrect Password','Your Username or Password was Incorrect.Try Again') 

window.mainloop() 
con.close()      
