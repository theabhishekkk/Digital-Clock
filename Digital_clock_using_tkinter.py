from tkinter import *
import datetime

def date_time():
    time = datetime.datetime.now()
    h=time.strftime('%I')
    m=time.strftime('%M')
    sec=time.strftime('%S')
    am=time.strftime('%p')

    date=time.strftime("%d")
    month=time.strftime('%m')
    year=time.strftime("%y")
    day=time.strftime("%a")
    

    lab_h.config(text=h)
    lab_m.config(text=m)
    lab_sec.config(text=sec)
    lab_am.config(text=am)
    lab_h.after(200,date_time)

    lab_date.config(text=date)
    lab_year.config(text=year)
    lab_day.config(text=day)
    lab_mo.config(text=month)

clock = Tk()
clock.title('))))-  Digital Clock  -(((')
clock.geometry("1000x500")
clock.config(bg="#B3F933")


#Displaying Time

#for hour
lab_h = Label(clock,text="00",font=('Time New Roman',60,"bold"),bg='red',fg='white')
lab_h.place(x=120,y=50,height=110,width=100)
lab_h_txt = Label(clock,text="Hour",font=('Time New Roman',22,"bold"),bg='red',fg='white')
lab_h_txt.place(x=120,y=190,height=40,width=100)

#for minute
lab_m = Label(clock,text="00",font=('Time New Roman',60,"bold"),bg='red',fg='white')
lab_m.place(x=340,y=50,height=110,width=100)
lab_m_txt = Label(clock,text="Min.",font=('Time New Roman',22,"bold"),bg='red',fg='white')
lab_m_txt.place(x=340,y=190,height=40,width=100)

#for seconds
lab_sec = Label(clock,text="00",font=('Time New Roman',60,"bold"),bg='red',fg='white')
lab_sec.place(x=560,y=50,height=110,width=100)
lab_sec_txt = Label(clock,text="Sec.",font=('Time New Roman',22,"bold"),bg='red',fg='white')
lab_sec_txt.place(x=560,y=190,height=40,width=100)

#for am/pm
lab_am = Label(clock,text="00",font=('Time New Roman',50,"bold"),bg='red',fg='white')
lab_am.place(x=780,y=50,height=110,width=100)
lab_h_txt = Label(clock,text="AM/PM",font=('Time New Roman',22,"bold"),bg='red',fg='white')
lab_h_txt.place(x=780,y=190,height=40,width=100)

#Displaying Date
lab_date = Label(clock,text="00",font=('Time New Roman',60,"bold"),bg='red',fg='white')
lab_date.place(x=120,y=270,height=110,width=100)
lab_date_txt = Label(clock,text="Date",font=('Time New Roman',22,"bold"),bg='red',fg='white')
lab_date_txt.place(x=120,y=410,height=40,width=100)

lab_mo = Label(clock,text="00",font=('Time New Roman',60,"bold"),bg='red',fg='white')
lab_mo.place(x=340,y=270,height=110,width=100)
lab_mo_txt = Label(clock,text="Month",font=('Time New Roman',22,"bold"),bg='red',fg='white')
lab_mo_txt.place(x=340,y=410,height=40,width=100)

lab_year = Label(clock,text="00",font=('Time New Roman',60,"bold"),bg='red',fg='white')
lab_year.place(x=560,y=270,height=110,width=100)
lab_year_txt = Label(clock,text="Year",font=('Time New Roman',22,"bold"),bg='red',fg='white')
lab_year_txt.place(x=560,y=410,height=40,width=100)

lab_day = Label(clock,text="00",font=('Time New Roman',35,"bold"),bg='red',fg='white')
lab_day.place(x=780,y=270,height=110,width=100)
lab_day_txt = Label(clock,text="Day",font=('Time New Roman',22,"bold"),bg='red',fg='white')
lab_day_txt.place(x=780,y=410,height=40,width=100)


date_time()
clock.mainloop()
#End