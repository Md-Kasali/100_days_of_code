from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json

# Password Generator Project

# ------------------------------PASSWORD GENERATOR------------------#


def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)


# ------------------------------SAVE DATA in Json format--------------------------- #


def save():

    website_data = website_entry.get().title()
    email_data = email_username_entry.get()
    password_data = password_entry.get()
    new_data = {
        website_data: {
                "email": email_data,
                "password": password_data,
            }
    }

    if len(website_data) == 0 or len(password_data) == 0 or len(email_data) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")

    else:
        # Read json file
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            email_username_entry.delete(0, END)
            password_entry.delete(0, END)

# ------------------------------FIND PASSWORD----------------------- #


def find_password():
    user_search = website_entry.get().title()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
        try:
            user_data = {website: details for (website, details) in data.items() if user_search == website}
            account_data = user_data[user_search]
        except KeyError:
            messagebox.showerror(title="Error", message=f"No details for {user_search} exists.")
        else:
            messagebox.showinfo(title=user_search, message=f"Username: {account_data['email']}\n Password: {account_data['password']}")


# ------------------------------UI SETUP---------------------------- #


window = Tk()
window.config(padx=50, pady=80, bg="#FFFFFF")
window.title("Password Manager")

canvas = Canvas(width=200, height=200, bg="#FFFFFF", highlightthickness=0)
padlock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", bg="#FFFFFF", fg="#000000")
website_label.grid(row=1, column=0, padx=0, pady=5)

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, padx=5, sticky="w")

search_button = Button(text="Search", bg="#FFFFFF", width=14, font=("Arial", 9, "normal"), command=find_password, fg="#000000")
search_button.grid(row=1, column=2)

email_username_label = Label(text="Email/Username:", bg="#FFFFFF", fg="#000000")
email_username_label.grid(row=2, column=0, padx=10, pady=5)

email_username_entry = Entry(width=40)
email_username_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:", bg="#FFFFFF", fg="#000000")
password_label.grid(row=3, column=0, padx=0, pady=5)

password_entry = Entry(width=22)
password_entry.grid(row=3, column=1, sticky="w", padx=5)

generate_button = Button(text="Generate Password", width=14, height=1, font=("Arial", 9, "normal"), bg="#FFFFFF",
                         borderwidth=0.5, command=generate_password, fg="#000000")
generate_button.grid(row=3, column=2, padx=5, sticky="w")

add_button = Button(text="Add", width=43, bg="#FFFFFF", command=save, font=("Arial", 9, "normal"), fg="#000000")
add_button.grid(row=4, column=1, columnspan=2, pady=2)

window.mainloop()
