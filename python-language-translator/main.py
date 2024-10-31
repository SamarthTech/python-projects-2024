
from tkinter import *
import tkinter as tk
from tkinter import ttk
from googletrans import Translator
from tkinter import messagebox

# Creating Tkinter Scaffold
root = tk.Tk()
root.title('Language Translator')
root.geometry('530x330')
root.maxsize(530, 330)
root.minsize(530, 330)

# Dictionary mapping language names to their codes
language_mapping = {
    'Afrikaans': 'af', 'Albanian': 'sq', 'Arabic': 'ar', 'Armenian': 'hy', 
    'Azerbaijani': 'az', 'Basque': 'eu', 'Belarusian': 'be', 'Bengali': 'bn', 
    'Bosnian': 'bs', 'Bulgarian': 'bg', 'Catalan': 'ca', 'Cebuano': 'ceb', 
    'Chichewa': 'ny', 'Chinese (Simplified)': 'zh-cn', 'Corsican': 'co', 
    'Croatian': 'hr', 'Czech': 'cs', 'Danish': 'da', 'Dutch': 'nl', 
    'English': 'en', 'Esperanto': 'eo', 'Estonian': 'et', 'Filipino': 'tl', 
    'Finnish': 'fi', 'French': 'fr', 'Frisian': 'fy', 'Galician': 'gl', 
    'Georgian': 'ka', 'German': 'de', 'Greek': 'el', 'Gujarati': 'gu', 
    'Haitian Creole': 'ht', 'Hausa': 'ha', 'Hawaiian': 'haw', 'Hebrew': 'he', 
    'Hindi': 'hi', 'Hmong': 'hmn', 'Hungarian': 'hu', 'Icelandic': 'is', 
    'Igbo': 'ig', 'Indonesian': 'id', 'Irish': 'ga', 'Italian': 'it', 
    'Japanese': 'ja', 'Javanese': 'jv', 'Kannada': 'kn', 'Kazakh': 'kk', 
    'Khmer': 'km', 'Kinyarwanda': 'rw', 'Korean': 'ko', 'Kurdish': 'ku', 
    'Kyrgyz': 'ky', 'Lao': 'lo', 'Latin': 'la', 'Latvian': 'lv', 
    'Lithuanian': 'lt', 'Luxembourgish': 'lb', 'Macedonian': 'mk', 
    'Malagasy': 'mg', 'Malay': 'ms', 'Malayalam': 'ml', 'Maltese': 'mt', 
    'Maori': 'mi', 'Marathi': 'mr', 'Mongolian': 'mn', 'Myanmar (Burmese)': 'my', 
    'Nepali': 'ne', 'Norwegian': 'no', 'Odia': 'or', 'Pashto': 'ps', 
    'Persian': 'fa', 'Polish': 'pl', 'Portuguese': 'pt', 'Punjabi': 'pa', 
    'Romanian': 'ro', 'Russian': 'ru', 'Samoan': 'sm', 'Scots Gaelic': 'gd', 
    'Serbian': 'sr', 'Sesotho': 'st', 'Shona': 'sn', 'Sindhi': 'sd', 
    'Sinhala': 'si', 'Slovak': 'sk', 'Slovenian': 'sl', 'Somali': 'so', 
    'Spanish': 'es', 'Sundanese': 'su', 'Swahili': 'sw', 'Swedish': 'sv', 
    'Tajik': 'tg', 'Tamil': 'ta', 'Tatar': 'tt', 'Telugu': 'te', 'Thai': 'th', 
    'Turkish': 'tr', 'Turkmen': 'tk', 'Ukrainian': 'uk', 'Urdu': 'ur', 
    'Uyghur': 'ug', 'Uzbek': 'uz', 'Vietnamese': 'vi', 'Welsh': 'cy', 
    'Xhosa': 'xh', 'Yiddish': 'yi', 'Yoruba': 'yo', 'Zulu': 'zu'
}

# Function to translate using the updated Translator package
def translate():
    language_1 = t1.get("1.0", "end-1c")
    selected_language = choose_langauge.get()

    if language_1 == '':
        messagebox.showerror('Language Translator', 'Please fill the box')
    else:
        t2.delete(1.0, 'end')
        translator = Translator()
        language_code = language_mapping[selected_language]
        output = translator.translate(language_1, dest=language_code)
        t2.insert('end', output.text)

# Function to clear the input fields
def clear():
    t1.delete(1.0, 'end')
    t2.delete(1.0, 'end')

# SelectBox 1 for auto-detected language
auto_detect_language = tk.StringVar()
auto_detect = ttk.Combobox(
    root,
    width=20,
    textvariable=auto_detect_language,
    state='readonly',
    font=('verdana', 10, 'bold'),
)
auto_detect['values'] = ('Auto Detect',)
auto_detect.place(x=30, y=70)
auto_detect.current(0)

# SelectBox 2 for selected language
language_selected = tk.StringVar()
choose_langauge = ttk.Combobox(root,
                               width=20,
                               textvariable=language_selected,
                               state='readonly',
                               font=('verdana', 10, 'bold'))
choose_langauge['values'] = list(language_mapping.keys())
choose_langauge.place(x=290, y=70)
choose_langauge.current(0)

# To store Input Text
t1 = Text(root, width=30, height=10, borderwidth=5, relief=RIDGE)
t1.place(x=10, y=100)

# To store translated Text
t2 = Text(root, width=30, height=10, borderwidth=5, relief=RIDGE)
t2.place(x=260, y=100)

# Translate Button
button = Button(root,
                text="Translate",
                relief=RIDGE,
                borderwidth=3,
                font=('verdana', 10, 'bold'),
                cursor="hand2",
                foreground='Green',
                command=translate)
button.place(x=150, y=280)

# Clear Button
clear_button = Button(root,
                      text="Clear",
                      relief=RIDGE,
                      borderwidth=3,
                      font=('verdana', 10, 'bold'),
                      cursor="hand2",
                      foreground='Red',
                      command=clear)
clear_button.place(x=280, y=280)

root.mainloop()
