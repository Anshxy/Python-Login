try:
    import tkinter as tk
    from functools import partial
    import sqlite3
    from tkinter import messagebox
    con = sqlite3.connect("database.db")
    
except Exception as e:
    print(e)

cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS details(username, password)")

def validateLogin(username, password):

    if not(len(username.get().strip()) or len(password.get().strip())):
        messagebox.showwarning(title="User Authentication Failed", message="Please enter Valid details")
        print("Non Valid Details Entered")
    else:
        cur.execute(f"SELECT username from details WHERE username='{username.get()}' AND password = '{password.get()}';")
        if not cur.fetchone():
            messagebox.showerror(title="User Authentication Failed", message="Invalid Login Details", )
            print("Invalid Details Entered")
        else:
            print("Successfully Logged in")
            print("Welcome, {}.".format(username.get()))
            messagebox.showinfo(title="User Authentication Successful", message="Successfully Logged in")
            
        


def register(username, password):
    if not(len(username.get().strip()) or len(password.get().strip())):
        messagebox.showwarning(title="User Authentication Failed", message="Please enter Valid details")
        print("Non Valid Details Entered")
    else:
        cur.execute(f"SELECT username from details WHERE username='{username.get()}';")
        if not cur.fetchone():
            cur.execute(f"INSERT INTO details VALUES ('{username.get()}', '{password.get()}')")
            con.commit()
            messagebox.showinfo(title="User Registration Successful", message="Successfully Registered")

        else:
            messagebox.showerror(title="User Registration Failed", message="Username matches an already entered username", )
            print("Invalid Details Entered")
            return






root = tk.Tk()
root.geometry("300x300")
root.title("Dummy sqlite3 Login Page")
  
 
# Defining the first row
lblfrstrow = tk.Label(root, text ="Username -", )
lblfrstrow.place(x = 50, y = 20)
 
Username = tk.Entry(root, width = 35)
Username.place(x = 150, y = 20, width = 100)
  
lblsecrow = tk.Label(root, text ="Password -")
lblsecrow.place(x = 50, y = 50)
 
password = tk.Entry(root, width = 35)
password.place(x = 150, y = 50, width = 100)
 
validateLogin = partial(validateLogin, Username, password)
register = partial(register, Username, password)


submitbtn = tk.Button(root, text ="Login",
                      bg ='light blue', command = validateLogin)
submitbtn.place(x = 150, y = 135, width = 55)
registerbtn = tk.Button(root, text ="Register",
                      bg ='light green', command = register)
registerbtn.place(x = 150, y = 180, width = 55)
 
root.mainloop()