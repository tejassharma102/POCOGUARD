def calc_total(data):
    t = 0
    for row in data:
        p = float(row[1])
        t = t + p
    return t

def check_warning(total, limit):
    if total > limit:
        return "Warning: Over Budget!!"
    else:
        left = limit - total
        return f"Safe. (Remaining: {left})"