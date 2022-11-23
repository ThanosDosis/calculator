from tkinter import *

def add_function():
    e3.insert(0, str(int(e1.get()) + int(e2.get())))

def sub_function():
    e4.insert(0, str(int(e1.get()) - int(e2.get())))

def multi_function():
    e5.insert(0, str(int(e1.get()) * int(e2.get())))

def div_function():
    e6.insert(0, str(int(e1.get()) // int(e2.get())))

def clear_entries():
    e1.delete(0,10)
    e2.delete(0,10)
    e3.delete(0,10)
    e4.delete(0,10)
    e5.delete(0,10)
    e6.delete(0,10)
    

root=Tk()

l1=Label(root, text='Calculator v1.0')
l1.grid(row=0, sticky=W)
l2=Label(root, text='1ος αριθμός:')
l2.grid(row=1, sticky=W)
e1=Entry(root)
e1.grid(row=1, column=1)
l3=Label(root, text='2ος αριθμός:')
l3.grid(row=2, sticky=W)
e2=Entry(root)
e2.grid(row=2, column=1)
b1=Button(root, text=' + ', fg='navy', command=add_function)
b1.grid(row=3, sticky=W)
e3=Entry(root)
e3.grid(row=3, column=1)
b2=Button(root, text=' - ', fg='navy', command=sub_function)
b2.grid(row=4, sticky=W)
e4=Entry(root)
e4.grid(row=4, column=1)
b3=Button(root, text=' * ', fg='navy', command=multi_function)
b3.grid(row=5, sticky=W)
e5=Entry(root)
e5.grid(row=5, column=1)
b4=Button(root, text=' / ', fg='navy', command=div_function)
b4.grid(row=6, sticky=W)
e6=Entry(root)
e6.grid(row=6, column=1)
b5=Button(root, text='Καθαρισμός', fg='navy', command=clear_entries)
b5.grid(row=7, sticky=W)

root.mainloop()
