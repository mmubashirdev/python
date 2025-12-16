import pyodbc
import tkinter as tk
from tkinter import messagebox

con = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    r"Server={localhost\\MSSQLSERVER01};"
    "trusted_connection=yes;",
    autocommit=True
)
cursor = con.cursor()

cursor.execute("IF DB_ID('PRODUCT_DB') IS NULL CREATE DATABASE PRODUCT_DB;")
cursor.execute("USE PRODUCT_DB;")
cursor.execute("""
IF OBJECT_ID('Product_Table') IS NULL
CREATE TABLE Product_Table(
    id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(50),
    quantity INT,
    price FLOAT
)
""")
con.commit()

def add_product():
    n = entry_name.get()
    q = entry_qty.get()
    p = entry_price.get()
    if n == "" or q == "" or p == "":
        messagebox.showerror("Error", "Fill all fields")
        return
    cursor.execute("INSERT INTO Product_Table(name,quantity,price) VALUES(?,?,?)", (n,q,p))
    con.commit()
    messagebox.showinfo("Done", "Product Added")

def view_products():
    cursor.execute("SELECT * FROM Product_Table")
    rows = cursor.fetchall()
    txt = ""
    for r in rows:
        txt += f"{r[0]}  |  {r[1]}  |  {r[2]}  |  {r[3]}\n"
    if txt == "":
        txt = "No products"
    messagebox.showinfo("Products", txt)

def update_product():
    pid = entry_id.get()
    if pid == "":
        messagebox.showerror("Error", "Enter ID")
        return
    cursor.execute("UPDATE Product_Table SET name=?, quantity=?, price=? WHERE id=?",
                   (entry_name.get(), entry_qty.get(), entry_price.get(), pid))
    con.commit()
    messagebox.showinfo("Done", "Updated")

def delete_product():
    pid = entry_id.get()
    if pid == "":
        messagebox.showerror("Error", "Enter ID")
        return
    cursor.execute("DELETE FROM Product_Table WHERE id=?", (pid,))
    con.commit()
    messagebox.showinfo("Done", "Deleted")

root = tk.Tk()
root.title("Product Management System")
root.geometry("500x420")
root.configure(bg="#1e1e1e")

tk.Label(root, text="Product ID", fg="white", bg="#1e1e1e", font=("Arial",14)).grid(row=0,column=0,padx=10,pady=10)
entry_id = tk.Entry(root, font=("Arial",14))
entry_id.grid(row=0,column=1)

tk.Label(root, text="Name", fg="white", bg="#1e1e1e", font=("Arial",14)).grid(row=1,column=0,padx=10,pady=10)
entry_name = tk.Entry(root, font=("Arial",14))
entry_name.grid(row=1,column=1)

tk.Label(root, text="Quantity", fg="white", bg="#1e1e1e", font=("Arial",14)).grid(row=2,column=0,padx=10,pady=10)
entry_qty = tk.Entry(root, font=("Arial",14))
entry_qty.grid(row=2,column=1)

tk.Label(root, text="Price", fg="white", bg="#1e1e1e", font=("Arial",14)).grid(row=3,column=0,padx=10,pady=10)
entry_price = tk.Entry(root, font=("Arial",14))
entry_price.grid(row=3,column=1)

tk.Button(root, text="Add", width=15, bg="blue", fg="white", font=("Arial",14), command=add_product).grid(row=4,column=0,padx=10,pady=10)
tk.Button(root, text="View", width=15, bg="green", fg="white", font=("Arial",14), command=view_products).grid(row=4,column=1,padx=10,pady=10)
tk.Button(root, text="Update", width=15, bg="yellow", fg="black", font=("Arial",14), command=update_product).grid(row=5,column=0,padx=10,pady=10)
tk.Button(root, text="Delete", width=15, bg="red", fg="white", font=("Arial",14), command=delete_product).grid(row=5,column=1,padx=10,pady=10)

root.mainloop()
