import serial
import time
import os
from datetime import datetime
# import everything from tkinter module
from tkinter import *
import tkinter.messagebox
from PIL import Image
from PIL import ImageTk

# create a tkinter window
root = Tk()	




def GPS_data():
    f=open("/dev/ttyULR0")
    for line in f:
        if line.startswith('$GPRMC'):
            time=line.strip().split(",")[1]
            date=line.strip().split(",")[9]
            gps_time=time[0:2]+":"+time[2:4]+":"+time[4:6]
            gps_date=date[0:2]+"/"+date[2:4]+"/"+date[4:]
            entry_widget0.delete(0,END)
            entry_widget0.insert(0,gps_time +", "+ gps_date)
            f.close()
            break

      

def GPSD():
    #stream = os.open('mv /dev/ttyULR0 /dev/tty16')
    #stream = os.open('systemctl disable gpsd.socket')
    #stream = os.open('systemctl stop gpsd.service')
    #stream = os.open('systemctl start gpsd.service')
    #stream = os.open('killall -9 gpsd')
    #stream = os.open('gpsd -n -N /dev/tty16 &')
    f=open("/dev/ttyULR0")
    for line in f:
        if line.startswith('$GPRMC'):
            time=line.strip().split(",")[1]
            date=line.strip().split(",")[9]
            gps_time=time[0:2]+":"+time[2:4]+":"+time[4:6]
            gps_date=date[0:2]+"/"+date[2:4]+"/"+date[4:]
            entry_widget1.delete(0,END)
            entry_widget1.insert(0,gps_time +", "+ gps_date)
            f.close()
            break
    entry_widget2.delete(0,END)
    entry_widget2.insert(0,"Acquired")



def Chrony():
    #entry_widget3.insert(0,"system Time")
    now = datetime.now()
    now =datetime.now()
    system_time=now.strftime("%H:%M:%S %d/%m/%Y")
    entry_widget3.delete(0,END)
    entry_widget4.delete(0,END)
    entry_widget3.insert(0,system_time)
    entry_widget4.insert(0,"yes")



def Phc2sys():
    stream = os.popen('phc_ctl /dev/ptp1 get')
    output = stream.read()
    time=output.strip().split("or ")[1]
    entry_widget5.delete(0,END)
    entry_widget6.delete(0,END)
    entry_widget5.insert(0,time)
    entry_widget6.insert(0,"Yes")


root.geometry('400x400')

def onClick():
    tkinter.messagebox.showinfo("welcome",  "service started ")


# Create a photoimage object of the image in the path
gps_image = Image.open("/home/ubuntu/latest.png")
resize=gps_image.resize((440,350))
test = ImageTk.PhotoImage(resize)

label1 = tkinter.Label(image=test)
label1.image = test

# Position image
label1.place(x=465, y=60)

# Create a photoimage object of the image in the path
demo_image = Image.open("/home/ubuntu/demo_image.jpg")
resize1=demo_image.resize((390,290))
test1 = ImageTk.PhotoImage(resize1)

label2 = tkinter.Label(image=test1)
label2.image = test

# Position image
label2.place(x=465, y=410)



gps_widget = Canvas(root, width=350, height=40, bg="Cyan")
gps_widget.place(x=350, y=10)

gps_btn=Button(gps_widget, text = '  GPS TIME   ',font = ('calibri',10,'bold'),  bg = 'DodgerBlue',foreground='black',
                        command = GPS_data)
gps_btn.place(x=25,y=10)

#label_widget1 = Label(root, text="GPS Time")
#gps_widget.create_window(40, 25, window=label_widget1)

entry_widget0 = Entry(root)
gps_widget.create_window(250,24, window=entry_widget0)


canvas_widget = Canvas(root, width=350, height=350, bg="orange")
canvas_widget.place(x=115, y=60)
#canvas_widget.pack()

label_widget1 = Label(root, text="GPS Time")
canvas_widget.create_window(45, 50, window=label_widget1)

label_widget2 = Label(root, text="Gps Status")
canvas_widget.create_window(49, 100, window=label_widget2)

label_widget3 = Label(root, text="sytem time")
canvas_widget.create_window(49, 150, window=label_widget3)

label_widget4 = Label(root, text="sys clk sync status")
canvas_widget.create_window(65, 200, window=label_widget4)

label_widget5 = Label(root, text="Phc clock")
canvas_widget.create_window(45, 250, window=label_widget5)

label_widget6 = Label(root, text="phc clock sync")
canvas_widget.create_window(54, 300, window=label_widget6)

entry_widget1 = Entry(root)
canvas_widget.create_window(220,50, window=entry_widget1)

entry_widget2 = Entry(root)
canvas_widget.create_window(220,100, window=entry_widget2)

entry_widget3 = Entry(root)
canvas_widget.create_window(220,150, window=entry_widget3)

entry_widget4 = Entry(root)
canvas_widget.create_window(220,200, window=entry_widget4)

entry_widget5 = Entry(root)
canvas_widget.create_window(220,250, window=entry_widget5)

entry_widget6 = Entry(root)
canvas_widget.create_window(220,300, window=entry_widget6)

# Create a Button
gpsd_btn = Button(root, text = '  GPSD   ',font = ('calibri',10,'bold'),  bg = 'DodgerBlue',foreground='black',
        command =lambda: [GPSD(), onClick()])
chrony_btn = Button(root, text = '  Chrony ',font = ('calibri',10,'bold'),  bg = 'DodgerBlue',foreground='black',
						command = Chrony)
phc2sys_btn = Button(root, text = 'phc2sys ',font = ('calibri',10,'bold'),  bg = 'DodgerBlue',foreground='black',
						command = Phc2sys)
ptp4l_btn = Button(root, text = '  ptp4l   ',font = ('calibri',10,'bold'),  bg = 'DodgerBlue',foreground='black',
						command = root.destroy)
exit_btn = Button(root, text = '  exit   ',font = ('calibri',10,'bold'),  bg = 'DodgerBlue',foreground='black',
						command = root.destroy)

# Set the position of button on the top of window.

gpsd_btn.pack()
gpsd_btn.place(x=10,y=120)
chrony_btn.place(x=10,y=190)
phc2sys_btn.place(x=10,y=260)
ptp4l_btn.place(x=10,y=330)
exit_btn.place(x=10,y=20)


root.mainloop()

