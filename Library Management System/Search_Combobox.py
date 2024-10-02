from tkinter import *
from tkinter import ttk
import tkinter.font as font






class cmbxAUTHOR:
    def __init__(self,con,k):
        self.root=Toplevel()
        self.root.geometry('1062x422+150+100')
        self.con=con
        self.cursor=self.con.cursor()
        self.root.title("Search Result")
        self.root.resizable(0,0)

        self.frm1 = Frame(self.root, width=1060, height=45, bd=3, relief=SUNKEN, bg='#4589aa')
        self.frm1.place(x=0, y=2)
        Label(self.frm1, text='Author Name', width=11, font=('Times', 15, font.BOLD), bg="#deadaf", relief=RIDGE,
              bd=5).place(x=468, y=5)

        s = ttk.Style()
        s.theme_use('clam')
        s.configure('Treeview', background="green", fieldbackground="#deadaf", foreground="yellow")
        self.t = ttk.Treeview(self.root, height=17)
        self.t["show"] = "headings"
        self.t["columns"] = ['BookID', 'BookName', 'Author', 'Quantity', 'Cost']
        for i in range(5):
            self.t.heading(i, text="{}".format(self.t["columns"][i]))
        self.t.column(i, anchor=CENTER, width=240)
        self.t.place(x=0, y=50)
        #self.t.bind('<<TreeviewSelect>>', self.enabler5)
        self.cursor.execute("select * from bookdetails where author like '%{}%'".format(k))
        row = self.cursor.fetchall()
        x = self.t.get_children()
        for item in x:
            self.t.delete(item)
        for r in row:
            self.t.insert('', 0, text=r[0], values=(r[0], r[1], r[2], r[3], r[4]))

        self.scrol = ttk.Scrollbar(self.root, orient=VERTICAL, command=self.t.yview)
        self.t["yscrollcommand"] = self.scrol.set
        self.scrol.place(x=1046, y=50, height=370)

        self.root.mainloop()
















class cmbxBKNAME:
    def __init__(self,con,k):
        self.root=Toplevel()
        self.root.geometry('1062x422+150+100')

        self.con=con
        self.cursor=self.con.cursor()
        self.root.title("Search Result")
        self.root.resizable(0,0)

        self.frm1 = Frame(self.root, width=1060, height=45, bd=3, relief=SUNKEN, bg='#4589aa')
        self.frm1.place(x=0, y=2)
        Label(self.frm1, text='Book Name', width=11, font=('Times', 15, font.BOLD), bg="#deadaf", relief=RIDGE,
              bd=5).place(x=468, y=5)



        s = ttk.Style()
        s.theme_use('clam')
        s.configure('Treeview', background="green", fieldbackground="#deadaf", foreground="yellow")
        self.t = ttk.Treeview(self.root, height=17)
        self.t["show"] = "headings"
        self.t["columns"] = ['BookID', 'BookName', 'Author', 'Quantity', 'Cost']
        for i in range(5):
            self.t.heading(i, text="{}".format(self.t["columns"][i]))
        self.t.column(i, anchor=CENTER, width=240)
        self.t.place(x=0, y=50)
        #self.t.bind('<<TreeviewSelect>>', self.enabler5)
        self.cursor.execute("select * from bookdetails where bkname like '%{}%'".format(k))
        row = self.cursor.fetchall()
        x = self.t.get_children()
        for item in x:
            self.t.delete(item)
        for r in row:
            self.t.insert('', 0, text=r[0], values=(r[0], r[1], r[2], r[3], r[4]))

        self.scrol = ttk.Scrollbar(self.root, orient=VERTICAL, command=self.t.yview)
        self.t["yscrollcommand"] = self.scrol.set
        self.scrol.place(x=1046, y=50, height=370)

        self.root.mainloop()















class cmbxMEMBER:
    def __init__(self,con,k):
        self.root=Toplevel()
        self.root.geometry('1062x422+150+100')
        self.con=con
        self.cursor=self.con.cursor()
        self.root.title("Search Result")
        self.root.resizable(0,0)

        self.frm1 = Frame(self.root, width=1060, height=45, bd=3, relief=SUNKEN, bg='#4589aa')
        self.frm1.place(x=0, y=2)
        Label(self.frm1, text='Member ID', width=11, font=('Times', 15, font.BOLD), bg="#deadaf", relief=RIDGE,
              bd=5).place(x=468, y=5)



        s = ttk.Style()
        s.theme_use('clam')
        s.configure('Treeview', background="green", fieldbackground="#deadaf", foreground="yellow")
        self.t = ttk.Treeview(self.root, height=17)
        self.t["show"] = "headings"
        self.t["columns"] = ['MemberID', 'Member Name', 'Contact', 'Registration Date', 'Address']
        for i in range(5):
            self.t.heading(i, text="{}".format(self.t["columns"][i]))
        self.t.column(i, anchor=CENTER, width=240)
        self.t.place(x=0, y=50)
        #self.t.bind('<<TreeviewSelect>>', self.enabler5)
        self.cursor.execute("select * from userdetails where mid like %s;", ('%'+k,))
        row = self.cursor.fetchall()
        x = self.t.get_children()
        for item in x:
            self.t.delete(item)
        for r in row:
            self.t.insert('', 0, text=r[0], values=(r[0], r[1], r[2], r[3], r[4]))

        self.scrol = ttk.Scrollbar(self.root, orient=VERTICAL, command=self.t.yview)
        self.t["yscrollcommand"] = self.scrol.set
        self.scrol.place(x=1046, y=50, height=370)
        self.root.mainloop()










