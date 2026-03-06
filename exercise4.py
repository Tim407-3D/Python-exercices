data = [
    {"Name": "Alice", "Age": 23, "Salary": 40000},
    {"Name": "Bob", "Age": 35, "Salary": 50000},
    {"Name": "Charlie", "Age": 31, "Salary": 45000},
    {"Name": "David", "Age": 28, "Salary": 48000}
]

uptosalary= ([person["Salary"] for person in data if person["Salary"] > 45000]) 
for person in data:
    if person["Salary"] >= 45000:
        print(person["Name"], person["Salary"])

