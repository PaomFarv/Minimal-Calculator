import tkinter as tk

def button_click(value):
    current_text = entry.get()
    entry.delete(0,tk.END)
    entry.insert(0,current_text + value)


def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(0,str(result))
    except Exception:
        entry.delete(0,tk.END)
        entry.insert(0,"Error")

def clear():
    entry.delete(0,tk.END)

def resize_font(event):
    new_height = entry.winfo_height()
    new_font_size = max(34,int(new_height * 0.4))
    entry.config(font=("Bahnschrift SemiBold",new_font_size))

root = tk.Tk()
root.title("Minimal Calculator")
root.minsize(280,350)
root.config(bg="#f4921a")
root.iconbitmap("calcicon.ico")

for i in range(4):
    root.columnconfigure(i, weight=1)
for i in range(5):
    root.rowconfigure(i, weight=1)

entry = tk.Entry(root,width=14,font=("Bahnschrift SemiBold",34),justify="left")
entry.grid(row=0,column=0,columnspan=16,sticky="nsew",ipady=10)
entry.bind("<Configure>",resize_font)

buttons = [
    ('7',1,0),('8',1,1),('9',1,2),('/',1,3),
    ('4',2,0),('5',2,1),('6',2,2),('*',2,3),
    ('1',3,0),('2',3,1),('3',3,2),('-',3,3),
    ('0',4,0),('C',4,1),('=',4,2),('+',4,3),
]

for (text,row,col) in buttons:
    if text == "=":
        action = calculate
    elif text == "C":
        action = clear
    else:
        action = lambda value=text:button_click(value)

    tk.Button(root,text=text,width=3,height=1,font=("Bahnschrift SemiBold",20),relief="ridge",command=action).grid(row=row,column=col,sticky="nsew",padx=5,pady=5)

root.mainloop()