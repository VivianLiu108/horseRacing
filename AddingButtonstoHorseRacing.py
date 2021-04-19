
from tkinter import *
import random

root = Tk()
root.title("Adding Buttons to Horse Racing")

horsegraph = "~/-\^"

long = 40
label = []
tim = 0
global btnr
btnr = Button(root, text = "Restart")
global winlabel
winlabel = Label(root)
def runhorse(position, tim, btnr, winlabel):
    btns.pack_forget()
    run = random.randrange(8)
    position[run] += 1
    end = 0
    for i in range(8):
        if position[i] <= long:
            horses = "{}{}{}|".format(" "*position[i],horsegraph," "*(long - position[i]))
            label[i].config(text = horses)
        else:
            horses = "{}{}".format(" "*(long + 1),horsegraph)
            label[i].config(text = horses)
            end = 1
            winner=i
    if end == 0:
        root.after(10,lambda:runhorse(position, tim, btnr, winlabel))
    if end == 1:
        winlabel.config(text="Horse {} wins!".format(winner + 1))
        winlabel.pack()
        
        #print(btnr["state"])
        if tim == 0:
            btnr = Button(root, text = "Restart", command = lambda:br(tim, btnr, winlabel))
            btnq = Button(root, text = "Quit", command = root.destroy)
            btnr.pack(side = LEFT)
            btnq.pack(side = LEFT)
            tim = 1
        else:
            btnr["state"] = NORMAL 
        
def main(tim, btnr, winlabel):
    position = [0]*8
    for i in range(8):
        horses = "{}{}{}|".format(" "*position[i],horsegraph," "*(long - position[i]))
        label.append(Label(root,text=horses))
        label[i].pack()
    if tim == 0:
        global btns
        btns = Button(root, text = "Start", command = lambda:runhorse(position, tim, btnr, winlabel))
        btns.pack(side = LEFT)
    else:
        runhorse(position, tim, btnr, winlabel)
    
def br(tim, btnr, winlabel):
    print(type(btnr))
    winlabel.pack_forget()
    btnr["state"] = DISABLED
    main(tim, btnr, winlabel)
main(tim, btnr, winlabel)

root.mainloop()





