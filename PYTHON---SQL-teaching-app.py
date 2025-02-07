import sqlite3
import tkinter as tk
from tkinter import messagebox, scrolledtext

def execute_query():
    query = query_text.get("1.0", tk.END).strip()
    if not query:
        messagebox.showwarning("Warning", "Please enter an SQL query.")
        return
    
    try:
        cursor.execute(query)
        conn.commit()
        
        if query.lower().startswith("select"):
            rows = cursor.fetchall()
            result_text.delete("1.0", tk.END)
            for row in rows:
                result_text.insert(tk.END, f"{row}\n")
        else:
            messagebox.showinfo("Success", "Query executed successfully.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Initialize SQLite database
conn = sqlite3.connect(":memory:")  # In-memory database for practice
cursor = conn.cursor()

# Create a sample table
cursor.execute("""
    CREATE TABLE students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
""")
conn.commit()

# GUI Setup
root = tk.Tk()
root.title("SQL Teaching App")
root.geometry("600x400")

tk.Label(root, text="Enter your SQL query:").pack()
query_text = scrolledtext.ScrolledText(root, height=5)
query_text.pack(fill=tk.BOTH, expand=True)

tk.Button(root, text="Run Query", command=execute_query).pack()

tk.Label(root, text="Results:").pack()
result_text = scrolledtext.ScrolledText(root, height=10)
result_text.pack(fill=tk.BOTH, expand=True)

root.mainloop()

# Close connection on exit
conn.close()
