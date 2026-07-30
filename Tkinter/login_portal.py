import tkinter as tk

# -----------------------------
# Create Main Window
# -----------------------------
window = tk.Tk()
window.title("Student Login System")
window.geometry("500x400")
window.configure(bg="white")

# --------------------------------------------------------
# Header Frame
# --------------------------------------------------------
header_frame = tk.Frame(
    window,
    bg="#1976D2",
    height=70,
)
header_frame.pack(fill="x")

# Prevent the frame from shrinking
header_frame.pack_propagate(False)
title = tk.Label(
    header_frame,
    text="STUDENT LOGIN SYSTEM",
    bg="#19D238",
    fg="white",
    font=("Arial",18,"bold")
)
title.pack(expand=True)

# --------------------------------------------------------
# Login Frame
# --------------------------------------------------------
login_frame = tk.Frame(
    window,
    bg="white"
)
login_frame.pack(expand=True)

# ========================================================
# Username Frame
# ========================================================
username_frame = tk.Frame(
    login_frame,
    bg="white"
)
username_frame.pack(pady=10)
username_label = tk.Label(
    username_frame,
    text="Username :",
    bg="white",
    font=("Arial",12)
)
username_label.pack(side="left",padx=10)

username_entry = tk.Entry(
    username_frame,
    width=25,
    font=("Arial",12)
)
username_entry.pack(side="left")

# ========================================================
# Password Frame
# ========================================================
password_frame = tk.Frame(
    login_frame,
    bg="white"
)
password_frame.pack(pady=10)
password_label = tk.Label(
    password_frame,
    text="Password :",
    bg="white",
    font=("Arial",12)
)
password_label.pack(side="left",padx=10)
password_entry = tk.Entry(
    password_frame,
    width=25,
    font=("Arial",12),
    show="*"
)
password_entry.pack(side="left")

# ========================================================
# Button Frame
# ========================================================
button_frame = tk.Frame(
    login_frame,
    bg="white"
)
button_frame.pack(pady=20)
login_button = tk.Button(
    button_frame,
    text="Login",
    width=15,
    bg="#1976D2",
    fg="white",
    font=("Arial",12)
)
login_button.pack()

# ========================================================
# Forgot Password
# ========================================================
forgot_frame = tk.Frame(
    login_frame,
    bg="white"
)
forgot_frame.pack()
forgot_label = tk.Label(
    forgot_frame,
    text="Forgot Password?",
    fg="blue",
    bg="white",
    cursor="hand2",
    font=("Arial",10,"underline")
)
forgot_label.pack()

# --------------------------------------------------------
# Footer Frame
# --------------------------------------------------------
footer_frame = tk.Frame(
    window,
    bg="lightgray",
    height=35
)
footer_frame.pack(fill="x",side="bottom")
footer_frame.pack_propagate(False)
footer_label = tk.Label(
    footer_frame,
    text="© 2026 LBEF College",
    bg="lightgray",
    font=("Arial",10)
)
footer_label.pack(expand=True)

window.mainloop()
