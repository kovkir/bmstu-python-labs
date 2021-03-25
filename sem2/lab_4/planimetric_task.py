#На плоскости заданы множество точек А и множество треугольников.
#Найти две такие точки из А, что проходящая через них прямая пересекается
#с максимальным количеством треугольников из В.
#Дать графическое изображение результатов.

from math import *
from tkinter import *
from tkinter import messagebox

def triangle_check(triangle):
    x1 = triangle[0]
    y1 = triangle[1]
    x2 = triangle[2]
    y2 = triangle[3]
    x3 = triangle[4]
    y3 = triangle[5]
    
    AB = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    BC = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    AC = sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
    
    if AC < AB + BC and BC < AB + AC and AB < BC + AC:
        return 1
    else:
        return 0
           
def delete():
    return 0

def clear_canvas():
    point_coordinates.clear()
    coordinates_of_triangles.clear()
    triangle.clear()
    canvas.delete("all")

def clear_fields():
    a=point_txt.get()
    a1=len(a)
    
    while a1>=1:
        point_txt.delete(a1-1)
        a1-=1
        
    b=triangle_txt.get()
    b1=len(b)
    
    while b1>=1:
        triangle_txt.delete(b1-1)
        b1-=1

def build_point():
    a = point_txt.get()
    array = a.split()
    
    for i in range(len(array)):
        try:
            array[i] = int(array[i])
        except:
            messagebox.showwarning('Ошибка',
            'Неверно введены координаты точки!')
            return;
        
    if len(array)!=2:
        messagebox.showerror('Ошибка',
            'У точки должно быть две координаты!')
        return;

    if point_coordinates.count(array) == 0:
        point_coordinates.append(array)
        r = 3.5
        canvas.create_oval(array[0]-r, array[1]-r, array[0]+r, array[1]+r,
                       width=1, outline='red',fill = 'red')
    
def build_a_triangle():
    a = triangle_txt.get()
    array = a.split()
    
    for i in range(len(array)):
        try:
            array[i] = int(array[i])
        except:
            messagebox.showwarning('Ошибка',
            'Неверно введены координаты треугольника!')
            return;
        
    if len(array)!=6:
        messagebox.showwarning('Ошибка',
            'У треугольника должно быть шесть координат!')
        return;

    r = 3.5

    for i in range(0,6,2):
        canvas.create_oval(array[i]-r, array[i+1]-r, array[i]+r, array[i+1]+r,
                       width=1, outline='green',fill = 'green')
    
    if triangle_check(array) == 1:
        
        if  coordinates_of_triangles.count(array) == 0:

            for i in range(0,6,2):
                canvas.create_oval(array[i]-r, array[i+1]-r, array[i]+r,
                        array[i+1]+r, width=1, outline='green',fill = 'green')
                
            coordinates_of_triangles.append(array[:])
            array.append(array[0])
            array.append(array[1])
            canvas.create_line(array, width=3, fill = 'green')

    else:
        messagebox.showwarning('Ошибка',
                             'Треугольника с такими сторонами не существует')
    
def click1(event):
    x = event.x
    y = event.y

    if point_coordinates.count([x,y]) == 0:
        point_coordinates.append([x,y])
        r = 3.5
        canvas.create_oval(x-r, y-r, x+r, y+r, width=1, outline='red',
                           fill = 'red')

def click2(event):
    x = event.x
    y = event.y
    
    triangle.append(x)
    triangle.append(y)

    r = 3.5
    canvas.create_oval(x-r, y-r, x+r, y+r, width=1, outline='green',
                       fill = 'green')
    
    if len(triangle) == 6 and triangle_check(triangle) == 1:
        
        if  coordinates_of_triangles.count(triangle) == 0:
            
            coordinates_of_triangles.append(triangle[:])
            triangle.append(triangle[0])
            triangle.append(triangle[1])
            canvas.create_line(triangle, width=3, fill = 'green')
            
        triangle.clear()
        
    elif len(triangle) == 6:
        messagebox.showwarning('Ошибка',
                             'Треугольника с такими сторонами не существует')
        triangle.clear()

def build_a_line():
    n_max = 0
    
    for i in range(len(point_coordinates) - 1):
        
        x1 = point_coordinates[i][0]
        y1 = point_coordinates[i][1]

        for j in range(i + 1,len(point_coordinates)):
            n = 0;
            
            x2 = point_coordinates[j][0]
            y2 = point_coordinates[j][1]

            a1 = x2 - x1
            b1 = y2 - y1

            for y in range(len(coordinates_of_triangles)):

                x3 = coordinates_of_triangles[y][0]
                y3 = coordinates_of_triangles[y][1]
                x4 = coordinates_of_triangles[y][2]
                y4 = coordinates_of_triangles[y][3]
                x5 = coordinates_of_triangles[y][4]
                y5 = coordinates_of_triangles[y][5]

                a2 = x3 - x1
                b2 = y3 - y1
                a3 = x4 - x1
                b3 = y4 - y1
                a4 = x5 - x1
                b4 = y5 - y1

                p1 = a1*b2 - a2*b1
                p2 = a1*b3 - a3*b1
                p3 = a1*b4 - a4*b1
                
                if not ((p1 < 0 and p2 < 0 and p3 < 0) or
                    (p1 > 0 and p2 > 0 and p3 > 0)):
                    n += 1

            if n > n_max:
            
                x1_max = x1
                y1_max = y1
                x2_max = x2
                y2_max = y2
                n_max = n
    
    if n_max != 0:
        
        if (x1_max != x2_max):
            y01 = x1_max * (y1_max - y2_max) / (x2_max - x1_max) + y1_max
            y02 = (x1_max - 800) * (y1_max - y2_max) / (x2_max - x1_max) + y1_max
        
            canvas.create_line(0, y01, 800, y02,
                           width=3, fill = 'yellow')
        else:
            canvas.create_line(x1_max, 0, x2_max, 600,
                           width=3, fill = 'yellow')
        r = 3.5
        canvas.create_oval(x1_max - r, y1_max - r, x1_max + r,
        y1_max + r, width=1, outline='blue', fill = 'blue')
        canvas.create_oval(x2_max - r, y2_max - r, x2_max + r,
        y2_max + r, width=1, outline='blue', fill = 'blue')
    else:
        messagebox.showwarning('Ошибка',
                            'Пересечений с треугольниками не найдено :(')

    
window = Tk()
window.title('Решение планиметрических задач')
window.geometry("800x600")
window.resizable(False, False)

canvas = Canvas(window, width=800, height=500, bg = "lightgray")
canvas.place(x = 0, y = 175)

point_coordinates = []
coordinates_of_triangles = []
triangle = []

canvas.bind('<1>', click1)
canvas.bind('<2>', click2)

point_lbl = Label(window, text = 'Координаты точки',
                   font=('Courier New',18)).place(x = 10, y = 10)
triangle_lbl = Label(window, text = 'Координаты треугольника',
                     font=('Courier New',18)).place(x = 10, y = 50)

point_txt = Entry(window, font=('Courier New', 18))
point_txt.place(width=490, x = 290, y = 10)
triangle_txt = Entry(window, font=('Courier New', 18))
triangle_txt.place(width=490, x = 290, y = 50)

point_txt.insert(0,'50 40')
triangle_txt.insert(0,'60 30 190 200 150 60')

clear_canvas = Button(text = 'Отчистить полотно', font=('Courier New',18),
                command = clear_canvas).place(width=200,height=40,x=330,y=130)
clear_fields = Button(text = 'Отчистить поля', font = ('Courier New', 18),
                command = clear_fields).place(width=200,height=40,x=330,y=88)

build_point = Button(text = 'Построить\nточку', font = ('Courier New',18),
                command = build_point).place( width=140,height=60,x=10,y=100)
build_a_triangle = Button(text = 'Построить\nтреугольник',
        font = ('Courier New',18), command = build_a_triangle).place(width=140,
                                                    height=60, x=170, y=100)
build_a_line = Button(text = 'Построить прямую\nчерез искомые точки',
        font = ('Courier New',18), command = build_a_line).place(width=230,
                                                    height=60, x=550, y=100)

window.mainloop()
