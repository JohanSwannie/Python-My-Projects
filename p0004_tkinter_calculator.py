from tkinter import *
expr = ""  # Global expression string

def press(key):
    global expr
    expr += str(key)
    display.set(expr)

def equal():
    global expr
    try:
        result = str(eval(expr))
        display.set(result)
        expr = ""
    except:
        display.set("error")
        expr = ""

def clear():
    global expr
    
    expr = ""
    display.set("")

if __name__ == "__main__":
    root = Tk()
    root.configure(bg="red")
    root.title("Simple Calculator")
    root.geometry("400x330")

    display = StringVar()
    entry = Entry(root, textvariable=display, bg="black", fg="white", width=57, font=("Arial", 10))
    entry.grid(columnspan=7, ipady=15)

    # Number buttons
    btn1 = Button(root, text='1', fg='black', bg='red', command=lambda: press(1), height=3, width=13)
    btn1.grid(row=3, column=0)
    btn2 = Button(root, text='2', fg='black', bg='red', command=lambda: press(2), height=3, width=13)
    btn2.grid(row=3, column=1)
    btn3 = Button(root, text='3', fg='black', bg='red', command=lambda: press(3), height=3, width=13)
    btn3.grid(row=3, column=2)
    btn4 = Button(root, text='4', fg='black', bg='red', command=lambda: press(4), height=3, width=13)
    btn4.grid(row=4, column=0)
    btn5 = Button(root, text='5', fg='black', bg='red', command=lambda: press(5), height=3, width=13)
    btn5.grid(row=4, column=1)
    btn6 = Button(root, text='6', fg='black', bg='red', command=lambda: press(6), height=3, width=13)
    btn6.grid(row=4, column=2)
    btn7 = Button(root, text='7', fg='black', bg='red', command=lambda: press(7), height=3, width=13)
    btn7.grid(row=5, column=0)
    btn8 = Button(root, text='8', fg='black', bg='red', command=lambda: press(8), height=3, width=13)
    btn8.grid(row=5, column=1)
    btn9 = Button(root, text='9', fg='black', bg='red', command=lambda: press(9), height=3, width=13)
    btn9.grid(row=5, column=2)
    btn0 = Button(root, text='0', fg='black', bg='red', command=lambda: press(0), height=3, width=13)
    btn0.grid(row=6, column=0)

    # Operator buttons
    plus = Button(root, text='+', fg='black', bg='red', command=lambda: press('+'), height=3, width=13)
    plus.grid(row=3, column=3)
    minus = Button(root, text='-', fg='black', bg='red', command=lambda: press('-'), height=3, width=13)
    minus.grid(row=4, column=3)
    mult = Button(root, text='*', fg='black', bg='red', command=lambda: press('*'), height=3, width=13)
    mult.grid(row=5, column=3)
    div = Button(root, text='/', fg='black', bg='red', command=lambda: press('/'), height=3, width=13)
    div.grid(row=6, column=3)

    # Other buttons
    eq = Button(root, text='=', fg='black', bg='red', command=equal, height=3, width=13)
    eq.grid(row=6, column=2)
    clr = Button(root, text='Clear', fg='black', bg='red', command=clear, height=3, width=13)
    clr.grid(row=6, column=1)
    dot = Button(root, text='.', fg='black', bg='red', command=lambda: press('.'), height=3, width=13)
    dot.grid(row=7, column=0)

    root.mainloop()