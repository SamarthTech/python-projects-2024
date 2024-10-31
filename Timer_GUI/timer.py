from tkinter import *


FONT = ("Arial", 10, "bold")
work_time = None
s_break_time= None
l_break_time= None
frequency = None
wrk_count= 0
rep = 0
done = " "
time_machine = None



# Reset Timer
def reset():
    global rep
    global wrk_count
    try:
        window.after_cancel(time_machine)
        canvas.itemconfig(timer_text, text = "00 : 00")
        timer.config(text="SET TIMER...")
        check_box.config(text=" ")
        start.config(state="normal")
        work.config(state="normal")
        s_break.config(state="normal")
        l_break.config(state="normal")
        freq.config(state="normal")
        rep= 0
        wrk_count = 0
    except ValueError:
        check_box.config(text = "Something went wrong!", fg="red")

# Setting The Timer
def set_time():
    global work_time 
    global s_break_time
    global l_break_time
    global frequency

    try: 
        work_time = int(work.get()) * 60
        s_break_time= int(s_break.get()) * 60
        l_break_time= int(l_break.get()) * 60
        frequency= int(freq.get())
        check_box.config(text = " ", fg="green")
        if work_time > 0 and s_break_time> 0 and l_break_time > 0 and frequency > 0:
            timer_start()
        else :
            check_box.config(text = "Invalid Time!", fg="red")
        
    except ValueError:
        check_box.config(text = "Something went wrong! please check your inputs.", fg="red")
            
# Timer Mechanism
def timer_start():
    global rep
    global done
    global wrk_count
    start.config(state="disabled")
    work.config(state="disabled")
    s_break.config(state="disabled")
    l_break.config(state="disabled")
    freq.config(state="disabled")
    
    
    if wrk_count % frequency == 0 and wrk_count != 0:
        count_down(l_break_time)
        timer.config(text="Long Break Time", fg="blue")
        done += "   ✔"
        check_box.config(text=done, fg="green")
        

    elif rep % 2 == 0:
        count_down(work_time)
        timer.config(text="Working Time", fg="red")
        wrk_count += 1
    
         
    else:
        count_down(s_break_time)
        timer.config(text="Short Break Time", fg="green")
        done += "   ✔"
        check_box.config(text=done, fg="green")
        
        
    rep += 1

# Time Mechanism  
def count_down(count):
    global time_machine
    hr = count // 3600
    hr_rem = count % 3600
    min= hr_rem // 60
    sec = hr_rem % 60

    # dynamically typing : changing datatype dynamically
    if sec < 10:
        sec = f"0{sec}"
    if min < 10:
        min = f"0{min}"

    show= f"{min} : {sec}"
    if hr > 0:
        show = f"{hr} : {min} : {sec}"

    canvas.itemconfig(timer_text, text=show)
    if count > 0:
        time_machine= window.after(1000, count_down, count-1)
        
    else:
        timer_start()

window= Tk()
window.config(bg="yellow")
window.title("Timer")

# Timer Label
timer= Label(text="SET TIMER...", fg="green", font=("Cursive", 30, "italic"),bg="yellow")
timer.grid(column=1, row=1, columnspan=2)

# Screen Set Up
canvas = Canvas(width=400, height= 400, bg="yellow", highlightthickness=0)
photo = PhotoImage(file="image.png")
canvas.create_image(200, 200, image= photo)
timer_text = canvas.create_text(200, 220, text="00 : 00", fill="red", font=("Arial", 20, "bold"))
canvas.grid(column=0, row=1)

# User's Input
ins1= Label(text="Set Work Duration: ", font=FONT, fg="blue", bg="yellow")
ins1.grid(column=0, row=3)
work = Entry(width=20)
work.grid(column= 1 , row=3)
unit1= Label(text="min", font=FONT, fg="blue", bg="yellow")
unit1.grid(column= 2 , row=3)

ins2= Label(text="Set Short Break Duration: ", font=FONT, fg="blue", bg="yellow")
ins2.grid(column=0, row=4)
s_break = Entry(width=20)
s_break.grid(column= 1 , row=4)
unit2= Label(text="min", font=FONT, fg="blue", bg="yellow")
unit2.grid(column= 2 , row=4)

ins3= Label(text="Set Interval (Long Break) Duration: ", font=FONT, fg="blue", bg="yellow")
ins3.grid(column=0, row=5)
l_break = Entry(width=20)
l_break.grid(column= 1 , row=5)
unit3= Label(text="min", font=FONT, fg="blue", bg="yellow")
unit3.grid(column= 2 , row=5)

ins4= Label(text="Set Interval Frequency: ", font=FONT, fg="blue", bg="yellow", padx=10)
ins4.grid(column=0, row=6)
freq = Entry(width=20)
freq.grid(column= 1 , row=6)
unit3= Label(text="times", font=FONT, fg="blue", bg="yellow")
unit3.grid(column= 2 , row=6)


# Start Btn
start= Button(text="Start", font=FONT, fg="pink", bg="red", command=set_time, padx=10)
start.grid(column=3, row=4)

# Reset Btn
reset = Button(text="Reset", font=FONT, fg="pink", bg="red", command= reset, padx=10)
reset.grid(column=3, row=6)

# Check Box
check_box = Label(font= FONT, bg="yellow")
check_box.grid(column=0, row=2)


window.mainloop()