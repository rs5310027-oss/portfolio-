import sqlite3
import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt

# Database setup
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT,
    amount REAL
)
""")
conn.commit()

# Add expense
def add_expense():
    category = category_entry.get()
    amount = amount_entry.get()

    if category == "" or amount == "":
        messagebox.showerror("Error", "Fill all fields")
        return

    cursor.execute(
        "INSERT INTO expenses (category, amount) VALUES (?, ?)",
        (category, float(amount))
    )
    conn.commit()

    messagebox.showinfo("Success", "Expense Added")

    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

# Monthly report
def show_report():
    df = pd.read_sql_query("SELECT * FROM expenses", conn)

    if df.empty:
        messagebox.showerror("Error", "No data")
        return

    report = df.groupby("category")["amount"].sum()

    report.plot.pie(
        autopct='%1.1f%%',
        figsize=(8, 8)
    )

    plt.title("Expense Distribution")
    plt.show()

# Export to Excel
def export_excel():
    df = pd.read_sql_query("SELECT * FROM expenses", conn)
    df.to_excel("expenses_report.xlsx", index=False)

    messagebox.showinfo("Success", "Exported to Excel")

# GUI
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("400x350")

tk.Label(root, text="Expense Tracker", font=("Arial", 16)).pack(pady=10)

tk.Label(root, text="Category").pack()
category_entry = tk.Entry(root)
category_entry.pack()

tk.Label(root, text="Amount").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Button(root, text="Add Expense", command=add_expense).pack(pady=10)
tk.Button(root, text="Show Report", command=show_report).pack(pady=10)
tk.Button(root, text="Export to Excel", command=export_excel).pack(pady=10)

root.mainloop()
