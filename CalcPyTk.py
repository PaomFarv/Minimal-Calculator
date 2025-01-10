import tkinter as tk

def button_click(value):
    current_text = entry.get()
    entry.delete(0,tk.END)
    entry.insert(0,current_text + value)

def calculate():
    global result
    try:
        result = eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(0,str(round(result,7)))
    except Exception:
        entry.delete(0,tk.END)
        entry.insert(0,"Error")

def clear():
    entry.delete(0,tk.END)

def resize_font(event):
    new_height = entry.winfo_height()
    new_font_size = max(34,int(new_height * 0.4))
    entry.config(font=("Bahnschrift SemiBold",new_font_size))

def plus_minus():
    current_value = entry.get()
    if current_value:
        if current_value.startswith("-"):
            entry.delete(0,tk.END)
            entry.insert(0,current_value[1:])
        else:
            entry.delete(0,tk.END)
            entry.insert(0,"-" + current_value)

def percentage():
    current_value = entry.get()
    if current_value:
        entry.delete(0,tk.END)
        perc = float(current_value)/100
        entry.insert(0,perc)
    else:
        pass

def del_char():
    current_value = entry.get()
    if current_value:
        entry.delete(0,tk.END)
        entry.insert(0,current_value[:-1])
    else:
        pass


root = tk.Tk()
root.title("Minimal Calculator")
root.minsize(280,350)
root.config(bg="Black")

try:
    root.iconbitmap("calcicon.ico")
except tk.TclError:
    print("Icon file not found. Using default icon.")


for i in range(4):
    root.columnconfigure(i, weight=1)
for i in range(5):
    root.rowconfigure(i, weight=1)

entry = tk.Entry(root,width=14,font=("Bahnschrift SemiBold",34),justify="left",bg="Black",fg="White")
entry.grid(row=0,column=0,columnspan=16,sticky="nsew",ipady=10)
entry.bind("<Configure>",resize_font)

buttons = [
    ('AC',1,0,1,1),('+/-',1,1,1,1),('DEL',1,2,1,1),('/',1,3,1,1),
    ('7',2,0,1,1),('8',2,1,1,1),('9',2,2,1,1),('*',2,3,1,1),
    ('4',3,0,1,1),('5',3,1,1,1),('6',3,2,1,1),('-',3,3,1,1),
    ('1',4,0,1,1),('2',4,1,1,1),('3',4,2,1,1),('+',4,3,1,1),
    ('%',5,0,1,1),('0',5,1,1,2),('.',5,2,1,1),('=',5,3,1,1)
]

for (text,row,col,colspan,rowspan) in buttons:
    if text == "=":
        action = calculate
    elif text == "AC":
        action = clear
    elif text == "+/-":
        action = plus_minus
    elif text == "%":
        action = percentage
    elif text == "DEL":
        action = del_char
    else:
        action = lambda value=text:button_click(value)

    tk.Button(root,text=text,width=3,height=1,font=("Bahnschrift SemiBold",20),bg="grey",fg="White",relief="ridge",
              command=action).grid(row=row,column=col,sticky="nsew",padx=5,pady=5)

root.mainloop()