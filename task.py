from tkinter import *
import functools

@functools.singledispatch
def perevod(a):
    type_name = type(arg).__name__
    assert False, "Unsupported notation : " + type_name

@perevod.register(int)
def _(a):
    if a == 0:
        return 'Ноль'
    if a == 1:
        return 'Один'
    if a == 2:
        return 'Два'
    if a == 3:
        return 'Три'
    if a == 4:
        return 'Четыре'
    if a == 5:
        return 'Пять'
    if a == 6:
        return 'Шесть'
    if a == 7:
        return 'Семь'
    if a == 8:
        return 'Восемь'
    if a == 9:
        return 'Девять'
    else:
        return 'Данная функция доступна только от чисел от 0 до 9'


@perevod.register(str)
def _(a):
    return a[2::]

def butt():
    try:
        dt = digType.get()
        d = int(dig.get())
        if dt == 'int':
            res = perevod(d)
        if dt == 'bin':
            res = perevod(bin(d))
        if dt == 'oct':
            res = perevod(oct(d))
        if dt == 'hex':
            res = perevod(hex(d))
        result = Label(root, bg="steelblue3", text=res, width = '200', fg='gray1')
        result.pack()
    except ValueError as e:
        result = Label(root, bg="red", text="Введите ЧИСЛО", width = '200', fg='gray1')
        result.pack()    


root = Tk()
root.geometry('500x400+300+200')
root.title("Экзаменационное задание")

dig = Entry(root)
dig.pack()
digType = StringVar()

rbutton1=Radiobutton(root,text='Имя',variable=digType,value='int')
rbutton2=Radiobutton(root,text='bin',variable=digType,value='bin')
rbutton3=Radiobutton(root,text='oct',variable=digType,value='oct')
rbutton4=Radiobutton(root,text='hex',variable=digType,value='hex')
rbutton1.pack()
rbutton2.pack()
rbutton3.pack()
rbutton4.pack()
button = Button(root, bg="blue", fg='gray1', text="Перевод", command=butt)
button.pack()

root.mainloop()
