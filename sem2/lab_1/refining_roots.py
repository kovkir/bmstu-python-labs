#Лабороторная работа: Уточнение корней;

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize
from time import perf_counter
from tkinter import Tk, ttk, Label, Button, Entry, messagebox, NO, CENTER

#уточнение корней методом Brentq
def Brentq(a, b, tree):
    start2 = perf_counter()
    xa = a
    fa = f(xa)
    xc = b
    fc = f(xc)

    if fa < fc:
        x_root = xa
        x1 = xc
    else:
        x_root = xc
        x1 = xa

    d = abs(x1 - x_root)
    numb_iter = 1
    
    while d >= EPS and abs(f(x1)) >= EPS: 
        # деление отрез к а пополам
        xb = (xa + xc) / 2
        fb = f(xb)
        # обратная квадратичная интерполяция
        if fb != 0 and fa != 0 and fc != 0:
            R = fb / fc
            S = fb / fa
            T = fa / fc

            P = S * (T * (R - T) * (xc - xb) - (1 - R) * (xb - xa))
            Q = (T - 1) * (R - 1) * (S - 1)

            xd = xb + P / Q
            fd = f(xd)
        else:
            if fc!=0:
                break

        numb_iter += 1
        
        #метод секущих
        if numb_iter != 2:
            xs = x_root - f(x_root) * (x_root - x1) / (f(x_root) - f(x1))
            fs = f(xs)
        else:
            xs = xb
            fs = xb
            
        if xa <= xd and xd <= xc and \
            abs(fd) < abs(fb) and abs(fd) < abs(fs):
        #лучше использовать обратную квадратичную интерполяцию
            x_root = x1
            x1 = xd

            if fa * fd > 0:
                d = abs(x1 - x_root)

                xa = xd
                fa = fd
            else:
                d = abs(x1 - x_root) 

                xc = xd
                fc = fd
                
        elif xa <= xs and xs <= xc and \
            abs(fs) < abs(fb) and abs(fs) < abs(fd):
        #лучше использовать метод секущих
            x_root = x1
            x1 = xs

            if fa * fs > 0:
                d = abs(x1 - x_root)

                xa = xs
                fa = fs
            else:
                d = abs(x1 - x_root)

                xc = xs
                fc = fs
                
        else:
        #лучше использовать деление отрезка пополам
            x_root = x1
            x1 = xb

            if fa * fb > 0:
                d = abs(x1 - x_root) 

                xa = xb
                fa = fb
            else:
                d = abs(x1 - x_root) 

                xc = xb
                fc = fb
                
    if abs(fa) < abs(fc):
            x2 = xa
            y2 = fa
    else:
            x2 = xc
            y2 = fc

    stop2 = perf_counter()
    error = 0

    if numb_iter > max_iter:
        error = 1

        tree.insert('', 'end', text = '', 
            values = ('Брент', '{:.2f}'.format(a), '{:.2f}'.format(b),\
                       '', '', '', '', ' ' * 9 + str(error)))
        tree.insert('', 'end', text = '')

    else:
        tree.insert('', 'end', text = '', 
            values = ('Брент', '{:.2f}'.format(a), '{:.2f}'.format(b),\
                      '{:^25.9g}'.format(x2), '{:^20.1e}'.format(y2),\
                      ' ' * 9 + str(numb_iter) , '{:^20.1e}'.format(stop2 - start2),\
                      ' ' * 9 + str(error)))
 
def f(x):
    return(np.sin(x) + 0.5)

def f2(x):
    return((np.sin(x)) * (-1))

def clicked():
    try:
        beg = float(beg_txt.get())
        end = float(end_txt.get())
        step = float(step_txt.get())  
    except:
        messagebox.showerror('Ошибка', 'Ожидался ввод вещественных чисел!')
        return

    #построение графика функции
    x = np.linspace(beg, end, 1000)

    plt.plot(x, f(x), label = 'sin(x) + 0.5')
    plt.plot([beg, end], [0, 0], color = 'y', label = 'Ox')

    plt.title('Graph')
    plt.legend(loc = 1)
    plt.xlabel('$x$')
    plt.ylabel('$f(x)$')
    plt.grid(True)

    a = beg
    b = a + step
    numb = 0
    x1 = (a + b) / 2

    while a <= end:
        error = 0

        if b > end:
            b = end

        if f(a) * f(b) <= 0 and f(a) != f(x1):
            if numb == 0:

                #построение таблицы
                window2 = Tk()
                window2.title('Уточнение корней')
                
                tree = ttk.Treeview(window2, height = 20)
                tree.tag_configure('ttk', background = 'light gray')
                
                tree['columns'] = ('one','two','three','four','five','six',\
                                   'seven','eight')
                tree.column('#0', width = 70, minwidth = 70, stretch = NO)
                tree.column('one', width = 70, minwidth = 75, stretch = NO)
                tree.column('two', width = 50, minwidth = 50,stretch = NO)
                tree.column('three', width = 50, minwidth = 50, stretch = NO)
                tree.column('four', width = 120, minwidth = 120, stretch = NO)
                tree.column('five', width = 100, minwidth = 100, stretch = NO)
                tree.column('six', width = 80, minwidth = 80, stretch = NO)
                tree.column('seven', width = 100, minwidth = 100, stretch = NO)
                tree.column('eight', width = 80, minwidth = 80, stretch = NO)

                tree.heading('#0', text = '№ корня', anchor = CENTER)
                tree.heading('one', text = 'метод', anchor = CENTER)
                tree.heading('two', text = 'A', anchor = CENTER)
                tree.heading('three', text = 'B', anchor = CENTER)
                tree.heading('four', text = 'Значение X', anchor = CENTER)
                tree.heading('five', text = 'F(X)', anchor = CENTER)
                tree.heading('six', text = 'Итераций', anchor = CENTER)
                tree.heading('seven', text = 'Время раб.', anchor = CENTER)
                tree.heading('eight', text = 'Код ошибки', anchor = CENTER)

            numb += 1
      
            try:
                start = perf_counter()
                x1, x3 = optimize.brentq(f, a, b, 
                    xtol = EPS , maxiter = max_iter, full_output = True)
                stop = perf_counter()

                tree.insert('','end', text = '   ' + str(numb), 
                            tags = ('ttk'), values = ('brentq',
                            '{:.2f}'.format(a), '{:.2f}'.format(b),
                            '{:^25.9g}'.format(x1), '{:^20.1e}'.format(f(x1)),
                            ' ' * 9 + str(x3.iterations),
                            '{:^20.1e}'.format(stop - start), ' ' * 9 + str(error)))
                
                x_root = optimize.brentq(f, a, b)
                #x_root - точное значение корня

                if numb == 1:
                    plt.plot(x_root, 0, 'ro', label = 'Roots')
                    plt.legend(loc = 1)
                else:
                    plt.plot(x_root, 0, 'ro')
                    
            except RuntimeError:
                error = 1
                tree.insert('', 'end', text = '   ' + str(numb), 
                            tags = ('ttk'), values = ('brentq', 
                            '{:.2f}'.format(a), '{:.2f}'.format(b),
                            '', '', '', '', ' ' * 9 + str(error)))

            Brentq(a, b, tree)
            
        a += step
        b += step

    a = beg
    b = a + step
    x_infl = (a + b) / 2
    numb2 = 0
    
    while a <= end:
        if b > end:
            b = end

        if f2(a) * f2(b) <= 0 and f2(a) != f(x_infl):
            numb2 += 1
            x_infl = optimize.brentq(f2, a, b)
            #x_infl - точка перегиба

            if numb2 == 1:
                plt.plot(x_infl, f(x_infl), 'gp', label = 'Inflection points')
                plt.legend(loc = 1)
            else:
                plt.plot(x_infl, f(x_infl), 'gp')

        a += step
        b += step
    
    if numb != 0:
        tree.pack()
        plt.show()
        window2.mainloop() 
    else:
        window2 = Tk()
        window2.title('Уточнение корней')
        window2.geometry('320x50')

        Label(window2, text = 'На данном участке корней нет',
            font = ('Courier New', 14)).grid(column = 0, row = 1)

        plt.legend(loc = 1)
        plt.show()
        window2.mainloop()

EPS = 1e-6
max_iter = 100

#создание окна
window = Tk()
window.title('Уточнение корней')
window.geometry("500x330")

Label(window, text = '').\
    grid(column = 0, row = 0, columnspan = 2)

Label(window, text = 'Начало интервала', font = ('Courier New', 14)).\
    grid(column = 0, row = 1)

beg_txt = Entry(window, width = 15, font = ('Courier New', 14))
beg_txt.grid(column = 1, row = 1)
beg_txt.insert(0, '-10')
beg_txt.focus()

Label(window, text = 'Конец интервала ', font = ('Courier New', 14)).\
    grid(column = 0, row = 2)

end_txt = Entry(window, width = 15, font = ('Courier New', 14))
end_txt.grid(column = 1, row = 2)
end_txt.insert(0, '10')

Label(window, text = 'Шаг разбиения   ', font = ('Courier New', 14)).\
    grid(column = 0, row = 3)

step_txt = Entry(window, width = 15, font = ('Courier New', 14))
step_txt.grid(column = 1, row = 3)
step_txt.insert(0, '1')

Label(window, text = '\nТочность = ' + '{:.0e}'.format(EPS ) +
      ' ' * 24 + '\n' + 'Максимальное кол-во итераций = ' + 
      str(max_iter) + ' ' * 6, font = ('Courier New', 14)).\
      grid(column = 0, row = 4, columnspan = 2)

Label(window, text = '\nВиды ошибок:' + ' ' * 28 +
      '\n0. Нет ошибок' + ' ' * 23 + 
      '\n Превышено максимальное число итераций\n',
      font = ('Courier New',14)).\
      grid(column = 0, row = 5, columnspan = 2)
                         
Button(window, text = '   Найти корни   ',font = ('Courier New', 14),
       bg = 'dark gray', fg = 'white', command = clicked).\
       grid(column = 0, row = 6, columnspan = 2)

window.mainloop()
