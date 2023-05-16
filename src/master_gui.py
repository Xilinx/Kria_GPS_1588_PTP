#!/usr/bin/python3
# Copyright (C) 2023 Advanced Micro Devices, Inc.
# SPDX-License-Identifier: MIT
#
import serial
import time
import os
from datetime import datetime
from tkinter import *
import tkinter.messagebox
from PIL import Image
from PIL import ImageTk
from tkinter import scrolledtext
import sys 
import subprocess



        

def GPSD():
    stream = os.popen('mv /dev/ttyULR0 /dev/tty16')
    stream = os.popen('killall -9 gpsd')
    stream = os.popen('systemctl disable gpsd.socket')
    stream = os.popen('systemctl stop gpsd.service')
    stream = os.popen('systemctl start gpsd.service')
    stream = os.popen('killall -9 gpsd')
    termf.process = subprocess.Popen(['xterm', '-into', str(termf.winfo_id()), '-e', 'bash -c "  gpsd -D 5 -N -n /dev/tty16  & bash"'])
    gps_status_entry_widget.delete(0,END)
    gps_status_entry_widget.insert(0,"Acquired")


def Chrony():
    stream=os.popen('systemctl start chrony')
    time.sleep(120)
    now = datetime.now()
    now =datetime.now()
    system_time=now.strftime("%H:%M:%S %d/%m/%Y")
    system_time_entry_widget.delete(0,END)
    system_time_status_entry_widget.delete(0,END)
    system_time_entry_widget.insert(0,system_time)
    system_time_status_entry_widget.insert(0,"yes")
    termf.process = subprocess.Popen(['xterm', '-into', str(termf.winfo_id()), '-e', 'bash -c " chronyc sources;chronyc tracking; bash"'])

 

def Phc2sys():
    termf.process = subprocess.Popen(['xterm', '-into', str(termf.winfo_id()), '-e', 'bash -c "  phc2sys -c /dev/ptp1 -s CLOCK_REALTIME -O 0 -m & bash"'])
    time.sleep(5)
    phc_clock_entry_widget.delete(0,END)
    phc_clock_status_entry_widget.delete(0,END)
    now = datetime.now()
    now =datetime.now()
    system_time=now.strftime("%H:%M:%S %d/%m/%Y")
    system_time_entry_widget.delete(0,END)
    system_time_entry_widget.insert(0,system_time)
    stream = os.popen('sudo phc_ctl /dev/ptp1 get')
    output = stream.read()
    phc_time=output.strip().split("or ")[1]
    phc_clock_entry_widget.insert(0,phc_time)
    phc_clock_status_entry_widget.insert(0,"Yes")

def Ptp4l():
    termf.process = subprocess.Popen(['xterm', '-into', str(termf.winfo_id()), '-e', 'bash -c "  ptp4l -i eth0 -m & bash"'])



def onClick():
    tkinter.messagebox.showinfo("welcome",  "Gpsd service started ")

def chrony_status():
    tkinter.messagebox.showinfo("welcome",  "system Time updated with gps time ")

def phc2sys_status():
    tkinter.messagebox.showinfo("welcome",  "PHC Time updated with gps time ")

def ptp4l_status():
    tkinter.messagebox.showinfo("welcome",  "ptp4l Application Running ")


masterWindow= Tk()
masterWindow.title('Master')
screen_width = masterWindow.winfo_screenwidth()
screen_height = masterWindow.winfo_screenheight()
masterWindow.geometry("%dx%d" % (screen_width, screen_height))
canvas_window_width=(screen_width*0.5)
canvas_window_height=(screen_height*0.5)

#### Demo setup widget #####

canvas_widget=Canvas(masterWindow,width=canvas_window_width,height=canvas_window_height,bg="Floralwhite")
canvas_widget.place(relx=0.5,rely=0.5,anchor=NW)
canvas_window_width=int(canvas_window_width)
canvas_window_height=int(canvas_window_height)
demo_image=Image.open("/opt/xilinx/kr260-gps-1588-ptp/share/images/demo_setup.png")
demo_image=demo_image.resize((canvas_window_width,canvas_window_height),Image.ANTIALIAS)
demo_image1=ImageTk.PhotoImage(demo_image)
canvas_widget.create_image(canvas_window_width*0.99,canvas_window_height*0.96,anchor='se',image=demo_image1)

##### Buttons widget #############

canvas_window_width=(screen_width*0.5)
canvas_window_height=(screen_height*0.5)
canvas_widget1=Canvas(masterWindow,width=canvas_window_width,height=canvas_window_height,bg="DarkOliveGreen2")
canvas_widget1.place(relx=0.5,rely=0.5,anchor=SE)
canvas_widget5=Canvas(canvas_widget1,width=canvas_window_width*0.7,height=canvas_window_height,bg="FloralWhite")
canvas_widget5.place(relx=0.7,rely=0.5,anchor='center')

######## Block Diagram Widget ###########

canvas_window_width=(screen_width*0.5)
canvas_window_height=(screen_height*0.5)
canvas_widget2=Canvas(masterWindow,width=canvas_window_width,height=canvas_window_height,bg="Floralwhite")
canvas_widget2.place(relx=0.5,rely=0.5,anchor=SW)
canvas_window_width=int(canvas_window_width)
canvas_window_height=int(canvas_window_height)
image=Image.open("/opt/xilinx/kr260-gps-1588-ptp/share/images/board2board.png")
image=image.resize((canvas_window_width,canvas_window_height),Image.ANTIALIAS)
blk_dgm=ImageTk.PhotoImage(image)
canvas_widget2.create_image(canvas_window_width,canvas_window_height,anchor='se',image=blk_dgm)

#### Status text creation ############

canvas_widget = canvas_widget5.create_text(canvas_window_width*0.1,canvas_window_height*0.2,anchor='n', font = ('Rockwell', 9),fill="purple1",text=" GPS Status   :")
canvas_widget = canvas_widget5.create_text(canvas_window_width*0.1,canvas_window_height*0.33,anchor='n', font = ('Rockwell', 9),fill="purple1",text="System Time :")
canvas_widget = canvas_widget5.create_text(canvas_window_width*0.1,canvas_window_height*0.46,anchor='n', font = ('Rockwell', 9),fill="purple1",text="System Time  :\nSync status ")
canvas_widget = canvas_widget5.create_text(canvas_window_width*0.1,canvas_window_height*0.62,anchor='n', font = ('Rockwell', 9),fill="purple1",text=" PHC Time      :")
canvas_widget = canvas_widget5.create_text(canvas_window_width*0.1,canvas_window_height*0.75,anchor='n', font = ('Rockwell', 9),fill="purple1",text=" PHC Time     :\nSync status  ")


#### Status Entry widget ###########

gps_status_entry_widget = Entry(canvas_widget1,highlightthickness=1)
canvas_widget5.create_window(canvas_window_width*0.4,canvas_window_height*0.25,anchor='s',window=gps_status_entry_widget)
gps_status_entry_widget.config(highlightbackground = "black",highlightcolor = "red")

system_time_entry_widget = Entry(canvas_widget1,highlightthickness=1)
canvas_widget5.create_window(canvas_window_width*0.4,canvas_window_height*0.38,anchor='s',window=system_time_entry_widget)
system_time_entry_widget.config(highlightbackground = "black",highlightcolor = "red")

system_time_status_entry_widget = Entry(canvas_widget1,highlightthickness=1)
canvas_widget5.create_window(canvas_window_width*0.4,canvas_window_height*0.53,anchor='s',window=system_time_status_entry_widget)
system_time_status_entry_widget.config(highlightbackground = "black",highlightcolor = "red")

phc_clock_entry_widget = Entry(canvas_widget1,highlightthickness=1)
canvas_widget5.create_window(canvas_window_width*0.4,canvas_window_height*0.68,anchor='s',window=phc_clock_entry_widget)
phc_clock_entry_widget.config(highlightbackground = "black",highlightcolor = "red")

phc_clock_status_entry_widget = Entry(canvas_widget1,highlightthickness=1)
canvas_widget5.create_window(canvas_window_width*0.4,canvas_window_height*0.8,anchor='s',window=phc_clock_status_entry_widget)
phc_clock_status_entry_widget.config(highlightbackground = "black",highlightcolor = "red")


#### Buttons Creation ########

gpsd_btn = Button(canvas_widget1, text = '  GPSD  ',font = ('calibri',10,'bold'),  bg = 'IndianRed1',foreground='black',command =lambda: [GPSD(),onClick()], anchor='n')
gpsd_btn.place(x=canvas_window_width*0.1,y=canvas_window_height*0.2)

chrony_btn = Button(canvas_widget1, text = ' Chrony ',font = ('calibri',10,'bold'),  bg = 'light slate blue',foreground='black',command =lambda: [Chrony(),chrony_status()], anchor='n')
chrony_btn.place(x=canvas_window_width*0.1,y=canvas_window_height*0.35)

phc2sys_btn = Button(canvas_widget1,text = 'phc2sys ',font = ('calibri',10,'bold'),  bg = 'salmon4',foreground='black',command = lambda: [Phc2sys(),phc2sys_status()],anchor='n')
phc2sys_btn.place(x=canvas_window_width*0.1,y=canvas_window_height*0.5)

ptp4l_btn = Button(canvas_widget1,text = '  ptp4l   ',font = ('calibri',10,'bold'),  bg = 'MediumPurple1',foreground='black',command =lambda:[Ptp4l(),ptp4l_status()],anchor='n')
ptp4l_btn.place(x=canvas_window_width*0.1,y=canvas_window_height*0.65)

exit_btn = Button(canvas_widget1, text = '   exit    ',font = ('calibri',10,'bold'),  bg = 'SeaGreen2',foreground='black',command = masterWindow.destroy,anchor='n')
exit_btn.place(x=canvas_window_width*0.1,y=canvas_window_height*0.8)


### Default GPS status #####

gps_status_entry_widget.delete(0,END)
gps_status_entry_widget.insert(0,"NotAcquired")

#### Default system Time #####

now = datetime.now()
now =datetime.now()
system_time=now.strftime("%H:%M:%S %d/%m/%Y")
system_time_entry_widget.delete(0,END)
system_time_status_entry_widget.delete(0,END)
system_time_entry_widget.insert(0,system_time)
system_time_status_entry_widget.insert(0,"No")


### Default PHC clock and status##############
stream = os.popen('sudo phc_ctl /dev/ptp1 get')
output = stream.read()
phc_time=output.strip().split("or ")[1]
phc_clock_entry_widget.delete(0,END)
phc_clock_status_entry_widget.delete(0,END)
phc_clock_entry_widget.insert(0,phc_time)
phc_clock_status_entry_widget.insert(0,"No")


#### Terminal Creation #####

termf = Frame(masterWindow, height=canvas_window_height*0.9,width=canvas_window_width*0.91)
termf.place(relx=0.49,rely=0.52,anchor=NE)
wid = termf.winfo_id()

masterWindow.mainloop()
