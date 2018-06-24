from tkinter import *
import functools

@functools.singledispatch
def Name(a):
    type_name = type(a).__name__
    assert False, "Unsupported type : " + type_name

@Name.register(int)
def _(a):
    if (a == 0):
        return 'Ноль'
    elif (a == 1):
        return 'Один'
    elif (a == 2):
        return 'Два'
    elif (a == 3):
        return 'Три'
    elif (a == 4):
        return 'Четыре'
    elif (a == 5):
        return 'Пять'
    elif (a == 6):
        return 'Шесть'
    elif (a == 7):
        return 'Семь'
    elif (a == 8):
        return 'Восемь'
    elif (a == 9):
        return 'Девять'

@Name.register(str)
def _(a):
    return a

def butt():
    try:
        dt = digType.get()
        d = int(dig.get())
        if dt == 'int':
            res = (d)
        if dt == 'bin':
            res = Name(bin(d))
        if dt == 'oct':
            res = Name(oct(d))
        if dt == 'hex':
            res = Name(hex(d))
        result = Label(root, bg="steelblue3", text=res, width = '200', fg='gray1')
        result.pack()
    except ValueError as e:
        result = Label(root, bg="red", text="Введите ЦИФРУ", width = '200', fg='gray1')
        result.pack()


root = Tk()
dig = Entry(root)
dig.pack()
digType = StringVar()
rbutton1=Radiobutton(root,text='int',variable=digType,value='int')
rbutton2=Radiobutton(root,text='bin',variable=digType,value='bin')
rbutton3=Radiobutton(root,text='oct',variable=digType,value='oct')
rbutton4=Radiobutton(root,text='hex',variable=digType,value='hex')
rbutton1.pack()
rbutton2.pack()
rbutton3.pack()
rbutton4.pack()
button = Button(root, bg="blue", fg='gray1', text="Преобразовать", command=butt)
button.pack()
root.geometry('500x400+300+200')
root.mainloop()
