from tkinter import *
root = Tk()
root.geometry('441x452')
done = ''
jung = 0
mpl = [0]
msl = [0]

def number(num):
    global done, jung
    if jung == 1:
        done = ''
        jung = 0
        ans_win.delete(0, END)
    done += str(num)
    ans_win.insert(END, num)


def ans():
    global jung
    jung += 1
    jhu = ans_win.get()
    ans_win.delete(0, END)
    ans_win.insert(END, str(eval(jhu)))
def m(num):
    global ans_win, jung, done

    if num == 1:
        msl.append(int(eval(ans_win.get())))
        ans_win.delete(0, END)
    if num == 2:
        mpl.append(int(eval(ans_win.get())))
        ans_win.delete(0, END)
    if num == 3:
        so = sum(msl)
        st = sum(mpl)
        mh = so-st
        ans_win.delete(0, END)
        ans_win.insert(END, mh)


def pen():
    global jung
    ans1 = int(eval(ans_win.get()))
    ans_win.delete(0, END)
    ans_win.insert(END, str(ans1/100))
    jung+=1


b1 = Button(root, text='1', width=15, background='gray', foreground='white', height=5, command=lambda: number(1))
b1.place(x=0, y=50)
b2 = Button(root, text='2', width=15, background='gray', foreground='white', height=5, command=lambda: number(2))
b2.place(x=110, y=50)
b3 = Button(root, text='3', width=15, background='gray', foreground='white', height=5, command=lambda: number(3))
b3.place(x=220, y=50)
b4 = Button(root, text='4', width=15, background='gray', foreground='white', height=5, command=lambda: number(4))
b4.place(x=0, y=130)
b5 = Button(root, text='5', width=15, background='gray', foreground='white', height=5, command=lambda: number(5))
b5.place(x=110, y=130)
b6 = Button(root, text='6', width=15, background='gray', foreground='white', height=5, command=lambda: number(6))
b6.place(x=220, y=130)
b7 = Button(root, text='7', width=15, background='gray', foreground='white', height=5, command=lambda: number(7))
b7.place(x=0, y=210)
b8 = Button(root, text='8', width=15, background='gray', foreground='white', height=5, command=lambda: number(8))
b8.place(x=110, y=210)
b9 = Button(root, text='9', width=15, background='gray', foreground='white', height=5, command=lambda: number(9))
b9.place(x=220, y=210)
b0 = Button(root, text='0', width=15, background='gray', foreground='white', height=5, command=lambda: number(0))
b0.place(x=110, y=290)
bd = Button(root, text='.', width=15, background='gray', foreground='white', height=5, command=lambda: number('.'))
bd.place(x=0, y=290)
bp = Button(root, text='%', width=15, background='gray', foreground='white', height=5, command=lambda: pen())
bp.place(x=220, y=290)
div = Button(root, text='/', width=15, background='gray', foreground='white', height=5, command=lambda: number('/'))
div.place(x=0, y=370)
mul = Button(root, text='* ', width=15, background='gray', foreground='white', height=5, command=lambda: number('*'))
mul.place(x=110, y=370)
sub = Button(root, text='-', width=15, background='gray', foreground='white', height=5, command=lambda: number('-'))
sub.place(x=220, y=370)
add = Button(root, text='+', width=15, background='gray', foreground='white', height=5, command=lambda: number('+'))
add.place(x=330, y=50)
equ = Button(root, text='=', width=15, background='gray', foreground='white', height=5, command=lambda: ans())
equ.place(x=330, y=130)
ms = Button(root, text='m-', width=15, background='gray', foreground='white', height=5, command=lambda: m(2))
ms.place(x=330, y=210)
mp = Button(root, text='m+', width=15, background='gray', foreground='white', height=5, command=lambda: m(1))
mp.place(x=330, y=290)
mr = Button(root, text='mr', width=15, background='gray', foreground='white', height=5, command=lambda: m(3))
mr.place(x=330, y=370)
ans_win = Entry(root, width=83, borderwidth=3)
ans_win.place(x=0, y=0)
root.mainloop()
