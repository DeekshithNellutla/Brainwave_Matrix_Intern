import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import pandas as pd

# Database Connection
def connect_db():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      name TEXT,
                      category TEXT,
                      price REAL,
                      quantity INTEGER)''')
    conn.commit()
    conn.close()

# Add Product
def add_product():
    name = name_entry.get()
    category = category_entry.get()
    price = price_entry.get()
    quantity = quantity_entry.get()
    
    if name and category and price and quantity:
        conn = sqlite3.connect("inventory.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO products (name, category, price, quantity) VALUES (?, ?, ?, ?)", 
                       (name, category, float(price), int(quantity)))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Product added successfully!")
        load_products()
    else:
        messagebox.showerror("Error", "All fields are required!")

# Load Products
def load_products():
    for row in tree.get_children():
        tree.delete(row)
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    conn.close()
    for row in rows:
        tree.insert("", tk.END, values=row)

# Delete Product
def delete_product():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "Select a product to delete!")
        return
    product_id = tree.item(selected_item)['values'][0]
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id=?", (product_id,))
    conn.commit()
    conn.close()
    load_products()
    messagebox.showinfo("Success", "Product deleted successfully!")

# Generate Report
def generate_report():
    conn = sqlite3.connect("inventory.db")
    df = pd.read_sql_query("SELECT * FROM products", conn)
    df.to_csv("inventory_report.csv", index=False)
    conn.close()
    messagebox.showinfo("Success", "Report generated as inventory_report.csv")

# GUI Setup
root = tk.Tk()
root.title("Inventory Management System")
root.geometry("600x500")
connect_db()

# Labels and Entries
tk.Label(root, text="Product Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Category").pack()
category_entry = tk.Entry(root)
category_entry.pack()

tk.Label(root, text="Price").pack()
price_entry = tk.Entry(root)
price_entry.pack()

tk.Label(root, text="Quantity").pack()
quantity_entry = tk.Entry(root)
quantity_entry.pack()

# Buttons
tk.Button(root, text="Add Product", command=add_product).pack()
tk.Button(root, text="Delete Product", command=delete_product).pack()
tk.Button(root, text="Generate Report", command=generate_report).pack()

# Treeview Table
tree = ttk.Treeview(root, columns=("ID", "Name", "Category", "Price", "Quantity"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Category", text="Category")
tree.heading("Price", text="Price")
tree.heading("Quantity", text="Quantity")
tree.pack()

load_products()
root.mainloop()
