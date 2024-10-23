from bs4 import BeautifulSoup
from decimal import Decimal
import requests,os
import tkinter as tk
from tkinter import ttk

class MainApplication(tk.Frame):

    font = ('arial', 11)
    precision=4 #how many numbers after the "."
    # add icon and name to window
    def setup_apear(self):
        window.title("Currency Converter")
        try:
            window.iconbitmap("icon.ico")
        except:
            pass

    # saves current parameters to .conf file
    def save_size(self):
        with open("myapp.conf", "w") as conf:
            conf.write(self.create_conf_data())

    # create data in .conf file format
    def create_conf_data(self):
        return self.window.geometry() + '\n'+str(self.font[0])+","+str(self.font[1])+'\n' + str(self.window.state())

    # set up window parameters
    def set_gui_parameters(self):
        if os.path.isfile('myapp.conf'):
            with open("myapp.conf", "r") as conf:
                self.get_info_of_conff_file(conf.read())

    # read conff file
    def get_info_of_conff_file(self,data):
        global font
        temp = data.split("\n")
        self.window.geometry(temp[0])
        self.font=(str(temp[1]).split(',')[0], int(str(temp[1]).split(',')[1]))
        if temp[2] == 'zoomed':
            self.window.state('zoomed')

    # takes the number in amount and conver by given parameters
    def convert(self):
        self.save_size()
        self.print_num()
        number = Decimal(self.textbox_amount.get("1.0", tk.END))
        index_from = self.Names.index(self.from_box.get())
        index_to = self.Names.index(self.to_box.get())
        number *= Decimal(self.Values[index_to]) / Decimal(self.Values[index_from])
        self.textbox_output.config(state=tk.NORMAL)
        self.textbox_output.delete("1.0", tk.END)
        if Decimal(round((number), self.precision)) % Decimal(1.0) == 0:
            number = Decimal(round((number), 1))
        else:
            number = Decimal(round((number), self.precision))
        self.textbox_output.insert(tk.END, number)
        self.textbox_output.config(state=tk.DISABLED)

    # delete characters that are not numbers from 'amount' text box
    def print_num(self):
        point = False
        number = "0"
        for i in str(self.textbox_amount.get("1.0", tk.END)):
            if ord(i) >= ord('0') and ord(i) <= ord('9'):
                number += i
            elif ord(i) == ord('.') and not point:
                point = True
                number += i
        number=float(number)
        if Decimal(round(Decimal(number), self.precision)) % Decimal(1.0) == 0:
            number = Decimal(round(Decimal(number), 1))
        else:
            number = Decimal(round(Decimal(number), self.precision))

        self.textbox_amount.delete("1.0", tk.END)
        self.textbox_amount.insert(tk.END, number)

    # saves the data about the exchange rate
    def save_to_file(self,data):
        data_to_save = str(data[0][0]) + "," + str(data[0][1])
        data = data[1:]
        for i in range(data.__len__()):
            data_to_save += "|" + str(data[i][0]) + "," + str(data[i][1])
        with open('data.txt', 'w') as f:
            f.write(data_to_save)
        return data_to_save

    # gets the data about the exchange rate relative to usd
    def exchanges_list_comp_usd(self):
        exchanges = []
        try:
            exchanges = [["US Dollar", "1"]]
            text = requests.get("https://www.x-rates.com/table/?from=USD&amount=1")
            soup = BeautifulSoup(text.content, 'lxml')
            for tr_tag in soup.find_all('tbody')[1]:
                try:
                    td_tags = tr_tag.find_all('td')
                    exchanges.append([td_tags[0].text, td_tags[1].text])

                except:
                    pass
            exchanges.sort()
            exchanges = self.save_to_file(exchanges)
        except:
            if os.path.isfile('data.txt'):
                with open('data.txt', 'r') as f:
                    exchanges = f.read()
        return exchanges

    # returns the names and the values of the excange in 2 lists
    def get_exchanges_names_and_value(self,ex):
        self.Names = []
        self.Value = []
        for i in ex.split("|"):
            self.Names.append(i.split(',')[0])
            self.Value.append(i.split(',')[1])
        return (self.Names, self.Value)


    def __init__(self, window, *args, **kwargs):
        tk.Frame.__init__(self, window, *args, **kwargs)
        self.window = window
        self.setup_apear()
        self.set_gui_parameters() #set up font,window size form conf sife may be disabled
        self.setup_wigets()

    # set up all the wigets and their settings
    def setup_wigets(self):

        exchanges = self.exchanges_list_comp_usd()
        name_and_value = self.get_exchanges_names_and_value(exchanges)
        self.Names = name_and_value[0]
        self.Values = name_and_value[1]

        #self.window.geometry("400x200")

        self.amount_lable = tk.Label(self.window, text="Amount",font=self.font)
        self.from_lable = tk.Label(self.window, text="From",font=self.font)
        self.to_lable = tk.Label(self.window, text="To",font=self.font)
        self.output_lable = tk.Label(self.window, text="Output",font=self.font)

        self.textbox_amount = tk.Text(height="1",width="45",font=self.font)
        self.textbox_output = tk.Text(height="1",width="45",font=self.font)
        self.textbox_output.config(state=tk.DISABLED)

        self.from_box = ttk.Combobox(values=self.Names, takefocus=0,font=self.font)
        self.to_box = ttk.Combobox(values=self.Names, takefocus=0,font=self.font)
        self.from_box.current(0)
        self.to_box.current(0)

        self.Button_convert = tk.Button(self.window, text="Convert", command=self.convert)


        self.amount_lable.grid(row=0, column=1, sticky=tk.W)
        self.textbox_amount.grid(row=1, column=1, sticky=tk.EW)

        self.from_lable.grid(row=2, column=1, sticky=tk.W)
        self.from_box.grid(row=3, column=1, sticky=tk.EW)

        self.to_lable.grid(row=4, column=1, sticky=tk.W)
        self.to_box.grid(row=5, column=1, sticky=tk.EW)

        self.output_lable.grid(row=6, column=1, sticky=tk.W)
        self.textbox_output.grid(row=7, column=1, sticky=tk.EW)

        self.Button_convert.grid(row=8, column=1, sticky=tk.N)
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=5)
        self.window.columnconfigure(2, weight=1)
        self.window.grid_columnconfigure(0, minsize=10)
        self.window.grid_columnconfigure(2, minsize=10)
        self.window.grid_rowconfigure(9, minsize=10)

if __name__ == "__main__":
    window = tk.Tk()
    MainApplication(window)
    window.mainloop()
