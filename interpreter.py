from tkinter import *
from tkinter import filedialog, messagebox
import subprocess

path = r''
def run():
    global path, output
    if path == '':
        path = filedialog.asksaveasfilename(parent=root)
    save()
    result, error =  subprocess.Popen(f'python {path}', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate()
    if path[:2] != 'C:':
        error = 'Save File in C:'
    if error == b'':
        output.delete(0.0, END)
        output.insert('1.0', result)
    else:
        output.delete(0.0, END)
        output.insert('1.0', error)
def save():
    global path
    if path == '':
        path = filedialog.asksaveasfilename(parent=root)
    if path:
        f = open(path, 'w')
        f.write(textEditor.get(0.0, END))
def save_as():
    global path
    path = filedialog.asksaveasfilename(parent=root)
    if path:
        f = open(path, 'w')
        f.write(textEditor.get(0.0, END))
def open_file():
    f = filedialog.askopenfilename()
    print(f)
    if f:
        f = open(f).read()
        textEditor.delete(0.0, END)
        textEditor.insert(0.0, f)
def new():
    global text, path
    h = messagebox.askyesnocancel('save', 'Do you want to save')
    if h:
        save_as()
    elif h == None:
        return
    textEditor.delete(0.0, END)
    output.delete(0.0, END)
    path = ''

root = Tk()
textEditor = Text()
textEditor.config(bg='#362f2e', fg='#d2ded1', insertbackground='white')
textEditor.pack(fill='both', expand=1)

output = Text(height=7)
output.config(bg='#362f2e', fg='#1dd604')
output.pack(fill='both', expand=1)
menu = Menu(root)
root.config(menu=menu)
menu1 = Menu(menu)
menu.add_cascade(label='file', menu=menu1)
menu1.add_cascade(label='New...', command=new)
menu1.add_cascade(label='open', command=open_file)
menu1.add_cascade(label='save as', command=save_as)
menu1.add_cascade(label='save', command=save)
menu1.add_cascade(label='run', command=run)
menu1.add_cascade(label='quit', command=root.quit)
root.mainloop()