from tkinter import *
from tkinter import font
from tkinter import ttk
from datetime import date, timedelta


class AdminInfo:
    def __init__(self, con):
        self.con = con
        self.cursor = self.con.cursor()

        self.root = Toplevel()
        self.root.geometry("1250x600+5+10")
        self.root.configure(bg="#192734")
        '''remove the title bar'''
        # self.root.overrideredirect(True)  # Remove default title bar
        # add a button to close the window overriding the title bar
        # Button(text="X", fg='white', bg='red', width=2, relief='solid', font=('Helvetica', 12, font.BOLD),
        # command=self.root.destroy).place(x=1220, y=0)
        self.root.resizable(0, 0)

        '''input designs'''
        Label(self.root, text="Admin ID", fg='#FFFFFF', anchor='w', bg='#192734',
              font=('Helvetica', 12, font.BOLD)).place(x=20,
                                                       y=20)

        self.e1 = Entry(self.root, relief=SOLID, bd=5, width=35)
        self.e1.place(x=150, y=20)

        Label(self.root, text="Admin Name", fg='#FFFFFF', anchor='w', bg='#192734',
              font=('Helvetica', 12, font.BOLD)).place(x=20,
                                                       y=60)

        self.e2 = Entry(self.root, relief=SOLID, bd=5, width=35)
        self.e2.place(x=150, y=60)

        Label(self.root, text="Password", fg='#FFFFFF', anchor='w', bg='#192734', width=9,
              font=('Helvetica', 12, font.BOLD)).place(
            x=20, y=100)

        self.e3 = Entry(self.root, relief=SOLID, bd=5, width=35)
        self.e3.place(x=150, y=100)
        '''----------------------------------------------------------------------------'''

        self.l5 = Label(self.root, text="", fg="red", font=('Helvetica', 12, font.BOLD),
                        bg="#192734")
        self.l5.place(x=400, y=550)

        self.b1 = Button(self.root, text="Insert", relief=SOLID, command=self.insert, bd=5, bg="#90aaf5")
        self.b1.place(x=20, y=220)

        self.b2 = Button(self.root, text="Display", relief=SOLID, command=self.display, bd=5, bg="#90aaf5")
        self.b2.place(x=100, y=220)

        self.b3 = Button(self.root, text="Delete", relief=SOLID, command=self.delete, bd=5, fg='#FFFFFF', bg="#f2746b")
        self.b3.place(x=180, y=220)

        self.b4 = Button(self.root, text="Clear", relief=SOLID, command=self.clear, bd=5, bg="#90aaf5")
        self.b4.place(x=260, y=220)

        self.b5 = Button(self.root, text="Update", relief=SOLID, command=self.updatebox, bd=5, bg="#90aaf5")
        self.b5.place(x=320, y=220)

        Label(self.root, text="Highly Confidential", fg='#FFFFFF', bg='#7463f2', font=('Helvetica', 12, font.BOLD)).place(
            x=1070, y=550)


        '''TREE  VIEW'''
        s = ttk.Style()
        s.theme_use('default')
        s.configure('Treeview', relief=SOLID, background="#192734", fieldbackground="#90aaf5", foreground="white")
        s.configure("Treeview.Heading", background="#7463f2", foreground="black")
        self.t = ttk.Treeview(self.root, height=25)
        self.t["show"] = "headings"
        self.t["columns"] = ['Admin Id', 'Admin Name', 'Password']
        for i in range(3):
            self.t.heading(i, text="{}".format(self.t["columns"][i]))
            if i == 0:
                self.t.column(i, width=200)  # Column 0 width is set to 200 pixels
            elif i == 1:
                self.t.column(i, width=200)
            elif i == 2:
                self.t.column(i, width=400)

        self.t.place(x=400, y=20)

        self.e1["state"] = "disabled"
        self.e3["state"] = "disabled"
        self.b1["state"] = "disabled"
        self.b3["state"] = "disabled"
        self.b5["state"] = "disabled"
        if self.count() == 0:
            self.b2["state"] = "disabled"

        self.e2.bind("<KeyPress>", lambda a: self.e3.configure(state=NORMAL))
        self.e3.bind("<KeyPress>", lambda a: self.b1.configure(state=NORMAL))
        self.t.bind("<<TreeviewSelect>>", self.enable)
        self.genID()
        self.display()

        self.root.mainloop()

    def enable(self, e):
        name = self.t.item(self.t.selection())['text']
        if (len(name) > 0):
            self.b3["state"] = "normal"
            self.b5["state"] = "normal"

    def count(self):
        cursor = self.con.cursor()
        cursor.execute("select count(*) from Admininfo;")
        c1 = cursor.fetchall()
        c = c1[0][0]
        self.con.commit()
        cursor.close()
        return c

    def clear(self):
        self.genID()
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)


        # self.e1["state"] = "disabled"
        self.e3["state"] = "disabled"


        self.b1["state"] = "disabled"
        self.b2["state"] = "disabled"
        self.b3["state"] = "disabled"
        self.b5["state"] = "disabled"


    def insert(self):
        cursor = self.con.cursor()
        a1 = self.e1.get()
        a2 = self.e2.get()
        a3 = self.e3.get()

        self.l5.configure(text="")
        if len(a3) != 0 and len(a1) !=0 and len(a2) !=0:
            st = "insert into Admininfo (adminid,aname,password) values('{}','{}','{}')".format(a1,a2,a3)
            cursor.execute(st)
            self.l5.configure(text="Latest insert: Success")
        else:
            self.l5.configure(text="Unsupported value")
        self.clear()
        self.display()
        self.con.commit()
        cursor.close()

    def delete(self):
        cursor = self.con.cursor()
        name = self.t.item(self.t.selection())['text']
        cursor.execute("delete from Admininfo where adminid='%s';" % name)
        self.b3["state"] = "disabled"
        self.l5.configure(text="Last delete: Success")
        self.display()
        self.genID()
        self.con.commit()
        cursor.close()

    def updatebox(self):
        name = self.t.item(self.t.selection())['values']
        '''UPDATE   FRAME'''
        self.frm1 = Frame(self.root, width=350, height=270, bd=3, relief=SUNKEN, bg='#313866')

        Label(self.frm1, text="Admin ID", fg='#FFFFFF', anchor='w', bg='#313866',
              font=('Helvetica', 12, font.BOLD)).place(x=5,
                                                       y=10)

        self.ue1 = Entry(self.frm1, relief=SOLID, bd=5, width=30)
        self.ue1.place(x=150, y=10)

        Label(self.frm1, text="Admin Name", fg='#FFFFFF', anchor='w', bg='#313866',
              font=('Helvetica', 12, font.BOLD)).place(x=5,
                                                       y=50)

        self.ue2 = Entry(self.frm1, relief=SOLID, bd=5, width=30)
        self.ue2.place(x=150, y=50)

        Label(self.frm1, text="Password", fg='#FFFFFF', anchor='w', bg='#313866', width=9,
              font=('Helvetica', 12, font.BOLD)).place(
            x=5, y=90)

        self.ue3 = Entry(self.frm1, relief=SOLID, bd=5, width=30)
        self.ue3.place(x=150, y=90)


        self.ub1 = Button(self.frm1, text="Update", relief=SOLID, command=self.update, bd=5, bg="#90aaf5")
        self.ub1.place(x=5, y=210)

        '''---------------------------------------------------------------------------------------'''

        self.frm1.place(x=20, y=270)
        '''ue1(update entry 1)'''
        self.ue1.config(state=NORMAL)
        self.ue1.delete(0, END)
        self.ue1.insert(0, name[0])
        self.ue1.config(state=DISABLED)
        '''--------------------------'''
        self.ue2.delete(0, END)
        self.ue2.insert(0, name[1])
        self.ue3.delete(0, END)
        self.ue3.insert(0, name[2])


    def update(self):
        cursor = self.con.cursor()
        a1 = self.ue1.get()
        a2 = self.ue2.get()
        a3 = self.ue3.get()


        self.l5.configure(text="")
        if len(a3) != 0 and len(a1) !=0 and len(a2) !=0:
            # update query
            query = 'UPDATE Admininfo SET aname = %s, password = %s WHERE adminid = %s'

            # values to update
            values = (a2,a3,a1)

            # execute query
            cursor.execute(query, values)
            self.l5.configure(text="Latest update: Success")
        else:
            self.l5.configure(text="Unsupported value")

        self.clear()
        self.display()
        self.con.commit()
        cursor.close()
        self.frm1.destroy()

    def display(self):
        c = self.count()
        cursor = self.con.cursor()
        cursor.execute("select * from Admininfo;")
        row = cursor.fetchall()
        x = self.t.get_children()
        for item in x:
            self.t.delete(item)
        for r in row:
            self.t.insert('', 0, text=r[0], values=(r[0], r[1], r[2]))
        if c > 0:
            self.b2["state"] = "normal"
        else:
            self.b2["state"] = "disabled"
        self.con.commit()
        cursor.close()

    def genID(self):
        cursor = self.con.cursor()
        cursor.execute("select adminid from Admininfo order by adminid;")
        r = cursor.fetchall()
        max = 0
        for row in r:
            i = int(row[0][1:])
            if i > max:
                max = i
        max = max + 1
        s2 = 'A' + "0" * (4 - len(str(max))) + str(max)
        self.e1.config(state=NORMAL)
        self.e1.delete(0, END)
        self.e1.insert(0, s2)
        self.e1.config(state=DISABLED)







class finance:
    def __init__(self,con):
        self.con = con
        self.cursor = self.con.cursor()

        self.sum=0

        self.root=Toplevel()
        self.root.geometry('630x486+150+100')

        self.frm1 = Frame(self.root, width=626, height=60, bd=3, relief=SUNKEN, bg='#4589aa')
        self.frm1.place(x=2, y=2)

        self.frm2 = Frame(self.root, width=626, height=420, bd=3, relief=SUNKEN, bg='#4589aa')
        self.frm2.place(x=2, y=64)

        self.option = IntVar()
        self.option.set(2)

        self.b1 = Radiobutton(self.frm1, bg='#4589aa', variable=self.option, value=1, text="Reg. Fees",font=('Helvetica', 15, font.BOLD),command=self.display)
        self.b1.place(x=150, y=5)

        self.b2 = Radiobutton(self.frm1, bg='#4589aa', variable=self.option, value=2, text="Fine",font=('Helvetica', 15, font.BOLD),command=self.display)
        self.b2.place(x=400, y=5)

        self.l=[]
        self.cmbvar1 = StringVar()
        self.cmbvar1.set('                SELECT')
        self.cmb1 = ttk.Combobox(self.frm2, width=21, textvariable=self.cmbvar1,values=self.l)
        self.cmb1.place(x=345, y=18)
        self.cmb1.bind('<<ComboboxSelected>>',self.enable)

        self.esearch = Entry(self.frm2, relief=SUNKEN, bd=5, width=40, state=DISABLED)
        self.esearch.place(x=75, y=15)
        self.esearch.bind("<KeyRelease>",self.search)

        self.b3 = Button(self.frm2, text=" X ",command=self.cancel, relief=SUNKEN, bd=5, bg="red", fg="black")
        self.b3.place(x=505,y=13)

        self.lbl1=Label(self.frm2,relief=SUNKEN,bd=5,bg="#deadaf",width=13)
        self.lbl1.place(x=485,y=385)

        self.a=0
        self.display()

        self.root.mainloop()

    def display(self):
        s = ttk.Style()
        s.theme_use('default')
        s.configure('Treeview', relief=SOLID, background='#90aaf5', fieldbackground="#90aaf5", foreground="black")
        s.configure("Treeview.Heading", background="#deadaf", foreground="black")
        self.t = ttk.Treeview(self.frm2, height=15)
        self.t["show"] = "headings"
        self.t.config(selectmode='none')
        self.t.place(x=7, y=60)

        self.scrol = ttk.Scrollbar(self.frm2, orient=VERTICAL, command=self.t.yview)
        self.t["yscrollcommand"] = self.scrol.set
        self.scrol.place(x=600,y=77,height=300)

        self.esearch.config(state=NORMAL)
        self.esearch.delete(0,END)
        self.esearch.config(state=DISABLED)

        self.cmbvar1 = StringVar()
        self.cmbvar1.set('                SELECT')
        self.cmb1.config(textvariable=self.cmbvar1)

        self.l=[]

        if self.option.get()==1:
            if self.a==0:
                self.t.destroy()
                self.a=1
                self.display()
            else:
                self.t["columns"] = ['MemberId', 'MemberName','Registration Date', 'Fees']
                for i in range(4):
                    self.t.heading(i, text="{}".format(self.t["columns"][i]))
                    self.t.column(i, width=145)
                self.cursor.execute("select * from UserDetails;")
                row=self.cursor.fetchall()
                for r in row:
                    self.t.insert('', 0, text=r[0], values=(r[0], r[1], r[3], '500'))
                self.cursor.execute("select count(*) from UserDetails;")
                self.sum=((self.cursor.fetchall())[0][0])*500

                self.l=['MemberId','MemberName','YearWise']
                self.cmb1.config(values=self.l)


        elif self.option.get()==2:
            if self.a==1:
                self.t.destroy()
                self.a = 0
                self.display()
            else:
                self.t["columns"] = ['IssueId','MemberId','BookID','ReturnDate','Fine/Fees']
                for i in range(5):
                    self.t.heading(i, text="{}".format(self.t["columns"][i]))
                    self.t.column(i, width=116)
                self.cursor.execute("select * from book_issue_return where Status='Returned';")
                row = self.cursor.fetchall()
                for r in row:
                    self.t.insert('', 0, text=r[0], values=(r[0], r[1], r[2],r[4],r[5]))
                self.cursor.execute("select sum(Fine) from book_issue_return;")
                self.sum = (self.cursor.fetchall())[0][0]

                self.l = ['IssueId','MemberId','MemberName','Yearwise']
                self.cmb1.config(values=self.l)

        self.lbl1.config(text='Total = ₹'+str(self.sum))


    def enable(self,e):
        self.esearch.config(state=NORMAL)
        self.esearch.delete(0,END)

        for i in self.t.get_children():
            self.t.delete(i)

        if self.option.get()==1:
            self.cursor.execute("select * from UserDetails;")
            row = self.cursor.fetchall()
            for r in row:
                self.t.insert('', 0, text=r[0], values=(r[0], r[1], r[3], '500'))
            self.cursor.execute("select count(*) from UserDetails;")
            self.sum = ((self.cursor.fetchall())[0][0]) * 500

        elif self.option.get()==2:
            self.cursor.execute("select * from book_issue_return where Status='Returned';")
            row = self.cursor.fetchall()
            for r in row:
                self.t.insert('', 0, text=r[0], values=(r[0], r[1], r[2], r[4], r[5]))
            self.cursor.execute("select sum(Fine) from book_issue_return;")
            self.sum = (self.cursor.fetchall())[0][0]

        self.lbl1.config(text='Total = ₹' + str(self.sum))
        self.sum=0

    def search(self,e):
        a=self.cmb1.get()
        b=self.esearch.get()
        for i in self.t.get_children():
            self.t.delete(i)
        self.sum=0

        if self.option.get()==1:
            if a==(self.l)[0]:
                self.cursor.execute('select * from UserDetails where mid like %s;', ('%'+b+'%',))
            elif a==(self.l)[1]:
                self.cursor.execute('select * from UserDetails where mname like %s;', ('%'+b+'%',))
            elif (a==(self.l)[2]):
                self.cursor.execute('select * from UserDetails where Year(regdate) like %s;', ('%'+b+'%',))

            row=self.cursor.fetchall()
            for r in row:
                self.t.insert('', 0, text=r[0], values=(r[0], r[1], r[2], '500'))
            self.sum=(len(row))*500


        elif self.option.get()==2:
            if a == (self.l)[0]:
                self.cursor.execute('select * from book_issue_return where Status="Returned" and IssueId like %s;', ('%'+b+'%',))
            elif a==(self.l)[1]:
                self.cursor.execute('select * from book_issue_return where Status="Returned" and Mid like %s;', ('%'+b+'%',))
            elif a==(self.l)[2]:
                self.cursor.execute('select IssueID,A.Mid,Bid,Issuedate,Returndate,Fine,Status from book_issue_return A,UserDetails B where Status="Returned" and A.Mid=B.mid and mname like %s;', ('%'+b+'%',))
            elif a==(self.l)[3]:
                self.cursor.execute('select * from book_issue_return where Status="Returned" and Year(Returndate) like %s;', ('%'+b+'%',))


            row = self.cursor.fetchall()
            for r in row:
                self.t.insert('', 0, text=r[0], values=(r[0], r[1], r[2], r[4], r[5]))
                self.sum+=int(r[5])

        self.lbl1.config(text='Total = ₹' + str(self.sum))
        self.sum=0

    def cancel(self):
        self.cmbvar1 = StringVar()
        self.cmbvar1.set('                SELECT')
        self.cmb1.config(textvariable=self.cmbvar1)

        self.enable(1)

        self.esearch.config(state=DISABLED)







class UserDetails:
    def __init__(self, con):
        self.con = con
        self.cursor = self.con.cursor()

        self.root = Toplevel()
        self.root.geometry("1250x600+5+10")
        self.root.configure(bg="#192734")
        '''remove the title bar'''
        # self.root.overrideredirect(True)  # Remove default title bar
        # add a button to close the window overriding the title bar
        # Button(text="X", fg='white', bg='red', width=2, relief='solid', font=('Helvetica', 12, font.BOLD),
        # command=self.root.destroy).place(x=1220, y=0)
        self.root.resizable(0, 0)

        '''input designs'''
        Label(self.root, text="Member ID", fg='#FFFFFF', anchor='w', bg='#192734',
              font=('Helvetica', 12, font.BOLD)).place(x=20,
                                                       y=20)

        self.e1 = Entry(self.root, relief=SOLID, bd=5, width=35)
        self.e1.place(x=150, y=20)

        Label(self.root, text="Member Name", fg='#FFFFFF', anchor='w', bg='#192734',
              font=('Helvetica', 12, font.BOLD)).place(x=20,
                                                       y=60)

        self.e2 = Entry(self.root, relief=SOLID, bd=5, width=35)
        self.e2.place(x=150, y=60)

        Label(self.root, text="Contact", fg='#FFFFFF', anchor='w', bg='#192734', width=9,
              font=('Helvetica', 12, font.BOLD)).place(
            x=20, y=100)

        self.e3 = Entry(self.root, relief=SOLID, bd=5, width=35)
        self.e3.place(x=150, y=100)

        Label(self.root, text="Reg. Date", fg='#FFFFFF', anchor='w', bg='#192734', width=10,
              font=('Helvetica', 12, font.BOLD)).place(x=20,
                                                       y=140)

        Label(self.root, text=date.today(), relief=SOLID, bg="white", width=21,
              font=('Helvetica', 12, font.BOLD)).place(x=153,
                                                       y=140)

        Label(self.root, text="Address", fg='#FFFFFF', anchor='w', bg='#192734', width=9,
              font=('Helvetica', 12, font.BOLD)).place(
            x=20, y=180)

        self.t1 = Text(self.root, bd=7, relief=SOLID, height=3.5, width=26)
        self.t1.place(x=150, y=180)
        '''----------------------------------------------------------------------------'''

        self.l5 = Label(self.root, text="", fg="red", font=('Helvetica', 12, font.BOLD),
                        bg="#192734")
        self.l5.place(x=400, y=550)

        self.b1 = Button(self.root, text="Insert", relief=SOLID, command=self.insert, bd=5, bg="#90aaf5")
        self.b1.place(x=20, y=270)

        self.b2 = Button(self.root, text="Display", relief=SOLID, command=self.display, bd=5, bg="#90aaf5")
        self.b2.place(x=100, y=270)

        self.b3 = Button(self.root, text="Delete", relief=SOLID, command=self.delete, bd=5, fg='#FFFFFF', bg="#f2746b")
        self.b3.place(x=180, y=270)

        self.b4 = Button(self.root, text="Clear", relief=SOLID, command=self.clear, bd=5, bg="#90aaf5")
        self.b4.place(x=260, y=270)

        self.b5 = Button(self.root, text="Update", relief=SOLID, command=self.updatebox, bd=5, bg="#90aaf5")
        self.b5.place(x=320, y=270)

        Label(self.root, text="Joining Fee= ₹500", fg='#FFFFFF', bg='#7463f2', font=('Helvetica', 12, font.BOLD)).place(
            x=1070, y=550)


        '''TREE  VIEW'''
        s = ttk.Style()
        s.theme_use('default')
        s.configure('Treeview', relief=SOLID, background="#192734", fieldbackground="#90aaf5", foreground="white")
        s.configure("Treeview.Heading", background="#7463f2", foreground="black")
        self.t = ttk.Treeview(self.root, height=25)
        self.t["show"] = "headings"
        self.t["columns"] = ['Member-ID', 'Member-Name', 'Contact', 'Address', 'Reg.Date']
        for i in range(5):
            self.t.heading(i, text="{}".format(self.t["columns"][i]))
            if i == 0:
                self.t.column(i, width=100)  # Column 0 width is set to 100 pixels
            elif i == 1:
                self.t.column(i, width=180)
            elif i == 2:
                self.t.column(i, width=180)
            elif i == 3:
                self.t.column(i, width=250)
            else:
                self.t.column(i, width=100)  # Columns 2, 3, and 4 width is set to 150 pixels
        self.t.place(x=400, y=20)

        self.e1["state"] = "disabled"
        self.e3["state"] = "disabled"
        self.b1["state"] = "disabled"
        self.b3["state"] = "disabled"
        self.b5["state"] = "disabled"
        self.t1["state"] = "disabled"
        if self.count() == 0:
            self.b2["state"] = "disabled"

        self.e2.bind("<KeyPress>", lambda a: self.e3.configure(state=NORMAL))
        self.e3.bind("<KeyPress>", lambda a: self.t1.configure(state=NORMAL))
        self.t1.bind("<KeyPress>", lambda a: self.b1.configure(state=NORMAL))
        self.t.bind("<<TreeviewSelect>>", self.enable)
        self.genID()
        self.display()

        self.root.mainloop()

    def enable(self, e):
        name = self.t.item(self.t.selection())['text']
        if(len(name)>0):
            self.b3["state"] = "normal"
            self.b5["state"] = "normal"

    def count(self):
        cursor = self.con.cursor()
        cursor.execute("select count(*) from UserDetails;")
        c1 = cursor.fetchall()
        c = c1[0][0]
        self.con.commit()
        cursor.close()
        return c

    def clear(self):
        self.genID()
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)
        self.t1.delete("1.0", "end")
        # self.e1["state"] = "disabled"
        self.e3["state"] = "disabled"
        self.t1["state"] = "disabled"
        self.b1["state"] = "disabled"
        self.b2["state"] = "disabled"
        self.b3["state"] = "disabled"
        self.b5["state"] = "disabled"


    def insert(self):
        cursor = self.con.cursor()
        a1 = self.e1.get()
        a2 = self.e2.get()
        a3 = self.e3.get()
        a4 = date.today()
        a5 = self.t1.get(1.0, "end-1c")
        self.l5.configure(text="")
        if len(a3) <= 10:
            if len(a3) != 0 and a3.isdigit():
                st = "insert into UserDetails (mid,mname,contact,address,regdate) values('{}','{}',{},'{}','{}')".format(a1,
                                                                                                                   a2,
                                                                                                                   a3,
                                                                                                                   a5,
                                                                                                                   a4)
                cursor.execute(st)
                self.l5.configure(text="Latest insert: Success")
            else:
                self.l5.configure(text="Unsupported value")
        else:
            self.l5.configure(text="please enter a 10 digit phone number")
        self.clear()
        self.display()
        self.con.commit()
        cursor.close()

    def delete(self):
        cursor = self.con.cursor()
        name = self.t.item(self.t.selection())['text']
        cursor.execute("delete from UserDetails where mid='%s';" % name)
        self.b3["state"] = "disabled"
        self.l5.configure(text="Last delete: Success")
        self.display()
        self.genID()
        self.con.commit()
        cursor.close()

    def updatebox(self):
        name = self.t.item(self.t.selection())['values']
        '''UPDATE   FRAME'''
        self.frm1 = Frame(self.root, width=350, height=270, bd=3, relief=SUNKEN, bg='#313866')

        Label(self.frm1, text="Member ID", fg='#FFFFFF', anchor='w', bg='#313866',
              font=('Helvetica', 12, font.BOLD)).place(x=5,
                                                       y=10)

        self.ue1 = Entry(self.frm1, relief=SOLID, bd=5, width=30)
        self.ue1.place(x=150, y=10)

        Label(self.frm1, text="Member Name", fg='#FFFFFF', anchor='w', bg='#313866',
              font=('Helvetica', 12, font.BOLD)).place(x=5,
                                                       y=50)

        self.ue2 = Entry(self.frm1, relief=SOLID, bd=5, width=30)
        self.ue2.place(x=150, y=50)

        Label(self.frm1, text="Contact", fg='#FFFFFF', anchor='w', bg='#313866', width=9,
              font=('Helvetica', 12, font.BOLD)).place(
            x=5, y=90)

        self.ue3 = Entry(self.frm1, relief=SOLID, bd=5, width=30)
        self.ue3.place(x=150, y=90)

        Label(self.frm1, text="Registration Date", fg='#FFFFFF', anchor='w', bg='#313866', width=9,
              font=('Helvetica', 12, font.BOLD)).place(x=5, y=130)

        self.ue4 = Entry(self.frm1, relief=SOLID, bd=5, width=30)
        self.ue4.place(x=150, y=130)

        Label(self.frm1, text="Address", fg='#FFFFFF', anchor='w', bg='#313866', width=9,
              font=('Helvetica', 12, font.BOLD)).place(
            x=5, y=170)

        self.ut1 = Text(self.frm1, bd=7, relief=SOLID, height=4, width=22)
        self.ut1.place(x=150, y=170)

        self.ub1 = Button(self.frm1, text="Update", relief=SOLID, command=self.update, bd=5, bg="#90aaf5")
        self.ub1.place(x=5, y=210)

        '''---------------------------------------------------------------------------------------'''

        self.frm1.place(x=20, y=320)
        '''ue1(update entry 1)'''
        self.ue1.config(state=NORMAL)
        self.ue1.delete(0, END)
        self.ue1.insert(0, name[0])
        self.ue1.config(state=DISABLED)
        '''--------------------------'''
        self.ue2.delete(0, END)
        self.ue2.insert(0, name[1])
        self.ue3.delete(0, END)
        self.ue3.insert(0, name[2])
        self.ue4.delete(0, END)
        self.ue4.insert(0, name[4])
        self.ut1.delete("1.0", "end")
        self.ut1.insert('end', name[3])

    def update(self):
        cursor = self.con.cursor()
        a1 = self.ue1.get()
        a2 = self.ue2.get()
        a3 = self.ue3.get()
        a4 = self.ue4.get()
        a5 = self.ut1.get(1.0, "end-1c")
        self.l5.configure(text="")
        if len(a3) <= 10:
            if len(a3) != 0 and len(a4) != 0 and a3.isdigit():
                # update query
                query = "UPDATE UserDetails SET mname = %s, contact = %s, address = %s, regdate = %s WHERE mid = %s"

                # values to update
                values = (a2, a3, a5, a4, a1)

                # execute query
                cursor.execute(query, values)
                self.l5.configure(text="Latest update: Success")
            else:
                self.l5.configure(text="Unsupported value")
        else:
            self.l5.configure(text="please enter a 10 digit phone number")
        self.clear()
        self.display()
        self.con.commit()
        cursor.close()
        self.frm1.destroy()

    def display(self):
        c = self.count()
        cursor = self.con.cursor()
        cursor.execute("select * from UserDetails;")
        row = cursor.fetchall()
        x = self.t.get_children()
        for item in x:
            self.t.delete(item)
        for r in row:
            self.t.insert('', 0, text=r[0], values=(r[0], r[1], r[2], r[4], r[3]))
        if c > 0:
            self.b2["state"] = "normal"
        else:
            self.b2["state"] = "disabled"
        self.con.commit()
        cursor.close()

    def genID(self):
        cursor = self.con.cursor()
        cursor.execute("select mid from UserDetails order by mid;")
        r = cursor.fetchall()
        max = 0
        for row in r:
            i = int(row[0][1:])
            if i > max:
                max = i
        max = max + 1
        s2 = 'M' + "0" * (4 - len(str(max))) + str(max)
        self.e1.config(state=NORMAL)
        self.e1.delete(0, END)
        self.e1.insert(0, s2)
        self.e1.config(state=DISABLED)








class issue:
    def __init__(self,con):
        self.con = con
        self.cursor = self.con.cursor()
        self.root = Toplevel()
        self.root.geometry('1062x418+150+100')

        self.root.title('Book Issue')
        self.root.resizable(0, 0)

        self.frm1 = Frame(self.root, width=515, height=60, bd=3, relief=SUNKEN, bg='#4589aa')
        self.frm1.place(x=3, y=2)
        self.frm2 = Frame(self.root, width=515, height=351, bd=3, relief=SUNKEN, bg='#4589aa')
        self.frm2.place(x=3, y=64)
        self.frm3 = Frame(self.root, width=540, height=60, bd=3, relief=SUNKEN, bg='#4589aa')
        self.frm3.place(x=520, y=2)
        self.frm4 = Frame(self.root, width=540, height=351, bd=3, relief=SUNKEN, bg='#4589aa')
        self.frm4.place(x=520, y=64)

                                 #------------------RADIO BUTTONS---------------------

        self.option = IntVar()
        self.option.set(1)

        self.r1 = Radiobutton(self.frm1, bg='#4589aa', variable=self.option, value=1, text="Issue",font=('Helvetica', 15, font.BOLD),command=self.enabled)
        self.r1.place(x=100, y=12)

        self.r2 = Radiobutton(self.frm1, bg='#4589aa', variable=self.option, value=2, text="Return",font=('Helvetica', 15, font.BOLD),command=self.enabled)
        self.r2.place(x=300, y=12)
                               #--------------------ISSUE DATE--------------------

        self.lirdate1=Label(self.frm2, text='Issue Date :', width=11, font=('Helvetica', 15, font.BOLD), bg="#deadaf", relief=RIDGE,bd=5)
        self.lirdate1.place(x=70, y=10)

        self.lirdate2 = Label(self.frm2, font=('Helvetica', 12, font.BOLD), text=date.today(), width=18,relief=RIDGE, bd=5)
        self.lirdate2.place(x=240, y=12)

                            #----------------------ISSUE ID LABEL------------------

        Label(self.frm2, text='   Issue ID :   ', width=11, font=('Helvetica', 15, font.BOLD), bg="#deadaf",relief=RIDGE, bd=5).place(x=70, y=55)
        self.liid = Label(self.frm2, font=('Helvetica', 12, font.BOLD), width=18, relief=RIDGE, bd=5)
        self.liid.place(x=240, y=55)

                           #------------------BOOK ID COMBOBOX----------------------

        Label(self.frm2, text='Book ID :', width=11, font=('Helvetica', 15, font.BOLD), bg="#deadaf", relief=RIDGE,bd=5).place(x=70, y=100)

        self.cursor.execute("select bookid from BookDetails;")
        r1 = self.cursor.fetchall()
        self.lst1 = []
        for i in r1:
            self.lst1.append(i[0])
        self.cmbvar1 = StringVar()
        self.cmbvar1.set('                   SELECT')
        self.cmbbid = ttk.Combobox(self.frm2, width=28, textvariable=self.cmbvar1, values =self.lst1)
        self.cmbbid.place(x=243, y=107)
        self.cmbbid.bind('<<ComboboxSelected>>', lambda k: self.enabled2(k, 1))

                        #---------------------BORROWER ID COMBOBOX-------------------

        Label(self.frm2, text='Borrower ID :', width=11, font=('Helvetica', 15, font.BOLD), bg="#deadaf", relief=RIDGE,bd=5).place(x=70, y=145)

        self.cursor.execute("select mid from Userdetails;")
        r2 = self.cursor.fetchall()
        self.lst2 = []
        for i in r2:
            self.lst2.append(i[0])
        self.cmbvar2 = StringVar()
        self.cmbvar2.set('                   SELECT')
        self.cmbmid = ttk.Combobox(self.frm2, width=28, textvariable=self.cmbvar2, values=self.lst2, state=DISABLED)
        self.cmbmid.place(x=243, y=150)
        self.cmbmid.bind('<<ComboboxSelected>>', lambda k: self.enabled2(k, 2))

                           #-------------------RETURN DATE LABEL---------------------

        self.lreturnby1=Label(self.frm2, text='Return by :', width=11, font=('Helvetica', 15, font.BOLD), bg="#deadaf", relief=RIDGE,bd=5)
        self.lreturnby1.place(x=70, y=190)

        self.lreturnby2 = Label(self.frm2, font=('Helvetica', 12, font.BOLD), width=18, relief=RIDGE, bd=5)
        self.lreturnby2.place(x=240, y=192)

                         # -------------------LOGIN CANCEL BUTTONS---------------------

        self.b1 = Button(self.frm2, bg="#deadaf", text="Issue", font=('Helvetica', 14, font.BOLD), relief=RAISED, bd=5,width=7, command=self.fun, state=DISABLED)
        self.b1.place(x=110, y=275)

        self.b2 = Button(self.frm2, bg="#deadaf", text="Cancel", font=('Helvetica', 14, font.BOLD), relief=RAISED,width=7, bd=5, command=self.cancel)
        self.b2.place(x=300, y=275)

        self.lresult = Label(self.frm2, bg='#4589aa', fg="#deadaf", font=('Helvetica', 12, font.BOLD),width=30)
        self.lresult.place(x=98,y=235)

                           # -------------------RETURN LABELS---------------------

        self.lmid = Label(self.frm2, font=('Helvetica', 12, font.BOLD), width=18, relief=RIDGE, bd=5)

        self.lbid = Label(self.frm2, font=('Helvetica', 12, font.BOLD), width=18, relief=RIDGE, bd=5)

                           # -------------------TREE VIEW---------------------

        s=ttk.Style()
        s.theme_use('default')
        s.configure('Treeview', relief=SOLID,background='#90aaf5', fieldbackground="#90aaf5", foreground="black")
        s.configure("Treeview.Heading", background="#deadaf", foreground="black")
        self.t = ttk.Treeview(self.frm4, height=16)
        self.t["show"] = "headings"
        self.t["columns"] = ['IssueID', 'MemberId', 'BookId', 'IssueDate', 'ReturnDate','Fine','Status']
        for i in range(7):
            self.t.heading(i, text="{}".format(self.t["columns"][i]))
            if i==0 or i==2:
                self.t.column(i, width=60)
            elif i==1 or i==6:
                self.t.column(i, width=80)
            elif i==3 or i==4:
                self.t.column(i, width=100)
            elif i==5:
                self.t.column(i, width=45)

        self.t.place(x=4,y=3)
        self.t.config(selectmode='none')
        self.t.bind("<<TreeviewSelect>>",self.enabled3)

                           # -------------------SEARCH BOX---------------------

        self.b3=Button(self.frm3,text=' SEARCH ', width=12, font=('Helvetica', 12, font.BOLD),command=self.search ,bg="#deadaf", relief=RIDGE,bd=5)
        self.b3.place(x=20, y=10)

        self.esearch=Entry(self.frm3,width=33,font=('Helvetica', 12, font.BOLD),relief=RAISED, bd=5)
        self.esearch.place(x=170,y=13)

        self.b4=Button(self.frm3,bg="red",text="X",fg='white',font=('Helvetica',8,font.BOLD),relief=RAISED,width=2,height=1, bd=5,command=self.cancel)
        self.b4.place(x=490,y=13)

        self.scrol = ttk.Scrollbar(self.root, orient=VERTICAL, command=self.t.yview)
        self.t["yscrollcommand"] = self.scrol.set
        self.scrol.place(x=1046, y=70, height=342)

        self.display()
        self.root.mainloop()

                     # -------------------SELECTED ISSUE/RETURN FROM RADIO BUTTONS---------------------
    def enabled(self):
        if self.option.get()==1:
            self.t.config(selectmode='none')
            self.lmid.destroy()
            self.lbid.destroy()

            self.cmbvar1 = StringVar()
            self.cmbvar1.set('                   SELECT')
            self.cmbbid = ttk.Combobox(self.frm2, width=28, textvariable=self.cmbvar1, values=[i for i in range(10)])
            self.cmbbid.place(x=243, y=105)
            self.cmbbid.bind('<<ComboboxSelected>>', lambda k: self.enabled2(k, 1))

            self.cmbvar2 = StringVar()
            self.cmbvar2.set('                   SELECT')
            self.cmbmid = ttk.Combobox(self.frm2, width=28, textvariable=self.cmbvar2, values=self.lst2, state=DISABLED)
            self.cmbmid.place(x=243, y=150)
            self.cmbmid.bind('<<ComboboxSelected>>', lambda k: self.enabled2(k, 2))

            self.b1.configure(text='Issue')
            self.lirdate1.configure(text='Issue Date :')

        elif self.option.get()==2:
            self.t.config(selectmode='browse')
            self.cmbvar3 = StringVar()
            self.cmbvar3.set('                   SELECT')

            self.cmbbid.destroy()
            self.cmbmid.destroy()

            self.lmid = Label(self.frm2, font=('Helvetica', 12, font.BOLD), width=18, relief=RIDGE, bd=5)
            self.lmid.place(x=240, y=145)

            self.lbid = Label(self.frm2, font=('Helvetica', 12, font.BOLD), width=18, relief=RIDGE, bd=5)
            self.lbid.place(x=240, y=100)

            self.b1.configure(text='Return')
            self.lirdate1.configure(text='Return Date :')

        self.display()
        self.liid.config(text='')
        self.lreturnby2.configure(text='')
        self.lresult.configure(text='')

           # -------------------self.conFIG. BUTTONS/LABELS ON SELECTION FROM COMBOBOX---------------------

    def enabled2(self, e, n):
        if n == 1:
            self.liid.configure(text=self.issueidgen())
            self.lreturnby2.configure(text=str(self.rdate()))
            self.cmbmid['state'] = NORMAL
            self.lresult.config(text=' Fees = ₹50')
        elif n == 2:
            self.b1['state'] = DISABLED
            st="select * from book_issue_return where Bid=%s and Mid=%s order by ReturnDate desc,IssueId desc;"
            values=(self.cmbbid.get(),self.cmbmid.get())
            self.cursor.execute(st,values)
            r=self.cursor.fetchall()
            if len(r)>0:
                if r[0][6]=="Issued":
                    self.lresult.config(text="PLease return before borrowing again")
                elif r[0][6]=="Returned":
                    self.b1['state'] = NORMAL
            else:
                self.b1['state'] = NORMAL

    def enabled3(self,e):
        name = self.t.item(self.t.selection())['text']
        if len(name)>0:
            self.cursor.execute("select * from book_issue_return where IssueId='%s';" % name)
            r=self.cursor.fetchall()
            if len(r)>0:
                if r[0][6]=='Issued':
                    self.liid.config(text=r[0][0])
                    self.lmid.config(text=r[0][1])
                    self.lbid.config(text=r[0][2])
                    self.lreturnby2.config(text=r[0][4])
                    self.b1.configure(state=NORMAL)
                    self.fine(r[0][3])

                          # -------------------CLEARING SELECTED DATA---------------------

    def cancel(self):
        if self.option.get()==1:
            self.cmbvar1 = StringVar()
            self.cmbvar1.set('                   SELECT')

            self.cmbvar2 = StringVar()
            self.cmbvar2.set('                   SELECT')

            self.cmbbid.delete(0, END)
            self.cmbbid.configure(textvariable=self.cmbvar1)
            self.cmbmid.delete(0, END)
            self.cmbmid.configure(textvariable=self.cmbvar2)
            self.cmbmid['state'] = DISABLED

        elif self.option.get()==2:
            self.lbid.config(text='')
            self.lmid.config(text='')

        self.display()
        self.lresult.config(text='')
        self.liid.config(text='')
        self.b1['state'] = DISABLED
        self.lreturnby2.config(text='')

                           # -------------------ACTUAL ISSUE/RETURN---------------------

    def fun(self):
        if self.option.get()==1:
            st = "insert into book_issue_return (IssueId,Mid,Bid,Issuedate,Returndate,Fine,Status) values('{}','{}','{}','{}','{}',{},'{}');".format(self.issueidgen(),self.cmbmid.get(),self.cmbbid.get(),date.today(),self.rdate(),0,'Issued')
            self.cursor.execute(st)
            self.cancel()
            self.lresult.configure(text='Last Issue : Success')

        elif self.option.get()==2:
            name = self.t.item(self.t.selection())['text']
            self.cursor.execute("select * from book_issue_return where IssueId='%s';" % name)
            r = self.cursor.fetchall()
            st="update book_issue_return set status='Returned',fine=%s,Returndate=%s where IssueId=%s;"
            values=(self.fine(r[0][3]),date.today(),r[0][0])
            self.cursor.execute(st,values)
            self.option.set(1)
            self.enabled()
            self.lresult.configure(text='Last Return : Success')

        self.b1.configure(state=DISABLED)
        self.display()
        self.con.commit()

                         # -------------------GENERATING ISSUEID---------------------

    def issueidgen(self):
        self.cursor.execute("select count(*) from book_issue_return")
        r = self.cursor.fetchall()
        if r[0][0] > 0:
            self.cursor.execute("select IssueId from book_issue_return")
            ad = self.cursor.fetchall()
            max = 0
            for i in ad:
                if int(str(i[0])[1::]) > max:
                    max = int(str(i[0])[1::])

            s = 'i' + '0' * (4 - len(str(max + 1))) + str(max + 1)
        elif r[0][0] == 0:
            s = 'i0001'

        return s

                      # -------------------GENERATING RETURN DATE---------------------

    def rdate(self):
        d=date.today() + timedelta(days=10)
        return d

    def display(self):
        self.esearch.delete(0,END)
        if self.option.get() == 1:
            self.cursor.execute('select * from book_issue_return;')
            row=self.cursor.fetchall()
            for i in self.t.get_children():
                self.t.delete(i)
            for r in row:
                self.t.insert('', 0, text=r[0], values=(r[0],r[1],r[2],r[3],r[4],r[5],r[6]))

        elif self.option.get() == 2:
            self.cursor.execute('select * from book_issue_return where status="Issued";')
            row = self.cursor.fetchall()
            for i in self.t.get_children():
                self.t.delete(i)
            for r in row:
                self.t.insert('', 0, text=r[0], values=(r[0], r[1], r[2], r[3], r[4], r[5], r[6]))


    def search(self):
        k=self.esearch.get()
        self.cursor.execute("select * from book_issue_return where IssueId like %s;",('%'+k,))
        row = self.cursor.fetchall()
        for i in self.t.get_children():
            self.t.delete(i)
        for r in row:
            self.t.insert('', 0, text=r[0], values=(r[0], r[1], r[2], r[3], r[4], r[5], r[6]))

    def fine(self,a):
        f=0
        d=(date.today() - a).days
        if d>0:
            if d>10:
                f=100
            elif d>20:
                f=200
            elif d>30:
                f=500
            self.lresult.configure(text=(' Fine = ₹'+str(f)))


        elif d<=0:
            self.lresult.configure(text='Fees = ₹50')
        return f








class bookdetails:
    def __init__(self, con):
        self.con = con
        self.cursor = self.con.cursor()
        self.root = Toplevel()
        self.root.geometry('1062x418+150+100')
        self.root.config(bg='white')
        self.frm1 = Frame(self.root, width=515, height=414, bd=3, relief=SUNKEN, bg='#4589aa')
        self.frm1.place(x=3, y=2)
        self.frm3 = Frame(self.root, width=540, height=60, bd=3, relief=SUNKEN, bg='#4589aa')
        self.frm3.place(x=520, y=2)
        Label(self.frm1, text='   Book ID :   ', width=11, font=('Times', 15, font.BOLD), bg="#deadaf", relief=RIDGE,
              bd=5).place(x=30, y=35)
        Label(self.frm1, text='   Book Name :   ', width=11, font=('Times', 15, font.BOLD), bg="#deadaf", relief=RIDGE,
              bd=5).place(x=30, y=95)
        Label(self.frm1, text='   Author :   ', width=11, font=('Times', 15, font.BOLD), bg="#deadaf", relief=RIDGE,
              bd=5).place(x=30, y=155)
        Label(self.frm1, text='   Quantity :   ', width=11, font=('Times', 15, font.BOLD), bg="#deadaf", relief=RIDGE,
              bd=5).place(x=30, y=215)
        Label(self.frm1, text='   Cost :    ', width=11, font=('Times', 15, font.BOLD), bg="#deadaf", relief=RIDGE,
              bd=5).place(x=30, y=275)

        self.cursor.execute("select count(*) from bookdetails")
        r = self.cursor.fetchall()
        if (r[0][0] == 0):
            x = 1001
        else:
            self.cursor.execute("select max(bookid) from bookdetails")
            r = self.cursor.fetchall()
            x = 1 + int(r[0][0])

        text = StringVar(value=str(x))
        self.e5 = Entry(self.frm1, textvariable=text, state=DISABLED, width=20, relief=RIDGE,
                        font=('Times', 15, font.BOLD), bd=5)
        self.e5.place(x=230, y=35)

        self.frm2 = Frame(self.root, width=515, height=100, bd=3, relief=SUNKEN, bg='#66CDAA')
        self.frm2.place(x=3, y=325)

        self.b1 = Button(self.root, text="Insert", command=self.insert, bg="cyan", state=DISABLED, relief=SUNKEN, bd=5,
                         font=('Comic Sans MS', 10, font.BOLD), width=8)
        self.b1.place(x=140, y=335)

        self.b2 = Button(self.root, text="Delete", command=self.delete, bg="cyan", state=DISABLED, relief=SUNKEN, bd=5,
                         font=('Comic Sans MS', 10, font.BOLD), width=8)
        self.b2.place(x=260, y=335)

        self.l5 = Label(self.root, bg="cyan", text='Remarks:', width=10, font=('Times', 10, font.BOLD), bd=5,
                        relief=RIDGE)
        self.l5.place(x=115, y=385)

        self.l6 = Label(self.root, bg="cyan", width=20, font=('Helvetica', 10, font.BOLD), bd=5, relief=RIDGE)
        self.l6.place(x=205, y=385)

        self.e2 = Entry(self.frm1, font=('Times', 15, font.BOLD), relief=RIDGE, bd=5, state=DISABLED)
        self.e2.place(x=230, y=155)
        self.e2.bind('<KeyPress>', self.enabler2)

        self.e3 = Entry(self.frm1, font=('Times', 15, font.BOLD), relief=RIDGE, bd=5, state=DISABLED)
        self.e3.place(x=230, y=215)
        self.e3.bind('<KeyPress>', self.enabler3)

        self.e4 = Entry(self.frm1, font=('Times', 15, font.BOLD), relief=RIDGE, bd=5, state=DISABLED)
        self.e4.place(x=230, y=275)
        self.e4.bind('<KeyPress>', self.enabler4)

        self.e1 = Entry(self.frm1, font=('Times', 15, font.BOLD), relief=RIDGE, bd=5)
        self.e1.place(x=230, y=95)
        self.e1.bind('<KeyPress>', self.enabler1)

        s = ttk.Style()
        s.theme_use('clam')
        s.configure('Treeview', background="green", fieldbackground="#deadaf", foreground="yellow")
        self.t = ttk.Treeview(self.root, height=16)
        self.t["show"] = "headings"
        self.t["columns"] = ['BookID', 'BookName', 'Author', 'Quantity', 'Cost']
        for i in range(5):
            self.t.heading(i, text="{}".format(self.t["columns"][i]))
            self.t.column(i, anchor=CENTER, width=107)
        self.t.place(x=520, y=65)
        self.t.bind('<<TreeviewSelect>>', self.enabler5)
        self.cursor.execute("select * from bookdetails;")
        row = self.cursor.fetchall()
        x = self.t.get_children()
        for item in x:
            self.t.delete(item)
        for r in row:
            self.t.insert('', 0, text=r[0], values=(r[0], r[1], r[2], r[3], r[4]))

            # -------------------SEARCH BOX---------------------

        self.b3 = Button(self.frm3, text=' SEARCH ', width=12, font=('Helvetica', 12, font.BOLD), command=self.search,
                         bg="#deadaf", relief=RIDGE, bd=5)
        self.b3.place(x=20, y=10)

        self.esearch = Entry(self.frm3, width=33, font=('Helvetica', 12, font.BOLD), relief=RAISED, bd=5)
        self.esearch.place(x=170, y=13)

        self.scrol = ttk.Scrollbar(self.root, orient=VERTICAL, command=self.t.yview)
        self.t["yscrollcommand"] = self.scrol.set
        self.scrol.place(x=1046, y=66, height=345)

        self.root.mainloop()

    def bookidgen(self):
        self.cursor.execute("select count(*) from bookdetails")
        r = self.cursor.fetchall()
        if (r[0][0] == 0):
            x = 1001
        else:
            self.cursor.execute("select max(bookid) from bookdetails")
            r = self.cursor.fetchall()
            x = 1 + int(r[0][0])
        s = StringVar(value=str(x))
        self.e5.configure(textvariable=s)

    def insert(self):
        f = 0
        a = self.e5.get()
        b = self.e1.get()
        c = self.e2.get()
        d = self.e3.get()
        e = self.e4.get()
        L = []
        self.cursor = self.con.cursor()

        for i in d:
            if (i.isdigit() == False):
                self.l6.configure(text="Unsupported Type")
                f = 1

        for i in e:
            if (i.isdigit() == False):
                self.l6.configure(text="Unsupported Type")
                f = 1

        if (f == 0):
            st = "insert into bookdetails (bookid,bkname,author,qty,cost) values({},'{}','{}',{},{})".format(a, b, c, d,
                                                                                                             e)
            self.cursor = self.con.cursor()
            self.cursor.execute(st)
            self.con.commit()
            self.cursor.close()
            self.e1.delete(0, END)
            self.e2.delete(0, END)
            self.e3.delete(0, END)
            self.e4.delete(0, END)
            self.updater()
            self.bookidgen()
        elif (f == 1):
            self.l6.configure(text="Unsupported Type")
            self.e1.delete(0, END)
            self.e2.delete(0, END)
            self.e3.delete(0, END)
            self.e4.delete(0, END)

        self.restoreback()

    def delete(self):
        bookid = int(self.t.item(self.t.selection())['text'])
        self.cursor = self.con.cursor()
        self.cursor.execute("delete from bookdetails where bookid=%d;" %bookid)
        self.restoreback()
        self.con.commit()
        self.cursor.close()
        self.updater()
        self.bookidgen()

    def updater(self):
        self.cursor = self.con.cursor()
        self.cursor.execute("select * from bookdetails;")
        row = self.cursor.fetchall()
        x = self.t.get_children()
        for item in x:
            self.t.delete(item)
        for r in row:
            self.t.insert('', 0, text=r[0], values=(r[0], r[1], r[2], r[3], r[4]))

    def search(self):
        k = self.esearch.get()
        self.cursor.execute("select * from bookdetails where bookid like %s;", ('%' + k + '%',))
        row = self.cursor.fetchall()
        self.t.delete(*self.t.get_children())
        for r in row:
            self.t.insert('', 0, text=r[0], values=(r[0], r[1], r[2], r[3], r[4]))

    def restoreback(self):
        self.e2["state"] = "disabled"
        self.e3["state"] = "disabled"
        self.e4["state"] = "disabled"
        self.b1["state"] = "disabled"
        self.b2["state"] = "disabled"

    def enabler4(self, Event):
        self.b1["state"] = "normal"

    def enabler1(self, Event):
        self.e2["state"] = "normal"
        self.l6.configure(text="")
        self.esearch.delete(0, END)

    def enabler2(self, Event):
        self.e3["state"] = "normal"

    def enabler3(self, Event):
        self.e4["state"] = "normal"

    def enabler5(self, Event):
        bid = self.t.item(self.t.selection())['text']
        if (len(str(bid)) > 0):
            self.b2["state"] = "normal"


















class purchase:
    def __init__(self, con):
        self.con = con
        self.cursor = self.con.cursor()
        self.root = Toplevel()
        self.root.geometry('1062x418+150+100')
        self.root.config(bg='white')
        self.frm1 = Frame(self.root, width=515, height=414, bd=3, relief=SUNKEN, bg='#4589aa')
        self.frm1.place(x=3, y=2)
        Label(self.frm1, text='   Order ID :   ', width=11, font=('Times', 15, font.BOLD), bg="#deadaf", relief=RIDGE,
              bd=5).place(x=30, y=35)
        Label(self.frm1, text='   Book ID :   ', width=11, font=('Times', 15, font.BOLD), bg="#deadaf", relief=RIDGE,
              bd=5).place(x=30, y=95)
        Label(self.frm1, text='   Purchase Date :   ', width=11, font=('Times', 15, font.BOLD), bg="#deadaf",
              relief=RIDGE, bd=5).place(x=30, y=155)
        Label(self.frm1, text='   Quantity :   ', width=11, font=('Times', 15, font.BOLD), bg="#deadaf", relief=RIDGE,
              bd=5).place(x=30, y=215)
        Label(self.frm1, text='   Total Cost :    ', width=11, font=('Times', 15, font.BOLD), bg="#deadaf",
              relief=RIDGE, bd=5).place(x=30, y=275)
        Label(self.frm1, text=date.today(), width=17, font=('Times', 15, font.BOLD), relief=RIDGE, bd=5).place(x=230,
                                                                                                               y=155)

        self.frm2 = Frame(self.root, width=515, height=100, bd=3, relief=SUNKEN, bg='#66CDAA')
        self.frm2.place(x=3, y=325)

        self.b1 = Button(self.root, text="Insert", command=self.insert, bg="cyan", state=DISABLED, relief=SUNKEN, bd=5,
                         font=('Comic Sans MS', 10, font.BOLD), width=8)
        self.b1.place(x=140, y=335)

        self.b2 = Button(self.root, text="Delete", command=self.delete, bg="cyan", state=DISABLED, relief=SUNKEN, bd=5,
                         font=('Comic Sans MS', 10, font.BOLD), width=8)
        self.b2.place(x=260, y=335)

        self.l5 = Label(self.root, bg="cyan", text='Remarks:', width=10, font=('Times', 10, font.BOLD), bd=5,
                        relief=RIDGE)
        self.l5.place(x=115, y=385)

        self.l6 = Label(self.root, bg="cyan", width=20, font=('Helvetica', 10, font.BOLD), bd=5, relief=RIDGE)
        self.l6.place(x=205, y=385)

        self.e1 = Entry(self.frm1, font=('Times', 15, font.BOLD), relief=RIDGE, bd=5, state=DISABLED)
        self.e1.place(x=230, y=35)
        self.e1.bind('<KeyPress>', self.enabler1)

        self.e2 = Entry(self.frm1, font=('Times', 15, font.BOLD), relief=RIDGE, bd=5, state=DISABLED)
        self.e2.place(x=230, y=215)
        self.e2.bind('<KeyPress>', self.enabler2)

        self.e3 = Entry(self.frm1, font=('Times', 15, font.BOLD), relief=RIDGE, bd=5, state=DISABLED)
        self.e3.place(x=230, y=275)
        self.e3.bind('<KeyPress>', self.enabler5)

        self.cmbtxt = StringVar()
        self.cmbtxt.set('                   SELECT')
        self.cursor.execute("select bookid from bookdetails;")
        d = self.cursor.fetchall()
        self.L = []
        for i in d:
            self.L.append(i[0])

        self.bid = ttk.Combobox(self.frm1, width=32, textvariable=self.cmbtxt, values=self.L, state=NORMAL)
        self.bid.place(x=230, y=101)
        self.bid.bind('<<ComboboxSelected>>', self.enabler7)

        s = ttk.Style()
        s.theme_use('clam')
        s.configure('Treeview', background="green", fieldbackground="#deadaf", foreground="yellow")
        self.t = ttk.Treeview(self.root, height=16)
        self.t["show"] = "headings"
        self.t["columns"] = ['Order ID', 'Book ID', 'Purchase Date', 'Quantity', 'Total Cost']
        for i in range(5):
            self.t.heading(i, text="{}".format(self.t["columns"][i]))
            self.t.column(i, anchor=CENTER, width=107)
        self.t.place(x=520, y=65)
        self.t.bind('<<TreeviewSelect>>', self.enabler6)
        self.cursor.execute("select * from purchase;")
        row = self.cursor.fetchall()
        x = self.t.get_children()
        for item in x:
            self.t.delete(item)
        for r in row:
            self.t.insert('', 0, text=r[0], values=(r[0], r[1], r[2], r[3], r[4]))

            # -------------------SEARCH BOX---------------------

        self.frm3 = Frame(self.root, width=540, height=60, bd=3, relief=SUNKEN, bg='#4589aa')
        self.frm3.place(x=519, y=2)

        self.b3 = Button(self.frm3, text=' SEARCH ', width=12, font=('Helvetica', 12, font.BOLD), command=self.search,
                         bg="#deadaf", relief=RIDGE, bd=5)
        self.b3.place(x=20, y=10)

        self.esearch = Entry(self.frm3, width=33, font=('Helvetica', 12, font.BOLD), relief=RAISED, bd=5)
        self.esearch.place(x=170, y=13)

        self.scrol = ttk.Scrollbar(self.root, orient=VERTICAL, command=self.t.yview)
        self.t["yscrollcommand"] = self.scrol.set
        self.scrol.place(x=1046, y=66, height=345)

        self.root.mainloop()

    def insert(self):
        a = self.e1.get()
        b = self.bid.get()
        c = date.today()
        d = self.e2.get()
        e = self.e3.get()
        f = 0
        for i in a:
            if (i.isdigit() == False):
                self.l6.configure(text="Unsupported Type")
                self.e1.delete(0, END)
                self.e2.delete(0, END)
                self.e3.delete(0, END)
                f = 1
        for i in d:
            if (i.isdigit() == False):
                self.l6.configure(text="Unsupported Type")
                self.e1.delete(0, END)
                self.e2.delete(0, END)
                self.e3.delete(0, END)
                f = 1
        for i in e:
            if (i.isdigit() == False):
                self.l6.configure(text="Unsupported Type")
                self.e1.delete(0, END)
                self.e2.delete(0, END)
                self.e3.delete(0, END)
                f = 1

        if (f == 1):
            self.l6.configure(text="Book does not exist")
            self.e1.delete(0, END)
            self.e2.delete(0, END)
            self.e3.delete(0, END)
        else:
            self.cursor = self.con.cursor()
            a = self.e1.get()
            b = self.bid.get()
            c = date.today()
            d = self.e2.get()
            e = self.e3.get()
            st = "insert into purchase (orderid,bookid,pdate,quantity,totalcost) values({},{},'{}',{},{})".format(a, b,
                                                                                                                  c, d,
                                                                                                                  e)
            self.cursor.execute(st)
            self.con.commit()
            self.cursor.close()
            self.e1.delete(0, END)
            self.e2.delete(0, END)
            self.e3.delete(0, END)

            self.l6.configure(text="Last Insert: Success")
            self.updater()

        self.restoreback()

    def delete(self):
        orderid = self.t.item(self.t.selection())['text']
        self.cursor = self.con.cursor()
        self.cursor.execute("delete from purchase where orderid=%d" % (orderid,))
        self.restoreback()
        self.l6.configure(text="Last Delete: Success")
        self.con.commit()
        self.cursor.close()
        self.updater()

    def search(self):
        k = self.esearch.get()
        self.cursor.execute("select * from purchase where orderid like %s;", ('%' + k + '%',))
        row = self.cursor.fetchall()
        self.t.delete(*self.t.get_children())
        for r in row:
            self.t.insert('', 0, text=r[0], values=(r[0], r[1], r[2], r[3], r[4]))

    def updater(self):
        self.cursor = self.con.cursor()
        self.cursor.execute("select * from purchase;")
        row = self.cursor.fetchall()
        x = self.t.get_children()
        for item in x:
            self.t.delete(item)
        for r in row:
            self.t.insert('', 0, text=r[0], values=(r[0], r[1], r[2], r[3], r[4]))

    def restoreback(self):
        self.e1["state"] = "disabled"
        self.e2["state"] = "disabled"
        self.e3["state"] = "disabled"
        self.t.selection_clear()
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)
        self.b1["state"] = "disabled"
        self.b2["state"] = "disabled"
        self.cmbvar2 = StringVar()
        self.cmbvar2.set('                   SELECT')
        self.bid.delete(0, END)
        self.bid.configure(textvariable=self.cmbvar2)

    def enabler5(self, Event):
        self.b1["state"] = "normal"

    def enabler1(self, Event):
        self.e2["state"] = "normal"

    def enabler2(self, Event):
        self.e3["state"] = "normal"

    def enabler6(self, Event):
        orderid = self.t.item(self.t.selection())['text']
        if (len(str(orderid)) > 0):
            self.b2["state"] = "normal"
        self.l6.configure(text="")

    def enabler7(self, Event):
        self.e1["state"] = "normal"
        self.l6.configure(text="")
        self.esearch.delete(0, END)






