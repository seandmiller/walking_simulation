from backend import random_walk, simulate
from tkinter import *
from time import sleep
import tkinter.font as font

path=[['-' for x in range(5)] for y in range(5)]

window=Tk()

#for x in simulate(path,1):
 #   print(x)
lbl=Label(text=f'Graph will show here',pady=80,padx=50)
lbl_1=Label(text=f'-',pady=80,padx=50)
lbl_2=Label(text=f'-',pady=80,padx=50)
lbl_3=Label(text=f'-',pady=80,padx=50)
lbl_4=Label(text="xt")

count=0

my_font=font.Font(size=35)
lbl['font']=my_font
lbl_1['font']=my_font
lbl_2['font']=my_font
lbl_3['font']=my_font
lbl_4['font']=my_font

lbl.grid(row=1,column=1)
t_entry=Entry(borderwidth=3)
t_entry.grid(row=0,column=1)



tracker=0


def anima(pth,num,lop,track):
  global path
  path=pth
  trcker=track
  try:
    lop=int(lop)
    reset=False
    
  except:
    if lop=='reset':
      lop=1
      reset=True
      trcker=0
      path=[['-' for x in range(5)] for y in range(5)]
    else:
      lop=0  
      print('bad dabs')
  def lp(reset,pah,t):
     path=pah
     global tracker
     tracker=t
     the_end=path[4][4]
     for x in range(lop):
       if the_end!='#':
         tracker+=1
         print('asa')
       if reset==True:
         
         print('bad dabs')
         reset=False
       else:
         path=simulate(path,num)
       lbl.config(text=f"{path[0]}",padx=10,pady=5)
       lbl_1.config(text=f"{path[1]}",padx=10,pady=5)
       lbl_2.config(text=f"{path[2]}",padx=10,pady=5)
       lbl_3.config(text=f"{path[3]}",padx=10,pady=5)
       lbl_4.config(text=f"{path[4]}",padx=10,pady=5)
       lbl_1.grid(row=2,column=1)
       lbl_2.grid(row=3,column=1)
       lbl_3.grid(row=4,column=1)
       lbl_4.grid(row=5,column=1)

  lp(reset,path,trcker)
  the_end=path[4][4]
  success=Label(text='We have reached the end',fg='red')
  if the_end=='#' and lop!='reset':
    
    success.config(text=f'We have reached the end,\nAfter {tracker} steps',fg='green',pady=15,bg='lightgray')
    success.grid(row=8,column=1)
  else:
    
    success.config(text='End has not been reached',fg='red',bg='black',pady=15,padx=1)
    success.grid(row=8,column=1)  
    


def stop_anmat(arg):
  window.after_cancel(arg)
  
btn=Button(text="The Button",command=lambda: anima(path,1,t_entry.get(),tracker))
btn.grid(row=6,column=1)
window.bind('<Return>', lambda x: anima(path,1,t_entry.get(),tracker))

window.mainloop()





