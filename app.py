expenses =[]

num_items=int(input("Enter the number of expenses you want to add: "))
for i in range(num_items):
    name=input("Enter the name of the expense: ")
    amount=float(input("Enter the amount of the expense: "))
    expenses.append({"name": name, "amount": amount})
print("Expenses added successfully!")

print("Expense Tracker")
for i in expenses:
    print(f"Name: {i['name']} \t \t\tAmount: {i['amount']}")
