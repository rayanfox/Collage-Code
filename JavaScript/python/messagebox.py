from tkinter import messagebox

responce = messagebox.askyesno(" Are furries the best?", "Are furries the best?")
if responce == True:
   messagebox.showinfo("YASS!", "YASSS!") 
elif responce == False:
   messagebox.showinfo("Booo!", "Booo!")  
else:
   messagebox.showinfo("Nothing Selected", "Nothing Selected")
   

    
