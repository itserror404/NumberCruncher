from tkinter import *
import tkinter.messagebox
import math

root=Tk()
root.title("Number Cruncher")
root.geometry("650x400+300+300")


switch=None

#display where they show the equation

display= Entry(root, font="Verdana 20",fg="white", bg="#83ccb2",cursor="arrow", justify=RIGHT,bd=0, insertbackground="#83ccb2")
display.pack(fill=BOTH,expand=TRUE)
display.focus_set()
display.insert(0,"0")
entry1=""
#button for save
def save():
    rinput= Tk()
    global entry1
    canvas1 = Canvas(rinput, width = 400, height = 300)
    canvas1.pack()
    entry1 = Entry(rinput) 
    canvas1.create_window(200, 140, window=entry1)
    button1 = Button(rinput,text='SAVE', command=saveas)
    button1.pack(side=LEFT, expand=TRUE, fill=BOTH)
    rinput.mainloop()

def sfor():
    sinput= Tk()
    global entryf
    canvasf = Canvas(sinput, width = 400, height = 300)
    canvasf.pack()
    entryf = Entry(sinput) 
    canvasf.create_window(200, 140, window=entryf)
    button1 = Button(sinput,text='SAVE', command=savef)
    button1.pack(side=LEFT, expand=TRUE, fill=BOTH)
    sinput.mainloop()
    


def saveas():
    answer=display.get()
    date=entry1.get()
    sava=open("save.txt","a+")
    anda=str(answer)+" asked on "+date
    sava.write(anda)
    sava.close()

def savef():
    formul=entryf.get()
    sava=open("Formulae.txt","a+")
    anda=formul
    sava.write(anda)
    sava.close()
        




button=Button(display, height=2, width=4,text="SAVE",activebackground="black",activeforeground="white",bg="#5fa18a",fg="white",relief=GROOVE,command=save)
button.place(x=15,y=10)



#command function for buttons!!
def b1():
    if display.get()=='0':
        display.delete(0,END)
    pos=len(display.get())
    display.insert(pos,"1")

def b2():
    if display.get()=='0':
        display.delete(0,END)
    pos=len(display.get())
    display.insert(pos,"2")
    
def b3():
    if display.get()=='0':
        display.delete(0,END)
    pos=len(display.get())
    display.insert(pos,"3")

def b4():
    if display.get()=='0':
        display.delete(0,END)
    pos=len(display.get())
    display.insert(pos,"4")

def b5():
    if display.get()=='0':
        display.delete(0,END)
    pos=len(display.get())
    display.insert(pos,"5")

def b6():
    if display.get()=='0':
        display.delete(0,END)
    pos=len(display.get())
    display.insert(pos,"6")

def b7():
    if display.get()=='0':
        display.delete(0,END)
    pos=len(display.get())
    display.insert(pos,"7")

def b8():
    if display.get()=='0':
        display.delete(0,END)
    pos=len(display.get())
    display.insert(pos,"8")

def b9():
    if display.get()=='0':
        display.delete(0,END)
    pos=len(display.get())
    display.insert(pos,"9")

def b0():
    if display.get()=='0':
        display.delete(0,END)
    pos=len(display.get())
    display.insert(pos,"0")

def keyevent():
    if display.get()=='0':
        display.delete(0,END)
        
def bplus():
    pos=len(display.get())
    display.insert(pos,"+")

def bminus():
    pos=len(display.get())
    display.insert(pos,"-")

def bmul():
    pos=len(display.get())
    display.insert(pos,"x")

def bdiv():
    pos=len(display.get())
    display.insert(pos,"/")

def bC():
    display.delete(0,END)
    display.insert(0,"0")

def bsin():
    try:
        ans=float(display.get)
        if switch==True:
            ans=math.sin(math.radians(ans))
        else:
            ans=math.sin(ans)
        display.delete(0,END)
        display.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

def bcos():
    try:
        ans=float(display.get())
        if switch==True:
            ans=math.cos(math.radians(ans))
        else:
            ans=math.cos(ans)
        display.delete(0,END)
        display.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error","Check your values and operators")

def btan():
    try:
        ans=float(display.get())
        if switch==True:
            ans=math.tan(math.radians(ans))
        else:
            ans=math.tan(ans)
        display.delete(0,END)
        display.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error","Check your values and operators")

def barccos():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.degrees(math.acos(ans))
        else:
            ans = math.acos(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

def barcsin():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.degrees(math.asin(ans))
        else:
            ans = math.acos(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

def barctan():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.degrees(math.atan(ans))
        else:
            ans = math.acos(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

def bdot():
    pos=len(display.get())
    display.insert(pos,".")

def bpow():
    pos=len(display.get())
    display.insert(pos,"**")
    
def blog():
    try:
        ans = float(display.get())
        ans=math.log10(ans)
        display.delete(0,END)
        display.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")
    
def bfacto():
    try:
        ans=float(display.get())
        ans=math.factorial(ans)
        display.delete(0,END)
        display.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")
        
def bsquare():
    try:
        ans=float(display.get())
        ans=math.square(ans)
        display.delete(0,END)
        display.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")
   
def bpi():
    if display.get()=='0':
        display.delete(0,END)
    pos=len(display.get())
    display.insert(pos,str(math.pi))
    
def be():
    if display.get()=='0':
        display.delete(0,END)
    pos=len(display.get())
    display.insert(pos,str(math.e))

def sqroot():
    try:
        ans = float(display.get())
        ans = math.sqrt(ans)
        display.delete(0, END)
        display.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")
    
def bdelete():
    pos = len(display.get())
    disp = str(display.get())
    
    if disp == '':
        display.insert(0, '0')
    elif disp == ' ':
        display.insert(0, '0')
    elif disp == '0':
        pass
    else:
        display.delete(0, END)
        display.insert(0, disp[0:pos-1])
    
    
def bbrac1():
    pos=len(display.get())
    display.insert(pos,"(")
    
def bbrac2():
    pos=len(display.get())
    display.insert(pos,")")
    
def bmod():
    pos=len(display.get())
    display.insert(pos,"%")
    
def bconvo():
    global switch
    if switch==None:
        switch=True
        bconv["text"]="deg"
    else:
        switch=None
        bconv["text"]="rad"
        
    
def bln():
    try:
        ans = float(display.get())
        ans = math.log(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")
        
def beq():
    try:
        ans =(display.get())
        ans = eval(ans)
        disp.delete(0, END)
        disp.insert(0, ans)
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")
    
def bround():
    try:
        ans = float(display.get())
        ans = round(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")
    

#ROW 1 BUTTONS
brow1=Frame(root, bg="#000000")
brow1.pack(expand=TRUE,fill=BOTH)

bpi=Button(brow1,text="π",activebackground="black",activeforeground="white",bg="white",fg="#167050",relief=GROOVE,font="Segoe 18",bd=0, command=bpi)
bpi.pack(side=LEFT,expand=TRUE,fill=BOTH)

bfact=Button(brow1,text="x!",activebackground="black",activeforeground="white",bg="white",fg="#167050",relief=GROOVE,font="Segoe 18",bd=0,command=bfacto)
bfact.pack(side=LEFT,expand=TRUE,fill=BOTH)


bsin=Button(brow1,text="Sin",activebackground="black",activeforeground="white",bg="white",fg="#167050",relief=GROOVE,font="Segoe 18",bd=0,command=bsin)
bsin.pack(side=LEFT,expand=TRUE,fill=BOTH)


bcos=Button(brow1,text="Cos",activebackground="black",activeforeground="white",bg="white",fg="#167050",relief=GROOVE,font="Segoe 18",bd=0,command=bcos)
bcos.pack(side=LEFT,expand=TRUE,fill=BOTH)


btan=Button(brow1,text="Tan",activebackground="black",activeforeground="white",bg="white",fg="#167050",relief=GROOVE,font="Segoe 18",bd=0,command=btan)
btan.pack(side=LEFT,expand=TRUE,fill=BOTH)


b1=Button(brow1,text="1",activebackground="black",activeforeground="white",bg="white",fg="#167050",relief=GROOVE,font="Segoe 23",bd=0,command=b1)
b1.pack(side=LEFT,expand=TRUE,fill=BOTH)


b2=Button(brow1,text="2",activebackground="black",activeforeground="white",bg="white",fg="#167050",relief=GROOVE,font="Segoe 23",bd=0,command=b2)
b2.pack(side=LEFT,expand=TRUE,fill=BOTH)


b3=Button(brow1,text="3",activebackground="black",activeforeground="white",bg="white",fg="#167050",relief=GROOVE,font=("Segoe 23"),bd=0,command=b3)
b3.pack(side=LEFT,expand=TRUE,fill=BOTH)


bplus=Button(brow1,text="+",activebackground="black",activeforeground="white",bg="white",fg="#167050",relief=GROOVE,font="Segoe 23",bd=0,command=bplus)
bplus.pack(side=LEFT,expand=TRUE,fill=BOTH)

#ROW 2 BUTTONS
brow2=Frame(root)
brow2.pack(expand=TRUE,fill=BOTH)

be=Button(brow2,text="e",activebackground="black",activeforeground="white",bg="white",fg="#167050",relief=GROOVE,font="Segoe 18",bd=0)
be.pack(side=LEFT,expand=TRUE,fill=BOTH)

broot=Button(brow2,text="√x",activebackground="black",activeforeground="white",bg="white",fg="#167050",relief=GROOVE,font="Segoe 18",bd=0,command= sqroot)
bfact.pack(side=LEFT,expand=TRUE,fill=BOTH)


bsinin=Button(brow2,text="Sin-1",activebackground="black",activeforeground="white",bg="white",fg="#167050",relief=GROOVE,font="Segoe 11",bd=0,command=barcsin)
bsinin.pack(side=LEFT,expand=TRUE,fill=BOTH)


bcosin=Button(brow2,text="Cos-1",activebackground="black",activeforeground="white",bg="white",fg="#167050",relief=GROOVE,font="Segoe 11",bd=0,command=barcsin)
bcosin.pack(side=LEFT,expand=TRUE,fill=BOTH)


btanin=Button(brow2,text="Tan-1",activebackground="black",activeforeground="white",bg="white",fg="#167050",relief=GROOVE,font="Segoe 11",bd=0,command=barctan)
btanin.pack(side=LEFT,expand=TRUE,fill=BOTH)


b4=Button(brow2,text="4",activebackground="black",activeforeground="white",bg="white",fg="#167050",relief=GROOVE,font="Segoe 23",bd=0,command=b4)
b4.pack(side=LEFT,expand=TRUE,fill=BOTH)


b5=Button(brow2,text="5",activebackground="black",activeforeground="white",bg="white",fg="#167050",relief=GROOVE,font="Segoe 23",bd=0,command=b5)
b5.pack(side=LEFT,expand=TRUE,fill=BOTH)


b6=Button(brow2,text="6",activebackground="black",activeforeground="white",bg="white",fg="#167050",relief=GROOVE,font="Segoe 23",bd=0,command=b6)
b6.pack(side=LEFT,expand=TRUE,fill=BOTH)


bminus=Button(brow2,text="-",activebackground="black",activeforeground="white",bg="white",fg="#167050",relief=GROOVE,font="Segoe 23",bd=0,command=bminus)
bminus.pack(side=LEFT,expand=TRUE,fill=BOTH)

#ROW3 BUTTON
btnrow3 = Frame(root)
btnrow3.pack(expand=TRUE, fill=BOTH)

bconv = Button(btnrow3, text="Rad", font="Segoe 12 bold", relief=GROOVE, bd=0,  activebackground="black",activeforeground="white",bg="white",fg="#167050",command=bconvo)
bconv.pack(side=LEFT, expand=TRUE, fill=BOTH)

bround = Button(btnrow3, text="round", font="Segoe 10 bold", relief=GROOVE, bd=0,activebackground="black",activeforeground="white",bg="white",fg="#167050",command=bround)
bround.pack(side=LEFT, expand=TRUE, fill=BOTH)

bln = Button(btnrow3, text="ln", font="Segoe 18", relief=GROOVE, bd=0, activebackground="black",activeforeground="white",bg="white",fg="#167050",command=bln)
bln.pack(side=LEFT, expand=TRUE, fill=BOTH)

blog = Button(btnrow3, text="log", font="Segoe 17", relief=GROOVE, bd=0, activebackground="black",activeforeground="white",bg="white",fg="#167050",command=blog)
blog.pack(side=LEFT, expand=TRUE, fill=BOTH)

bpow = Button(btnrow3, text="x^y", font="Segoe 17", relief=GROOVE, bd=0, activebackground="black",activeforeground="white",bg="white",fg="#167050",command=bpow)
bpow.pack(side=LEFT, expand=TRUE, fill=BOTH)

b7 = Button(btnrow3, text="7", font="Segoe 23", relief=GROOVE, bd=0, activebackground="black",activeforeground="white",bg="white",fg="#167050",command=b7)
b7.pack(side=LEFT, expand=TRUE, fill=BOTH)

b8 = Button(btnrow3, text="8", font="Segoe 23", relief=GROOVE, bd=0,activebackground="black",activeforeground="white",bg="white",fg="#167050",command=b8)
b8.pack(side=LEFT, expand=TRUE, fill=BOTH)

b9 = Button(btnrow3, text="9", font="Segoe 23", relief=GROOVE, bd=0, activebackground="black",activeforeground="white",bg="white",fg="#167050",command=b9)
b9.pack(side=LEFT, expand=TRUE, fill=BOTH)

bmul = Button(btnrow3, text="*", font="Segoe 23", relief=GROOVE, bd=0, activebackground="black",activeforeground="white",bg="white",fg="#167050",command=bmul)
bmul.pack(side=LEFT, expand=TRUE, fill=BOTH)

#ROW 4 BUTTON

btnrow4 = Frame(root)
btnrow4.pack(expand=TRUE, fill=BOTH)

bmod = Button(btnrow4, text="%", font="Segoe 21", relief=GROOVE, bd=0, activebackground="black",activeforeground="white",bg="white",fg="#167050",command=bmod)
bmod.pack(side=LEFT, expand=TRUE, fill=BOTH)

bbod1 = Button(btnrow4, text=" ( ", font="Segoe 21", relief=GROOVE, bd=0, activebackground="black",activeforeground="white",bg="white",fg="#167050",command=bbrac1)
bbod1.pack(side=LEFT, expand=TRUE, fill=BOTH)

bbod2 = Button(btnrow4, text=" ) ", font="Segoe 21", relief=GROOVE, bd=0, activebackground="black",activeforeground="white",bg="white",fg="#167050",command=bbrac2)
bbod2.pack(side=LEFT, expand=TRUE, fill=BOTH)

bdot= Button(btnrow4, text=" • ", font="Segoe 21", relief=GROOVE, bd=0, activebackground="black",activeforeground="white",bg="white",fg="#167050",command=bdot)
bdot.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnc = Button(btnrow4, text="C", font="Segoe 23", relief=GROOVE, bd=0, activebackground="black",activeforeground="white",bg="white",fg="#167050",command=bC)
btnc.pack(side=LEFT, expand=TRUE, fill=BOTH)

bdel = Button(btnrow4, text="⌫", font="Segoe 20", relief=GROOVE, bd=0, activebackground="black",activeforeground="white",bg="white",fg="#167050",command=bdelete)
bdel.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn0 = Button(btnrow4, text="0", font="Segoe 23", relief=GROOVE, bd=0, activebackground="black",activeforeground="white",bg="white",fg="#167050",command=b0)
btn0.pack(side=LEFT, expand=TRUE, fill=BOTH)

btneq = Button(btnrow4, text="=", font="Segoe 23", relief=GROOVE, bd=0, activebackground="black",activeforeground="white",bg="white",fg="#167050",command=beq)
btneq.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnd = Button(btnrow4, text="/", font="Segoe 23", relief=GROOVE, bd=0, activebackground="black",activeforeground="white",bg="white",fg="#167050",command=bdiv)
btnd.pack(side=LEFT, expand=TRUE, fill=BOTH)
#for inputing the formulae

#for the equationss
def ro():
    ro=Tk()
    ro.title("FORMULAE")
    ro.geometry("450x400+300+300")
    scrollbar = Scrollbar(ro)
    scrollbar.pack( side = RIGHT, fill = "both" )

    configfile = Text(ro, wrap=WORD, width=45, height= 20,bg="#83ccb2",fg='black')
    with open("Formulae.txt", 'r') as f:
        configfile.insert(INSERT, f.read())
        configfile.pack(expand=TRUE,fill=X)
    
    butformulae = Button(ro,text=' WANT TO ADD SOME FORMULAE? ', command=sfor,fg="white",bg="#5fa18a")
    butformulae.place(x=4, y=0)
    f.close()
    ro.mainloop()

#saved calcs
def so():
    so=Tk()
    so.title("SAVED CALCULATIONS")
    so.geometry("450x400+300+300")
    
    w = Label(so, text='Saved Calculations',font="vivaldi") 
    w.pack()
    
    scrollbar = Scrollbar(so)
    scrollbar.pack( side = RIGHT, fill = "both" )
    
    configfile = Text(so, wrap=WORD, width=45, height= 20,bg="#83ccb2",fg='black')
    with open("save.txt", 'r') as f:
        configfile.insert(INSERT, f.read())
        configfile.pack(expand=TRUE,fill=X)
    
    f.close()
    so.mainloop()
    

#menuu
menubar = Menu(root)
def iExit():
    iExit = tkinter.messagebox.askyesno('Number Cruncher', 'Confirm if you want to exit')
    if iExit > 0:
        root.destroy()
        return

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
#filemenu.add_separator()
filemenu.add_command(label="Exit",command=iExit)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label="Formulae",command=ro)
editmenu.add_command(label="Saved Calculation",command=so)
#editmenu.add_separator()

    
root.config(menu=menubar)
root.mainloop()
