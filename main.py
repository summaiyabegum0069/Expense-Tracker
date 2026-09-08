import json
from datetime import date
expenses=[]
categories = ["Food", "Travel", "Shopping", "Entertainment", "Bills", "Education", "Other"]
def add_expenses():
    try:
      expenses_id=int(input("enter the id: "))
      for expense in expenses:
        if(expense["id"]==expenses_id):
          print("already exisit in file")
          return
    except ValueError:
        print("invalid id ")
        return
        
    name = input("Enter expense name: ").strip() 
    if(name==""):
        print("invalid name")
        return
    try:
        amount =float(input("Enter amount: "))
        if(amount<=0):
          print("invalid")
          return
    except ValueError:
        print("invalid amount")
        return
    print("Available categories:")

    for category in categories:
       print(category)

    category = input("Enter category: ").strip()
    if category not in categories:
      print("Invalid category")
      return
    expense_date=date.today()
    expense={"id":expenses_id,
             "name":name,
             "amount":amount,
             "category":category,
             "date":expense_date
             }
    expenses.append(expense)

def view_expenses():
    if(len(expenses)==0):
        print("list is empty")
        return
    for expense in expenses:
        print("ID:", expense["id"])
        print("Name:", expense["name"])
        print("Amount:", expense["amount"])
        print("Category:", expense["category"])
        print("Date:", expense["date"])
        print("--------------------")

def total_expenses():
    if(len(expenses)==0):
            print("list is empty")
            return
    total=0
    for expense in expenses:
        total+=expense["amount"]
    print("total expenses are: ",total)

def view_by_expenses():
    if(len(expenses)==0):
            print("list is empty")
            return

    category=input("enter the categeory").strip()
    if category not in categories:
          print("Invalid category")
          return
    
    found=False
    for expense in expenses:
        if(expense["category"]==category):
            found=True
            print("ID:", expense["id"])
            print("Name:", expense["name"])
            print("Amount:", expense["amount"])
            print("Category:", expense["category"])
            print("Date:", expense["date"])
            print("--------------------")
    if(found==False):
        print("these categeory is not present")

def delete_expenses():
    try:
       expenses_id=int(input("enter the id: "))
    except ValueError:
        print("invalid id")
        return
    found=False
    for expense in expenses:
        if expense["id"] == expenses_id:
            expenses.remove(expense)
            found=True
            print("expenses are deleted successfully")
            return
    if(found==False):
        print("no expenses is present with these id ")

def update_expenses():
    try:
          expenses_id=int(input("enter the id: "))

    except ValueError:
            print("invalid id ")
            return
    found = False
    for expense in expenses:
        if expense["id"] == expenses_id:
            found = True
            try:
              new_amount=float(input("enter the new amount: "))
              if new_amount <= 0:
                    print("Invalid amount")
                    return
            except ValueError:
                print("Invalid amount")
                return
            new_name=input("enter the new name: ").strip()
            if new_name == "":
                print("Invalid name")
                return

            print("Available categories:")
            for category in categories:
                print(category)

            new_category = input("Enter the new category: ").strip()

            if new_category not in categories:
                print("Invalid category")
                return
            expense["amount"]=new_amount
            expense["name"]=new_name
            expense["category"]=new_category
            print("Expense updated successfully")
            return
    if not found:
        print("No expense is present with this ID")

def save_expenses():
    with open("expenses.json","w") as f:
      data=[]
      for expense in expenses:
        expense_copy=expense.copy()
        expense_copy["date"]=str(expense_copy["date"])
        data.append(expense_copy)
      json.dump(data,f)

    
def load_expenses():
    global expenses
    try:
       with open("expenses.json","r") as f:
        expenses=json.load(f)
        print("Expenses loaded successfully")
    except FileNotFoundError:
        expenses = []
        print("No saved expenses found")

load_expenses()
while True:
    print("===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. View By Category")
    print("5. Delete Expense")
    print("6. Update Expense")
    print("7. save expenses")
    print("8. load expenses")
    print("9. exit")

    try:
      choice = int(input("Enter your choice: "))
    except ValueError:
        print("invalid")
        continue
    if(choice==1):
        add_expenses()
    elif(choice==2):
        view_expenses()
    elif(choice==3):
        total_expenses()
    elif(choice==4):
        view_by_expenses()
    elif(choice==5):
        delete_expenses()
    elif(choice==6):
        update_expenses()
    elif(choice==7):
        save_expenses()
    elif(choice==8):
        load_expenses()
    elif(choice==9):
        break
    else:
        print("invalid choice")