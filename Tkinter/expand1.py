import tkinter as tk
window = tk.Tk()
window.geometry("400x300")
tk.Label(window,
         text="Python",
         bg="yellow").pack()
tk.Label(window,
         text="Java",
         bg="yellow").pack(expand=True, fill="both")
window.mainloop()
