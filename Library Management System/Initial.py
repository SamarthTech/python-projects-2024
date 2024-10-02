from tkinter import *
from tkinter import font
import mysql.connector
from tkinter import messagebox as msg
from Library_Management import main

class login:
    def __init__(self):
        #connecting DB
        self.con = mysql.connector.connect(host="localhost", user="root", password="2005")
        self.cursor = self.con.cursor()
        self.cursor.execute("Create database if not exists Library;")
        self.cursor.execute("use Library;")
        self.cursor.execute("create table if not exists admininfo(adminid varchar(7) not null primary key, aname char(35), password char(18));")

        #creating root
        self.root=Tk()
        self.root.geometry('500x300+150+100')

        #creating frames
        self.root.title('Login')
        self.frm1=Frame(self.root,width=490,height=50,bd=3,relief=SUNKEN,bg='#4589aa')
        self.frm1.place(x=5,y=2)
        self.frm2=Frame(self.root,width=490,height=240,bd=3,relief=SUNKEN,bg='#4589aa')
        self.frm2.place(x=5,y=54)
        self.option=IntVar()
        self.option.set(1)

        '''self.root.overrideredirect(True)
        Button(self.frm1,text="X",fg='white',bg='red',width=5,height=5,relief='solid',font=('Helvetica',12,font.BOLD),command=self.root.destroy).place(x=460,y=0)'''

        #placing,defining buttons,labels,entryboxes
        self.b1=Radiobutton(self.frm1,bg='#4589aa',variable=self.option,value=1,text="Login",font=('Helvetica',15,font.BOLD),command=self.select)
        self.b1.place(x=100,y=5)#login
        
        self.b2=Radiobutton(self.frm1,bg='#4589aa',variable=self.option,value=2,text="New User",font=('Helvetica',15,font.BOLD),command=self.select)
        self.b2.place(x=300,y=5)#register

        Label(self.frm2,text='User Name:',font=('Helvetica',12,font.BOLD),bg='#4589aa').place(x=50,y=20)#labels
        Label(self.frm2,text='Password:',font=('Helvetica',12,font.BOLD),bg='#4589aa').place(x=50,y=70)
        Label(self.frm2,text='Confirm Password:',font=('Helvetica',12,font.BOLD),bg='#4589aa').place(x=50,y=120)

        self.un=Entry(self.frm2,font=('Helvetica',12,font.BOLD),relief=RIDGE,bd=5)       
        self.un.place(x=250,y=20)#username
        
        self.pwd=Entry(self.frm2,show='*',font=('Helvetica',12,font.BOLD),relief=RIDGE,bd=5)
        self.pwd.place(x=250,y=70)#password
        self.pwd.bind('<KeyPress>',lambda k:self.enabled(k,1))
        
        self.cnfpwd=Entry(self.frm2,show='*',font=('Helvetica',12,font.BOLD),relief=RIDGE,bd=5,state=DISABLED)       
        self.cnfpwd.place(x=250,y=120)#confirm password
        self.cnfpwd.bind('<KeyRelease>',lambda k:self.enabled1(k))
        
        self.b3=Button(self.root,bg="#deadaf",text="Login",font=('Helvetica',14,font.BOLD),relief=RAISED,bd=5,state=DISABLED,command=self.fun)
        self.b3.place(x=130,y=240)#login button

        self.b4=Button(self.root,bg="#deadaf",text="Cancel",font=('Helvetica',14,font.BOLD),relief=RAISED,bd=5,command=self.cancel)
        self.b4.place(x=280,y=240)#cancel button




        self.con.commit()
        self.cursor.close()

        self.root.mainloop()
    def select(self):#from radio buttons
        if self.option.get()==1:#from login
            self.un.delete(0,END)
            self.pwd.delete(0,END)
            self.cnfpwd.delete(0,END)
            self.b3.config(text='Login')

        elif self.option.get()==2:#from register
            self.un.delete(0, END)
            self.pwd.delete(0,END)
            self.cnfpwd.delete(0,END)
            self.b3.config(text='Register')

        self.cnfpwd['state']=DISABLED
        self.b3['state']=DISABLED

    def enabled(self,e,a):#from password, enables confirm password
        if a==1:
            self.cnfpwd['state']=NORMAL

    def enabled1(self,event):#after tab, checks both passwords and enables login/register
        if self.cnfpwd.get()==self.pwd.get():
            self.b3['state']=NORMAL

    def cancel(self):#clears all entry boxes
        self.un.delete(0,END)
        self.pwd.delete(0,END)
        self.cnfpwd.delete(0,END)
        self.cnfpwd['state']=DISABLED
        self.b3['state']=DISABLED

    def fun(self):#to login/register
        cursor = self.con.cursor()
        if self.option.get()==1:#to login
            cursor.execute("select Password from admininfo where aname='%s';"%self.un.get())
            r=cursor.fetchall()
            if len(r)==0:
                msg.showerror("Alert!!!!","Admin Doesn't exist")
                self.cancel()
                return
            if self.pwd.get()==r[0][0]:
                self.root.destroy()
                main()
            else:
                self.cancel()




        elif self.option.get()==2:#new admin registration
            st="insert into AdminInfo (AdminId,aname,Password) values('{}','{}','{}');".format(self.adminid(),self.un.get(),self.pwd.get())
            cursor.execute(st)
            msg.showinfo("Success","Admin successfully registered")
            self.option.set(1)
            self.select()
            self.cancel()

        self.con.commit()
        cursor.close()

    def adminid(self):#generates an adminid
        self.cursor = self.con.cursor()
        self.cursor.execute("select count(*) from admininfo;")
        r=self.cursor.fetchall()
        if r[0][0]>0:
            self.cursor.execute("select adminid from admininfo;")
            ad = self.cursor.fetchall()
            max=0
            for i in ad:
                if int(str(i[0])[1::])>max:
                    max=int(str(i[0])[1::])
            s = 'A' + '0' * (4 - len(str(max+1))) + str(max + 1)
        elif r[0][0]==0:
            s='A0001'
        self.con.commit()
        self.cursor.close()
        return s


login()
