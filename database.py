import csv
import os
import settings

def get_all():
    l = []
    if os.path.exists(settings.filename):
        with open(settings.filename, "r") as f:
            r = csv.reader(f)
            for row in r:
                l.append(row)
    return l

def save_one(name, price):
    with open(settings.filename, "a", newline="") as f:
        w = csv.writer(f)
        w.writerow([name, price])

def save_budget_limit(amount):
    with open(settings.budget_file, "w") as f:
        f.write(str(amount))

def get_budget_limit():
    if not os.path.exists(settings.budget_file):
        return 5000.0  
    with open(settings.budget_file, "r") as f:
        data = f.read()
        return float(data)

def delete_row(line_number):
    rows = get_all()
    idx = line_number - 1
    
    if idx < 0 or idx >= len(rows):
        return False 
    rows.pop(idx)
    with open(settings.filename, "w", newline="") as f:
        w = csv.writer(f)
        w.writerows(rows)
    return True