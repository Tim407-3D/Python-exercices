data = {"Name": [], "Age": [], "Salary": []}
while True:
    newName = str(input("Enter name: "))
    if newName.isalpha():
        break
    else:
        print("Error: Name must contain only letters. Try again.")
while True:
    newAge = input("Enter age: ")
    if newAge.isnumeric() and int(newAge)>0:
        break
    else:
        print("Error: Age must be a positive number. Try again.")
while True:     
    newSalary =input("Enter salary: ")
    if newSalary.isnumeric() and int(newSalary)>0:
        break
    else:
        print("Error: Salary must be a positive number. Try again.")

data["Name"].append(newName)
data["Age"].append(newAge)
data["Salary"].append(newSalary)
