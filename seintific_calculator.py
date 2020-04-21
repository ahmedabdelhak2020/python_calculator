from tkinter import*
import tkinter
import math
import parser
import tkinter.messagebox

root = Tk()
root.title("seintific_calculator")
root.configure(bg="powder blue")
root.resizable(width=False, height=False)
root.geometry("475x485+0+0")

calc = Frame(root)
calc.grid()

txtDisplay = Entry(calc, font=('arial',20,'bold'), bg="powder blue", bd=30, width=29, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0,"0")

numberpad = "789456123"
i = 0
btn = []
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2, font=('arial',20,'bold'), bd=4, text=numberpad[i]))
        btn[i].grid(row=j, column=k, pady=1)
        i +=1
#========================================button============================
btnclear = Button(calc, text=chr(67), width=6,height=2, font=('arial',20,'bold'),
                     bd=4, bg="powder blue").grid(row=1, column=0, pady=1)

btnallclear1 = Button(calc, text=chr(67)+chr(69), width=6,height=2, font=('arial',20,'bold'),
                     bd=4, bg="powder blue").grid(row=1, column=1, pady=1)
btnsq = Button(calc, text="sqrt", width=6,height=2, font=('arial',20,'bold'),
                     bd=4, bg="powder blue").grid(row=1, column=2, pady=1)

btnadd = Button(calc, text="+", width=6,height=2, font=('arial',20,'bold'),
                     bd=4, bg="powder blue").grid(row=1, column=3, pady=1)

btnsub = Button(calc, text="-", width=6,height=2, font=('arial',20,'bold'),
                     bd=4, bg="powder blue").grid(row=2, column=3, pady=1)

btnmul = Button(calc, text="*", width=6,height=2, font=('arial',20,'bold'),
                     bd=4, bg="powder blue").grid(row=3, column=3, pady=1)

btndiv = Button(calc, text=chr(247), width=6,height=2, font=('arial',20,'bold'),
                     bd=4, bg="powder blue").grid(row=4, column=3, pady=1)

btnzero = Button(calc, text="0", width=6,height=2, font=('arial',20,'bold'),
                     bd=4, bg="powder blue").grid(row=5, column=0, pady=1)

btndot = Button(calc, text=".", width=6,height=2, font=('arial',20,'bold'),
                     bd=4, bg="powder blue").grid(row=5, column=1, pady=1)

btnPM = Button(calc, text=chr(177), width=6,height=2, font=('arial',20,'bold'),
                     bd=4, bg="powder blue").grid(row=5, column=2, pady=1)

btnEqual = Button(calc, text="=", width=6,height=2, font=('arial',20,'bold'),
                     bd=4, bg="powder blue").grid(row=5, column=3, pady=1)
#=======================================seintific calculator===========================================================
btnPi = Button(calc, text="pi", width=6,height=2, font=('arial',20,'bold'),
                     bd=4, bg="powder blue").grid(row=1, column=4, pady=1)

btnCos = Button(calc, text="cos", width=6,height=2, font=('arial',20,'bold'),
                     bd=4, bg="powder blue").grid(row=1, column=5, pady=1)

btnTan= Button(calc, text="tan", width=6,height=2, font=('arial',20,'bold'),
                     bd=4, bg="powder blue").grid(row=1, column=6, pady=1)

btnSin= Button(calc, text="sin", width=6,height=2, font=('arial',20,'bold'),
                     bd=4, bg="powder blue").grid(row=1, column=7, pady=1)
#=========================================================================================================================
btn2Pi = Button(calc, text="2pi", width=6,height=2, font=('arial',20,'bold'),
                     bd=4, bg="powder blue").grid(row=2, column=4, pady=1)

btnCosh = Button(calc, text="cosh", width=6,height=2, font=('arial',20,'bold'),
                     bd=4, bg="powder blue").grid(row=2, column=5, pady=1)

btnTanh = Button(calc, text="tanh", width=6,height=2, font=('arial',20,'bold'),
                     bd=4, bg="powder blue").grid(row=2, column=6, pady=1)

btnSinh = Button(calc, text="sinh", width=6,height=2, font=('arial',20,'bold'),
                     bd=4, bg="powder blue").grid(row=2, column=7, pady=1)
#==========================================================================================================================
btnLog = Button(calc, text="log", width=6,height=2, font=('arial',20,'bold'),
                     bd=4, bg="powder blue").grid(row=3, column=4, pady=1)

btnExp = Button(calc, text="exp", width=6,height=2, font=('arial',20,'bold'),
                     bd=4, bg="powder blue").grid(row=3, column=5, pady=1)

btnMod = Button(calc, text="mod", width=6,height=2, font=('arial',20,'bold'),
                     bd=4, bg="powder blue").grid(row=3, column=6, pady=1)

btnE = Button(calc, text="e", width=6,height=2, font=('arial',20,'bold'),
                     bd=4, bg="powder blue").grid(row=3, column=7, pady=1)
#======================================================================================================================
btnLog2 = Button(calc, text="log2", width=6,height=2, font=('arial',20,'bold'),
                     bd=4, bg="powder blue").grid(row=4, column=4, pady=1)

btnDeg = Button(calc, text="deg", width=6,height=2, font=('arial',20,'bold'),
                     bd=4, bg="powder blue").grid(row=4, column=5, pady=1)

btnAcosh = Button(calc, text="acosh", width=6,height=2, font=('arial',20,'bold'),
                     bd=4, bg="powder blue").grid(row=4, column=6, pady=1)

btnAsinh = Button(calc, text="asinh", width=6,height=2, font=('arial',20,'bold'),
                     bd=4, bg="powder blue").grid(row=4, column=7, pady=1)
#======================================================================================================================
btnLog10 = Button(calc, text="log10", width=6,height=2, font=('arial',20,'bold'),
                     bd=4, bg="powder blue").grid(row=5, column=4, pady=1)

btnNcos = Button(calc, text="loglp", width=6,height=2, font=('arial',20,'bold'),
                     bd=4, bg="powder blue").grid(row=5, column=5, pady=1)

btnExpml = Button(calc, text="expml", width=6,height=2, font=('arial',20,'bold'),
                     bd=4, bg="powder blue").grid(row=5, column=6, pady=1)

btnLgamma = Button(calc, text="lgamma", width=6,height=2, font=('arial',20,'bold'),
                     bd=4, bg="powder blue").grid(row=5, column=7, pady=1)
#===================================Menu and Function==================================================================

def iExit():
    iExit = tkinter.messagebox.askyesno("seintific calculator","contirm if you want to exit")
    if iExit>0:
        root.destroy()
        return

def Scientific():
    root.resizable(width=False, height=False)
    root.geometry("945x485+0+0")

def Standard():
    root.resizable(width=False, height=False)
    root.geometry("475x485+0+0")

menubar = Menu(calc)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="file", menu=filemenu)
filemenu.add_command(label="Standard", command=Standard)
filemenu.add_command(label="Scientific", command=Scientific)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=iExit)


editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_separator()
editmenu.add_command(label="Past")

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="View Help")

root.config(menu=menubar)
root.mainloop()










            












































