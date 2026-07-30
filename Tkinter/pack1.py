import tkinter as tk
window = tk.Tk()
window.geometry("400x300")
tk.Label(window, text="A",  bg="aqua").pack( fill="x", side="left")
tk.Label(window, text="B").pack(side="top")
tk.Label(window, text="C").pack(side="left")
tk.Label(window, text="D").pack(side="bottom")
window.mainloop()
