import tkinter as tk
window = tk.Tk()
window.title("Student Login System")
window.geometry("500x400")
# -----------------------------
# Main Frames
# -----------------------------
header_frame = tk.Frame(window, bg="lightblue", height=60)
login_frame = tk.Frame(window, bg="white")
footer_frame = tk.Frame(window, bg="lightgray", height=40)
# -----------------------------
# Packing Main Frames
# -----------------------------
header_frame.pack(fill="x")
login_frame.pack(fill="both", expand=True)
footer_frame.pack(fill="x", side="bottom")
window.mainloop()
