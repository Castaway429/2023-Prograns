import customtkinter
import tkinter as tk
import time
import threading
import datetime
import winsound

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

Stop = False

AM = False
PM = False

Alarm = False

alarmTime = ""

def show_page(page):
    for frame in frames:
        if frame == page:
            frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        else:
            frame.pack_forget()

def stopT():
    global Stop
    Stop = True

def start_timer():
    global Stop

    mins = MinEntry.get()
    secs = SecEntry.get()
    hour = HourEntry.get()

    if hour == '':
        hour = 0
    if mins == '':
        mins = 0
    if secs == '':
        secs = 0
        
    myTime = int(secs) + (int(mins) * 60) + (int(hour) * 3600)

    MinEntry.pack_forget()
    Mlabel.pack_forget()

    SecEntry.pack_forget()
    Slabel.pack_forget()

    HourEntry.pack_forget()
    Hlabel.pack_forget()

    StartButton.pack_forget()

    StopButton = customtkinter.CTkButton(master=frame1, text="Stop!", font=("Arial", 25), command=stopT)
    StopButton.pack(pady=10, padx=0, anchor=tk.CENTER)

    for x in range(myTime, 0, -1):
        if Stop == False:
            seconds = x % 60
            minutes = int(x / 60) % 60
            hours = int(x / 3600)
            setTime = f"{hours:02}:{minutes:02}:{seconds:02}"

            Timerlabel.configure(text = setTime, font=("Roboto", 40))

            time.sleep(1)

    Timerlabel.configure(text = "Set a timer for...", font=("Roboto", 20))

    StopButton.pack_forget()

    HourEntry.pack(padx=0, pady=0, anchor=tk.CENTER)
    Hlabel.pack(pady=0, padx=0, anchor=tk.CENTER)

    MinEntry.pack(padx=0, pady=0, anchor=tk.CENTER)
    Mlabel.pack(pady=0, padx=0, anchor=tk.CENTER)

    SecEntry.pack(padx=0, pady=0, anchor=tk.CENTER)
    Slabel.pack(pady=0, padx=0, anchor=tk.CENTER)

    StartButton.pack(pady=10, padx=0, anchor=tk.CENTER)

    if Stop == False:
        winsound.PlaySound('alarmSound.wav', 0)

    Stop = False 

def startT():
    # Create a new thread for the timer
    timer_thread = threading.Thread(target=start_timer)
    # Start the timer thread
    timer_thread.start()

def AmSelected():
    global AM
    global PM

    AM = True

    AMbutton.configure(fg_color="#0AA900")
    PMbutton.configure(fg_color="#808080")

def PmSelected():
    global AM
    global PM

    PM = True

    PMbutton.configure(fg_color="#0AA900")
    AMbutton.configure(fg_color="#808080")

def getTime():
    global Alarm
    global alarmTime
    global AM
    global PM

    hour = AlarmEntryH.get()
    minute = AlarmEntryM.get()

    if hour == '':
        hour = 12
    if minute == '':
        minute = 0
    if hour == '' and minute == '':
        print("Enter a valid timer")

    alarmTime = f"{int(hour):02}:{int(minute):02} "
    if AM == True:
        alarmTime += "AM"
    elif PM == True:
        alarmTime += "PM"
    else:
        alarmTime += "AM"

    current_time = datetime.datetime.now().strftime("%I:%M %p")

    if current_time != alarmTime:
        Alarmlabel.configure(text=f"Timer set for {alarmTime}")
        threading.Timer(1, getTime).start()

    if current_time == alarmTime:
        Alarmlabel.configure(text="Set an alarm for...")
        winsound.PlaySound('alarmSound.wav', 0)
        alarmTime = ""
 

# Navbar
nav = customtkinter.CTkFrame(master=root)
nav.pack(pady=0, padx=0, fill=tk.X)

label = customtkinter.CTkLabel(master=nav, text="Valid Times", font=("Roboto", 40))
label.pack(pady=20, padx=10)

button_frame = customtkinter.CTkFrame(master=nav)
button_frame.pack()

TimerNav = customtkinter.CTkButton(master=button_frame, text="Timer!", font=("Roboto", 13), command=lambda: show_page(frame1))
TimerNav.pack(side=tk.LEFT, padx=10, pady=10, anchor=tk.CENTER)

AlarmNav = customtkinter.CTkButton(master=button_frame, text="Alarm!", font=("Roboto", 13), command=lambda: show_page(frame2))
AlarmNav.pack(side=tk.LEFT, padx=10, pady=10, anchor=tk.CENTER)

# Timer Page
frame1 = customtkinter.CTkScrollableFrame(master=root)
frame1.pack(fill=tk.BOTH, expand=True)

Timerlabel = customtkinter.CTkLabel(master=frame1, text="Set a timer for...", font=("Roboto", 20))
Timerlabel.pack(pady=30, padx=10)

HourEntry = customtkinter.CTkEntry(master=frame1, placeholder_text="HH")
HourEntry.pack(padx=0, pady=0, anchor=tk.CENTER)
Hlabel = customtkinter.CTkLabel(master=frame1, text="Hours", font=("Roboto", 15))
Hlabel.pack(pady=0, padx=0, anchor=tk.CENTER)

MinEntry = customtkinter.CTkEntry(master=frame1, placeholder_text="MM")
MinEntry.pack(padx=0, pady=0, anchor=tk.CENTER)
Mlabel = customtkinter.CTkLabel(master=frame1, text="Minutes", font=("Roboto", 15))
Mlabel.pack(pady=0, padx=0, anchor=tk.CENTER)

SecEntry = customtkinter.CTkEntry(master=frame1, placeholder_text="SS")
SecEntry.pack(padx=0, pady=0, anchor=tk.CENTER)
Slabel = customtkinter.CTkLabel(master=frame1, text="Seconds", font=("Roboto", 15))
Slabel.pack(pady=0, padx=0, anchor=tk.CENTER)

StartButton = customtkinter.CTkButton(master=frame1, text="Start!", font=("Arial", 25), command=startT)
StartButton.pack(pady=10, padx=0, anchor=tk.CENTER)



# Alarm Pages
frame2 = customtkinter.CTkScrollableFrame(master=root)
frame2.pack(fill=tk.BOTH, expand=True)

Alarmlabel = customtkinter.CTkLabel(master=frame2, text="Set an alarm for...", font=("Roboto", 20))
Alarmlabel.pack(pady=10, padx=10)

input_frame = customtkinter.CTkFrame(master=frame2)
input_frame.pack()

time_frame = customtkinter.CTkFrame(master=frame2)
time_frame.pack()

AlarmEntryH = customtkinter.CTkEntry(master=input_frame, placeholder_text="Hour")
AlarmEntryH.pack(side=tk.LEFT, padx=10, pady=10, anchor=tk.CENTER)

seperatorlabel = customtkinter.CTkLabel(master=input_frame, text = ":")
seperatorlabel.pack(side=tk.LEFT, padx=10, pady=10, anchor=tk.CENTER)

AlarmEntryM = customtkinter.CTkEntry(master=input_frame, placeholder_text="Minute")
AlarmEntryM.pack(side=tk.LEFT, padx=10, pady=10, anchor=tk.CENTER)

AMbutton = customtkinter.CTkButton(master=time_frame, text="AM", font=("Roboto", 20), fg_color="#808080", command=AmSelected)
AMbutton.pack(side=tk.LEFT, padx=10, pady=10, anchor=tk.CENTER)
PMbutton = customtkinter.CTkButton(master=time_frame, text="PM", font=("Roboto", 20), fg_color="#808080", command=PmSelected)
PMbutton.pack(side=tk.LEFT, padx=10, pady=10, anchor=tk.CENTER)

SetAlarm = customtkinter.CTkButton(master=frame2, text="Set Timer!",  font=("Roboto", 25), command=getTime)
SetAlarm.pack(pady=20, padx=10)



frames = [frame1, frame2]

show_page(frame1)

root.mainloop()
