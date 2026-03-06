data = [
    {"Name": "Alice", "Age": 23, "Salary": 40000},
    {"Name": "Bob", "Age": 35, "Salary": 50000},
    {"Name": "Charlie", "Age": 31, "Salary": 45000},
    {"Name": "David", "Age": 28, "Salary": 48000}
]

print(f"{[person["Name"] for person in data if person["Salary"] >= 45000]}", f"{[person["Salary"] for person in data if person["Salary"] > 45000]}") 


