from tkinter import *
from pytubefix import YouTube
from pytubefix.exceptions import RegexMatchError
import os
import threading

BACKGROUND_COLOR = "#DAF7A6" 


def download_mp3_format () :
    url = link.get()
    if url != "":
        status.config(text=f"Trying to download...", fg="#0364fa")
        threading.Thread(target=download_audio, args=(url,)).start()
        
    else :
        status.config(text="No URL Found!!", fg= "#f34f4f")


def download_audio (url) :
    try:
        video = YouTube(url)

        # Extracting The Audio
        stream = video.streams.filter(only_audio=True).order_by('abr').first()
        downloaded_file = stream.download()
        
        # Saving to a mp3 file
        base, ext = downloaded_file.rsplit(".", 1)
        changed_name = f"{base}.mp3"
        os.rename(downloaded_file, changed_name)

        

    except RegexMatchError as e:
        status.config(text=f"Regex Error: {e}",fg= "#f34f4f")

    except Exception as e:
        status.config(text=f"Something went wrong:\n {e}",fg= "#f34f4f")

    else:
        update_status("Video downloaded in mp3 format")

        


def download_mp4_format () :
    url = link.get()
    if url != "":
        status.config(text=f"Trying to download...", fg="#0364fa")
        threading.Thread(target=download_video, args=(url,)).start()
        

    else :
        status.config(text="No URL Found!!", fg= "#f34f4f")


def download_video (url) :
    try:
        video = YouTube(url)

        # Downloading mp4
        stream = video.streams.filter(progressive=True).order_by('resolution').first()

        # File ext is already mp4 no need to change 
        stream.download()
            

    except RegexMatchError as e:
        status.config(text=f"Regex Error: {e}",fg= "#f34f4f")

    except Exception as e:
        status.config(text=f"Something went wrong:\n{e}",fg= "#f34f4f")

    else:
        update_status("Video downloaded in mp4 format")


def update_status(message):
    # Updating the GUI after download finish
    window.after(0, lambda: status.config(text=message, fg="#41f707"))


    


window = Tk()
window.config(bg= BACKGROUND_COLOR)
window.title("YouTube Video Downloder.")

logo = Canvas(height=400, width=400, bg= BACKGROUND_COLOR, highlightthickness=0)
logo_img = PhotoImage(file="youtube1.png")
logo.create_image(200,200, image = logo_img)
logo.create_text(200, 300, text="YouTube Video Downloader", font=("Arial", 20, "bold"), fill="#FF5733")
logo.grid(column=0, row=0, columnspan=2)


lable = Label(text="Entre Video Link: ", font=("Arial", 10, "bold"), bg= BACKGROUND_COLOR, fg="#900C3F")
lable.grid(column=0, row=1)

link = Entry(width=50, bg= "#f3e3e3", fg="#1d1d1d", highlightthickness=0)
link.grid(column= 1, row=1)

status = Label(text="", font=("Arial", 10, "bold"), bg= BACKGROUND_COLOR)
status.grid(column=0, row=2, columnspan=2)

downloadmp4 = Button(text="Download_mp4_format",font=("Arial", 10, "bold"), bg="#41f707", fg="#1d1d1d", command= download_mp4_format)
downloadmp4.grid(column=0, row=3, columnspan=2)


downloadmp3 = Button(text="Download_mp3_format", font=("Arial", 10, "bold"), bg="#b2eb1c", fg="#1d1d1d", command= download_mp3_format)
downloadmp3.grid(column=0, row=4, columnspan=2)





window.mainloop()