
food_expense=[]
transport_expense=[]
shopping_expense=[]

num_items=int(input("Enter the number of expenses you want to add: "))
for i in range(num_items):
    category=input("Enter the category of the expense: ")
    name=input("Enter the name of the expense: ")
    amount=float(input("Enter the amount of the expense: "))
    if category.lower()=="food":
        food_expense.append({"name": name, "amount": amount})
    elif category.lower()=="transport":
        transport_expense.append({"name": name, "amount": amount})
    elif category.lower()=="shopping":
        shopping_expense.append({"name": name, "amount": amount})
print("Expenses added successfully!")

print("Expense Tracker")
categorical_expense=[sum(expense["amount"] for expense in food_expense),
               sum(expense["amount"] for expense in transport_expense),
               sum(expense["amount"] for expense in shopping_expense)]
total_expense=[sum(categorical_expense)]
print(f"Food Expense: {categorical_expense[0]}")
print(f"Transport Expense: {categorical_expense[1]}")
print(f"Shopping Expense: {categorical_expense[2]}")
print(f"Total Expense: {total_expense[0]}")
