import tkinter as tk
from tkinter import messagebox
import sqlite3

# Database Initialization
conn = sqlite3.connect("reservations.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS reservations (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                destination TEXT NOT NULL,
                airline TEXT NOT NULL,
                date TEXT NOT NULL)''')
conn.commit()

class ReservationManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Reservation Management System")
        
        # Admin Login
        self.admin_frame = tk.Frame(root)
        self.admin_frame.pack(pady=20)
        self.admin_label = tk.Label(self.admin_frame, text="Admin Password:")
        self.admin_label.pack(side=tk.LEFT)
        self.admin_entry = tk.Entry(self.admin_frame, show="*")
        self.admin_entry.pack(side=tk.LEFT)
        self.login_button = tk.Button(self.admin_frame, text="Login", command=self.admin_login)
        self.login_button.pack(side=tk.LEFT)
        
        # Reservation Entry
        self.entry_frame = tk.Frame(root)
        self.entry_frame.pack(pady=20)
        
        self.name_label = tk.Label(self.entry_frame, text="Name:")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(self.entry_frame)
        self.name_entry.grid(row=0, column=1)
        
        self.phone_label = tk.Label(self.entry_frame, text="Phone Number:")
        self.phone_label.grid(row=1, column=0)
        self.phone_entry = tk.Entry(self.entry_frame)
        self.phone_entry.grid(row=1, column=1)
        
        self.destination_label = tk.Label(self.entry_frame, text="Destination:")
        self.destination_label.grid(row=2, column=0)
        self.destination_entry = tk.Entry(self.entry_frame)
        self.destination_entry.grid(row=2, column=1)
        
        self.airline_label = tk.Label(self.entry_frame, text="Airline:")
        self.airline_label.grid(row=3, column=0)
        self.airline_var = tk.StringVar()
        self.airline_choices = ["Indigo", "Vistara", "Akasa", "Deccan", "SpiceJet"]
        self.airline_var.set(self.airline_choices[0])
        self.airline_menu = tk.OptionMenu(self.entry_frame, self.airline_var, *self.airline_choices)
        self.airline_menu.grid(row=3, column=1)
        
        self.date_label = tk.Label(self.entry_frame, text="Date of Travel:")
        self.date_label.grid(row=4, column=0)
        self.date_entry = tk.Entry(self.entry_frame)
        self.date_entry.grid(row=4, column=1)
        
        self.add_button = tk.Button(self.entry_frame, text="Add Reservation", command=self.add_reservation)
        self.add_button.grid(row=5, columnspan=2)
        
        # Reservation List
        self.reservation_list = tk.Listbox(root, height=10, width=80)
        self.reservation_list.pack(pady=20)
        
        # Delete Button
        self.delete_button = tk.Button(root, text="Delete Selected", command=self.delete_reservation)
        self.delete_button.pack()
        
        # Quit Button
        self.quit_button =tk.Button(root, text="Quit", command=self.quit).pack()
        
        
    def admin_login(self):
        password = self.admin_entry.get()
        if password == "admin":
            self.admin_frame.destroy()
            self.load_reservations()
        else:
            messagebox.showerror("Login Error", "Invalid admin password.")

    def quit(self):
        messagebox.askyesno("Exit", "Do you want Exit?")
        root.destroy()
        
    def add_reservation(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        destination = self.destination_entry.get()
        airline = self.airline_var.get()
        date = self.date_entry.get()
	
        #if not name or not phone or not destination or not date or not airline:
	        #messagebox.showerror("Error", "All fields are required.")
	        #return
        if not name:
	        messagebox.showerror("Error", "Please Enter Name")
	        return
        if not phone:
	        messagebox.showerror("Error", "Please Enter Phone No.")
	        return
        if not destination:
	        messagebox.showerror("Error", "Please Enter Destination")
	        return
        if not date:
                messagebox.showerror("Error", "Please Enter Date Of Travel")
                return
        if not airline:
	        messagebox.showerror("Error", "Please select a airline")
	        return
        if name.strip() == "":
	        messagebox.showerror("Error", "name cannot be spaces")
	        return
        if phone.strip() == "":
	        messagebox.showerror("Error", "phone cannot be spaces")
	        return
        if destination.strip() == "":
	        messagebox.showerror("Error", "destination cannot be spaces")
	        return
        if date.strip() == "":
	        messagebox.showerror("Error", "Date of Travel cannot be spaces")
	        return
        if name.isdigit():
	        messagebox.showerror("Error", " Name cannot be Numbers")
	        return
        if phone.isalpha():
	        messagebox.showerror("Error", "Phone No. cannot be text")
	        return
        if destination.isdigit():
	        messagebox.showerror("Error", "Destination cannot be Numbers")
	        return
        if len(name) < 2 :
	        messagebox.showerror("Error", "Name is Too Short!")
	        return
        if len(name) > 20 :
	        messagebox.showerror("Error", "Name is Too Long!")
	        return
        if len(phone) < 10 :
	        messagebox.showerror("Error", "Phone No. must consist 10 digits")
	        return
        #if len(phone) < 0 :
	        #messagebox.showerror("Error", "Phone No. Cannot be Negative")
	        #return
        if len(destination) < 3 :
	        messagebox.showerror("Error", "Destination is Too Short!")
	        return
        if len(destination) > 30 :
	        messagebox.showerror("Error", "Destination is Too Long!")
	        return
        if not name.replace('.', '', 1).isalpha():
	        messagebox.showerror(f"Error", "Name cannot be Special Characters")
	        return
        if not phone.replace('.', '', 1).isdigit():
	        messagebox.showerror(f"Error", "phone cannot be Special Characters")
	        return
        if not destination.replace('.', '', 1).isalpha():
	        messagebox.showerror(f"Error", "destination cannot be Special Characters")
	        return
        #if not date.replace('.', '', 1).isdigit():
                #messagebox.showerror(f"Error", "date of travel cannot be Special Characters")
                #return
        
        #messagebox.showinfo("Success", "Reservation added successfully")
        
        # Perform input validations here
        try:
            name = str(name)
            phone = int(phone)
            destination = str(destination)
            #airline = choice(airline)
            date = str(date)
        except ValueError as e:
            messagebox.showerror("Error", "Something went wrong!")
            return
  
    
        cursor.execute("INSERT INTO reservations (name, phone, destination, airline, date) VALUES (?, ?, ?, ?, ?)",
                       (name, phone, destination, airline, date))
        messagebox.showinfo("Success", "Reservation added successfully")

        conn.commit()
        self.clear_entries()
        self.load_reservations()
        
    def delete_reservation(self):
        selected_item = self.reservation_list.curselection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a reservation to delete.")
            return
        
        confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete the reservation?")
        if confirm:
            reservation_id = self.reservation_list.get(selected_item[0]).split(":")[0]
            cursor.execute("DELETE FROM reservations WHERE id=?", (reservation_id,))
            conn.commit()
            self.load_reservations()
        
    def load_reservations(self):
        self.reservation_list.delete(0, tk.END)
        cursor.execute("SELECT * FROM reservations")
        reservations = cursor.fetchall()
        for reservation in reservations:
            self.reservation_list.insert(tk.END, f"{reservation[0]}: {reservation[1]} - {reservation[2]} ({reservation[3]}) ({reservation[4]}) ({reservation[5]})")
        
    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.destination_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x500+50+50")
    app = ReservationManagementSystem(root)
    root.mainloop()
    conn.close()
