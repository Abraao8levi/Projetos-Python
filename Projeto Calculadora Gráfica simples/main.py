'''
Calculadora Gráfica  Simples  em Python
Soma, subtração, multiplicação, divisão e porcentagem.

'''
import tkinter as tk

def calculate(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.set(result)
        except Exception as e:
            screen.set("Erro")
    elif text == "C":
        screen.set("")
    elif text == "⌫":
        screen.set(screen.get()[:-1])
    else:
        screen.set(screen.get() + text)

root = tk.Tk()
root.geometry("400x600")
root.configure(bg='dark slate gray')

screen = tk.StringVar()

entry = tk.Entry(root, textvar=screen, font="lucida 30 bold", bg='black', fg='lime')
entry.grid(row=0, column=0, columnspan=5, sticky="nsew")

buttons = [
    ['7', '8', '9', '/', '⌫'],
    ['4', '5', '6', '*', 'C'],
    ['1', '2', '3', '-', '%'],
    ['.', '0', '=', '+']
]

colors = ['light green', 'hot pink', 'light gray', 'tomato']

for i in range(len(buttons)):
    for j in range(len(buttons[i])):
        if buttons[i][j] in '0123456789.':
            color = 'light green'
        elif buttons[i][j] in '+-*/%':
            color = 'hot pink'
        else:
            color = 'light gray'
        btn = tk.Button(root, text=buttons[i][j], font='lucida 15 bold', bg=color, fg='white')
        btn.grid(row=i+1, column=j, sticky="nsew", padx=3, pady=3)
        btn.bind('<Button-1>', calculate)

# Adjust grid size
for x in range(len(buttons[0])):
    tk.Grid.columnconfigure(root, x, weight=1)

for y in range(len(buttons) + 1):
    tk.Grid.rowconfigure(root, y, weight=1)

root.mainloop()
