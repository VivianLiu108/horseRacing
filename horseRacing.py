# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 23:49:19 2021

@author: user
"""

from tkinter import*
import random
root=Tk()
root.title("runhorse")
horse="~/-\^"
position=[0]*8
end=0
label=[]
def runhorse():
    run=random.randrange(8)
    position[run]+=1
    global end
    for i in range(8):
        if position[i]<=40:
            horses="{}{}{}|".format(" "*position[i],horse," "*(40-position[i]))
            if end!=1:
                end=0
        else:
            horses="{}{}".format(""*41,horse)
            label[i].config(text=horses)
            end=1
            winner=i
        if end!=1:
            label[i].config(text=horses)
    if end==0:
        root.after(100,runhorse)
    if end==1:
        winlabel=Label(root,text="Horse {} wins!".format(winner+1)).pack()
for i in range(8):
    horses="{}{}{}|".format(" "*position[i],horse," "*(40-position[i]))
    label.append(Label(root,text=horses))
    label[i].pack()
runhorse()
root.mainloop()