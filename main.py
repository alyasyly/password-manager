import tkinter as tk
import csv
import tkinter.messagebox as messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list.extend(random.choice(letters) for _ in range(nr_letters))
    password_list.extend(random.choice(symbols) for _ in range(nr_symbols))
    password_list.extend(random.choice(numbers) for _ in range(nr_numbers))

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


###---- for csv files----###
# row_to_check = ['Website', 'Email/Username', 'Password']
# with open('data.csv', mode='a+', newline='') as file:
#     file.seek(0)
#     reader = csv.reader(file)
    
#     row_exists = False
#     for currnet_row in reader:
#         if currnet_row == row_to_check:
#             row_exists = True
#             break
    
        
#     if not row_exists:
#         writer = csv.writer(file)
#         writer.writerow(row_to_check)



def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }}

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Please fill in all fields.")
        return


    is_oky = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "f"\nPassword: {password} \nIs it ok to save?")

    if is_oky:
        website_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        try:
            with open('data.json', mode='r') as file:
                data = json.load(file)
        except (FileNotFoundError,json.decoder.JSONDecodeError):
            data = {}
            
        data.update(new_data)
            
        with open('data.json', mode='w') as file:
            json.dump(data, file, indent=4)


        messagebox.showinfo(title="Success", message="Password saved successfully!")

# ---------------------------- Search setup ---------------------------- #
def search():
    website = website_entry.get()
    try:
        with open('data.json', mode='r') as file:
            data = json.load(file)
    except (FileNotFoundError,json.decoder.JSONDecodeError):
        messagebox.showerror(title="Error", message="No data file found.")
        return

    if website in data:
        email = data[website]["email"]
        password = data[website]["password"]
        messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
    else:
        messagebox.showerror(title="Error", message=f"No details for {website} exists.")




# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = tk.Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = tk.Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=1, sticky="EW")
website_entry.focus()

email_entry = tk.Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_entry.insert(0, "example@gmail.com") 

password_entry = tk.Entry(width=21)
password_entry.grid(row=3, column=1, sticky="EW")

# Buttons
generate_password_button = tk.Button(text='Generate Password', command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="EW")

add_button = tk.Button(text='Add', width=36,command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

search_button = tk.Button(text='Search',bg='blue',activebackground='blue',command=search)
search_button.grid(row=1,column=2,sticky="EW")

window.mainloop()