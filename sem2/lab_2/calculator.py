#Лабороторная работа: Калькулятор;

from tkinter import Menu, Tk, Label, Button, Entry, messagebox

def clicked_7():
    a = input_txt.get()
    input_txt.insert(len(a), 7)

    global last
    last = 7

def clicked_8():
    a = input_txt.get()
    input_txt.insert(len(a), 8)

    global last
    last = 8
    
def clicked_9():
    a = input_txt.get()
    input_txt.insert(len(a), 9)

    global last
    last = 9
    
def clicked_4():
    a = input_txt.get()
    input_txt.insert(len(a), 4)

    global last
    last = 4

def clicked_5():
    a = input_txt.get()
    input_txt.insert(len(a), 5)

    global last
    last = 5
    
def clicked_6():
    a = input_txt.get()
    input_txt.insert(len(a), 6)

    global last
    last = 6

def clicked_1():
    a = input_txt.get()
    input_txt.insert(len(a), 1)

    global last
    last = 1

def clicked_2():
    a = input_txt.get()
    input_txt.insert(len(a), 2)

    global last
    last = 2
    
def clicked_3():
    a = input_txt.get()
    input_txt.insert(len(a), 3)

    global last
    last = 3

def clicked_0():
    a = input_txt.get()
    input_txt.insert(len(a), 0)

    global last
    last = 0
    
def clicked_p():
    a = input_txt.get()
    input_txt.insert(len(a), '.')

    global last
    last = 'p'

def Information():
    messagebox.showinfo('Information','Данная программа выполняет \
перевод чисел в двочиную систему счисления и обратно.\n\n\
Ковалец К. ИУ7-23Б')

    global last
    last = 'i'
    
def clicked_in_2():
    global last
    last = 'in_2'

    b = output_txt.get()
    len_b = len(b)

    while len_b >= 1:
        output_txt.delete(0)
        len_b -= 1

    minus = 0

    try:
        a = float(input_txt.get())

        if a < 0:
            minus = 1
            a *= (-1) 
    except:
        messagebox.showerror('Ошибка', 'Ожидался ввод вещественного числа!')
        return

    c = int(a)
    d = str(a)[len(str(a)) - (len(str(a)) - len(str(c)) - 1) -2:]
    d = '0' + d[1:]
    result = ''

    while c > 0:
        result += str(c % 2)
        c //= 2

    result = result[::-1]
    result += '.'
    l = 6

    while l > 0:
        d = str(float(d) * 2)
        result += d[0]
        d = '0' + d[1:]
        l -= 1

    while result[-1] == '0':
        result = result[:-1]

    if result[-1] == '.':
        result = result[:-1]

    output_txt.insert(0, result)

    if minus == 1:
        output_txt.insert(0,'-')
    
def clicked_in_10():
    global last
    last = 'in_10'

    b = output_txt.get()
    len_b = len(b)

    while len_b >= 1:
        output_txt.delete(0)
        len_b -= 1

    minus = 0
    
    try:
        a = float(input_txt.get())

        if a < 0:
            minus = 1
            a *= (-1)
    except:
        messagebox.showerror('Ошибка', 'Ожидался ввод вещественного числа!')
        return

    for i in str(a):
        if i > '1':
            messagebox.showerror('Ошибка', 'Ожидался ввод двоичного числа!')
            return

    c = int(a)
    d = str(a)[len(str(a)) - len(str(a)) - len(str(c)) - 1:]

    power = 0
    result = 0
    remains = 0

    while c > 0:
        remains = c % 10
        c //= 10
        result += remains * pow(2, power)
        power += 1

    if d != '0':
        power =- 1

        while len(d) > 0:
            result += int(d[0]) * pow(2, power)
            d = d[1:]
            power -= 1

    output_txt.insert(0, result)

    if minus == 1:
        output_txt.insert(0, '-')
        
def clicked_C():
    global last
    last = 'C'

    a = input_txt.get()
    len_a = len(a)

    while len_a >= 1:
        input_txt.delete(0)
        len_a -= 1

    b = output_txt.get()
    len_b = len(b)

    while len_b >= 1:
        output_txt.delete(0)
        len_b -= 1

def clicked_C1():
    global last
    last = 'C1'

    a = input_txt.get()
    input_txt.delete(len(a) - 1)

def replay():
    if last == 'C':
        clicked_C()
    elif last == 'C1':
        clicked_C1()
    elif last == 'in_10':
        clicked_in_10()
    elif last == 'in_2':
        clicked_in_2()
    elif last == 'i':
        Information()
    elif last == 'p':
        clicked_p()
    elif last == 0:
        clicked_0()
    elif last == 1:
        clicked_1()
    elif last == 2:
        clicked_2()
    elif last == 3:
        clicked_3()
    elif last == 4:
        clicked_4()
    elif last == 5:
        clicked_5()
    elif last == 6:
        clicked_6()
    elif last == 7:
        clicked_7()
    elif last == 8:
        clicked_8()
    elif last == 9:
        clicked_9() 

last = 'C'

#создание окна
window = Tk()
window['bg'] = 'light gray'
window.title('Калькулятор')
window.geometry("555x390")

Label(window,text = '', width = 1, bg = 'light gray').grid(column = 0, row = 0)
Label(window,text = '', width = 1, bg = 'light gray').grid(column = 1, row = 0)
Label(window,text = '', width = 1, bg = 'light gray').grid(column = 2, row = 0)
Label(window,text = '', width = 1, bg = 'light gray').grid(column = 3, row = 0)
Label(window,text = '', width = 1, bg = 'light gray').grid(column = 4, row = 0)
Label(window,text = '', width = 1, bg = 'light gray').grid(column = 5, row = 0)
Label(window,text = '', width = 1, bg = 'light gray').grid(column = 6, row = 0)
Label(window,text = '', width = 1, bg = 'light gray').grid(column = 7, row = 0)

Label(window, width = 18, text = 'input window', bg = 'light gray',
    font = ('Courier New', 18)).grid(column = 1, row = 1, columnspan = 5)

input_txt = Entry(window, width = 18, font = ('Courier New', 18))
input_txt.grid(column = 1, row = 2, columnspan = 5)
input_txt.focus()

Label(window, width = 18, text = 'output window', bg = 'light gray',
    font = ('Courier New',18)).grid(column = 7,row = 1)

output_txt = Entry(window, width = 18, font = ('Courier New', 18))
output_txt.grid(column = 7, row = 2, columnspan = 2)

Label(window, text = '', bg = 'light gray').\
    grid(column = 0,row = 3, columnspan = 8)

Button(window, text = '  7  ', font = ('Courier New', 14),
    command = clicked_7).grid(column = 1, row = 4)

Button(window, text = '  8  ', font = ('Courier New', 14), 
    command = clicked_8).grid(column = 3, row = 4)

Button(window, text = '  9  ', font = ('Courier New', 14),
    command = clicked_9).grid(column = 5, row = 4)

Label(window, text = '', bg = 'light gray').\
    grid(column = 0, row = 5, columnspan = 8)

Button(window, text = '  4  ', font = ('Courier New', 14),
    command = clicked_4).grid(column = 1, row = 6)

Button(window, text = '  5  ',font = ('Courier New', 14),
    command = clicked_5).grid(column = 3, row = 6)

Button(window, text = '  6  ', font = ('Courier New', 14),
    command = clicked_6).grid(column = 5, row = 6)

Label(window, text = '', bg = 'light gray').\
    grid(column = 0, row = 7, columnspan = 8)

Button(window, text = '  1  ', font = ('Courier New', 14),
    command = clicked_1).grid(column = 1, row = 8)

Button(window, text = '  2  ', font = ('Courier New', 14),
    command = clicked_2).grid(column = 3, row = 8)

Button(window, text = '  3  ', font = ('Courier New', 14),
    command = clicked_3).grid(column = 5, row = 8)

Label(window, text = '', bg = 'light gray').\
    grid(column = 0, row = 9, columnspan = 8)

Button(window, text = '  0  ', font = ('Courier New', 14),
    command = clicked_0).grid(column = 1, row = 10)

Button(window, text = '  .  ', font = ('Courier New', 14),
    command=clicked_p).grid(column = 3, row = 10)

Button(window, text = '  <  ', font = ('Courier New', 14),
    command = clicked_C1).grid(column = 5, row = 10)

Label(window, text = '', bg = 'light gray').\
    grid(column = 0, row = 11, columnspan = 8)

Button(window, text = '  C  ', font = ('Courier New', 14),
    command = clicked_C).grid(column = 1, row = 12)

Label(window, text = '', bg = 'light gray').\
    grid(column = 0, row = 13, columnspan = 8)

Button(window, width = 18, text = 'Перевод\n из 2-ой в 10-ую ',
    font = ('Courier New', 14), command = clicked_in_10).\
    grid(column = 7, row = 6, rowspan = 3)

Button(window, width = 18, text = 'Перевод\n из 10-ой в 2-ую ',
    font = ('Courier New', 14), command = clicked_in_2).\
    grid(column = 7, row = 9, rowspan = 2)

Button(window, width = 18, text = 'повтор действия',
    font = ('Courier New', 14), command = replay).\
    grid(column = 7, row = 4)

menu = Menu(window)
window.config(menu = menu)
menu.add_command(label = 'Информация', command = Information)

window.mainloop()
