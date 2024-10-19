import tkinter as tk
from tkinter import ttk, messagebox
import requests

class CurrencyConverter:
    def __init__(self):
        self.api_url = "https://api.exchangerate-api.com/v4/latest/USD"
        self.rates = self.fetch_rates()

    def fetch_rates(self):
        try:
            response = requests.get(self.api_url)
            data = response.json()
            return data["rates"]
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching exchange rates: {e}")
            return {}

    def convert(self, amount, from_currency, to_currency):
        if from_currency == "USD":
            return amount * self.rates[to_currency]
        else:
            # Convert to USD first
            amount_in_usd = amount / self.rates[from_currency]
            return amount_in_usd * self.rates[to_currency]

class CurrencyConverterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Currency Converter")
        self.master.geometry("400x300")

        self.converter = CurrencyConverter()

        self.amount_label = tk.Label(master, text="Amount:")
        self.amount_label.pack(pady=10)

        self.amount_entry = tk.Entry(master)
        self.amount_entry.pack()

        self.from_currency_label = tk.Label(master, text="From Currency:")
        self.from_currency_label.pack(pady=10)

        self.from_currency_combobox = ttk.Combobox(master, values=list(self.converter.rates.keys()), state='readonly')
        self.from_currency_combobox.set("USD")
        self.from_currency_combobox.pack()

        self.to_currency_label = tk.Label(master, text="To Currency:")
        self.to_currency_label.pack(pady=10)

        self.to_currency_combobox = ttk.Combobox(master, values=list(self.converter.rates.keys()), state='readonly')
        self.to_currency_combobox.set("EUR")
        self.to_currency_combobox.pack()

        self.convert_button = tk.Button(master, text="Convert", command=self.perform_conversion)
        self.convert_button.pack(pady=20)

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def perform_conversion(self):
        try:
            amount = float(self.amount_entry.get())
            from_currency = self.from_currency_combobox.get()
            to_currency = self.to_currency_combobox.get()
            converted_amount = self.converter.convert(amount, from_currency, to_currency)
            self.result_label.config(text=f"Converted Amount: {converted_amount:.2f} {to_currency}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid amount.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()