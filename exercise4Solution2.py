data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [23, 35, 31, 28],
    "Salary": [40000, 50000, 45000, 48000]
}
# Pandas data fram workflow
import pandas as pd
df = pd.DataFrame(data)
uptosalary= df[df["Salary"]] > 45000
print(uptosalary["Name"])