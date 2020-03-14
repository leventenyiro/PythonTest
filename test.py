import osztaly as os
import tkinter as tk

o = os.Osztaly(5)
print(o.x)
s = o.szorzas(6)
print(str(s))

root = tk.Tk()
canvas = tk.Canvas(root, height=600, width=1000, bg="#00A1E4")
canvas.pack()
root.title("Python GUI")


root.mainloop()