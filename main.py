import json

# read `expenses.json`
filename = "expenses.json"
with open (filename, "r") as f:
    expense = json.load(f)
    
# get and print total "price" for all expenses at the "pet store"

total = sum(item["price"] for item in expense["pet store"])

print(total)
    
