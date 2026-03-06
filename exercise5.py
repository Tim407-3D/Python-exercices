data = {"Name": [], "Age": [], "Salary": []}
history = []
def dataUpdate():

    while True:
        newName = str(input("Enter name: "))
        if newName.isalpha():
            break
        else:
            print("Error: Name must contain only letters. Try again.")

    while True:
        newAge = input("Enter age: ")
        if newAge.isnumeric() and int(newAge)>=16 and int(newAge)<65:
            break
        else:
            print("Error: Age must be a positive number between 16 and 65. Try again.")

    while True:     
        newSalary =input("Enter salary: ")
        if newSalary.isnumeric() and int(newSalary)>0:
            break
        else:
            print("Error: Salary must be a positive number. Try again.")

    result= {"Name": newName, "Age": newAge, "Salary": newSalary}
    return result



while True:
    choices= input("Enter 'r' to run the function or 'q' to quit: ")
    if choices =="r"or choices=="R":
       result= dataUpdate()
       history.append(result)
    if choices =="q" or choices=="Q":
       break


for person in history:
    print(f"Name: {person['Name']}, Age: {person['Age']}, Salary: ${person['Salary']}")