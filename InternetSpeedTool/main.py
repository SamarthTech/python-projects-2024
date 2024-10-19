from turtle import st
import speedtest
import socket
import threading
from tkinter.ttk import Progressbar
from tkinter import Tk, Label, Button

def internet_speed_cli():
    '''Command-line program to test internet speed.'''
    try:
        st = speedtest.Speedtest()
        download = st.download() / 1000000
        upload = st.upload() / 1000000
        st.get_servers([])
        ping = st.results.ping
        
        print(f"Your ⏬ Download speed is {round(download, 3)} Mbps")
        print(f"Your ⏫ Upload speed is {round(upload, 3)} Mbps")
        print(f"Your Ping is {ping} ms")
    except Exception as e:
        print(f"Error testing speed: {e}")

def internet_speed_gui():
    '''Tkinter GUI for internet speed testing.'''
    
    def check_speed():
        '''Fetch download and upload speeds.'''
        try:
            global download_speed, upload_speed, ping
            speed_test = speedtest.Speedtest()  # Correct instance of Speedtest
            download = speed_test.download()
            upload = speed_test.upload()

            download_speed = round(download / (10 ** 6), 2)
            upload_speed = round(upload / (10 ** 6), 2)

            # Fetch ping data
            speed_test.get_best_server()  # Retrieves the best server first before ping
            ping = speed_test.results.ping
        except Exception as e:
            down_label.config(text=f"Error: {e}")
            up_label.config(text="")
            ping_label.config(text="")

    def update_text():
        '''Update the GUI text with speed test results.'''
        global download_speed, upload_speed, ping
        download_speed, upload_speed, ping = 0, 0, 0
        
        thread = threading.Thread(target=check_speed)
        thread.start()
        
        progress = Progressbar(root, orient='horizontal', length=250, mode='indeterminate')
        progress.place(x=110, y=180)
        progress.start()

        while thread.is_alive():
            root.update()

        down_label.config(text="⏬ Download Speed - " + str(download_speed) + " Mbps")
        up_label.config(text="⏫ Upload Speed - " + str(upload_speed) + " Mbps")

        if ping != 0:
            ping_label.config(text="Your Ping is - " + str(ping) + " ms")
        else:
            ping_label.config(text="Ping Error: Unable to fetch ping")

        progress.stop()
        progress.destroy()

    root = Tk()
    root.title("Test Internet Speed")
    root.geometry('480x320')
    root.resizable(False, False)
    root.configure(bg="#ffffff")

    Label(root, text='TEST INTERNET SPEED', bg='#ffffff', fg='#404042', font='arial 25 bold').pack(pady=10)


    down_label = Label(root, text="⏬ Download Speed - ", bg='#fff', font='arial 12 bold')
    down_label.place(x=110, y=70)
    up_label = Label(root, text="⏫ Upload Speed - ", bg='#fff', font='arial 12 bold')
    up_label.place(x=110, y=100)
    ping_label = Label(root, text="Your Ping - ", bg='#fff', font='arial 12 bold')
    ping_label.place(x=110, y=130)

    button = Button(root, text="Check Speed ▶", width=35, bd=0, bg='#404042', fg='#fff', pady=10, command=update_text)
    button.place(x=110, y=220)

    root.mainloop()


def get_ip_address():
    '''Program to find IP address of a website.'''
    hostname = input("Please enter website address (URL): ")
    try:
        print(f'Hostname: {hostname}')
        print(f'IP: {socket.gethostbyname(hostname)}')
    except socket.gaierror as error:
        print(f'Invalid Hostname, error raised is {error}')

if __name__ == "__main__":
    print("Choose an option:")
    print("1: Test Internet Speed (Command Line)")
    print("2: Test Internet Speed (GUI)")
    print("3: Find IP Address of Website")
    choice = input("Enter your choice: ")

    if choice == '1':
        internet_speed_cli()
    elif choice == '2':
        internet_speed_gui()
    elif choice == '3':
        get_ip_address()
    else:
        print("Invalid choice!")
