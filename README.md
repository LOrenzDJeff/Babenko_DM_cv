# Babenko_DM_cv
## Бабенко Денис Максимович
Добрый человек на свете
## Образрвание
- Среднее общее образование
- Неоконченное высшее образование
## Навыки в области программирования
- python
    - Библиотека tkinter
    - Текстовая игра
    - Визуальный калькулятор
    - Шифровальная машина
    - telebot
- C
    - Операции над матрицами и замеры времени выполнения
## Выполненные проекты
### Шифровальная машина:
```python
from tkinter import *
from tkinter import filedialog as fd

def shifr(event):
    #Азбука Морзе
    yslovie = var.get()
    slovo = ent.get()
    if yslovie == 0:
        root1 = Tk()
        root1.minsize(300,50)
        root1.maxsize(300,50)
        label=Label(root1,text='Ошибка!\nВыберите шифр')
        label.pack()
        root1.mainloop()
    elif len(slovo)==0:
        yslovie=0
        root1 = Tk()
        root1.minsize(300,50)
        root1.maxsize(300,50)
        label=Label(root1,text='Ошибка!\nШифровать нечего')
        label.pack()
        root1.mainloop()
    else:
        for i in range(0,len(slovo)):
            shtoto = int(ord(slovo[i]))
            if shtoto!=32 and shtoto!=1025 and shtoto<1040 or shtoto>1071:
                ent.delete(0,END)
                yslovie=0
                root1 = Tk()
                root1.minsize(300,50)
                root1.maxsize(300,50)
                label=Label(root1,text='Ошибка!\nДанная шифровальная машина работает только с\nзаглавными буквами русского алфавита')
                label.pack()
                root1.mainloop()
                break
    morze={'А':'•−', 'Б': '−•••', 'В': '•−−', 'Г': '−−•', 'Д': '−••', 'Е': '•', 'Ж': '•••−', 'З': '−−••', 'И': '••', 'Й': '•−−−', 'К': '−•−', 'Л': '•−••', 'М': '−−', 'Н': '−•', 'О': '−−−', 'П': '•−−•', 'Р': '•−•', 'С': '•••', 'Т': '−', 'У': '••−', 'Ф': '••−•', 'Х': '••••', 'Ц': '−•−•', 'Ч': '−−−•', 'Ш': '−−−−', 'Щ': '−−•−', 'Ъ': '−−•−−', 'Ы': '−•−−', 'Ь': '−••−', 'Э': '••−••', 'Ю': '••−−', 'Я': '•−•−'}
    first={'А':'Ю', 'Б': 'Ь', 'В': 'Ъ', 'Г': 'Ш', 'Д': 'Ц', 'Е': 'Ф', 'Ж': 'Т', 'З': 'Р', 'И': 'О', 'Й': 'М', 'К': 'К', 'Л': 'И', 'М': 'Ж', 'Н': 'Д', 'О': 'В', 'П': 'А', 'Р': 'Б', 'С': 'Г', 'Т': 'Е', 'У': 'З', 'Ф': 'Й', 'Х': 'Л', 'Ц': 'Н', 'Ч': 'П', 'Ш': 'С', 'Щ': 'У', 'Ъ': 'Х', 'Ы': 'Ч', 'Ь': 'Щ', 'Э': 'Ы', 'Ю': 'Э', 'Я': 'Я'}
    #Алфавит
    bykv=dict()
    b=1
    a='А'
    c=1
    while b!=33:
        c = str(c)
        if c=='7':
            bykv['Ё']=c
            c=int(c)
            c=c+1
            c = str(c)
        bykv[a]=c
        a=ord(a)
        a=a+1
        c=int(c)
        a=chr(a)
        c=c+1
        b=b+1
    slojno1=dict()
    b=1
    a='А'
    d=1
    while b!=33:
        d = str(d)
        slojno1[d]=a
        a=ord(a)
        a=a+1
        d=int(d)
        a=chr(a)
        d=d+1
        b=b+1
    slojno=dict()
    b=1
    a='А'
    c=1
    while b!=33:
        c = str(c)
        slojno[a]=c
        a=ord(a)
        a=a+1
        c=int(c)
        a=chr(a)
        c=c+1
        b=b+1
    #Алфавит без Ё
    note=dict()
    b=1
    a='А'
    c=1
    while b!=32:
        c = str(c)
        if c=='7':
            note['Ё']=c
            c=int(c)
            c=c+1
            c = str(c)
        note[a]=c
        a=ord(a)
        a=a+1
        c=int(c)
        a=chr(a)
        c=c+1
        b=b+1
    #В обратную сторону
    bykv1=dict()
    b=1
    a='А'
    d=1
    while b!=33:
        d = str(d)
        if d=='7':
            bykv1[d]='Ё'
            d=int(d)
            d=d+1
            d = str(d)
        bykv1[d]=a
        a=ord(a)
        a=a+1
        d=int(d)
        a=chr(a)
        d=d+1
        b=b+1
    #Шифр Виженера
    bykvar=dict()
    b=1
    a='А'
    c='а'
    while b!=32:
        bykvar[c]=a
        a=ord(a)
        c=ord(c)
        a=a+1
        c=c+1
        c=chr(c)
        a=chr(a)
        b=b+1
    test =[0]*33
    for i in range(33):
        test[i] = [0] * 33
    a='А'
    b =0
    c=1
    d = 1
    while 1==1:
        if c==33:
            b=b+1
            c=0
        if b == 33:
            break
        if c == 0:
            test[b][c]=test[0][d]
            a = test[0][d]
            d=d+1
            c = c+1
        else:
            test[b][c]=a
            if test[b][c] in bykvar:
                test[b][c] = bykvar[test[b][c]]
            a=ord(a)
            a=a+1
            a=chr(a)
            c=c+1
    if yslovie == 1:
        x=str(ent.get())
        ent.delete(0,END)
        p=0
        while 1==1:
           if p==len(x):
               break
           if x[p]==' ':
               k = str(ent.get())
               ent.delete(0, END)
               ent.insert(END,k[:-1])
               ent.insert(END,' ')
           else:
               ent.insert(END,bykv[x[p]])
               ent.insert(END,'-')
           p=p+1
        x = str(ent.get())
        ent.delete(0, END)
        ent.insert(END,x[:-1])
    if yslovie == 2:
        x=str(ent.get())
        ent.delete(0,END)
        p=0
        b=16
        while 1==1:
            if p==len(x):
                break
            if x[p]==' ':
                ent.insert(END,' ')
                p=p+1
            if bykv[x[p]]=='33':
                ent.insert(END,'А')
                p=p+1
            else:
                b=int(bykv[x[p]])+1
                ent.insert(END,bykv1[str(b)])
                p=p+1
    if yslovie==3:
        x = 0
        if len(ent2.get())!=1:
            ent2.delete(0,END)
            root1 = Tk()
            root1.minsize(300,50)
            root1.maxsize(300,50)
            label=Label(root1,text='Ошибка!\nВ этом шифре нужно ввести\nколичество перестановок от 0 до 9')
            label.pack()
            root1.mainloop()
            x = 1
        if x!=1:
            shtoto=ord(ent2.get())
            if shtoto<48 or shtoto>57:
                ent2.delete(0,END)
                root1 = Tk()
                root1.minsize(300,50)
                root1.maxsize(300,50)
                label=Label(root1,text='Ошибка!\nВ этом шифре нужно ввести\nколичество перестановок от 0 до 9')
                label.pack()
                root1.mainloop()
            else:
                w=1
                r=int(ent2.get())
                while 1==1:
                    if r==0:
                        break
                    x=str(ent.get())
                    ent.delete(0,END)
                    p=0
                    q=0            
                    while 1==1:
                        if p==len(x) or x[p]==' ':
                            d=x[q:p]
                            k=1
                            while 1==1:
                                if k==len(d):
                                    ent.insert(END,d[0])
                                    break
                                ent.insert(END,d[k])
                                k=k+1
                            if p==len(x):
                                break
                            else:
                                ent.insert(END,' ')
                                q=p+1
                        p=1+p
                    if w==r:
                        break
                    w=w+1
    if yslovie==4:
        x=0
        slovo = str(ent.get())
        for i in range(0,len(slovo)):
            shtoto = int(ord(slovo[i]))
            if shtoto==1025:
                ent.delete(0,END)
                root1 = Tk()
                root1.minsize(300,50)
                root1.maxsize(300,50)
                label=Label(root1,text='Ошибка!\nДанный шифр не шифрует букву Ё')
                label.pack()
                root1.mainloop()
                x=1
                break
        if x !=1:
            x=str(ent.get())
            ent.delete(0,END)
            p=0
            while 1==1:
               if p==len(x):
                   break
               if x[p]==' ':
                   k = str(ent.get())
                   ent.delete(0, END)
                   ent.insert(END,k[:-1])
                   ent.insert(END,'   ')
               else:
                   ent.insert(END,morze[x[p]])
                   ent.insert(END,' ')
               p=p+1
            x = str(ent.get())
            ent.delete(0, END)
            ent.insert(END,x[:-1])
    if yslovie==6:
        slovo = str(ent.get())
        for i in range(0,len(slovo)):
            shtoto = int(ord(slovo[i]))
            x = 0
            if shtoto==1025:
                ent.delete(0,END)
                root1 = Tk()
                root1.minsize(300,50)
                root1.maxsize(300,50)
                label=Label(root1,text='Ошибка!\nДанный шифр не шифрует букву Ё')
                label.pack()
                root1.mainloop()
                x=1
                break
        if x != 1:
            x=str(ent.get())
            ent.delete(0,END)
            p=0
            while 1==1:
               if p==len(x):
                   break
               if x[p]==' ':
                   ent.insert(END,' ')
               else:
                   ent.insert(END,first[x[p]])
               p=p+1
    if yslovie==5:
        slovo = str(ent.get())
        key = str(ent1.get())
        plus = 0
        minus = 0
        z=0
        for i in range(0,len(slovo)):
            if plus ==0 and len(key)==0:
                plus = 4 
            elif plus ==0:
                plus = 1 
                for j in range(0,len(key)):
                    shtoto1 = int(ord(key[j]))
                    if shtoto1==1025:
                        plus = 2
                        break
                    if  shtoto1<1040 or shtoto1>1071:
                        plus = 3
                        break
                    if chr(shtoto1)==" ":
                        z=z+1
                    if z==len(key):
                        plus = 4
                        break
            shtoto = int(ord(slovo[i]))
            if shtoto==1025:
                minus = minus +1
                break
        if minus != 0 and plus ==1:
            ent.delete(0,END)
            root1 = Tk()
            root1.minsize(300,50)
            root1.maxsize(300,50)
            label=Label(root1,text='Ошибка!\nДанный шифр не шифрует букву Ё')
            label.pack()
            root1.mainloop()
        elif plus ==2 and minus ==0:
            ent1.delete(0,END)
            root1 = Tk()
            root1.minsize(300,50)
            root1.maxsize(300,50)
            label=Label(root1,text='Ошибка!\nДанный шифр не может иметь в ключе букву Ё')
            label.pack()
            root1.mainloop()
        elif plus ==2 and minus !=0:
            ent.delete(0,END)
            ent1.delete(0,END)
            root1 = Tk()
            root1.minsize(300,50)
            root1.maxsize(300,50)
            label=Label(root1,text='Ошибка!\nДанный шифр не шифрует букву Ё\nДанный шифр не может иметь в ключе букву Ё')
            label.pack()
            root1.mainloop()
        elif plus ==3:
            ent1.delete(0,END)
            root1 = Tk()
            root1.minsize(300,50)
            root1.maxsize(300,50)
            label=Label(root1,text='Ошибка!\nВ ключе используются только\nзаглавные буквы русского алфавита')
            label.pack()
            root1.mainloop()
        elif plus ==4:
            ent1.delete(0,END)
            root1 = Tk()
            root1.minsize(300,50)
            root1.maxsize(300,50)
            label=Label(root1,text='Ошибка!\nВ ключе нету букв')
            label.pack()
            root1.mainloop()
        else:
            key = str(ent1.get())
            slovo = str(ent.get())
            ent.delete(0,END)
            b=1
            c=1
            d=0
            e=0
            while 1==1:
                if e == len(slovo):
                    break
                if d == len(key):
                    d = 0
                if slovo[e]==' ':
                    ent.insert(END,' ')
                    e=e+1
                if key[d]==' ':
                    d=d+1
                while 1==1:
                    if key[d]==test[b][0]:
                        break
                    b=b+1
                while 1==1:
                    if slovo[e]==test[0][c]:
                        break
                    c=c+1
                ent.insert(END,test[b][c])
                b=1
                c=1
                e=e+1
                d=d+1
    if yslovie==7:
        slovo = str(ent.get())
        for i in range(0,len(slovo)):
            shtoto = int(ord(slovo[i]))
            x = 0
            if shtoto==1025:
                ent.delete(0,END)
                root1 = Tk()
                root1.minsize(300,50)
                root1.maxsize(300,50)
                label=Label(root1,text='Ошибка!\nДанный шифр не шифрует букву Ё')
                label.pack()
                root1.mainloop()
                x=1
                break
        if x != 1:
            slovo = str(ent.get())
            ent.delete(0,END)
            e = 0
            a = 0
            while e!=len(slovo):
                if slovo[e] == ' ':
                    ent.insert(END,' ')
                else:
                    if int(slojno[slovo[e]])<17:
                        a = int(slojno[slovo[e]])
                        a = a*2
                        a = str(a)
                        ent.insert(END,slojno1[a])
                    else:
                        ent.insert(END,slojno1[str(int(slojno[slovo[e]])*2-33)])
                e=e+1
    if yslovie==8:
        x=0
        y=0
        z=0
        slovo = str(ent.get())
        for i in range(0,len(slovo)):
            shtoto = int(ord(slovo[i]))
            if shtoto==1025:
                ent.delete(0,END)
                x=1
                break
        if len(ent3.get())==0:
            y=3
        if len(ent4.get())==0:
            z=3
        else:
            shtoto = int(ord(ent3.get()[0]))
            if shtoto==1025:
                ent3.delete(0,END)
                y=1
            elif shtoto!=32 and shtoto<1040 or shtoto>1071 or len(ent3.get())!=1:
                ent3.delete(0,END)
                y=2
            shtoto = int(ord(ent4.get()[0]))
            if shtoto==1025:
                ent4.delete(0,END)
                z=1
            elif shtoto!=32 and shtoto<1040 or shtoto>1071 or len(ent4.get())!=1:
                ent4.delete(0,END)
                z=2
        if x==1 and y==0 or x==1 and z==0:
            root1 = Tk()
            root1.minsize(300,50)
            root1.maxsize(300,50)
            label=Label(root1,text='Ошибка!\nДанный шифр не шифрует букву Ё')
            label.pack()
            root1.mainloop()
        elif x==0 and y==1 or x==0 and z==1:
            root1 = Tk()
            root1.minsize(300,50)
            root1.maxsize(300,50)
            label=Label(root1,text='Ошибка!\nРоторы не могут иметь букву Ё')
            label.pack()
            root1.mainloop()
        elif x==1 and y==1 or x==1 and z==1:
            root1 = Tk()
            root1.minsize(300,50)
            root1.maxsize(300,50)
            label=Label(root1,text='Ошибка!\nДанный шифр не шифрует букву Ё\nРоторы не могут иметь букву Ё')
            label.pack()
            root1.mainloop()
        elif y==2 or z==2:
            root1 = Tk()
            root1.minsize(300,70)
            root1.maxsize(300,70)
            label=Label(root1,text='Ошибка!\nВ роторах используется только одна\nзаглавная буква русского алфавита.\nБез пробелов')
            label.pack()
            root1.mainloop()
        elif y==3 or z==3:
            root1 = Tk()
            root1.minsize(300,70)
            root1.maxsize(300,70)
            label=Label(root1,text='Ошибка!\nЗаполните все роторы')
            label.pack()
            root1.mainloop()
        else:
            slovo = str(ent.get())
            e = 0
            ent.delete(0,END)
            k1 = str(ent3.get())
            k2 = str(ent4.get())
            e1 = 0
            while e!=len(slovo):
                k3 = k1+k2
                if slovo[e] == ' ':
                    ent.insert(END,' ')
                    e = e + 1
                else:
                    k = slovo[e]
                    o=int(slojno[k])
                    o1=int(slojno[k1])
                    o2=int(slojno[k2])
                    if o+o1>32:
                        k=slojno1[str((int(slojno[k1])+int(slojno[k])-32))]
                    else:
                        k=slojno1[str(int(slojno[k1])+int(slojno[k]))]
                    k = first[k]
                    o=int(slojno[k])
                    if o+o2>32:
                        k=slojno1[str((int (slojno[k]) + int(slojno[k2])-32))]
                    else:
                        k=slojno1[str(int(slojno[k2])+int(slojno[k]))]
                    if int(slojno[k])<17:
                        a = int(slojno[k])
                        a = a*2
                        a = str(a)
                        k = slojno1[a]
                    else:
                        a = int(slojno[k])
                        a = a*2-33
                        a = str(a)
                        k = slojno1[a]
                    b=1
                    c=1
                    while 1==1:
                        if k3[e1]==test[b][0]:
                            break
                        b=b+1
                    while 1==1:
                        if k==test[0][c]:
                           break
                        c=c+1
                    k = test[b][c]
                    if int(slojno[k])<17:
                        a = int(slojno[k])
                        a = a*2
                        a = str(a)
                        k = slojno1[a]
                    else:
                        a = int(slojno[k])
                        a = a*2-33
                        a = str(a)
                        k = slojno1[a]
                    o=int(slojno[k])
                    if o+o1>32:
                        k=slojno1[str((int(slojno[k1])+int(slojno[k])-32))]
                    else:
                        k=slojno1[str(int(slojno[k1])+int(slojno[k]))]
                    k = first[k]
                    ent.insert(END,k)
                    e = e+1
                    e1 = e1+1
                    if e1 == 2:
                        e1 = 0
                    if o1+1!=33:
                        k1=slojno1[str(int (slojno[k1])+1)]
                    else:
                        k1 = slojno1['1']
                        if o2+1!=33:
                            k2=slojno1[str(int (slojno[k2])+1)]
                        else:
                            k2 = slojno1['1']
                
                

def deshifr(event):
    yslovie = var.get()
    slovo = ent.get()
    if yslovie == 0:
        root1 = Tk()
        root1.minsize(300,50)
        root1.maxsize(300,50)
        label=Label(root1,text='Ошибка!\nВыберите шифр')
        label.pack()
        root1.mainloop()
    elif len(slovo)==0:
        yslovie=0
        root1 = Tk()
        root1.minsize(300,50)
        root1.maxsize(300,50)
        label=Label(root1,text='Ошибка!\nДешифровать нечего')
        label.pack()
        root1.mainloop()
    slojno1=dict()
    b=1
    a='А'
    d=1
    while b!=33:
        d = str(d)
        slojno1[d]=a
        a=ord(a)
        a=a+1
        d=int(d)
        a=chr(a)
        d=d+1
        b=b+1
    slojno=dict()
    b=1
    a='А'
    c=1
    while b!=33:
        c = str(c)
        slojno[a]=c
        a=ord(a)
        a=a+1
        c=int(c)
        a=chr(a)
        c=c+1
        b=b+1
    first={'Ю':'А', 'Ь': 'Б', 'Ъ': 'В', 'Ш': 'Г', 'Ц': 'Д', 'Ф': 'Е', 'Т': 'Ж', 'Р': 'З', 'О': 'И', 'М': 'Й', 'К': 'К', 'И': 'Л', 'Ж': 'М', 'Д': 'Н', 'В': 'О', 'А': 'П', 'Б': 'Р', 'Г': 'С', 'Е': 'Т', 'З': 'У', 'Й': 'Ф', 'Л': 'Х', 'Н': 'Ц', 'П': 'Ч', 'С': 'Ш', 'У': 'Щ', 'Х': 'Ъ', 'Ч': 'Ы', 'Щ': 'Ь', 'Ы': 'Э', 'Э': 'Ю', 'Я': 'Я'}
    #Шифр Виженера
    bykvar=dict()
    b=1
    a='А'
    c='а'
    while b!=32:
        bykvar[c]=a
        a=ord(a)
        c=ord(c)
        a=a+1
        c=c+1
        c=chr(c)
        a=chr(a)
        b=b+1
    test =[0]*33
    for i in range(33):
        test[i] = [0] * 33
    a='А'
    b =0
    c=1
    d = 1
    while 1==1:
        if c==33:
            b=b+1
            c=0
        if b == 33:
            break
        if c == 0:
            test[b][c]=test[0][d]
            a = test[0][d]
            d=d+1
            c = c+1
        else:
            test[b][c]=a
            if test[b][c] in bykvar:
                test[b][c] = bykvar[test[b][c]]
            a=ord(a)
            a=a+1
            a=chr(a)
            c=c+1
    morze={'•−': 'А', '−•••': 'Б', '•−−': 'В', '−−•': 'Г', '−••': 'Д', '•': 'Е', '•••−': 'Ж', '−−••': 'З', '••': 'И', '•−−−': 'Й', '−•−': 'К', '•−••': 'Л', '−−': 'М', '−•': 'Н', '−−−': 'О', '•−−•': 'П', '•−•': 'Р', '•••': 'С', '−': 'Т', '••−': 'У', '••−•': 'Ф', '••••': 'Х', '−•−•': 'Ц', '−−−•': 'Ч', '−−−−': 'Ш', '−−•−': 'Щ', '−−•−−': 'Ъ', '−•−−': 'Ы', '−••−': 'Ь', '••−••': 'Э', '••−−': 'Ю', '•−•−': 'Я'}
    bykv=dict()
    b=1
    a='А'
    c=1
    while b!=33:
        c = str(c)
        if c=='7':
            bykv['Ё']=c
            c=int(c)
            c=c+1
            c = str(c)
        bykv[a]=c
        a=ord(a)
        a=a+1
        c=int(c)
        a=chr(a)
        c=c+1
        b=b+1
    bykv1=dict()
    b=1
    a='А'
    d=1
    while b!=33:
        d = str(d)
        if d=='7':
            bykv1[d]='Ё'
            d=int(d)
            d=d+1
            d = str(d)
        bykv1[d]=a
        a=ord(a)
        a=a+1
        d=int(d)
        a=chr(a)
        d=d+1
        b=b+1
    if yslovie == 1:
        x=str(ent.get())
        for i in range(0,len(x)):
            shtoto=ord(x[i])
            if shtoto<48 and shtoto!=45 and shtoto!=32 or shtoto>57:
                ent.delete(0,END)
                root1 = Tk()
                root1.minsize(300,50)
                root1.maxsize(300,50)
                label=Label(root1,text='Ошибка!\nДешифровка данного шифра должна иметь только\nдеситичные цифры, тире и пробелы')
                label.pack()
                root1.mainloop()
                x = 1
                break
        if x !=1:
            x=str(ent.get())
            ent.delete(0,END)
            p=0
            while 1==1:
               if p==len(x):
                   break
               q=p+1
               while 1==1:
                   if x[q-1]=='-' or x[q-1]==' ':
                       break
                   if  q==len(x):
                       o=x[p:q]
                       break
                   o=x[p:q]
                   q=q+1
               ent.insert(END,bykv1[o])
               if x[q-1]==' ':
                   ent.insert(END,' ')
               p=q
    if yslovie == 2:
        slovo = ent.get()
        x = 0
        for i in range(0,len(slovo)):
            shtoto = int(ord(slovo[i]))
            if shtoto!=32 and shtoto!=1025 and shtoto<1040 or shtoto>1071:
                ent.delete(0,END)
                yslovie=0
                root1 = Tk()
                root1.minsize(300,50)
                root1.maxsize(300,50)
                label=Label(root1,text='Ошибка!\nДешифровка этого кода работает только с\nзаглавными буквами русского алфавита')
                label.pack()
                root1.mainloop()
                x=1
                break
        if x!=1:
            x=str(ent.get())
            ent.delete(0,END)
            p=0
            while 1==1:
                if p==len(x):
                   break
                if x[p]==' ':
                    ent.insert(END,' ')
                    p=p+1
                if bykv[x[p]]=='1':
                    ent.insert(END,'Я')
                    p=p+1
                else:
                    b=int(bykv[x[p]])-1
                    ent.insert(END,bykv1[str(b)])
                    p=p+1
    if yslovie==3:
        slovo = ent.get()
        x = 0
        for i in range(0,len(slovo)):
            shtoto = int(ord(slovo[i]))
            if shtoto!=32 and shtoto!=1025 and shtoto<1040 or shtoto>1071:
                ent.delete(0,END)
                yslovie=0
                root1 = Tk()
                root1.minsize(300,50)
                root1.maxsize(300,50)
                label=Label(root1,text='Ошибка!\nДешифровка этого кода работает только с\nзаглавными буквами русского алфавита')
                label.pack()
                root1.mainloop()
                x=1
                break
        if x!=1:
            x = 0
            if len(ent2.get())!=1:
                ent2.delete(0,END)
                root1 = Tk()
                root1.minsize(300,50)
                root1.maxsize(300,50)
                label=Label(root1,text='Ошибка!\nВ этом шифре нужно ввести\nколичество перестановок от 0 до 9')
                label.pack()
                root1.mainloop()
                x = 1
            if x!=1:
                shtoto=ord(ent2.get())
                if shtoto<48 or shtoto>57:
                    ent2.delete(0,END)
                    root1 = Tk()
                    root1.minsize(300,50)
                    root1.maxsize(300,50)
                    label=Label(root1,text='Ошибка!\nВ этом шифре нужно ввести\nколичество перестановок от 0 до 9')
                    label.pack()
                    root1.mainloop()
                else:
                    w=1
                    r=int(ent2.get())
                    while 1==1:
                        if r==0:
                            break
                        x=str(ent.get())
                        ent.delete(0,END)
                        p=0
                        q=0
                        while 1==1:
                            if p==len(x) or x[p]==' ':
                                d=x[q:p]
                                k=0
                                ent.insert(END,d[-1])
                                while 1==1:
                                    if k==len(d)-1:
                                        break
                                    ent.insert(END,d[k])
                                    k=k+1
                                if p==len(x):
                                    break
                                else:
                                    ent.insert(END,' ')
                                    q=p+1
                            p=1+p
                        if r==w:
                            break
                        w=w+1
    if yslovie==4:
        slovo = ent.get()
        x = 0
        for i in range(0,len(slovo)):
            shtoto = int(ord(slovo[i]))
            if shtoto!=8226 and shtoto!=8722 and shtoto!=32:
                ent.delete(0,END)
                yslovie=0
                root1 = Tk()
                root1.minsize(300,50)
                root1.maxsize(300,50)
                label=Label(root1,text='Ошибка!\nДешифровка этого кода работает только с\nточками и тире')
                label.pack()
                root1.mainloop()
                x=1
                break
        if x!=1:
            x=str(ent.get())
            ent.delete(0,END)
            p=0
            while 1==1:
               if p==len(x):
                   break
               q=p+1
               while 1==1:
                   if x[q-1]==' ' or x[q-1]==' ' and x[q]==' ' and x[q+1]==' ':
                       break
                   if  q==len(x):
                       o=x[p:q]
                       break
                   o=x[p:q]
                   q=q+1
               if o in morze:
                   ent.insert(END,morze[o])
               else:
                   ent.delete(0,END)
                   root1 = Tk()
                   root1.minsize(300,50)
                   root1.maxsize(300,50)
                   label=Label(root1,text='Ошибка!\nНе правильная комбинация точек и тире')
                   label.pack()
                   root1.mainloop()
                   break
               if x[q-1]==' ' and x[q]==' ' and x[q+1]==' ':
                   q=q+2
                   ent.insert(END,' ')
               p=q
    if yslovie==6:
        slovo = ent.get()
        x = 0
        for i in range(0,len(slovo)):
            shtoto = int(ord(slovo[i]))
            if shtoto!=32  and shtoto<1040 or shtoto>1071:
                ent.delete(0,END)
                yslovie=0
                root1 = Tk()
                root1.minsize(300,50)
                root1.maxsize(300,50)
                label=Label(root1,text='Ошибка!\nДешифровка этого кода работает только с\nзаглавными буквами русского алфавита, без буквы Ё')
                label.pack()
                root1.mainloop()
                x=1
                break
        if x!=1:
            x=str(ent.get())
            ent.delete(0,END)
            p=0
            while 1==1:
               if p==len(x):
                   break
               if x[p]==' ':
                   ent.insert(END,' ')
               else:
                   ent.insert(END,first[x[p]])
               p=p+1
    if yslovie==5:
        slovo = ent.get()
        x = 0
        for i in range(0,len(slovo)):
            shtoto = int(ord(slovo[i]))
            if shtoto!=32 and shtoto<1040 or shtoto>1071:
                ent.delete(0,END)
                yslovie=0
                root1 = Tk()
                root1.minsize(300,50)
                root1.maxsize(300,50)
                label=Label(root1,text='Ошибка!\nДешифровка этого кода работает только с\nзаглавными буквами русского алфавита, без буквы Ё')
                label.pack()
                root1.mainloop()
                x=1
                break
        if x!=1:
            slovo = str(ent.get())
            key = str(ent1.get())
            plus = 0
            minus = 0
            z=0
            for i in range(0,len(slovo)):
                if plus ==0 and len(key)==0:
                    plus = 4 
                elif plus ==0:
                    plus = 1 
                    for j in range(0,len(key)):
                        shtoto1 = int(ord(key[j]))
                        if shtoto1==1025:
                            plus = 2
                            break
                        if  shtoto1<1040 or shtoto1>1071:
                            plus = 3
                            break
                        if chr(shtoto1)==" ":
                            z=z+1
                        if z==len(key):
                            plus = 4
                            break
                shtoto = int(ord(slovo[i]))
                if shtoto==1025:
                    minus = minus +1
                    break
            if minus != 0 and plus ==1:
                ent.delete(0,END)
                root1 = Tk()
                root1.minsize(300,50)
                root1.maxsize(300,50)
                label=Label(root1,text='Ошибка!\nДанный шифр не шифрует букву Ё')
                label.pack()
                root1.mainloop()
            elif plus ==2 and minus ==0:
                ent1.delete(0,END)
                root1 = Tk()
                root1.minsize(300,50)
                root1.maxsize(300,50)
                label=Label(root1,text='Ошибка!\nДанный шифр не может иметь в ключе букву Ё')
                label.pack()
                root1.mainloop()
            elif plus ==2 and minus !=0:
                ent.delete(0,END)
                ent1.delete(0,END)
                root1 = Tk()
                root1.minsize(300,50)
                root1.maxsize(300,50)
                label=Label(root1,text='Ошибка!\nДанный шифр не шифрует букву Ё\nДанный шифр не может иметь в ключе букву Ё')
                label.pack()
                root1.mainloop()
            elif plus ==3:
                ent1.delete(0,END)
                root1 = Tk()
                root1.minsize(300,50)
                root1.maxsize(300,50)
                label=Label(root1,text='Ошибка!\nВ ключе используются только\nзаглавные буквы русского алфавита')
                label.pack()
                root1.mainloop()
            elif plus ==4:
                ent1.delete(0,END)
                root1 = Tk()
                root1.minsize(300,50)
                root1.maxsize(300,50)
                label=Label(root1,text='Ошибка!\nВ ключе нету букв')
                label.pack()
                root1.mainloop()
            else:
                key = str(ent1.get())
                slovo = str(ent.get())
                ent.delete(0,END)
                b=1
                c=1
                d=0
                e=0
                while 1==1:
                    if e == len(slovo):
                        break
                    if d == len(key):
                        d = 0
                    if slovo[e]==' ':
                        ent.insert(END,' ')
                        e=e+1
                    if key[d]==' ':
                        d=d+1
                    while 1==1:
                        if key[d]==test[b][0]:
                            break
                        b=b+1
                    while 1==1:
                        if slovo[e]==test[b][c]:
                            break
                        c=c+1
                    ent.insert(END,test[0][c])
                    b=1
                    c=1
                    e=e+1
                    d=d+1
    if yslovie==7:
        slovo = ent.get()
        x = 0
        for i in range(0,len(slovo)):
            shtoto = int(ord(slovo[i]))
            if shtoto!=32  and shtoto<1040 or shtoto>1071:
                ent.delete(0,END)
                yslovie=0
                root1 = Tk()
                root1.minsize(300,50)
                root1.maxsize(300,50)
                label=Label(root1,text='Ошибка!\nДешифровка этого кода работает только с\nзаглавными буквами русского алфавита, без буквы Ё')
                label.pack()
                root1.mainloop()
                x=1
                break
        if x!=1:
            slovo = str(ent.get())
            ent.delete(0,END)
            e = 0
            a = 0
            while e!=len(slovo):
                if slovo[e] == ' ':
                    ent.insert(END,' ')
                else:
                    if int(slojno[slovo[e]])%2==0:
                        a = int(slojno[slovo[e]])
                        a = int(a/2)
                        a = str(a)
                        ent.insert(END,slojno1[a])
                    if int(slojno[slovo[e]])%2==1:
                        a = int(slojno[slovo[e]])
                        a = int((a+33)/2)
                        a = str(a)
                        ent.insert(END,slojno1[a])
                e=e+1
    if yslovie==8:
        slovo = ent.get()
        x = 0
        for i in range(0,len(slovo)):
            shtoto = int(ord(slovo[i]))
            if shtoto!=32 and shtoto<1040 or shtoto>1071:
                ent.delete(0,END)
                yslovie=0
                root1 = Tk()
                root1.minsize(300,50)
                root1.maxsize(300,50)
                label=Label(root1,text='Ошибка!\nДешифровка этого кода работает только с\nзаглавными буквами русского алфавита, без буквы Ё')
                label.pack()
                root1.mainloop()
                x=1
                break
        if x!=1:
            x=0
            y=0
            z=0
            slovo = str(ent.get())
            for i in range(0,len(slovo)):
                shtoto = int(ord(slovo[i]))
                if shtoto==1025:
                    ent.delete(0,END)
                    x=1
                    break
            if len(ent3.get())==0:
                y=3
            if len(ent4.get())==0:
                z=3
            else:
                shtoto = int(ord(ent3.get()[0]))
                if shtoto==1025:
                    ent3.delete(0,END)
                    y=1
                elif shtoto!=32 and shtoto<1040 or shtoto>1071 or len(ent3.get())!=1:
                    ent3.delete(0,END)
                    y=2
                shtoto = int(ord(ent4.get()[0]))
                if shtoto==1025:
                    ent4.delete(0,END)
                    z=1
                elif shtoto!=32 and shtoto<1040 or shtoto>1071 or len(ent4.get())!=1:
                    ent4.delete(0,END)
                    z=2
            if x==1 and y==0 or x==1 and z==0:
                root1 = Tk()
                root1.minsize(300,50)
                root1.maxsize(300,50)
                label=Label(root1,text='Ошибка!\nДанный шифр не шифрует букву Ё')
                label.pack()
                root1.mainloop()
            elif x==0 and y==1 or x==0 and z==1:
                root1 = Tk()
                root1.minsize(300,50)
                root1.maxsize(300,50)
                label=Label(root1,text='Ошибка!\nРоторы не могут иметь букву Ё')
                label.pack()
                root1.mainloop()
            elif x==1 and y==1 or x==1 and z==1:
                root1 = Tk()
                root1.minsize(300,50)
                root1.maxsize(300,50)
                label=Label(root1,text='Ошибка!\nДанный шифр не шифрует букву Ё\nРоторы не могут иметь букву Ё')
                label.pack()
                root1.mainloop()
            elif y==2 or z==2:
                root1 = Tk()
                root1.minsize(300,70)
                root1.maxsize(300,70)
                label=Label(root1,text='Ошибка!\nВ роторах используется только одна\nзаглавная буква русского алфавита.\nБез пробелов')
                label.pack()
                root1.mainloop()
            elif y==3 or z==3:
                root1 = Tk()
                root1.minsize(300,70)
                root1.maxsize(300,70)
                label=Label(root1,text='Ошибка!\nЗаполните все роторы')
                label.pack()
                root1.mainloop()
            else:
                slovo = str(ent.get())
                e = 0
                ent.delete(0,END)
                k1 = str(ent3.get())
                k2 = str(ent4.get())
                e1 = 0
                while e!=len(slovo):
                    k3 = k1+k2
                    if slovo[e] == ' ':
                        ent.insert(END,' ')
                        e = e + 1
                    else:
                        k=slovo[e]
                        o1=int(slojno[k1])
                        o2=int(slojno[k2])
                        k = first[k]
                        o=int(slojno[k])
                        if o-o1<1:
                            k=slojno1[str(int(slojno[k])+32 - int(slojno[k1]))]
                        else:
                            k=slojno1[str(int(slojno[k]) - int(slojno[k1]))]
                        if int(slojno[k])%2==0:
                            a = int(slojno[k])
                            a = int(a/2)
                            a = str(a)
                            k =(slojno1[a])
                        else:
                            a = int(slojno[k])
                            a = int((a+33)/2)
                            a = str(a)
                            k=(slojno1[a])
                        b=1
                        c=1
                        while 1==1:
                            if k3[e1]==test[b][0]:
                                break
                            b=b+1
                        while 1==1:
                            if k==test[b][c]:
                                break
                            c=c+1
                        k=test[0][c]
                        if int(slojno[k])%2==0:
                            a = int(slojno[k])
                            a = int(a/2)
                            a = str(a)
                            k =(slojno1[a])
                        else:
                            a = int(slojno[k])
                            a = int((a+33)/2)
                            a = str(a)
                            k=(slojno1[a])
                        o=int(slojno[k])
                        if o-o2<1:
                            k=slojno1[str(int(slojno[k])+32 - int(slojno[k2]))]
                        else:
                            k=slojno1[str(int(slojno[k]) - int(slojno[k2]))]
                        k = first[k]
                        o=int(slojno[k])
                        if o-o1<1:
                            k=slojno1[str(int(slojno[k])+32 - int(slojno[k1]))]
                        else:
                            k=slojno1[str(int(slojno[k]) - int(slojno[k1]))]
                        ent.insert(END,k)
                        e = e+1
                        e1 = e1+1
                        if e1==2:
                            e1=0
                        if int(slojno[k1])+1!=33:
                            k1=slojno1[str(int (slojno[k1])+1)]
                        else:
                            k1 = slojno1['1']
                            if int (slojno[k2])+1!=33:
                                k2=slojno1[str(int (slojno[k2])+1)]
                            else:
                                k2 = slojno1['1']
def tire(event):
    ent.insert(END,'−')
def tochka(event):
    ent.insert(END,'•')

def one():
    root2 = Tk()
    root2.minsize(320,70)
    root2.maxsize(320,70)
    label=Label(root2,text='В данном шифре используются все заглавные\nбуквы русского алфавита для шифровки.\nДля дешифровки используются\nдесятичные цифры и тире.')
    label.pack()
    root2.mainloop()
def rot():
    root2 = Tk()
    root2.minsize(320,70)
    root2.maxsize(320,70)
    label=Label(root2,text='В данном шифре используются все заглавные\nбуквы русского алфавита для шифровки и дешифровки.')
    label.pack()
    root2.mainloop()
def tr():
    root2 = Tk()
    root2.minsize(320,70)
    root2.maxsize(320,70)
    label=Label(root2,text='В данном шифре используются все заглавные\nбуквы русского алфавита для шифровки и дешифровки.\nТакже вводится число, обозначающая\nколичество перестановок букв(от 0 до 9)')
    label.pack()
    root2.mainloop()
def am():
    root2 = Tk()
    root2.minsize(320,70)
    root2.maxsize(320,70)
    label=Label(root2,text='В данном шифре используются заглавные буквы\nрусского алфавита без буквы Ё для шифровки.\nДля дешифровки используются точки и тире.')
    label.pack()
    root2.mainloop()
def shv():
    root2 = Tk()
    root2.minsize(320,70)
    root2.maxsize(320,70)
    label=Label(root2,text='В данном шифре используются заглавные буквы\nрусского алфавита без буквы Ё для шифровки.\nДля ключа точно также')
    label.pack()
    root2.mainloop()
def f():
    root2 = Tk()
    root2.minsize(320,70)
    root2.maxsize(320,70)
    label=Label(root2,text='В данном шифре используются заглавные буквы\nрусского алфавита без буквы Ё для шифровки.')
    label.pack()
    root2.mainloop()
def s():
    root2 = Tk()
    root2.minsize(320,70)
    root2.maxsize(320,70)
    label=Label(root2,text='В данном шифре используются заглавные буквы\nрусского алфавита без буквы Ё для шифровки.')
    label.pack()
    root2.mainloop()
def anigma():
    root2 = Tk()
    root2.minsize(320,70)
    root2.maxsize(320,70)
    label=Label(root2,text='В данном шифре используются заглавные буквы\nрусского алфавита без буквы Ё для шифровки.\nДля роторов используется только по одной заглавной\nбукве русского алфавита без буквы Ё и пробелов')
    label.pack()
    root2.mainloop()
def paste():
    file_name = fd.askopenfilename()
    f = open(file_name)
    s = f.read()
    ent.insert(0, s)
    f.close()
def save():
    file_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
                                        ("HTML files", "*.html;*.htm"),
                                                ("All files", "*.*") ))
    f = open(file_name, 'w')
    s = ent.get()
    f.write(s)
    f.close()

root = Tk()
mainmenu = Menu(root) 
root.config(menu=mainmenu) 
helpmenu = Menu(mainmenu, tearoff=0)
filemenu = Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="Номер буквы",command=one)
helpmenu.add_command(label="Шифр Цезаря",command=rot)
helpmenu.add_command(label="Транспозиция",command=tr)
helpmenu.add_command(label="Азбука Морзе",command=am)
helpmenu.add_command(label="Шифр Виженера",command=shv)
helpmenu.add_command(label="The first",command=f)
helpmenu.add_command(label="The second",command=s)
helpmenu.add_command(label="Энигма lite",command=anigma)
mainmenu.add_cascade(label="Область допустимых значений", menu=helpmenu)
mainmenu.add_cascade(label="Файл", menu=filemenu)
filemenu.add_command(label="Открыть",command=paste)
filemenu.add_command(label="Сохранить",command=save)
root.minsize(500,200)
root.maxsize(500,200)
root.title("King cipher")
var=IntVar()
rbutton1=Radiobutton(root,text='Номер буквы',variable=var,value=1)
rbutton2=Radiobutton(root,text='Шифр Цезаря',variable=var,value=2)
rbutton3=Radiobutton(root,text='Транспозиция',variable=var,value=3)
rbutton4=Radiobutton(root,text='Азбука Морзе',variable=var,value=4)
rbutton5=Radiobutton(root,text='Шифр Виженера',variable=var,value=5)
rbutton6=Radiobutton(root,text='The first',variable=var,value=6)
rbutton7=Radiobutton(root,text='The second',variable=var,value=7)
rbutton8=Radiobutton(root,text='Энигма lite',variable=var,value=8)
ent = Entry(root,font='Arial 14')
ent1 = Entry(root,font='Arial 14')
ent2 = Entry(root,font='Arial 14')
ent3 = Entry(root,font='Arial 14')
ent4 = Entry(root,font='Arial 14')
but1 = Button(root, text='Шифровка')
but2 = Button(root, text='Дешифровка')
but3 = Button(root, text='–')
but4 = Button(root, text='•')
ent.place(x=0,y=0,height=50,width=500)
ent1.place(x=0,y=150,height=50,width=200)
ent2.place(x=310,y=92,height=20,width=20)
ent3.place(x=360,y=150,height=20,width=20)
ent4.place(x=400,y=150,height=20,width=20)
but1.place(x=0,y=50,height=50,width=100)
but2.place(x=100,y=50,height=50,width=100)
but3.place(x=0,y=100,height=50,width=100)
but4.place(x=100,y=100,height=50,width=100)
rbutton1.place(x=200,y=50)
rbutton2.place(x=200,y=70)
rbutton3.place(x=200,y=90)
rbutton4.place(x=200,y=110)
rbutton5.place(x=200,y=130)
rbutton6.place(x=200,y=150)
rbutton7.place(x=200,y=170)
rbutton8.place(x=350,y=170)
but1.bind('<Button-1>',shifr)
but2.bind('<Button-1>',deshifr)
but3.bind('<Button-1>',tire)
but4.bind('<Button-1>',tochka)
root.mainloop()

```