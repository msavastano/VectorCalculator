
import os, sys
import RADIANSDEGREES
import math
from tkinter import *

from tkinter import messagebox
from tkinter import colorchooser
from tkinter import filedialog
#from PIL import Image, ImageTk
import VECTORS
RADIUS = 125

vecList = []

CANWIDTH = 400
CANHEIGHT = 400

CIRSTARTY = 75
CIRSTARTX = 75

CIRDIAMY = 250
CIRDIAMX = 250

cbvar = False

def start():

    mtext = float(ment.get())
    mtext1 = float(ment2.get())
    tup = (mtext, mtext1)
    vecList.append(tup)

    lab2 = Label(app, text=vecList, font=18, bg='lightblue')
    lab2.grid(row=6, column=0,columnspan=10)
    callback()

    c = Checkbutton(app, text="Save to Text File?", variable=cbvar)
    c.grid(row=1, column=3, columnspan=2)
    if cbvar == True:

        vfile = 'vfile.txt'
        f = open(vfile,'w')
        f.write(str(callout1))
        f.close()


def mAbout():
    messagebox.showerror(title='About', message='This is my about box')
    return

def mQuit():
    mExit=messagebox.askyesnocancel(title='Quit', message='Are you Sure?')
    if mExit==True:
        root.destroy()
        return

def mColor():
    mycolor = colorchooser.askcolor()
    mlable4=Label(root,text=mycolor).pack()
    return

def mOpen():
    myopen = filedialog.askopenfile()
    mlable5=Label(root,text=myopen).pack()
    return

def callback():
    #print('h')
    app.ent2.delete(0, END)
    app.ent.delete(0, END)


class Applic(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack(expand=YES, fill=BOTH)

        self.createwids()
        self.createcan()



    def createwids(self):

        menubar=Menu(self)
        filemenu=Menu(menubar, tearoff=0)
        filemenu.add_command(label='New')
        filemenu.add_command(label='Open', command=mOpen)
        filemenu.add_command(label='Color', command=mColor)
        filemenu.add_command(label='Save As')
        filemenu.add_command(label='About', command=mAbout)
        filemenu.add_command(label='Close', command=mQuit)
        menubar.add_cascade(label='File', menu=filemenu)
        root.config(menu=menubar)

        setupmenu = Menu(menubar, tearoff=0)
        setupmenu.add_checkbutton(label='auto')
        menubar.add_cascade(label='Setup',menu=setupmenu)

        but = Button(self, relief='groove', bd=4, bg='yellow', fg='red', text='add to list', padx = 20, pady = 20, command=start)
        #but.config(command=callback)
        but.grid(row=0,column=0)
        but2 = Button(self, relief='groove', bd=4, bg='yellow', fg='red', text='send list', padx = 20, pady = 20, command=self.createcan)
        #but2.config(command=self.createcan)
        but2.grid(row=0,column=1)
        #but2.config(command=callback)
        #print(type(but))

        #quitbut = Button(self, text='QUIT', command=root.destroy).grid(row=0,column=1)
        entLab1 = Label(self, text='Magnatude')
        entLab1.grid(row=3,column=0)
        self.ent = Entry(self, width=29, textvariable=ment)
        self.ent.grid(row=4,column=0)
        entLab2 = Label(self, text='Direction')
        entLab2.grid(row=3,column=1)
        self.ent2 = Entry(self, width=29, textvariable=ment2)
        self.ent2.grid(row=4,column=1)



    def createcan(self):

        #print( len(vecList))
        w = Canvas(self, width=CANWIDTH, height=CANHEIGHT, bg="black")
        w.grid(row=5, column=0, columnspan=3)
        w.create_oval(CIRSTARTX, CIRSTARTY, CIRDIAMX+CIRSTARTX, CIRDIAMY+CIRSTARTY, outline="white", width=5)
        #print(VECTORS.Vecs(vecList))


        #print(callout1)
        if len(vecList) > 0:

            callout1 = VECTORS.Vecs(vecList)
            lab4 = Label(self, text=callout1, font= 20, bg='red', fg='yellow')
            lab4.grid(row=7, column=0, columnspan=4)
            rot = callout1.rotAng()
            #print(rot)
            #w.create_line(200, 200, 200, 100, fill='red', width=3)
            #w.create_line(CANHEIGHT/2, CANWIDTH/2, (CANHEIGHT/2)+(RADIANSDEGREES.rad2degrees(math.cos(rot))), (CANWIDTH/2)+(RADIANSDEGREES.rad2degrees(math.sin(rot))), fill='red', width=3)
            w.create_line(CANHEIGHT/2, CANWIDTH/2, CANWIDTH/2+(math.cos( math.radians(rot)) ) * RADIUS, 400-(CANHEIGHT/2+(math.sin( math.radians(rot)) ) * RADIUS), fill='red', width=(math.ceil(callout1.pt())/10))
            #print("sin ", CANHEIGHT/2+(math.sin( math.radians(rot)) ) * RADIUS)
            #print("cos ", CANWIDTH/2+(math.cos( math.radians(rot)) ) * RADIUS)

if __name__ == '__main__':
    root = Tk()
    ment = StringVar()
    ment2 = StringVar()

    #photo = ImageTk.PhotoImage(Image.open("1.png"))
    #print(photo.height())
    #Image.OPEN
    root.geometry('860x600+100+100')
    root.title('Vector Calculator')
    app = Applic(master=root)

    app.mainloop()

#lab = Label(self, bg='red', fg='yellow', height=5, width=10, font=('times', 20, 'bold'), text='Hello World').grid(row=3,column=3, sticky=E)
        #lab.config(bg='red', fg='yellow', height=5, width=10, font=('times', 20, 'bold'))
        #lab.pack(padx=20, pady=20)
        #but2 = Button(self, relief='groove', bd=4, bg='yellow', fg='red', text='press me2', padx = 10, pady = 10).grid(row=1,column=0)

        #but.config(relief='groove', bd=4, bg='yellow', fg='red')
        #but.pack(padx=20, pady=20)
#quitbut.pack()
##        spot = 0
##        for (key, value) in butDict.items():
##            spot = spot + 1
##
##            Button(self, text=key, fg=value).pack(side=TOP, fill=BOTH).grid(row=spot, column=spot)
##
##        for i in range(len(butList)):
##            Button(self, text=butList[i],).pack(side=TOP, fill=BOTH)
        #vecVar = ''


        #self.vecVar = vecVar


        #ent.pack()

        #textBox = Text(self, width=20, height=10)

        #textBox.pack()
