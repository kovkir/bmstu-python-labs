#Лабороторная работа: Исследование методов сортировки;
#Сортировка Шелла.

from tkinter import Tk, Label, Entry, Button, messagebox
import matplotlib.pyplot as plt
from time import perf_counter
from random import randint
            
def shell_sort(array, size):
    step = size // 2
    
    while step > 0:
        for i in range(step, size):
            j = i - step
            
            while j >= 0 and array[j] > array[j + step]:
                array[j + step], array[j] = array[j], array[j + step]
                j -= step

        step //= 2

def array_filling(n):
    a = []

    for _ in range(n):
        a.append(randint(1, 100))

    return a

def time_measurement(array, size):
    start = perf_counter()
    shell_sort(array, size)
    end = perf_counter()
    time = end - start

    return time
    
def sorting():
    b = outp_arr_txt.get()
    len_b = len(b)
    
    while len_b > 0:
        outp_arr_txt.delete(0)
        len_b -= 1
        
    a = inp_arr_txt.get() + ' '
    
    for i in a:
        if not ('0' <= i <= '9' or i == ' ' or i == '-'):
            messagebox.showerror('Ошибка', 'Недопустимые символы в массиве')
            return

    array = []
    string = ''
    
    for i in a:
        if i != ' ':
            string += i
        else:
            if string != '':
                array.append(int(string))
            string = ''

    if len(array) > 0:
        shell_sort(array, len(array))
        
        for i in range(len(array) - 1, -1, -1):
            outp_arr_txt.insert(0, str(array[i]) + ' ')
    else:
        messagebox.showwarning('Ошибка', 'В массиве нет элементов')

def graph():
    left = left_border.get()

    if left == '':
        messagebox.showwarning('Ошибка', 'Остались пустые ячейки')
        return

    for i in left:
        if not ('0' <= i <= '9') or (left[0] == '0'):
            messagebox.showerror('Ошибка', 'Недопустимое значение левой границы')
            return

    right = right_border.get()

    if right == '':
        messagebox.showwarning('Ошибка', 'Остались пустые ячейки')
        return

    for i in right:
        if not ('0' <= i <= '9') or (right[0] == '0'):
            messagebox.showerror('Ошибка', 'Недопустимое значение правой границы')
            return

    left = int(left)
    right = int(right)

    if left + 10 > right:
        messagebox.showwarning('Ошибка', 'Недопустимое значение левой границы')
        return
    
    plt.title("Сортировка Шеллом")
    plt.xlabel("Кол-во элементов, шт")
    plt.ylabel("Время сортировки, мс")

    x_numb_elem = []
    y_time = []

    a = array_filling(right)
            
    for i in range(left, right, (right - left) // 10):
        b = a[:]
        time = time_measurement(b, i)
        
        x_numb_elem.append(i)
        y_time.append(time * 1000)

    plt.plot(x_numb_elem, y_time, 'r')
    plt.grid(True)
    plt.show()

def table():
    n1 = n1_txt.get()

    if n1 == '':
        messagebox.showwarning('Ошибка', 'Остались пустые ячейки')
        return

    for i in n1:
        if not ('0' <= i <= '9') or (n1[0] == '0'):
            messagebox.showerror('Ошибка', 'Недопустимое значение N1')
            return

    n2 = n2_txt.get()

    if n2 == '':
        messagebox.showwarning('Ошибка', 'Остались пустые ячейки')
        return

    for i in n2:
        if not ('0' <= i <= '9') or (n2[0] == '0'):
            messagebox.showerror('Ошибка','Недопустимое значение N2')
            return

    n3 = n3_txt.get()

    if n3 == '':
        messagebox.showwarning('Ошибка', 'Остались пустые ячейки')
        return

    for i in n3:
        if not ('0' <= i <= '9') or (n3[0] == '0'):
            messagebox.showerror('Ошибка', 'Недопустимое значение N3')
            return
        
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
    
    table = Tk()
    table.title('Сортировка Шелла')
    table.geometry("680x340")
    
    Label(table, text = ' ', font = ('Courier New', 4)).\
        grid(column = 0, row = 0)
    
    Label(table, text = '  ').\
        grid(column = 0, row = 1)
    Label(table, text = '\u250C', font = ('Courier New', 18)).\
        grid(column = 1, row = 1)
    Label(table, text = '\u2500' * 16, font = ('Courier New', 18)).\
        grid(column = 2, row = 1)
    Label(table, text = '\u252C', font = ('Courier New', 18)).\
        grid(column = 3, row = 1)
    Label(table, text = '\u2500' * 10, font = ('Courier New', 18)).\
        grid(column = 4, row = 1)
    Label(table, text = '\u252C', font = ('Courier New', 18)).\
        grid(column = 5, row = 1)
    Label(table, text = '\u2500' * 10, font = ('Courier New', 18)).\
        grid(column = 6, row = 1)
    Label(table, text = '\u252C', font = ('Courier New', 18)).\
        grid(column = 7, row = 1)
    Label(table, text = '\u2500' * 10, font = ('Courier New', 18)).\
        grid(column = 8, row = 1)
    Label(table, text = '\u2510', font = ('Courier New', 18)).\
        grid(column = 9, row = 1)

    for i in range(2, 9, 2):
        if i <= 8:
            Label(table, text = '\u2502', font = ('Courier New', 18)).\
                grid(column = 1, row = i)
            Label(table, text = '\u2502', font = ('Courier New', 18)).\
                grid(column = 3, row = i)
            Label(table, text = '\u2502', font = ('Courier New', 18)).\
                grid(column = 5, row = i)
            Label(table, text = '\u2502', font = ('Courier New', 18)).\
                grid(column = 7, row = i)
            Label(table, text = '\u2502', font = ('Courier New', 18)).\
                grid(column = 9, row = i)

        Label(table, text = '\u251C', font = ('Courier New', 18)).\
            grid(column = 1, row = i + 1)
        Label(table, text = '\u2500' * 16, font = ('Courier New', 18)).\
            grid(column = 2, row = i + 1)
        Label(table, text = '\u253C', font = ('Courier New', 18)).\
            grid(column = 3, row = i + 1)
        Label(table, text = '\u2500' * 10, font = ('Courier New', 18)).\
            grid(column = 4, row = i + 1)
        Label(table, text = '\u253C', font = ('Courier New', 18)).\
            grid(column = 5, row = i + 1)
        Label(table, text = '\u2500' * 10, font = ('Courier New', 18)).\
            grid(column = 6, row = i + 1)
        Label(table, text = '\u253C', font = ('Courier New', 18)).\
            grid(column = 7, row = i + 1)
        Label(table, text = '\u2500' * 10, font = ('Courier New', 18)).\
            grid(column = 8, row = i + 1)
        Label(table, text = '\u2524', font = ('Courier New', 18)).\
            grid(column = 9, row = i + 1)

    Label(table, text = '\u2514', font = ('Courier New', 18)).\
        grid(column = 1, row = 9)
    Label(table, text = '\u2500' * 16, font = ('Courier New', 18)).\
        grid(column = 2, row = 9)
    Label(table, text = '\u2534', font = ('Courier New', 18)).\
        grid(column = 3, row = 9)
    Label(table, text = '\u2500' * 10, font = ('Courier New', 18)).\
        grid(column = 4, row = 9)
    Label(table, text = '\u2534', font = ('Courier New', 18)).\
        grid(column = 5, row = 9)
    Label(table, text = '\u2500' * 10, font = ('Courier New', 18)).\
        grid(column = 6, row = 9)
    Label(table, text = '\u2534', font = ('Courier New', 18)).\
        grid(column = 7, row = 9)
    Label(table, text = '\u2500' * 10, font = ('Courier New', 18)).\
        grid(column = 8, row = 9)
    Label(table, text = '\u2518', font = ('Courier New', 18)).\
        grid(column = 9, row = 9)

    Label(table, text = 'N1', font = ('Courier New', 18)).\
        grid(column = 4, row = 2)
    Label(table, text = 'N2', font = ('Courier New', 18)).\
        grid(column = 6, row = 2)
    Label(table, text = 'N3', font = ('Courier New', 18))\
        .grid(column = 8, row = 2)

    Label(table, text = 'Упорядоченный\nмассив', font = ('Courier New', 18)).\
        grid(column = 2, row = 4)
    Label(table, text = 'Случайный\nмассив', font = ('Courier New', 18)).\
        grid(column = 2, row = 6)
    Label(table, text = 'Упорядоченный в\nобратном порядке', font = ('Courier New', 18)).\
        grid(column = 2, row = 8)

    a = array_filling(n1)
    time = time_measurement(a, len(a))
    
    Label(table, text = '{:.7f}'.format(time), font = ('Courier New', 18)).\
        grid(column = 4, row = 6)

    time = time_measurement(a, len(a))
    
    Label(table, text = '{:.7f}'.format(time), font = ('Courier New', 18)).\
        grid(column = 4, row = 4)

    a.reverse()
    time = time_measurement(a, len(a))
 
    Label(table, text = '{:.7f}'.format(time), font = ('Courier New', 18)).\
        grid(column = 4, row = 8)
    
    a = array_filling(n2)
    time = time_measurement(a, len(a))

    Label(table, text = '{:.7f}'.format(time), font = ('Courier New', 18)).\
        grid(column = 6, row = 6)

    time = time_measurement(a, len(a))
    
    Label(table, text = '{:.7f}'.format(time), font = ('Courier New', 18)).\
        grid(column = 6, row = 4)

    a.reverse()
    time = time_measurement(a, len(a))
    
    Label(table, text = '{:.7f}'.format(time), font = ('Courier New', 18)).\
        grid(column = 6, row = 8)

    a = array_filling(n3)
    time = time_measurement(a, len(a))

    Label(table, text = '{:.7f}'.format(time), font = ('Courier New', 18)).\
        grid(column = 8, row = 6)

    time = time_measurement(a, len(a))
    
    Label(table, text = '{:.7f}'.format(time), font = ('Courier New', 18)).\
        grid(column = 8, row = 4)

    a.reverse()
    time = time_measurement(a, len(a))
    
    Label(table, text = '{:.7f}'.format(time), font = ('Courier New', 18)).\
        grid(column = 8, row = 8)
            
    table.mainloop()
    
#создание окна
window = Tk()
window.title('Сортировка Шелла')
window.geometry("455x520")

Label(window, text = '', font = ('Courier New', 1)).grid(column = 0, row = 0)
Label(window, text = '     ').grid(column = 0, row = 1)
Label(window, text = 'Демонстрационный массив', font = ('Courier New', 18)).\
    grid(column = 1, row = 1)

inp_arr_txt = Entry(window, width = 35, font = ('Courier New', 18))
inp_arr_txt.grid(column = 1, row = 2)
inp_arr_txt.insert(0, '29 98 16 82 24 66 35 7 75 54')
inp_arr_txt.focus()

Label(window, text = 'Отсортированный массив', font = ('Courier New', 18)).\
    grid(column = 1, row = 3)

outp_arr_txt = Entry(window, width = 35, font = ('Courier New', 18))
outp_arr_txt.grid(column = 1, row = 4)

Label(window, text = '', font = ('Courier New', 2)).grid(column = 0, row = 5)
Button(window, text = ' Отсортировать ', font = ('Courier New', 18), command = sorting).\
    grid(column = 1, row = 6)

Label(window, text = '', font = ('Courier New', 15)).grid(column = 0, row = 7)
Label(window, text = 'Построение таблицы', font = ('Courier New', 18)).\
    grid(column = 1, row = 8)

Label(window, text = '  N1 =', font = ('Courier New', 18)).\
    place(x = 0, y = 220)
Label(window, text = '  N2 =', font = ('Courier New', 18)).\
    place(x = 0, y = 250)
Label(window, text = '  N3 =', font = ('Courier New', 18)).\
    place(x = 0, y = 280)

n1_txt = Entry(window,width = 10, font = ('Courier New', 18))
n1_txt.place(x = 80, y = 220)
n1_txt.insert(0, 1000)

n2_txt = Entry(window, width = 10, font = ('Courier New', 18))
n2_txt.place(x = 80, y = 250)
n2_txt.insert(0, 2000)

n3_txt = Entry(window, width = 10, font = ('Courier New', 18))
n3_txt.place(x = 80, y = 280)
n3_txt.insert(0, 3000)

Label(window, text = 'Построение графика', font = ('Courier New', 18)).\
    place(x = 125, y = 330)
Label(window,text='  Левая граница ',font=('Courier New', 18)).\
    place(x = 0, y = 370)
Label(window,text='  Правая граница ',font=('Courier New', 18)).\
    place(x = 0, y = 400)

left_border = Entry(window, width = 10, font = ('Courier New', 18))
left_border.place(x = 185, y = 370)
left_border.insert(0, 500)

right_border = Entry(window, width = 10, font = ('Courier New', 18))
right_border.place(x = 185, y = 400)
right_border.insert(0, 5500)

Button(window, text = ' Построить \nтаблицу', font =('Courier New', 18),
    bg = 'dark gray', command = table).place(x = 260, y = 240)

Button(window, text = '  Построить \nграфик', font = ('Courier New', 18),
    bg = 'dark gray', command = graph).place(x = 160, y = 450)

window.mainloop()
