import tkinter as tk
import csv
import tkinter.messagebox as messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #




# ---------------------------- SAVE PASSWORD ------------------------------- #
row_to_check = ['Website', 'Email/Username', 'Password']
with open('data.csv', mode='a+', newline='') as file:
    file.seek(0)
    reader = csv.reader(file)
    
    row_exists = False
    for currnet_row in reader:
        if currnet_row == row_to_check:
            row_exists = True
            break
    
        
    if not row_exists:
        writer = csv.writer(file)
        writer.writerow(row_to_check)

def save_password():
    website = website_entry.get()
    website_entry.delete(0, tk.END)
    email = email_entry.get()
    email_entry.delete(0, tk.END)
    password = password_entry.get()
    password_entry.delete(0, tk.END)
    lis = [website, email, password]

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Please fill in all fields.")
        return


    is_oky = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "f"\nPassword: {password} \nIs it ok to save?")

    if is_oky:
        with open('data.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(lis)
    
        messagebox.showinfo(title="Success", message="Password saved successfully!")


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
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()

email_entry = tk.Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_entry.insert(0, "example@gmail.com") 

password_entry = tk.Entry(width=21)
password_entry.grid(row=3, column=1, sticky="EW")

# Buttons
generate_password_button = tk.Button(text='Generate Password')
generate_password_button.grid(row=3, column=2, sticky="EW")

add_button = tk.Button(text='Add', width=36,command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")



window.mainloop()