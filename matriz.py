from tkinter import *
from random import*
from numpy import *
import time
from math import*
root = Tk()
root.title ("Matrizes - Adão")
root.resizable(width=False, height=False)
def callback():
    print ("called the callback!")
def relogio():
    import time
    gmt = time.gmtime(time.time())
    fmt = '%a, %d %b %Y %H:%M:%S GMT'
    str = time.strftime(fmt, gmt)
    hdr = 'Date: ' + str
    print (hdr)
def tick():
    global curtime
    newtime = time.strftime('%H:%M:%S')
    if newtime != curtime:
        curtime = newtime
        clock.config(text=curtime)
    clock.after(200, tick)
def especial():
    y=b.get() 
    import funcao_especial
    res=funcao_especial.funcao(float(y))
    print(valor.set(res))
  
def matriz_identidade():
    global linha, coluna
    x=int(valor1.get())
    z=int(valor2.get())
    radio=(int(v.get()))
    y = eye(x,z)
    if(radio==2):
        a.set(y)
    if(radio==1):
        b.set(y)
def matriz_uns():
    global linha, coluna
    x=int(valor1.get())
    z=int(valor2.get())
    radio=(int(v.get()))
    y = ones((x,z))
    if(radio==2):
        a.set(y)
    if(radio==1):
        b.set(y)

def matriz_zero():
    global linha, coluna
    x=int(valor1.get())
    z=int(valor2.get())
    radio=(int(v.get()))
    y = zeros((x,z))
    if(radio==2):
        a.set(y)
    if(radio==1):
        b.set(y)

def desenha():
    global valor1, valor2,a,b 
    b = StringVar()
    a = StringVar()
    valor1 = StringVar()
    valor2 = StringVar()
    """
    b=Entry(root,textvariable=valor,font="Arial 10", width=10, bg="white", fg="red")
    b.pack(padx=10,anchor=N)
    label2.pack( anchor=NW,padx=2,  pady=3)
    label1.pack( anchor=NW,padx=2,  pady=3)
    """
    final=0
    iframe1 = Frame(root, relief=SUNKEN)
    fm = Frame(root)
    fm2 = Frame(root)
    resultado =Label(fm, text="Resultado:",width=12, bg="blue").pack(side=LEFT,padx=2,  pady=3)
    Label(fm, text="Linha",width=12, bg="blue").pack(side=LEFT,padx=2,  pady=3)
    Label(fm, text="Coluna",width=12, bg="blue").pack(side=LEFT,padx=2,  pady=3)
    fm.pack(fill=BOTH, expand=YES)
    fm.config(cursor='gumby')
    global linha, coluna
    fm1 = Frame(root)
    label1 =Label(fm1, text=final, width=12, height=4, bg="green").pack(side=LEFT,padx=2,  pady=3)
    linha=Entry(fm1,textvariable=valor1,font="Arial 10", width=12, bg="white", fg="red").pack(side=LEFT,anchor=N,padx=2,  pady=3)
    coluna=Entry(fm1,textvariable=valor2,font="Arial 10", width=13, bg="white", fg="red").pack(side=LEFT,anchor=N,padx=2,  pady=3)
    fm1.pack(fill=BOTH, expand=YES)

    global v
    Label(fm2, text="Matriz A:",width=12, bg="red").pack(side=LEFT,padx=2,  pady=3)
    v = IntVar()
    Radiobutton(fm2, variable=v, value=1).pack(side=LEFT,padx=2,  pady=3)
    matriza=Entry(fm2,textvariable=b,font="Arial 10", width=30, bg="white", fg="red").pack(side=LEFT,anchor=N,padx=2,  pady=4)
    fm2.pack(fill=BOTH, expand=YES)

    fm2 = Frame(root)
    Label(fm2, text="Matriz B:",width=12, bg="red").pack(side=LEFT,padx=2,  pady=3)
    Radiobutton(fm2, variable=v, value=2).pack(side=LEFT,padx=2,  pady=3)
    matrizb=Entry(fm2,textvariable=a,font="Arial 10", width=30, bg="white", fg="red").pack(side=LEFT,anchor=N,padx=2,  pady=4)
    fm2.pack(fill=BOTH, expand=YES)

    fm2 = Frame(root)
    Label(fm2, text="Inserir:",width=12, bg="red").pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='Matriz Zeros',command=matriz_zero).pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='Matriz Identidade',command=matriz_identidade).pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='Matriz Uns',command=matriz_uns).pack(side=LEFT,padx=2,  pady=3)

    fm2.pack(fill=BOTH, expand=YES)
def apagar():
    b.delete(0, END )
def apagarum():
    b.delete(0)
def calcular():
    result = eval(b.get())
    print (b.get(), "=>", result, type(result))
    print(valor.set(result))
def seno():
    import math
    graus = float(b.get())
    angulo = graus * 2 * math.pi / 360.0
    print(valor.set(math.sin(angulo)))
def coseno():
    import math
    print(valor.set('%g' % math.cos(float(b.get()))))
def tangente():
    import math
    print(valor.set('%g' % math.tan(float(b.get()))))
def logaritimo():#certo
    import math
    print(valor.set(math.log10(float(b.get()))))
def exponencial():#certo
    import math
    print(valor.set('%g' % math.exp(float(b.get()))))
def pi():
    import math
    print(valor.set('%g' % math.pi(float(b.get()))))
def factorial():
    import math
    n=float(b.get())
    if n == 0 :
        print(valor.set(1))
    else:
        while(i<=n):
            fact*=i
            i+=1
        return fact
        print(valor.set(fact))
e = Entry(root, width=60, state="readonly")
e.insert(0,"...")
def menu():     
    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label="Ver", menu=filemenu)
    filemenu.add_command(label="Equações", command=callback)
    filemenu.add_command(label="Matrizes", command=callback)
    filemenu.add_command(label="Conversor", command=callback)
    filemenu.add_separator()
    filemenu.add_command(label="Sair", command=callback)
    menu.add_cascade(label="Hora")
    helpmenu = Menu(menu)
    menu.add_cascade(label="Ajuda", menu=helpmenu)
menu()
desenha()
root.mainloop()
mainloop()
