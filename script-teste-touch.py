import tkinter as tk

def on_enter(event):

    print("Touche Entrée pressée")
    print(event.keycode)

root = tk.Tk()
entry = tk.Entry(root)
entry.pack()
entry.bind("<Return>", on_enter)
root.mainloop()
