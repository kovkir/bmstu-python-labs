#Лабороторная работа: Уточнение корней;

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize
from time import perf_counter
from tkinter import *
import tkinter as tk


#уточнение корней методом Brentq
def Brentq(a,b,tree):
    start2 = perf_counter()
    xa = a
    fa = f(xa)
    xc = b
    fc = f(xc)
    if fa<fc:
        x0=xa
        x1=xc
    else:
        x0=xc
        x1=xa
    d=abs(x1-x0)
    koliter=1
    
    while d>=toch and abs(f(x1))>=toch:
        # деление отрезка пополам
        xb = (xa+xc)/2
        fb = f(xb)
        # обратная квадратичная интерполяция
        if fb!=0 and fa!=0 and fc!=0:
            R = fb/fc
            S = fb/fa
            T = fa/fc
            P = S*(T*(R-T)*(xc-xb)-(1-R)*(xb-xa))
            Q = (T-1)*(R-1)*(S-1)
            xd = xb+P/Q
            fd = f(xd)
        else:
            if fc!=0:
                break
        koliter+=1
        
        #метод секущих
        if koliter!=2:
            xs=x0-f(x0)*(x0-x1)/(f(x0)-f(x1))
            fs=f(xs)
        else:
            xs=xb
            fs=xb
            
        if xa<=xd and xd<=xc and abs(fd)<abs(fb) and abs(fd)<abs(fs):
        #лучше использовать обратную квадратичную интерполяцию
            if fa*fd>0:
                x0=x1
                x1=xd
                d=abs(x1-x0)
                xa = xd
                fa = fd
            else:
                x0=x1
                x1=xd
                d=abs(x1-x0) 
                xc = xd
                fc = fd
                
        elif xa<=xs and xs<=xc and abs(fs)<abs(fb) and abs(fs)<abs(fd):
        #лучше использовать метод секущих
            if fa*fs>0:
                x0=x1
                x1=xs
                d=abs(x1-x0)
                xa = xs
                fa = fs
            else:
                x0=x1
                x1=xs
                d=abs(x1-x0)
                xc = xs
                fc = fs
                
        else:
        #лучше использовать деление отрезка пополам
            if fa*fb>0:
                x0=x1
                x1=xb
                d=abs(x1-x0) 
                xa = xb
                fa = fb
            else:
                x0=x1
                x1=xb
                d=abs(x1-x0) 
                xc = xb
                fc = fb
                
    if abs(fa)<abs(fc):
            x2 = xa
            y2 = fa
    else:
            x2 = xc
            y2 = fc
    stop2 = perf_counter()

    oshibka=0
    if koliter>max_iter:
        oshibka=1
        tree.insert('','end', text='', values=('Брент',\
                        '{:.2f}'.format(a),'{:.2f}'.format(b),\
                        '','','','',' '*9+str(oshibka)))
        tree.insert('','end',text='')
    else:
        tree.insert('','end', text='', values=('Брент',\
                        '{:.2f}'.format(a),'{:.2f}'.format(b),\
                        '{:^25.9g}'.format(x2),'{:^20.1e}'.format(y2),\
                        ' '*9+str(koliter),'{:^20.1e}'.format(stop2-start2),\
                                               ' '*9+str(oshibka)))
        #tree.insert('','end',text='')

       
def f(x):
    return(np.sin(x)+0.5)

def f2(x):
    return((np.sin(x))*(-1))

def clicked():
    nach=float(txt1.get())
    kon=float(txt2.get())
    shag=float(txt3.get())  

    #построение графика функции
    x=np.linspace(nach,kon,1000)
    plt.title('Graph')
    plt.plot(x,f(x),label='sin(x)+0.5')
    plt.plot([nach,kon],[0,0],color='y',label='Ox')
    plt.legend(loc=1)
    plt.xlabel('$x$')
    plt.ylabel('$f(x)$')
    plt.grid(True)

    a=nach
    b=a+shag
    nom=0
    x1=(a+b)/2
    while a<=kon:
        oshibka=0
        if b>kon:
            b=kon
        if f(a)*f(b)<=0 and f(a)!=f(x1):
            if nom==0:

                #построение таблицы
                window2 = Tk()
                window2.title('Уточнение корней')
                
                tree=ttk.Treeview(window2,height=20)
                tree.tag_configure('ttk', background='light gray')
                
                tree['columns']=('one','two','three','four','five','six',\
                                 'seven','eight')
                tree.column('#0', width=70, minwidth=70, stretch=tk.NO)
                tree.column('one', width=70, minwidth=75, stretch=tk.NO)
                tree.column('two', width=50, minwidth=50,stretch=tk.NO)
                tree.column('three', width=50, minwidth=50, stretch=tk.NO)
                tree.column('four', width=120, minwidth=120, stretch=tk.NO)
                tree.column('five', width=100, minwidth=100, stretch=tk.NO)
                tree.column('six', width=80, minwidth=80, stretch=tk.NO)
                tree.column('seven', width=100, minwidth=100, stretch=tk.NO)
                tree.column('eight', width=80, minwidth=80, stretch=tk.NO)

                tree.heading('#0',text='№ корня',anchor=tk.CENTER)
                tree.heading('one', text='метод',anchor=tk.CENTER)
                tree.heading('two', text='A',anchor=tk.CENTER)
                tree.heading('three', text='B',anchor=tk.CENTER)
                tree.heading('four', text='Значение X',anchor=tk.CENTER)
                tree.heading('five', text='F(X)',anchor=tk.CENTER)
                tree.heading('six', text='Итераций',anchor=tk.CENTER)
                tree.heading('seven', text='Время раб.',anchor=tk.CENTER)
                tree.heading('eight', text='Код ошибки',anchor=tk.CENTER)

                #tree.insert('','end',text='')
            nom+=1
      
            try:
                start = perf_counter()
                x1,x3=optimize.brentq(f,a,b,xtol=toch,maxiter=max_iter,\
                full_output = True)
                stop = perf_counter()

                tree.insert('','end', text='   '+str(nom),tags=('ttk'),\
                            values=('brentq',\
                        '{:.2f}'.format(a),'{:.2f}'.format(b),\
                        '{:^25.9g}'.format(x1),'{:^20.1e}'.format(f(x1)),\
                        ' '*9+str(x3.iterations),\
                        '{:^20.1e}'.format(stop-start),' '*9+str(oshibka)))
                
                x0=optimize.brentq(f,a,b)
                #x0 - точное значение корня
                #plt.scatter(x0,0,c='r')
                if nom==1:
                    plt.plot(x0,0,'ro',label='Roots')
                    plt.legend(loc=1)
                else:
                    plt.plot(x0,0,'ro')
                    
            except RuntimeError:
                oshibka=1
                tree.insert('','end', text='   '+str(nom),tags=('ttk'),\
                    values=('brentq','{:.2f}'.format(a),'{:.2f}'.format(b),\
                    '','','','',' '*9+str(oshibka)))

            Brentq(a,b,tree)
        a+=shag
        b+=shag

    a=nach
    b=a+shag
    x00=(a+b)/2
    nom2=0
    
    while a<=kon:
        if b>kon:
            b=kon
        if f2(a)*f2(b)<=0 and f2(a)!=f(x00):
            nom2+=1
            x00=optimize.brentq(f2,a,b)
            #x00 - точка перегиба
            #plt.scatter(x00,f(x00),c='g')
            if nom2==1:
                plt.plot(x00,f(x00),'gp',label='Inflection points')
                plt.legend(loc=1)
            else:
                plt.plot(x00,f(x00),'gp')
        a+=shag
        b+=shag
    
    if nom!=0:
        tree.pack()
        plt.show()
        window2.mainloop()
        
    else:
        window2 = Tk()
        window2.title('Уточнение корней')
        window2.geometry('320x50')
        lbl7=Label(window2,text='На данном участке корней нет',\
                   font=('Courier New',14))
        lbl7.grid(column=0,row=1)
        plt.legend(loc=1)
        plt.show()
        window2.mainloop()

toch=1e-6
max_iter=100

#создание окна
window = Tk()
window.title('Уточнение корней')
window.geometry("500x330")

txt0=Label(window,text='')
txt0.grid(column=0,row=0,columnspan=2)

lbl1=Label(window,text='Начало интервала',font=('Courier New',14))
lbl1.grid(column=0,row=1)
txt1=Entry(window,width=15,font=('Courier New',14))
txt1.grid(column=1,row=1)
txt1.focus()

lbl2=Label(window,text='Конец интервала ',font=('Courier New',14))
lbl2.grid(column=0,row=2)
txt2=Entry(window,width=15,font=('Courier New',14))
txt2.grid(column=1,row=2)

lbl3=Label(window,text='Шаг разбиения   ',font=('Courier New',14))
lbl3.grid(column=0,row=3)
txt3=Entry(window,width=15,font=('Courier New',14))
txt3.grid(column=1,row=3)
txt3.insert(1,'1')

txt4=Label(window,text='\nТочность = '+'{:.0e}'.format(toch)+' '*24+'\n'\
+'Максимальное кол-во итераций = '+str(max_iter)+' '*6,\
           font=('Courier New',14))
txt4.grid(column=0,row=4,columnspan=2)

lbl5=Label(window,text='\nВиды ошибок:'+' '*28+'\n0. Нет ошибок'+' '*23+'\n\
    1. Превышено максимальное число итераций\n',font=('Courier New',14))
lbl5.grid(column=0,row=5,columnspan=2)
                         
btn=Button(window,text='   Найти корни   ',font=('Courier New',14),\
           bg='dark gray',fg='white',command=clicked)
btn.grid(column=0,row=6,columnspan=2)

from tkinter import ttk

window.mainloop()








