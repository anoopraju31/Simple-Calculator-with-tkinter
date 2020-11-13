# Simple Calculator used to add, subtract, multiply and divide numbers with Python Tkinter

import tkinter as tk
from tkinter import PhotoImage


root = tk.Tk()
root.title('Calculator')
root.iconbitmap('img/calculator.ico')
root.config(bg='#bbb')
root.geometry('224x396')

container = tk.Frame(root, bd=5, padx=5, pady=5)
container.pack()
container.config(bg='#bbb')

# Entry part
e = tk.Text(container,width=24, height=6,bd=2, bg='#eee', fg='#333')
e.grid(row=0,column=0, columnspan=3, pady=(0,10))


# adding new number
def delete_add(current):
    e.delete("1.0","end")
    e.insert('1.0', current)


# number clicks  
def button_click(number):
    current = str(e.get("1.0","end"))[:-1] 

    if len(current) != 0 and current[0] == 'd':
        current = ''
    current += str(number)
    delete_add(current)


# clear screen  
def button_clear():
    if str(e.get("1.0","end"))[0].isalpha():
        e.config(fg='#333')
    e.delete("1.0","end")


# clear the last entered value
def button_clear_last():
    current = str(e.get('1.0', 'end'))[:-1]
    if current != '':
        if current[-1] != ' ':
            current = current[:-1]
        else:
            current = current[:-3]
        delete_add(current) 


# add button
def button_operation(operation):
    current = str(e.get("1.0","end"))[:-1]
    if current != '' and current[-1] != ' ':
        current += operation
        delete_add(current)
    elif current != '' and current[-1] == ' ':
        current = current[:-3] + operation
        delete_add(current)

# eqaul to button
def button_equal():
    expression = e.get("1.0","end")

    try:
        all_num = []
        all_operator = []

        # seperating operators and operands
        for num in expression.split():
            if num.isnumeric():
                all_num.append(eval(num))
            else:
                try:
                    if num.index ('.'):
                        all_num.append(eval(num))
                except:
                        all_operator.append(num)
        
        # division first
        i = 0
        l = len(all_operator)
        while i < l:    
            try:
                i = all_operator.index('/')
                try:
                    all_operator.remove('/')
                    all_num[i] = all_num[i] / all_num[i+1]
                    all_num[i+1] = '0'
                    all_num.remove('0')
                except ZeroDivisionError as zde:
                    e.config(fg='red')
                    delete_add(zde)
                    return      
                
            except:
                break
        
        # Multiplication Second
        i = 0
        l = len(all_operator)   
        while i < l:    
            try:
                i = all_operator.index('*')
                all_operator.remove('*')
                all_num[i] = all_num[i] * all_num[i+1]
                all_num[i+1] = '0'
                all_num.remove('0')
            except:
                break    
        
        # Addition Third
        i = 0
        l = len(all_operator)  
        while i < l:    
            try:
                i = all_operator.index('+')
                all_operator.remove('+')
                all_num[i] = all_num[i] + all_num[i+1]
                all_num[i+1] = '0'
                all_num.remove('0')
            except:
                break
        
        # Subtraction last
        i = 0
        l = len(all_operator)
        while i < l:    
            try:
                i = all_operator.index('-')
                all_operator.remove('-')
                all_num[i] = all_num[i] - all_num[i+1]
                all_num[i+1] = '0'
                all_num.remove('0')
            except:
                break
            
        delete_add(str(all_num[0]))
    except:
        return
             

# clear img 
photoimage = PhotoImage(file='img/clear.png')
photoimage = photoimage.zoom(15)
photoimage = photoimage.subsample(38)

# Define Buttons

button_1 = tk.Button(container,text='1', fg='red', padx=25, pady=10, command=lambda: button_click(1))
button_2 = tk.Button(container,text='2', fg='red', padx=25, pady=10, command=lambda: button_click(2))
button_3 = tk.Button(container,text='3', fg='red', padx=25, pady=10, command=lambda: button_click(3))
button_4 = tk.Button(container,text='4', fg='red', padx=25, pady=10, command=lambda: button_click(4))
button_5 = tk.Button(container,text='5', fg='red', padx=25, pady=10, command=lambda: button_click(5))
button_6 = tk.Button(container,text='6', fg='red', padx=25, pady=10, command=lambda: button_click(6))
button_7 = tk.Button(container,text='7', fg='red', padx=25, pady=10, command=lambda: button_click(7))
button_8 = tk.Button(container,text='8', fg='red', padx=25, pady=10, command=lambda: button_click(8))
button_9 = tk.Button(container,text='9', fg='red', padx=25, pady=10, command=lambda: button_click(9))
button_0 = tk.Button(container,text='0', fg='red', padx=25, pady=10, command=lambda: button_click(0))

button_add = tk.Button(container, text='+', fg='red', padx=24, pady=10, command=lambda: button_operation(' + '))
button_subtract = tk.Button(container, text='- ', fg='red', padx=24, pady=10, command=lambda: button_operation(' - '))
button_multiple = tk.Button(container, text='* ', fg='red', padx=24, pady=10, command=lambda: button_operation(' * '))
button_divide = tk.Button(container, text='/ ', fg='red', padx=24, pady=10, command=lambda: button_operation(' / '))

button_equal = tk.Button(container, text='=', fg='red', padx=24, pady=10, command=button_equal)
button_clear = tk.Button(container, text='clear ', fg='red', padx=47, pady=10, command=button_clear)
button_clear_last = tk.Button(container, text= 'X=', image=photoimage , width=59, pady=10, command=button_clear_last)

# Put the buttons on the screen

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_clear.grid(row=4,column=1, columnspan=2)

button_subtract.grid(row=5, column=0)
button_multiple.grid(row=5, column=1)
button_divide.grid(row=5, column=2)

button_add.grid(row=6,column=0)
button_equal.grid(row=6,column=1)
button_clear_last.grid(row=6, column=2)

root.mainloop()