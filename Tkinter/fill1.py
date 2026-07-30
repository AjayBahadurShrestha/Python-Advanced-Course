import tkinter as tk
window = tk.Tk()
window.geometry("400x200")
tk.Label(window, text="Python", bg="yellow").pack()
tk.Label( window, text="Java", bg="green" ).pack(fill="x")
window.mainloop()

