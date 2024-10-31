# Importing necessary libraries
from tkinter import *
import tkinter.messagebox as mb
import json
import requests
import os

# Functions
def extract_lyrics():
    global artist, song
    artist_name = str(artist.get())
    song_name = str(song.get()).lower()
    link = 'https://api.lyrics.ovh/v1/'+artist_name.replace(' ', '%20')+'/'+song_name.replace(' ', '%20')

    req = requests.get(link)
    json_data = json.loads(req.content)

    try:
        lyrics = json_data['lyrics']

        # Creating a file name for the song lyrics
        file_name = f"{artist_name}_{song_name}.txt".replace(' ', '_')

        # Saving the lyrics to a file in the current directory with UTF-8 encoding
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(f"Artist: {artist_name}\nSong: {song_name}\n\n{lyrics}")

        # Informing the user about the saved file
        mb.showinfo('Lyrics Saved', f'The lyrics to the song "{song_name.title()}" by {artist_name} have been saved as "{file_name}" in the current directory.')
    except KeyError:
        mb.showerror('No such song found',
        'We were unable to find such a song in our directory. Please recheck the name of the artist and the song, and if correct, we apologize because we do not have that song available with us.')

# Initializing the window
root = Tk()
root.title("Song Lyrics Extractor")
root.geometry("600x200")
root.resizable(0, 0)
root.config(bg='CadetBlue')

# Placing the components
Label(root, text='Song Lyrics Extractor', font=("Comic Sans MS", 16, 'bold'), bg='CadetBlue').pack(side=TOP, fill=X)

Label(root, text='Enter the song name: ', font=("Times New Roman", 14), bg='CadetBlue').place(x=20, y=50)
song = StringVar()
Entry(root, width=40, textvariable=song, font=('Times New Roman', 14)).place(x=200, y=50)

Label(root, text='Enter the artist\'s name: ', font=("Times New Roman", 14), bg='CadetBlue').place(x=20, y=100)
artist = StringVar()
Entry(root, width=40, textvariable=artist, font=('Times New Roman', 14)).place(x=200, y=100)

Button(root, text='Extract lyrics', font=("Georgia", 10), width=15, command=extract_lyrics).place(x=220, y=150)

# Finalizing the window
root.update()
root.mainloop()
