import tkinter as tk
window = tk.Tk()
window.geometry("500x300")
window.title("Padding Demonstration")

tk.Label(
    window,
    text="Python",
    bg="yellow",
    fg="black"
).pack( ipady=40)
tk.Label(
    window,
    text="Java",
    bg="lightgreen"

).pack(ipadx=40)

window.mainloop()
