import tkinter as tk
import tkinter.scrolledtext as sb_text
from tkinter import *
from PyDictionary import PyDictionary

# Defining CreateWidgets() function to create necessary tkinter widgets
def CreateWidgets():
    inputLabel = Label(root, text="WORD : ", bg="skyblue4")
    inputLabel.grid(row=0, column=0, padx=10, pady=5)

    wordEntry = Entry(root, width=25, bg='snow3', textvariable=inputWord)
    wordEntry.grid(row=0, column=1, padx=10, pady=5)

    searchButton = Button(root, text="SEARCH", command=findMeaning)
    searchButton.grid(row=0, column=2, padx=10, pady=5)

    resultsLabel = Label(root, text="MEANING : ", bg="skyblue4")
    resultsLabel.grid(row=1, column=0, padx=10, pady=5)

    root.meaningDetails = sb_text.ScrolledText(root, width=40, height=20, bg='snow3')
    root.meaningDetails.grid(row=2, column=0, rowspan=10, columnspan=3, padx=10, pady=5)
    # Making the Text Widget uneditable by setting state parameter of config() to DISABLED
    root.meaningDetails.config(state=DISABLED, font = "Calibri 15", wrap="word")

# Defining the findMeaning() to get the meaning of user-entered word
def findMeaning():
    # Creating object of PyDictionary Class of PyDictionary Library
    dictionaryObject = PyDictionary()
    # Finding meaning of user-entered word using meaning() of dictionaryObject
    wordMeaning = dictionaryObject.meaning(inputWord.get())
    # Creating an empty string variable called meaningDetails
    meaningDetails = ""
    # Checking if "Noun" keyword is there in the meaning result
    if "Noun" in wordMeaning:
        # Concatenating the list of meanings in the meaningDetails variable
        meaningDetails += "Noun:\n- " + "\n- ".join(wordMeaning['Noun'])
    # Checking if "Verb" keyword is there in the meaning result
    if "Verb" in wordMeaning:
        # Concatenating the list of meanings in the meaningDetails variable
        meaningDetails += "\n\nVerb:\n- " + "\n- ".join(wordMeaning['Verb'])
    # Enabling the Text Widget by setting state parameter of config() to NORMAL
    root.meaningDetails.config(state=NORMAL)
    # Clearing the entries from the Text Widget using the delete() method
    root.meaningDetails.delete('1.0', END)
    # Displaying user-entered word meaning details in the meaningDetails Widget
    root.meaningDetails.insert("end", meaningDetails)
    # Making Widget uneditable again after the displaying list of news from feed
    root.meaningDetails.config(state=DISABLED)

# Creating object of tk class
root = tk.Tk()

# Setting the title, background color, windowsize
# & disabling the resizing property
root.title("Python Dictionary")
root.geometry("480x320")
root.config(background="skyblue4")
root.resizable(True, True)

# Creating the tkinter variables
inputWord = StringVar()

# Calling the CreateWidgets() function
CreateWidgets()

# Defining infinite loop to run application
root.mainloop()