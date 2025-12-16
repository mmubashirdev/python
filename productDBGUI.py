import pyodbc
con = pyodbc.connect (
  "Driver={ODBC Driver 17 for SQL Server};"
  "Server={localhost\MSSQLSERVER01};"
  "Database=PRODUCT_DB;"
  "trusted_connection=yes;",
  autocommit=True
)
cursor = con.cursor()
print("Connetion Established")

cursor.execute("IF DB_ID('Product_DB') is null CREATE DATABASE PRODUCT_DB;")
con.commit()
print("Product Database created")

cursor.execute('''IF OBJECT_ID('Product_Table') is null
  create table Product_Table(
    id int identity(1,1) primary key,
    name nvarchar(20),
    quantity int, 
    price float
  )             
''')
con.commit()
print("Product table created")

cursor.execute('insert into Product_Table(name,quantity,price) values(?,?,?)',('Iphone',10,90000))
cursor.execute('insert into Product_Table(name,quantity,price) values(?,?,?)',('Samsung',50,86000))
cursor.execute('insert into Product_Table(name,quantity,price) values(?,?,?)',('Infinix',100,45000))
cursor.execute('insert into Product_Table(name,quantity,price) values(?,?,?)',('Redme',150,50000))
con.commit()
print("Products Inserted Successfully")

cursor.execute("select * from Product_Table;")
rows = cursor.fetchall()
for r in rows:
  print(r)  
print("Data Showed")

cursor.execute("""
  update Product_Table
  set name = 'Laptop'
  where id = 1;               
""")
con.commit()
print("Table updated")

cursor.execute("""
  delete from Product_Table
  where id = 1;            
""")
con.commit()

# cursor.execute("""
#   truncate table Product_Table           
# """)
# con.commit()

print("Element deleted")


import tkinter as tk

root = tk.Tk()
root.title("Product Management System")
root.geometry("500x500")

label_ProductName = tk.Label(root,text="Enter product Name",font=('Arial',14))
label_ProductName.grid(row=0,column=0,padx=15,pady=15)
label_ProductQuantity = tk.Label(root,text="Enter product Quantity",font=('Arial',14))
label_ProductQuantity.grid(row=1,column=1,padx=15,pady=15)
label_ProductPrice = tk.Label(root,text="Enter product Price",font=('Arial',14))
label_ProductPrice.grid(row=2,column=2,padx=15,pady=15)

Add_btn = tk.Button(root,text="Add Product", width=10,bg='blue',fg='white',font=('Arial',22))
Add_btn.grid(row=3,column=3, padx=5,pady=5)
View_btn = tk.Button(root,text="View Product", width=10,bg='green',fg='white',font=('Arial',22))
View_btn.grid(row=3,column=3, padx=5,pady=5)
Update_btn = tk.Button(root,text="Update Product", width=10,bg='yellow',fg='white',font=('Arial',22))
Update_btn.grid(row=3,column=3, padx=5,pady=5)
Delete_btn = tk.Button(root,text="Delete Product", width=10,bg='red',fg='white',font=('Arial',22))
Delete_btn.grid(row=3,column=3, padx=5,pady=5)


root.mainloop()