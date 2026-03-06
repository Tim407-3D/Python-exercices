data = [
    {"Name": "Alice", "Age": 23, "Salary": 40000},
    {"Name": "Bob", "Age": 35, "Salary": 50000},
    {"Name": "Charlie", "Age": 31, "Salary": 45000},
    {"Name": "David", "Age": 28, "Salary": 48000}
]

avg_age = sum([person["Age"] for person in data]) / len(data)
max_salary = max([person["Salary"] for person in data])
min_salary = min([person["Salary"] for person in data])

#create the output of the program as a data table 
for person in data:
    print(person ["Name"], person ["Age"], person ["Salary"])

print("Average age:", avg_age)
print("Max salary:", max_salary)
print("Min salary:", min_salary)
