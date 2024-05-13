from tkinter import *

root = Tk()
root.title("Turtle Bot Controller")
root.config(bg = "skyblue") 

frame1 = Frame(root, borderwidth = 2, width = 200, height = 400)
frame1.grid(row = 0, column = 0, padx = 10, pady = 5)

label1 = Label(frame1, text = "Connexion au Turtle Bot:")
label1.grid(row = 1, column = 0, padx = 5, pady = 5)


root.mainloop()