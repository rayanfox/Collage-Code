import tkinter as tk



def up():
    value=int(lbl_value["text"])
    lbl_value["text"] = f"{value+1}"

def down():
    value=int(lbl_value["text"])
    lbl_value["text"] = f"{value-1}"

window=tk.Tk()

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0,1,2], minsize=50, weight=1)

btn_decrease = tk.Button(master=window, text="-", command=down)
btn_decrease.grid(row=0, column=0, sticky="nsew")

lbl_value=tk.Label(master=window, text="0")
lbl_value.grid(row=0, column=1, sticky="nsew")

btn_increase = tk.Button(master=window, text="+", command=up)
btn_increase.grid(row=0, column=2, sticky="nsew")
window.mainloop()