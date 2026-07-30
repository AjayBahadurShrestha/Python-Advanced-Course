import tkinter as tk
window = tk.Tk()
frame = tk.Frame(
    window,
    bg="yellow",
    padx=50,
    pady=50
)
frame.pack()
tk.Label(
    frame,
    text="Hello Students"
).pack()
window.mainloop()
