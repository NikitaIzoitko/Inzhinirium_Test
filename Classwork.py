'''
from tkinter import *
from tkinter import messagebox

def fc1():
    messagebox.showinfo('Вы получили', str(int(a1.get())+int(a2.get())))

def fc2():
    messagebox.showinfo('Вы получили', str(int(a1.get())-int(a2.get())))

def fc3():
    messagebox.showinfo('Вы получили', str(int(a1.get())*int(a2.get())))

def fc4():
    messagebox.showinfo('Вы получили', str(int(a1.get())/int(a2.get())))

def fc5():
    messagebox.showinfo('Вы получили', str(int(a1.get())//int(a2.get())))

def fc6():
    messagebox.showinfo('Вы получили', str(int(a1.get())%int(a2.get())))


root = Tk()
root.title('Calculator')
root.geometry('200x150')
a1 = Entry(root, width=30)
a2 = Entry(root, width=30)
b1 = Button(root, text='+', width=7, height=2, command=fc1)
b2 = Button(root, text='-', width=7, height=2, command=fc2)
b3 = Button(root, text='*', width=7, height=2, command=fc3)
b4 = Button(root, text='/', width=7, height=2, command=fc4)
b5 = Button(root, text='//', width=7, height=2, command=fc5)
b6 = Button(root, text='%', width=7, height=2, command=fc6)
a1.pack()
a2.pack()
b1.place(x=10, y=50)
b2.place(x=70, y=50)
b3.place(x=130, y=50)
b4.place(x=10, y=100)
b5.place(x=70, y=100)
b6.place(x=130, y=100)
root.resizable(False, False)
root.mainloop()
'''
##############################################################
'''
from tkinter import *
def body():
    canvas.itemconfig(s1, fill='black')
    
def body1():
    canvas.itemconfig(s1, fill='red')
    
def color():
    canvas.config(canvas, bg="white")
    
def color1():
    canvas.config(canvas, bg="red")
    

root = Tk()
root.title('Spider')
root.geometry('300x470')
img = PhotoImage(file='C:\\Users\\izoit\\Videos\\Captures\\pig.png')
root.iconphoto(False, img)

canvas = Canvas(root, width=300, height=300)
canvas.pack()
s1 = canvas.create_rectangle(110, 110, 190, 190, width=1.5, fill='black')
canvas.create_line(15, 15, 110, 110, width=1.5)
canvas.create_line(15, 150, 110, 150, width=1.5)
canvas.create_line(15, 285, 110, 190, width=1.5)
canvas.create_line(285, 15, 190, 110, width=1.5)
canvas.create_line(285, 150, 190, 150, width=1.5)
canvas.create_line(285, 285, 190, 190, width=1.5)
b1 = Button(root, text='Body', width=20, height=5, command=body)
b2 = Button(root, text='Body1', width=20, height=5, command=body1)
b3 = Button(root, text='Color', width=20, height=5, command=color)
b4 = Button(root, text='Color1', width=20, height=5, command=color1)
b1.place(x=0, y=300)
b2.place(x=150, y=300)
b3.place(x=0, y=385)
b4.place(x=150, y=385)
root.resizable(False, False)
root.mainloop()
'''
'''
from tkinter import *
import random

score, max_score = 0, 20
size_x, size_y = 1280, 700


def put():
    global button
    button = Button(root, text='Нажми меня', bg='gray', activebackground='red', command=click)
    button.place(x=random.randint(20, size_x - 20), y=random.randint(10, size_y - 10))


def click():
    global score
    button.destroy()
    score += 1
    if score < 20:
        put()
    else:
        Label(root, text='Вы выиграли,\n поздравляю!').place(relx=0.5, rely=0.5)


root = Tk()
root.title('Первая игра')
root.geometry(f'{size_x}x{size_y}')
root.resizable(False, False)
put()
root.mainloop()
'''
"""
from tkinter import *


def set_value(formula):
    if formula == '':
        label['text'] = '0'
    else:
        label['text'] = str(eval(formula))


def logic(operator):
    if operator == 'C':
        set_value('')
    elif operator == 'DEL':
        label['text'] = label['text'][0:-1]
        if label['text'] == '':
            label['text'] = '0'
    elif operator == 'X^2':
        set_value(str((eval(label['text'])) ** 2))
    elif operator == '=':
        set_value(label['text'])
    else:
        if label['text'] == '0':
            label['text'] = ''
        label['text'] = label['text'] + operator


list = ['C', 'DEL', '*', '=', '1', '2', '3', '/', '4', '5', '6', '+', '7', '8', '9', '-', '(', '0', ')', 'X^2']
root = Tk()
root['bg'] = 'black'
root.title('Calculator')
root.geometry('485x550')
root.resizable(False, False)
label = Label(root, text='0', font=('Consolas', 21, 'bold'), bg='black', foreground='white')
label.place(x=10, y=50)
x = 10
y = 140
for lst in list:
    com = lambda x=lst: logic(x)
    Button(text=lst, bg='white', font=('Consolas', 15), command=com).place(x=x, y=y, width=115, height=79)
    x += 117
    if x > 400:
        x = 10
        y += 81
root.mainloop()
"""

filename = "C:\\Users\\izoit\\Documents\\Inzhinirium\\data.csv"


def read_from_file(filename):
    with open(filename, 'r') as file:
        columns = tuple(file.readline().split(','))
        data = []
        for line in file:
            line = line.split(',')
            data.append((int(line[0]), (line[1]), (line[2]), int(line[3]), int(line[4]), int(line[5])))
    return columns, data


def write_to_file(filename):
    with open(filename, 'w') as file:
        file.write(','.join(columns))
        for line in data:
            line = [str(i) for i in line]
            file.write(','.join(line) + '\n')

def print_data():
    m = max([len(i) for i in columns])
    for i in columns:
        print(str(i).ljust(m + 1, ' '), end='')
    print()
    for line in data:
        for i in line:
            print(str(i).ljust(m + 1, ' '), end='')
        print()


def insert(line):
    if line not in data:
        data.append(line)


def get_value():
    line = list(input().split())
    return int(line[0]), (line[1]), (line[2]), int(line[3]), int(line[4]), int(line[5])


global columns, data
columns, data = read_from_file(filename)
insert(get_value())
print_data()
write_to_file(filename)