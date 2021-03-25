#Лабороторная работа: Калькулятор;

from tkinter import *
from tkinter import messagebox

def clicked_7():
    a=txt1.get()
    txt1.insert(len(a),7)
    global last
    last=7

def clicked_8():
    a=txt1.get()
    txt1.insert(len(a),8)
    global last
    last=8
    
def clicked_9():
    a=txt1.get()
    txt1.insert(len(a),9)
    global last
    last=9
    
def clicked_4():
    a=txt1.get()
    txt1.insert(len(a),4)
    global last
    last=4

def clicked_5():
    a=txt1.get()
    txt1.insert(len(a),5)
    global last
    last=5
    
def clicked_6():
    a=txt1.get()
    txt1.insert(len(a),6)
    global last
    last=6

def clicked_1():
    a=txt1.get()
    txt1.insert(len(a),1)
    global last
    last=1

def clicked_2():
    a=txt1.get()
    txt1.insert(len(a),2)
    global last
    last=2
    
def clicked_3():
    a=txt1.get()
    txt1.insert(len(a),3)
    global last
    last=3

def clicked_0():
    a=txt1.get()
    txt1.insert(len(a),0)
    global last
    last=0
    
def clicked_t():
    a=txt1.get()
    txt1.insert(len(a),'.')
    global last
    last='t'

def Information():
    messagebox.showinfo('Information','Данная программа выполняет \
перевод чисел в двочиную систему счисления и обратно.\n\n\
Ковалец К. ИУ7-23Б')
    global last
    last='a'
    
def clicked_in_2():
    global last
    last='in_2'
    b=txt2.get()
    b1=len(b)
    while b1>=1:
        txt2.delete(b1-1)
        b1-=1
    k=0
    h=0
    try:
        a=float(txt1.get())
        if a<0:
            h=1
            a*=(-1)
            
    except:
        k=1
        txt2.insert(0,'Ошибка')
    if k==0:
        c=int(a)
        d=str(a)[len(str(a))-(len(str(a))-len(str(c))-1)-2:]
        d='0'+d[1:]
        result=''
        while c>0:
            result+=str(c%2)
            c//=2
        result=result[::-1]
        result+='.'
        l=6
        while l>0:
            d=str(float(d)*2)
            result+=d[0]
            d='0'+d[1:]
            l-=1
        while result[-1]=='0':
            result=result[:-1]
        if result[-1]=='.':
            result=result[:-1]
        txt2.insert(0,result)
        if h==1:
            txt2.insert(0,'-')
    
def clicked_in_10():
    global last
    last='in_10'
    b=txt2.get()
    b1=len(b)
    while b1>=1:
        txt2.delete(b1-1)
        b1-=1
    k=0
    h=0
    
    try:
        a=float(txt1.get())
        if a<0:
            h=1
            a*=(-1)
            
    except:
        k=1
        txt2.insert(0,'Ошибка')
    if k==0:
        array=['2','3','4','5','6','7','8','9']
        for i in array:
            if i in str(a):
                txt2.insert(0,'Ошибка')
                k=1
                break
    if k==0:
        c=int(a)
        d=str(a)[len(str(a))-(len(str(a))-len(str(c))-1):]
        power=0
        result=0
        ostatok=0
        while c>0:
            ostatok=c%10
            c//=10
            result+=ostatok*pow(2,power)
            power+=1
        if d!='0':
            power=-1
            while len(d)>0:
                result+=int(d[0])*pow(2,power)
                d=d[1:]
                power-=1
        txt2.insert(0,result)
        if h==1:
            txt2.insert(0,'-')
            
def clicked_C():
    global last
    last='C'
    a=txt1.get()
    a1=len(a)
    while a1>=1:
        txt1.delete(a1-1)
        a1-=1
    b=txt2.get()
    b1=len(b)
    while b1>=1:
        txt2.delete(b1-1)
        b1-=1

def clicked_C1():
    global last
    last='C1'
    a=txt1.get()
    txt1.delete(len(a)-1)

def replay():
    if last=='C':
        clicked_C()
    elif last=='C1':
        clicked_C1()
    elif last=='in_10':
        clicked_in_10()
    elif last=='in_2':
        clicked_in_2()
    elif last=='a':
        author()
    elif last=='t':
        clicked_t()
    elif last==0:
        clicked_0()
    elif last==1:
        clicked_1()
    elif last==2:
        clicked_2()
    elif last==3:
        clicked_3()
    elif last==4:
        clicked_4()
    elif last==5:
        clicked_5()
    elif last==6:
        clicked_6()
    elif last==7:
        clicked_7()
    elif last==8:
        clicked_8()
    elif last==9:
        clicked_9() 

last='C'

#создание окна
window = Tk()
window['bg']='light gray'
window.title('Калькулятор')
window.geometry("555x390")

txt00=Label(window,text='',width=1,bg='light gray')
txt00.grid(column=0,row=0)
txt01=Label(window,text='',width=1,bg='light gray')
txt01.grid(column=1,row=0)
txt02=Label(window,text='',width=1,bg='light gray')
txt02.grid(column=2,row=0)
txt03=Label(window,text='',width=1,bg='light gray')
txt03.grid(column=3,row=0)
txt04=Label(window,text='',width=1,bg='light gray')
txt04.grid(column=4,row=0)
txt05=Label(window,text='',width=1,bg='light gray')
txt05.grid(column=5,row=0)
txt06=Label(window,text='',width=1,bg='light gray')
txt06.grid(column=6,row=0)
txt07=Label(window,text='',width=1,bg='light gray')
txt07.grid(column=7,row=0)

txt_1=Label(window,width=18,text='input window',bg='light gray',\
            font=('Courier New',18))
txt_1.grid(column=1,row=1,columnspan=5)

txt1=Entry(window,width=18,font=('Courier New',18))
txt1.grid(column=1,row=2,columnspan=5)
txt1.focus()

txt_2=Label(window,width=18,text='output window',bg='light gray',\
            font=('Courier New',18))
txt_2.grid(column=7,row=1)

txt2=Entry(window,width=18,font=('Courier New',18))
txt2.grid(column=7,row=2,columnspan=2)

txt3=Label(window,text='',bg='light gray')
txt3.grid(column=0,row=3,columnspan=8)

btn7=Button(window,text='  7  ',font=('Courier New',14),\
        command=clicked_7)
btn7.grid(column=1,row=4)

btn8=Button(window,text='  8  ',font=('Courier New',14),\
        command=clicked_8)
btn8.grid(column=3,row=4)

btn9=Button(window,text='  9  ',font=('Courier New',14),\
        command=clicked_9)
btn9.grid(column=5,row=4)

txt4=Label(window,text='',bg='light gray')
txt4.grid(column=0,row=5,columnspan=8)

btn4=Button(window,text='  4  ',font=('Courier New',14),\
        command=clicked_4)
btn4.grid(column=1,row=6)

btn5=Button(window,text='  5  ',font=('Courier New',14),\
        command=clicked_5)
btn5.grid(column=3,row=6)

btn6=Button(window,text='  6  ',font=('Courier New',14),\
        command=clicked_6)
btn6.grid(column=5,row=6)

txt5=Label(window,text='',bg='light gray')
txt5.grid(column=0,row=7,columnspan=8)

btn1=Button(window,text='  1  ',font=('Courier New',14),\
        command=clicked_1)
btn1.grid(column=1,row=8)

btn2=Button(window,text='  2  ',font=('Courier New',14),\
        command=clicked_2)
btn2.grid(column=3,row=8)

btn3=Button(window,text='  3  ',font=('Courier New',14),\
        command=clicked_3)
btn3.grid(column=5,row=8)

txt6=Label(window,text='',bg='light gray')
txt6.grid(column=0,row=9,columnspan=8)

btn0=Button(window,text='  0  ',font=('Courier New',14),\
        command=clicked_0)
btn0.grid(column=1,row=10)

btn_t=Button(window,text='  .  ',font=('Courier New',14),\
        command=clicked_t)
btn_t.grid(column=3,row=10)

btn_C1=Button(window,text='  <  ',font=('Courier New',14),\
        command=clicked_C1)
btn_C1.grid(column=5,row=10)

txt7=Label(window,text='',bg='light gray')
txt7.grid(column=0,row=11,columnspan=8)

btn_C=Button(window,text='  C  ',font=('Courier New',14),\
             command=clicked_C)
btn_C.grid(column=1,row=12)

txt8=Label(window,text='',bg='light gray')
txt8.grid(column=0,row=13,columnspan=8)

btn_in_10=Button(window,width=18,text='Перевод\n из 2-ой в 10-ую ',\
                 font=('Courier New',14),command=clicked_in_10)
btn_in_10.grid(column=7,row=6,rowspan=3)

btn_in_2=Button(window,width=18,text='Перевод\n из 10-ой в 2-ую ',\
                font=('Courier New',14),command=clicked_in_2)
btn_in_2.grid(column=7,row=9,rowspan=2)

btn_replay=Button(window,width=18,text='повтор действия',\
                font=('Courier New',14),command=replay)
btn_replay.grid(column=7,row=4)

menu = Menu(window)
window.config(menu = menu)
menu.add_command(label = 'Информация', command = Information)

window.mainloop()
