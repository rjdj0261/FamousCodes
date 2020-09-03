import time
try:
    #python 2.7
    import Tkinter as tk
    from Tkinter import *
except  ImportError:
    #python 3.6
    import tkinter as tk
    from tkinter import *
 
root=Tk()
root.title("Real-time Digital clock")
root.geometry('700x200')
clock_frame=Label(root,font=('times',100,'bold'),bg='black',fg='green')
clock_frame.pack(fill='both',expand=1) 
 
def ticks(time1=""):
    #Get the current local time from the system
    time2= time.strftime('%I:%M:%S')
    #if the time string has changes, update it
    if time2 != time1:
        time1=time2
        clock_frame.config(text=time2)
    #Calls itself every 200 milliseconds to update
    clock_frame.after(200,ticks)
 
ticks()
mainloop()
