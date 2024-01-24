import sqlite3 as sq
from tkinter import *
from tkinter import messagebox
import random


def signup():
    # Get the value from the Entry widgets
    user_input_1 = e1.get()
    user_input_2 = e2.get()
    user_input_3 = e3.get()
    user_input_4 = e4.get()

    cursor.execute(
        "INSERT INTO information2 (fname, lname, email, pass) VALUES (%s, %s, %s, %s)",
        (user_input_1, user_input_2, user_input_3, user_input_4)
    )
    welcome_message(user_input_1, user_input_2)


def welcome_message(first_name, last_name):
    greeting = "Welcome"
    polite_words = ["dear", "honored", "respected", "valued", "esteemed"]
    polite_word = random.choice(polite_words)
    message = f"{greeting} {polite_word} {first_name} {last_name}!"
    messagebox.showinfo("Welcome", message)


def open_login_window():

    def login():
        entered_email = e5.get()
        entered_password = e6.get()
        # Check if the entered email and password match any records in the database
        query = "SELECT * FROM information2 WHERE email = ? AND pass = ?"
        cursor.execute(query, (entered_email, entered_password))
        result = cursor.fetchone()

        if result:
            # If a record is found, display a welcome message
          # Assuming the first and second columns are fname and lname
            welcome_message(result[0], result[1])
        else:
            # If no record is found, show an error message
            messagebox.showerror("Error", "Invalid email or password")
    top = Toplevel(root)
    top.geometry("400x500+560+150")
    top.configure(bg="black")

    frame2 = Frame(top, width=300, height=400,
                   highlightbackground="#2E2D2D", highlightthickness=2)
    frame2.place(x=50, y=50)
    frame2.configure(bg="#101010")

    main_text = Label(top, text="Login", font=(
        "Roboto", 18, "bold"), bg="black", fg="#00587B")
    main_text.place(x=160, y=10)

    main_text = Label(top, text="WELCOME BACK",
                      font=("Helvetica", 12), bg="#101010", fg="white")
    main_text.place(x=130, y=130)

    email_label = Label(top, text="Email", fg="white", bg="#101010")
    email_label.place(x=110, y=180, anchor="w")

    password_label = Label(top, text="Password", fg="white", bg="#101010")
    password_label.place(x=117, y=220, anchor="center")

    e5 = Entry(top, width=20, fg="white", bg="#595959")
    e5.place(x=150, y=170)

    e6 = Entry(top, show="*", width=20, fg="white", bg="#595959")
    e6.place(x=150, y=210)

    lbutton = Button(top, text="Login", width=27, height=2,
                     bg="#00587B", fg="white", command=login)
    lbutton.place(x=105, y=270)

    top.mainloop()


# Database setup
database_name = "Accounts"

# Connect to MySQL server
conn = sq.connect("Accounts.db"
                  )

# Create main window
root = Tk(className="Signup")
root.geometry("400x500+560+150")
root.configure(bg="black")
text = Label(root, text="Signup")
text.config(fg="#00587B", bg="black")
text.config(font=("Roboto", 18, "bold"))
text.place(x=160, y=10)

# Style setup
frame = Frame(root, width=300, height=400,
              highlightbackground="#2E2D2D", highlightthickness=2)
frame.place(x=50, y=50)
frame.configure(bg="#101010")

# Database operations
cursor = conn.cursor()
cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS information2 (
            fname VARCHAR(255),
            lname VARCHAR(255),
            email VARCHAR(255) UNIQUE,
            pass VARCHAR(255)
        )
    """)

# Label and Entry widgets
f_name_label = Label(root, text="First name", fg="white",
                     bg="#101010").place(x=100, y=140, anchor="w")
l_name_label = Label(root, text="Last name", fg="white",
                     bg="#101010").place(x=100, y=180, anchor="w")
email_label = Label(root, text="Email", fg="white",
                    bg="#101010").place(x=100, y=220, anchor="w")
password_label = Label(root, text="Password", fg="white",
                       bg="#101010").place(x=100, y=260, anchor="w")

e1 = Entry(root, bg="#595959", fg="white")
e1.place(x=170, y=130)

e2 = Entry(root, bg="#595959", fg="white")
e2.place(x=170, y=170)

e3 = Entry(root, bg="#595959", fg="white")
e3.place(x=170, y=210)

e4 = Entry(root, bg="#595959", fg="white")
e4.place(x=170, y=250)

button = Button(root, text="Sign up", width=27, height=2,
                bg="#00587B", fg="white", command=signup)
button.place(x=100, y=300)

loginvar = Label(root, text="--------or-------", fg="white",
                 bg="#101010").place(x=150, y=360, anchor="w")
loginvar2 = Label(root, text="Already have an Account ?", fg="white",
                  bg="#101010").place(x=120, y=380, anchor="w")
button2 = Button(root, text="Login", width=15, height=1,
                 bg="#00587B", fg="white", command=open_login_window)
button2.place(x=140, y=400)


root.mainloop()

# Commit changes and close the connection
conn.commit()
conn.close()
