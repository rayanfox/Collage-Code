import tkinter as tk

def f_to_C():

    f_temp=enter_temp.get()
    celsius=(5/9) * (float(f_temp)-32)
    lbl_result["text"]=f"{round(celsius,2)} \N{DEGREE CELSIUS}"


window=tk.Tk()



window.title("this is cool")

frm_input=tk.Frame(master=window)
enter_temp=tk.Entry(master=frm_input, width=10)
lbl_temp=tk.Label(master=frm_input,  text="\N{DEGREE FAHRENHEIT}")

enter_temp.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0 , column=0, sticky="e")

btn_convert=tk.Button(master=window, text="\N{RIGHTWARDS BLACK ARROW}", command=f_to_C)
lbl_result=tk.Label(master=window, text="\N{DEGREE CELSIUS}")

frm_input.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

window.mainloop()

