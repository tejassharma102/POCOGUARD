import tkinter as tk
from tkinter import simpledialog, messagebox
import database
import logic
import settings

def run_app():
    
    root = tk.Tk()
    root.title(settings.app_name)
    root.geometry("300x500") 
    l1 = tk.Label(root, text="Item Name:")
    l1.pack(pady=5)
    e1 = tk.Entry(root)
    e1.pack()
    
    l2 = tk.Label(root, text="Price:")
    l2.pack(pady=5)
    e2 = tk.Entry(root)
    e2.pack()
    
    def btn_add():
        n = e1.get()
        p = e2.get()
        
        if n == "" or p == "":
            messagebox.showerror("Error", "type something")
            return
        try:
            database.save_one(n, p)
            messagebox.showinfo("Saved", "Added item")
            e1.delete(0, tk.END)
            e2.delete(0, tk.END)
        except:
            print("save error")

    def btn_view():
        d = database.get_all()
        text = ""
        
        i = 1
        for row in d:
            text = text + str(i) + ". " + row[0] + " : " + row[1] + "\n"
            i = i + 1
            
        messagebox.showinfo("My List", text)

    def btn_total():
        d = database.get_all()
        limit = database.get_budget_limit()
        ans = logic.calc_total(d)
        stat = logic.check_warning(ans, limit)
        msg = f"Total Spent: {ans}\nMy Budget: {limit}\n{stat}"
        messagebox.showinfo("Report", msg)

    def btn_set_budget():
        new_b = simpledialog.askfloat("Budget", "Enter new budget limit:")
        if new_b is not None:
            database.save_budget_limit(new_b)
            messagebox.showinfo("Done", "Budget Updated")

    def btn_delete():
        btn_view()
        
        num = simpledialog.askinteger("Delete", "Enter line number to delete:")
        
        if num is not None:
            success = database.delete_row(num)
            if success:
                messagebox.showinfo("Deleted", "Item removed")
            else:
                messagebox.showerror("Error", "Invalid line number")

    b1 = tk.Button(root, text="Add Item", command=btn_add, bg="white")
    b1.pack(pady=10)
    
    b2 = tk.Button(root, text="View All", command=btn_view)
    b2.pack(pady=5)
    
    b3 = tk.Button(root, text="Check Total", command=btn_total, bg="lightgrey")
    b3.pack(pady=5)
    
    b4 = tk.Button(root, text="Set Budget", command=btn_set_budget, bg="orange")
    b4.pack(pady=5)
    b5 = tk.Button(root, text="Delete Item", command=btn_delete, bg="red", fg="white")
    b5.pack(pady=10)
    
    root.mainloop()