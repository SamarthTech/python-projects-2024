import tkinter.font as font
from tkinter import *
from tkinter import ttk
import mysql.connector
from PIL import Image, ImageTk
from Search_Combobox import *
from Tables import *
from graph_income import Graph
class main:
    def __init__(self):
        self.con = mysql.connector.connect(host="localhost",user="root",password="2005")
        self.cursor = self.con.cursor()
        self.root = Tk()
        w=self.root.winfo_screenwidth()
        h=self.root.winfo_screenheight()
        self.root.title("Library Management")
        self.root.geometry(str(w)+'x'+str(h)+'+0+5')
        self.root.resizable(True,True)

        #self.cursor.execute("Create database if not exists Library")
        self.cursor.execute("use library")
        self.cursor.execute("create table if not exists BookDetails(bookid char(10) not null primary key,bkname char(35),author char(35),qty int, cost int)")
        self.cursor.execute("create table if not exists purchase(orderid int not null primary key,bookid char(10) not null,pdate date,quantity int,totalcost int, foreign key (bookid) references bookdetails(bookid))")
        self.cursor.execute("create table if not exists UserDetails(mid varchar(7) primary key,mname text(20),contact BIGINT(20), regdate date, address varchar(50));")
        self.cursor.execute("create table if not exists book_issue_return(IssueId char(10) not null primary key,Mid varchar(7),Bid int, Issuedate date, Returndate date, Fine int, Status char(10));")

        self.frm1 = Frame(self.root, width=1350, height=145, bd=3, relief=SUNKEN, bg='#4589aa')
        self.frm1.place(x=3, y=3)

        self.frm3 = Frame(self.root, width=173, height=190, bd=3, relief=SUNKEN, bg='#4589aa')
        self.frm3.place(x=3, y=150)

        self.frm2 = Frame(self.root, width=903, height=500, bd=3, relief=SUNKEN, bg='#4589aa')
        self.frm2.place(x=178, y=190)

        self.frm4 = Frame(self.root, width=173, height=210, bd=3, relief=SUNKEN, bg='#4589aa')
        self.frm4.place(x=3, y=321)

        self.frm5 = Frame(self.root, width=173, height=180, bd=3, relief=SUNKEN, bg='#4589aa')
        self.frm5.place(x=3, y=507)

        self.frm6 = Frame(self.root, width=266, height=145, bd=3, relief=SUNKEN, bg='#4589aa')
        self.frm6.place(x=1083, y=150)

        self.frm7 = Frame(self.root, width=266, height=394, bd=3, relief=SUNKEN, bg='#4589aa')
        self.frm7.place(x=1083, y=297)

        self.frm8 = Frame(self.root, width=903, height=38, bd=3, relief=SUNKEN, bg='#4589aa')
        self.frm8.place(x=178, y=150)
        Label(self.frm8, text="CREATED BY: OM PANDEY AIML - A", fg='#deadaf',bg='#4589aa',width=50,font=('Helvetica',13,font.BOLD)).place(x=205, y=5)

        img1 = ImageTk.PhotoImage(file='librarymngt3.2.jpg', width=0, height=0)
        Label(self.frm2, image=img1, width=890, height=485).place(x=2, y=1)

        img2 = ImageTk.PhotoImage(file='librarymngt2.1.jpg', width=50, height=0)
        Label(self.frm1, image=img2, width=1330, height=125).place(x=5, y=5)

        img3 = ImageTk.PhotoImage(file='librarymngt4.1.jpg', width=0, height=0)
        Label(self.frm7, image=img3, width=265, height=385).place(x=0, y=0)

        Label(self.frm4, text=' B O O K S : ',fg='#deadaf',bg='#4589aa',width=11,font=('Helvetica',13,font.BOLD)).place(x=25, y=14)

        self.b1 = Button(self.frm4, text="Book Details", width=15, command=lambda: bookdetails(self.con), relief=SUNKEN, bd=5, bg="#deadaf")
        self.b1.place(x=23, y=50)

        self.b2 = Button(self.frm4, text="Book Issue/Return", width=15, command=lambda: issue(self.con), relief=SUNKEN, bd=5,bg="#deadaf")
        self.b2.place(x=23, y=90)

        self.b3 = Button(self.frm4, text="Purchase Details", width=15, command=lambda: purchase(self.con), relief=SUNKEN, bd=5, bg="#deadaf")
        self.b3.place(x=23, y=130)

        Label(self.frm5, text='A D M I N  & ', fg='#deadaf', bg='#4589aa', width=11,font=('Helvetica', 13, font.BOLD)).place(x=25, y=10)
        Label(self.frm5, text=' U S E R S : ', fg='#deadaf', bg='#4589aa', width=11,font=('Helvetica', 13, font.BOLD)).place(x=25, y=35)

        self.b4 = Button(self.frm5, text="Member Details", width=15, command=lambda : UserDetails(self.con), relief=SUNKEN, bd=5, bg="#deadaf")
        self.b4.place(x=23, y=65)

        self.b5 = Button(self.frm5, text="Admin Details", width=15, relief=SUNKEN, command=lambda: AdminInfo(self.con), bd=5, bg="#deadaf")
        self.b5.place(x=23, y=115)

        Label(self.frm3, text=' S E A R C H by : ', fg='#deadaf', bg='#4589aa', width=15,font=('Helvetica', 13, font.BOLD)).place(x=8, y=20)

        self.cmbvar1 = StringVar()
        self.cmbvar1.set('                SELECT')
        self.l=['Book Name','Book Author','Member Id']
        self.cmbsearch = ttk.Combobox(self.frm3, width=21, textvariable=self.cmbvar1, values=self.l)
        self.cmbsearch.place(x=10, y=55)
        self.cmbsearch.bind('<<ComboboxSelected>>',self.enabler)

        Label(self.frm3,text="Press Tab to search",fg='#deadaf', bg='#4589aa', width=15,font=('Helvetica', 11, font.BOLD)).place(x=15, y=140)

        self.e1 = Entry(self.frm3,width=16,font=('Helvetica', 12, font.BOLD),relief=SUNKEN, bd=5,state=DISABLED)
        self.e1.place(x=7,y=95)
        self.e1.bind('<KeyPress>',self.view)

        Label(self.frm6, text='    F I N A N C E :    ', fg='#deadaf', bg='#4589aa', width=18, font=('Helvetica', 13, font.BOLD)).place(x=38, y=14)
        self.b6 = Button(self.frm6, text="Income Details", width=18, relief=SUNKEN, command=lambda: finance(self.con), bd=5, bg="#deadaf")
        self.b6.place(x=53, y=50)

        self.b7 = Button(self.frm6, text="Monthly Income Graph", width=18, relief=SUNKEN, command=lambda: Graph(self.con), bd=5, bg="#deadaf")
        self.b7.place(x=53, y=90)

        self.root.mainloop()

    def enabler(self,event):
        self.e1.configure(state=NORMAL)

    def view(self,event):
        if event.char=='\t':
            values=(self.cmbsearch.get())
            st=self.e1.get()
            if(values=="Book Name"):
                cmbxBKNAME(self.con, st)
            elif(values=="Book Author"):
                cmbxAUTHOR(self.con, st)
            elif(values=="Member Id"):
                cmbxMEMBER(self.con, st)

main()

