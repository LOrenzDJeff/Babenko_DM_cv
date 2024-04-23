from math import *
from tkinter import *

def about():
     win = Toplevel(root)
     lab = Label(win,text="Калькулятор созданный с помощью python.\nСпасибо что пользуетесь.\n©Danny")
     lab.pack()
def pomosh():
     win = Toplevel(root)
     lab = Label(win,text="Обычный калькулятор, жми на кнопки или можешь вписывать самостояльно.\nЖелаю успехов!")
     lab.pack()
def one(event):
    ent.insert(END,'1')
def two(event):
    ent.insert(END,'2')
def three(event):
    ent.insert(END,'3')
def four(event):
    ent.insert(END,'4')
def five(event):
    ent.insert(END,'5')
def six(event):
    ent.insert(END,'6')
def seven(event):
    ent.insert(END,'7')
def eight(event):
    ent.insert(END,'8')
def nine(event):
    ent.insert(END,'9')
def zero(event):
    ent.insert(END,'0')
def tochka(event):
    ent.insert(END,'.')
def plus(event):
    ent.insert(END,'+')
def koren(event):
    ent.insert(END,'√')
def procent(event):
    ent.insert(END,'%')
def step(event):
    ent.insert(END,'^')
def minus(event):
    ent.insert(END,'-')
def ymn(event):
    ent.insert(END,'*')
def c(event):
    ent.delete(0, END)
def delen(event):
    ent.insert(END,'/')
def rovno(event):
    z=[]
    g=[]
    a = str(ent.get())
    y = 0
    x = 0
    while 1==1:
        if y==len(a):
            if a[x:y] != '':
                g.append(a[x:y])
                z.append(a[x:y])
            break
        elif a[y] == '(':
            if a[x:y] != '':
                g.append(a[x:y])
                z.append(a[x:y])   
            g.append('(')
            z.append('(')
            y = y + 1
            x = y
        elif a[y] == '√':
            if a[x:y] != '':
                g.append(a[x:y])
                z.append(a[x:y])
            g.append('√')
            z.append('√')
            y = y + 1
            x = y
        elif a[y] == ')':
            if a[x:y] != '':
                g.append(a[x:y])
                z.append(a[x:y])
            g.append(')')
            z.append(')')
            y = y + 1
            x = y
        elif a[y] == '%':
            if a[x:y] != '':
                g.append(a[x:y])
                z.append(a[x:y])
            g.append('%')
            z.append('%')
            y = y + 1
            x = y
        elif a[y] == '+':
            if a[x:y] != '':
                g.append(a[x:y])
                z.append(a[x:y])
            g.append('+')
            z.append('+')
            y = y + 1
            x = y
        elif a[y] == '^':
            if a[x:y] != '':
                g.append(a[x:y])
                z.append(a[x:y])
            g.append('^')
            z.append('^')
            y = y + 1
            x = y
        elif a[y] == '-':
            if a[x:y] != '':
                g.append(a[x:y])
                z.append(a[x:y])
            g.append('-')
            z.append('-')
            y = y + 1
            x = y
        elif a[y] == '/':
            if a[x:y] != '':
                g.append(a[x:y])
                z.append(a[x:y])
            g.append('/')
            z.append('/')
            y = y + 1
            x = y
        elif a[y] == '*':
            if a[x:y] != '':
                g.append(a[x:y])
                z.append(a[x:y])
            g.append('*')
            z.append('*')
            y = y + 1
            x = y
        else:
            y = y + 1
    while 1==1:
        y=0
        x=0
        f = 0
        while 1==1:
            if '(' in g:
                while 1 == 1:
                    if g[y] == '(':
                        f = f+1
                        for i in range(y+1):
                            del g[x]
                        x = 1    
                        while 1 == 1:
                            if g[-x] == ')':
                                del g[-x]
                                x = 0
                                y = 0
                                break
                            else:
                                y=y+1
                                del g[-x]
                        break
                    else:
                        y = y+1
            elif '^' in g:
                while 1==1:
                    if g[y] == '*' or g[y] == '-' or g[y] == '+' or g[y] == '/':
                        y=y+1
                        x=y
                    elif g[y] == '^':
                        p = int(g[y-1]) ** int(g[y+1])
                        g[y] = p
                        del g[y+1]
                        del g[y-1]
                        y=0
                        x=0
                        break
                    else:
                        y=y+1
            elif '√' in g:
                while 1==1:
                    if g[y] == '*' or g[y] == '-' or g[y] == '+' or g[y] == '/':
                        y=y+1
                        x=y
                    elif g[y] == '√':
                        p = g[y+1]
                        if p=='-':
                            g = []
                            g.append('Отрицательное число не может быть под корнем')
                            break
                        else:
                            p = sqrt(int(p))
                            g[y] = p
                            del g[y+1]
                            y=0
                            x=0
                            break
                    else:
                        y=y+1
            else:
                break
        if 'Отрицательное число не может быть под корнем' in g:
            break
        b = len(g)
        i = 1
        while i!=b:
            if g[0] == '-':
                if g[2] == '+':
                    if '%' in g:
                        if g[4] == '%':
                            g[3]=-float(g[1])/100*float(g[3])
                            g.remove(g[4])
                            i=i+1
                    y = -float(g[1]) + float(g[3])
                    g[0] = y
                    g.remove(g[1])
                    g.remove(g[1])
                    g.remove(g[1])
                    i = i+3
                elif g[2] == '*':
                    if '%' in g:
                        if g[4] == '%':
                            g[3]=-float(g[1])/100*float(g[3])
                            g.remove(g[4])
                            i=i+1
                    y = -float(g[1]) * float(g[3])
                    g[0] = y
                    g.remove(g[1])
                    g.remove(g[1])
                    g.remove(g[1])
                    i = i+3
                elif g[2] == '/':
                    if '%' in g:
                        if g[4] == '%':
                            g[3]=-float(g[1])/100*float(g[3])
                            g.remove(g[4])
                            i=i+1
                    if g[3] == '0':
                        g = []
                        g.append('На ноль не делится')
                        break
                    y = -float(g[1])/float(g[3])
                    g[0] = y
                    g.remove(g[1])
                    g.remove(g[1])
                    g.remove(g[1])
                    i = i+3
                elif g[2] == '-':
                    if '%' in g:
                        if g[3] == '%':
                            -float(g[1])/100*float(g[3])
                            g.remove(g[4])
                            i=i+1
                    y = -float(g[1])-float(g[3])
                    g[0] = y
                    g.remove(g[1])
                    g.remove(g[1])
                    g.remove(g[1])
                    i = i+3
            else:
                if g[1] == '+':
                    if '%' in g:
                        if g[3] == '%':
                            g[2]=float(g[0])/100*float(g[2])
                            g.remove(g[3])
                            i=i+1
                    y = float(g[0]) + float(g[2])
                    g[0] = y
                    g.remove(g[1])
                    g.remove(g[1])
                    i = i+2
                elif g[1] == '*':
                    if '%' in g:
                        if g[3] == '%':
                            g[2]=float(g[0])/100*float(g[2])
                            g.remove(g[3])
                            i=i+1
                    y = float(g[0]) * float(g[2])
                    g[0] = y
                    g.remove(g[1])
                    g.remove(g[1])
                    i = i+2
                elif g[1] == '/':
                    if '%' in g:
                        if g[3] == '%':
                            g[2]=float(g[0])/100*float(g[2])
                            g.remove(g[3])
                            i=i+1
                    if g[2] == '0':
                        g = []
                        g.append('На ноль не делится')
                        break
                    y = float(g[0]) / float(g[2])
                    g[0] = y
                    g.remove(g[1])
                    g.remove(g[1])
                    i = i+2
                elif g[1] == '-':
                    if '%' in g:
                        if g[3] == '%':
                            g[2]=float(g[0])/100*float(g[2])
                            g.remove(g[3])
                            i=i+1
                    y = float(g[0]) - float(g[2])
                    g[0] = y
                    g.remove(g[1])
                    g.remove(g[1])
                    i = i+2
        if 'На ноль не делится' in g:
            break
        c = 0
        y = 0
        if '(' in z:
            while 1==1:
                if z[y-1]==g[0]:
                    break
                elif z[y]=='(':
                    c = c+1
                    y=y+1
                    if c == f:
                        z[y-1]=g[0]
                        c=0
                        while 1==1:
                            if z[y]!=')':
                                del z[y]
                            else:
                                del z[y]
                                break
                else:
                    y=y+1
        else:
            z[y]=g[0]
            x=1
            l=len(z)
            while x!=l:
                del z[y+1]
                x=x+1
            break
        g.clear()
        while len(z) != x:
            g.append(z[x])
            x=x+1
    if 'На ноль не делится' in g or 'Отрицательное число не может быть под корнем' in g:
        ent.delete(0, END)
        ent.insert(END,g[0])
    else:
        ent.delete(0, END)
        if int(z[0]) == float(z[0]):
            x = int(z[0])
            ent.insert(END,x)
        else:
            ent.insert(END,z[0])
def delete(event):
    x = str(ent.get())
    ent.delete(0, END)
    ent.insert(END,x[:-1])
def left(event):
    ent.insert(END,'(')
def right(event):
    ent.insert(END,')')
root = Tk()
root.minsize(240,240)
root.maxsize(240,240)
ent = Entry (root)
m = Menu(root)
root.config(menu=m)
fm = Menu(m)
m.add_cascade(label="Помощь",menu=fm)
butcoren = Button(root, text='√')
but1 = Button(root, text='1')
but2 = Button(root, text='2')
but3 = Button(root, text='3')
but4 = Button(root, text='4')
but5 = Button(root, text='5')
but6 = Button(root, text='6')
but7 = Button(root, text='7')
but8 = Button(root, text='8')
but9 = Button(root, text='9')
but0 = Button(root, text='0')
butdel = Button(root, text='/')
butc = Button(root, text='C')
buty = Button(root, text='*')
butt = Button(root, text='.')
butdelete = Button(root, text='Del')
butm=Button(root, text='-')
butp=Button(root, text='+')
butr=Button(root, text='=')
butLEFT=Button(root, text='(')
butRIGHT=Button(root, text=')')
butstep=Button(root, text='^')
butprocent=Button(root,text='%')
butcoren.place(x=160,y=160,height=40,width=40)
butstep.place(x=160,y=200,height=40,width=40)
butprocent.place(x=200,y=160,height=80,width=40)
ent.place(x=0,y=0,height=40,width=240)
but1.place(x=0,y=160,height=40,width=40)
but2.place(x=40,y=160,height=40,width=40)
but3.place(x=80,y=160,height=40,width=40)
but4.place(x=0,y=120,height=40,width=40)
but5.place(x=40,y=120,height=40,width=40)
but6.place(x=80,y=120,height=40,width=40)
but7.place(x=0,y=80,height=40,width=40)
but8.place(x=40,y=80,height=40,width=40)
but9.place(x=80,y=80,height=40,width=40)
but0.place(x=0,y=200,height=40,width=80)
butc.place(x=0,y=40,height=40,width=40)
butdel.place(x=40,y=40,height=40,width=40)
buty.place(x=80,y=40,height=40,width=40)
butt.place(x=80,y=200,height=40,width=40)
butdelete.place(x=120,y=40,height=40,width=40)
butm.place(x=120,y=80,height=40,width=40)
butp.place(x=120,y=120,height=40,width=40)
butr.place(x=120,y=160,height=80,width=40)
butLEFT.place(x=160,y=40,height=120,width=40)
butRIGHT.place(x=200,y=40,height=120,width=40)
butLEFT.bind('<Button-1>',left)
butcoren.bind('<Button-1>',koren)
butstep.bind('<Button-1>',step)
butRIGHT.bind('<Button-1>',right)
butprocent.bind('<Button-1>',procent)
but1.bind('<Button-1>',one)
but2.bind('<Button-1>',two)
but3.bind('<Button-1>',three)
but4.bind('<Button-1>',four)
but5.bind('<Button-1>',five)
but6.bind('<Button-1>',six)
but7.bind('<Button-1>',seven)
but8.bind('<Button-1>',eight)
but9.bind('<Button-1>',nine)
but0.bind('<Button-1>',zero)
butt.bind('<Button-1>',tochka)
butp.bind('<Button-1>',plus)
butm.bind('<Button-1>',minus)
buty.bind('<Button-1>',ymn)
butc.bind('<Button-1>',c)
fm.add_command(label="О программе",command=about)
fm.add_command(label="Помощь",command=pomosh)
butdel.bind('<Button-1>',delen)
butr.bind('<Button-1>',rovno)
butdelete.bind('<Button-1>',delete)
ent.bind('<Return>',rovno)
root.mainloop()