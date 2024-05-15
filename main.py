from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    with open("data.txt", "a") as file:
        file.write(f"\n Website: {website} | Email: {email} | Password: {password}")

    website_entry.delete(0, "end")
    password_entry.delete(0, "end")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(bg="white", padx=20, pady=20)


canvas = Canvas(bg="white", width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(bg="white", text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(bg="white", text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(bg="white", text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "lemonCakes@gmail.com")
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, columnspan=2)


#Buttons
password_button = Button(bg="white", text="Generate Password")
password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=35, bg="white", command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
