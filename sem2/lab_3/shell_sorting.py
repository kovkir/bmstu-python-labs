#Лабороторная работа: Исследование методов сортировки;
#Сортировка Шелла.

from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
from time import perf_counter
from random import randint
            
def shell_sort(array, size):
    
    step = size // 2
    
    while step > 0:
        
        for i in range(step, size):
            j = i - step
            
            while j >= 0 and array[j] > array[j + step]:
                array[j + step],array[j] = array[j],array[j + step]
                j -= step

        step //= 2

def array_filling(n):

    a = []
    for j in range(n):
        a.append(randint(1, 100))

    return a

def time_measurement(array, size):
    
    start = perf_counter()
    shell_sort(array, size)
    end = perf_counter()
    time = end - start

    return time
    
def sorting():

    b=txt2.get()
    b1=len(b)
    
    while b1>0:
        txt2.delete(b1-1)
        b1-=1
        
    a=txt1.get()+' '
    
    for i in a:
        if not ('0' <= i <= '9' or i == ' ' or i == '-'):
            messagebox.showerror('Ошибка','Недопустимые символы в массиве')
            return

    array=[]
    string=''
    
    for i in a:
        if i != ' ':
            string+=i
        else:
            if string != '':
                array.append(int(string))
            string=''

    if len(array) > 0:
        shell_sort(array, len(array))
        
        for i in range(len(array)-1,-1,-1):
            txt2.insert(0,str(array[i])+' ')
    else:
        messagebox.showwarning('Ошибка','В массиве нет элементов')

def graph():

    left = txt6.get()
    if left == '':
        messagebox.showwarning('Ошибка',\
                               'Остались пустые ячейки')
        return
    for i in left:
        if not ('0' <= i <= '9') or (left[0] == '0'):
            messagebox.showerror('Ошибка',\
                                 'Недопустимое значение левой границы')
            return

    right = txt7.get()
    if right == '':
        messagebox.showwarning('Ошибка',\
                               'Остались пустые ячейки')
        return
    for i in right:
        if not ('0' <= i <= '9') or (right[0] == '0'):
            messagebox.showerror('Ошибка',\
                                 'Недопустимое значение правой границы')
            return

    if int(left)+ 10 > int(right):
        messagebox.showwarning('Ошибка',\
                                'Недопустимое значение левой границы')
        return

    left = int(left)
    right =int(right)
    
    plt.title("Сортировка Шеллом")
    plt.xlabel("Кол-во элементов, шт")
    plt.ylabel("Время сортировки, мс")

    x_kol_elem = []
    y_time = []

    a = array_filling(right)
            
    for i in range(left, right, (right-left)//10):

        b=a[:]
        time = time_measurement(b, i)
        
        x_kol_elem.append(i)
        y_time.append(time * 1000)

    plt.plot(x_kol_elem, y_time, 'r')
    plt.grid(True)
    plt.show()

def table():

    n1 = txt3.get()
    if n1 == '':
        messagebox.showwarning('Ошибка',\
                               'Остались пустые ячейки')
        return
    for i in n1:
        if not ('0' <= i <= '9') or (n1[0] == '0'):
            messagebox.showerror('Ошибка','Недопустимое значение N1')
            return

    n2 = txt4.get()
    if n2 == '':
        messagebox.showwarning('Ошибка',\
                               'Остались пустые ячейки')
        return
    for i in n2:
        if not ('0' <= i <= '9') or (n2[0] == '0'):
            messagebox.showerror('Ошибка','Недопустимое значение N2')
            return

    n3 = txt5.get()
    if n3 == '':
        messagebox.showwarning('Ошибка',\
                               'Остались пустые ячейки')
        return
    for i in n3:
        if not ('0' <= i <= '9') or (n3[0] == '0'):
            messagebox.showerror('Ошибка','Недопустимое значение N3')
            return
        
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
    
    table = Tk()
    table.title('Сортировка Шелла')
    table.geometry("680x340")
    
    lbl0=Label(table,text=' ',font=('Courier New',4))
    lbl0.grid(column=0,row=0)
    
    lbl1=Label(table,text='  ')
    lbl1.grid(column=0,row=1)
    lbl2=Label(table,text='\u250C',font=('Courier New',18))
    lbl2.grid(column=1,row=1)
    lbl3=Label(table,text='\u2500'*16,font=('Courier New',18))
    lbl3.grid(column=2,row=1)
    lbl4=Label(table,text='\u252C',font=('Courier New',18))
    lbl4.grid(column=3,row=1)
    lbl5=Label(table,text='\u2500'*10,font=('Courier New',18))
    lbl5.grid(column=4,row=1)
    lbl6=Label(table,text='\u252C',font=('Courier New',18))
    lbl6.grid(column=5,row=1)
    lbl7=Label(table,text='\u2500'*10,font=('Courier New',18))
    lbl7.grid(column=6,row=1)
    lbl8=Label(table,text='\u252C',font=('Courier New',18))
    lbl8.grid(column=7,row=1)
    lbl9=Label(table,text='\u2500'*10,font=('Courier New',18))
    lbl9.grid(column=8,row=1)
    lbl10=Label(table,text='\u2510',font=('Courier New',18))
    lbl10.grid(column=9,row=1)

    lbl11=Label(table,text='\u2502',font=('Courier New',18))
    lbl11.grid(column=1,row=2)
    lbl12=Label(table,text='\u2502',font=('Courier New',18))
    lbl12.grid(column=3,row=2)
    lbl13=Label(table,text='\u2502',font=('Courier New',18))
    lbl13.grid(column=5,row=2)
    lbl14=Label(table,text='\u2502',font=('Courier New',18))
    lbl14.grid(column=7,row=2)
    lbl15=Label(table,text='\u2502',font=('Courier New',18))
    lbl15.grid(column=9,row=2)

    lbl16=Label(table,text='\u251C',font=('Courier New',18))
    lbl16.grid(column=1,row=3)
    lbl17=Label(table,text='\u2500'*16,font=('Courier New',18))
    lbl17.grid(column=2,row=3)
    lbl18=Label(table,text='\u253C',font=('Courier New',18))
    lbl18.grid(column=3,row=3)
    lbl19=Label(table,text='\u2500'*10,font=('Courier New',18))
    lbl19.grid(column=4,row=3)
    lbl20=Label(table,text='\u253C',font=('Courier New',18))
    lbl20.grid(column=5,row=3)
    lbl21=Label(table,text='\u2500'*10,font=('Courier New',18))
    lbl21.grid(column=6,row=3)
    lbl22=Label(table,text='\u253C',font=('Courier New',18))
    lbl22.grid(column=7,row=3)
    lbl23=Label(table,text='\u2500'*10,font=('Courier New',18))
    lbl23.grid(column=8,row=3)
    lbl24=Label(table,text='\u2524',font=('Courier New',18))
    lbl24.grid(column=9,row=3)

    lbl11=Label(table,text='\u2502',font=('Courier New',18))
    lbl11.grid(column=1,row=4)
    lbl12=Label(table,text='\u2502',font=('Courier New',18))
    lbl12.grid(column=3,row=4)
    lbl13=Label(table,text='\u2502',font=('Courier New',18))
    lbl13.grid(column=5,row=4)
    lbl14=Label(table,text='\u2502',font=('Courier New',18))
    lbl14.grid(column=7,row=4)
    lbl15=Label(table,text='\u2502',font=('Courier New',18))
    lbl15.grid(column=9,row=4)

    lbl16=Label(table,text='\u251C',font=('Courier New',18))
    lbl16.grid(column=1,row=5)
    lbl17=Label(table,text='\u2500'*16,font=('Courier New',18))
    lbl17.grid(column=2,row=5)
    lbl18=Label(table,text='\u253C',font=('Courier New',18))
    lbl18.grid(column=3,row=5)
    lbl19=Label(table,text='\u2500'*10,font=('Courier New',18))
    lbl19.grid(column=4,row=5)
    lbl20=Label(table,text='\u253C',font=('Courier New',18))
    lbl20.grid(column=5,row=5)
    lbl21=Label(table,text='\u2500'*10,font=('Courier New',18))
    lbl21.grid(column=6,row=5)
    lbl22=Label(table,text='\u253C',font=('Courier New',18))
    lbl22.grid(column=7,row=5)
    lbl23=Label(table,text='\u2500'*10,font=('Courier New',18))
    lbl23.grid(column=8,row=5)
    lbl24=Label(table,text='\u2524',font=('Courier New',18))
    lbl24.grid(column=9,row=5)

    lbl11=Label(table,text='\u2502',font=('Courier New',18))
    lbl11.grid(column=1,row=6)
    lbl12=Label(table,text='\u2502',font=('Courier New',18))
    lbl12.grid(column=3,row=6)
    lbl13=Label(table,text='\u2502',font=('Courier New',18))
    lbl13.grid(column=5,row=6)
    lbl14=Label(table,text='\u2502',font=('Courier New',18))
    lbl14.grid(column=7,row=6)
    lbl15=Label(table,text='\u2502',font=('Courier New',18))
    lbl15.grid(column=9,row=6)

    lbl16=Label(table,text='\u251C',font=('Courier New',18))
    lbl16.grid(column=1,row=7)
    lbl17=Label(table,text='\u2500'*16,font=('Courier New',18))
    lbl17.grid(column=2,row=7)
    lbl18=Label(table,text='\u253C',font=('Courier New',18))
    lbl18.grid(column=3,row=7)
    lbl19=Label(table,text='\u2500'*10,font=('Courier New',18))
    lbl19.grid(column=4,row=7)
    lbl20=Label(table,text='\u253C',font=('Courier New',18))
    lbl20.grid(column=5,row=7)
    lbl21=Label(table,text='\u2500'*10,font=('Courier New',18))
    lbl21.grid(column=6,row=7)
    lbl22=Label(table,text='\u253C',font=('Courier New',18))
    lbl22.grid(column=7,row=7)
    lbl23=Label(table,text='\u2500'*10,font=('Courier New',18))
    lbl23.grid(column=8,row=7)
    lbl24=Label(table,text='\u2524',font=('Courier New',18))
    lbl24.grid(column=9,row=7)

    lbl11=Label(table,text='\u2502',font=('Courier New',18))
    lbl11.grid(column=1,row=8)
    lbl12=Label(table,text='\u2502',font=('Courier New',18))
    lbl12.grid(column=3,row=8)
    lbl13=Label(table,text='\u2502',font=('Courier New',18))
    lbl13.grid(column=5,row=8)
    lbl14=Label(table,text='\u2502',font=('Courier New',18))
    lbl14.grid(column=7,row=8)
    lbl15=Label(table,text='\u2502',font=('Courier New',18))
    lbl15.grid(column=9,row=8)

    lbl25=Label(table,text='\u2514',font=('Courier New',18))
    lbl25.grid(column=1,row=9)
    lbl26=Label(table,text='\u2500'*16,font=('Courier New',18))
    lbl26.grid(column=2,row=9)
    lbl27=Label(table,text='\u2534',font=('Courier New',18))
    lbl27.grid(column=3,row=9)
    lbl28=Label(table,text='\u2500'*10,font=('Courier New',18))
    lbl28.grid(column=4,row=9)
    lbl29=Label(table,text='\u2534',font=('Courier New',18))
    lbl29.grid(column=5,row=9)
    lbl30=Label(table,text='\u2500'*10,font=('Courier New',18))
    lbl30.grid(column=6,row=9)
    lbl31=Label(table,text='\u2534',font=('Courier New',18))
    lbl31.grid(column=7,row=9)
    lbl32=Label(table,text='\u2500'*10,font=('Courier New',18))
    lbl32.grid(column=8,row=9)
    lbl33=Label(table,text='\u2518',font=('Courier New',18))
    lbl33.grid(column=9,row=9)

    lbl34=Label(table,text='N1',font=('Courier New',18))
    lbl34.grid(column=4,row=2)
    lbl35=Label(table,text='N2',font=('Courier New',18))
    lbl35.grid(column=6,row=2)
    lbl36=Label(table,text='N3',font=('Courier New',18))
    lbl36.grid(column=8,row=2)

    lbl37=Label(table,text='Упорядоченный\nмассив',font=('Courier New',18))
    lbl37.grid(column=2,row=4)
    lbl38=Label(table,text='Случайный\nмассив',font=('Courier New',18))
    lbl38.grid(column=2,row=6)
    lbl39=Label(table,text='Упорядоченный в\nобратном порядке',\
                font=('Courier New',18))
    lbl39.grid(column=2,row=8)

    a = array_filling(n1)
    time = time_measurement(a, len(a))
    
    lbl40=Label(table,text='{:.7f}'.format(time),font=('Courier New',18))
    lbl40.grid(column=4,row=6)

    time = time_measurement(a, len(a))
    
    lbl41=Label(table,text='{:.7f}'.format(time),font=('Courier New',18))
    lbl41.grid(column=4,row=4)

    a.reverse()

    time = time_measurement(a, len(a))
 
    lbl42=Label(table,text='{:.7f}'.format(time),font=('Courier New',18))
    lbl42.grid(column=4,row=8)
    
    a = array_filling(n2)
    time = time_measurement(a, len(a))

    lbl43=Label(table,text='{:.7f}'.format(time),font=('Courier New',18))
    lbl43.grid(column=6,row=6)

    time = time_measurement(a, len(a))
    
    lbl44=Label(table,text='{:.7f}'.format(time),font=('Courier New',18))
    lbl44.grid(column=6,row=4)

    a.reverse()
    time = time_measurement(a, len(a))
    
    lbl45=Label(table,text='{:.7f}'.format(time),font=('Courier New',18))
    lbl45.grid(column=6,row=8)

    a = array_filling(n3)
    time = time_measurement(a, len(a))

    lbl46=Label(table,text='{:.7f}'.format(time),font=('Courier New',18))
    lbl46.grid(column=8,row=6)

    time = time_measurement(a, len(a))
    
    lbl47=Label(table,text='{:.7f}'.format(time),font=('Courier New',18))
    lbl47.grid(column=8,row=4)

    a.reverse()
    time = time_measurement(a, len(a))
    
    lbl48=Label(table,text='{:.7f}'.format(time),font=('Courier New',18))
    lbl48.grid(column=8,row=8)
            
    table.mainloop()
    
def start():
    
    n1 = txt3.get()
    if n1 == '':
        messagebox.showwarning('Ошибка',\
                               'Остались пустые ячейки')
        return
    for i in n1:
        if not ('0' <= i <= '9') or (n1[0] == '0'):
            messagebox.showerror('Ошибка','Недопустимое значение N1')
            return

    n2 = txt4.get()
    if n2 == '':
        messagebox.showwarning('Ошибка',\
                               'Остались пустые ячейки')
        return
    for i in n2:
        if not ('0' <= i <= '9') or (n2[0] == '0'):
            messagebox.showerror('Ошибка','Недопустимое значение N2')
            return

    n3 = txt5.get()
    if n3 == '':
        messagebox.showwarning('Ошибка',\
                               'Остались пустые ячейки')
        return
    for i in n3:
        if not ('0' <= i <= '9') or (n3[0] == '0'):
            messagebox.showerror('Ошибка','Недопустимое значение N3')
            return
        
    left = txt6.get()
    if left == '':
        messagebox.showwarning('Ошибка',\
                               'Остались пустые ячейки')
        return
    for i in left:
        if not ('0' <= i <= '9') or (left[0] == '0'):
            messagebox.showerror('Ошибка',\
                                 'Недопустимое значение левой границы')
            return

    right = txt7.get()
    if right == '':
        messagebox.showwarning('Ошибка',\
                               'Остались пустые ячейки')
        return
    for i in right:
        if not ('0' <= i <= '9') or (right[0] == '0'):
            messagebox.showerror('Ошибка',\
                                 'Недопустимое значение правой границы')
            return

    if int(left)+ 10 > int(right):
        messagebox.showwarning('Ошибка',\
                                'Недопустимое значение левой границы')
        return

    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
    left = int(left)
    right =int(right)

    graph(left,right)
    table(n1,n2,n3)
    
#создание окна
window = Tk()
window.title('Сортировка Шелла')
window.geometry("455x520")

lbl0=Label(window,text='',font=('Courier New',1))
lbl0.grid(column=0,row=0)
lbl01=Label(window,text='     ')
lbl01.grid(column=0,row=1)

lbl1=Label(window,text='Демонстрационный массив',font=('Courier New',18))
lbl1.grid(column=1,row=1)
txt1=Entry(window,width=35,font=('Courier New',18))
txt1.grid(column=1,row=2)
txt1.insert(0,'29 98 16 82 24 66 35 7 75 54')
txt1.focus()

lbl2=Label(window,text='Отсортированный массив',font=('Courier New',18))
lbl2.grid(column=1,row=3)
txt2=Entry(window,width=35,font=('Courier New',18))
txt2.grid(column=1,row=4)

lbl02=Label(window,text='  ',font=('Courier New',1))
lbl02.grid(column=0,row=5)

btn=Button(window,text=' Отсортировать ',font=('Courier New',18),\
            command = sorting)
btn.grid(column=1,row=6)

lbl03=Label(window,text='  ',font=('Courier New',15))
lbl03.grid(column=0,row=7)

lbl3=Label(window,text='Построение таблицы',font=('Courier New',18))
lbl3.grid(column=1,row=8)

lbl4=Label(window,text='  N1 =',font=('Courier New',18))
lbl4.place(x = 0, y = 220)
lbl5=Label(window,text='  N2 =',font=('Courier New',18))
lbl5.place(x = 0, y = 250)
lbl6=Label(window,text='  N3 =',font=('Courier New',18))
lbl6.place(x = 0, y = 280)

txt3=Entry(window,width=10,font=('Courier New',18))
txt3.place(x = 80, y = 220)
txt3.insert(0,1000)
txt4=Entry(window,width=10,font=('Courier New',18))
txt4.place(x = 80, y = 250)
txt4.insert(0,2000)
txt5=Entry(window,width=10,font=('Courier New',18))
txt5.place(x = 80, y = 280)
txt5.insert(0,3000)

lbl04=Label(window,text='  ',font=('Courier New',1))
lbl04.grid(column=0,row=12)

lbl7=Label(window,text='Построение графика',font=('Courier New',18))
lbl7.place(x = 125, y = 330)

lbl8=Label(window,text='  Левая граница ',font=('Courier New',18))
lbl8.place(x = 0, y = 370)
lbl9=Label(window,text='  Правая граница ',font=('Courier New',18))
lbl9.place(x = 0, y = 400)

txt6=Entry(window,width=10,font=('Courier New',18))
txt6.place(x = 185, y = 370)
txt6.insert(0,500)
txt7=Entry(window,width=10,font=('Courier New',18))
txt7.place(x = 185, y = 400)
txt7.insert(0,5500)

btn1=Button(window,text=' Построить \nтаблицу',font=('Courier New',18),\
           bg='dark gray',command = table)
btn1.place(x = 260, y = 240)

btn2=Button(window,text='  Построить \nграфик',font=('Courier New',18),\
           bg='dark gray',command = graph)
btn2.place(x = 160, y = 450)


window.mainloop()





