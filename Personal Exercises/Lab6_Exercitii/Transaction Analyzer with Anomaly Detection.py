transactions = [
    (1, "Alice", "Bob", 100.0, "income"),
    (2, "Alice", "EvilCorp", 5000.0, "expense"),
    (3, "Alice", "Bob", 120.0, "expense"),
    (4, "Alice", "Lilly", 140.0, "expense"),
    (5, "Alice", "Bob", 130.0, "expense"),
    (6, "Alice", "UnknownX", 3000.0, "expense"),
    (7, "Alice", "UnknownX", 3000.0, "expense"),
    (8, "Alice", "UnknownX", 3000.0, "expense"),   
    (9, "Alice", "Lilly", 140.0, "expense"),     
    (10, "Alice", "Bob", 140.0, "expense"),
    (11, "Alice", "Bob", 140.0, "expense"),
    (12, "Alice", "Ana", 140.0, "expense"),
    (12, "Alice", "Ana", 140.0, "expense"),
    (13, "Alice", "Ana", 140.0, "expense"),
    (14, "Alice", "Ana", 140.0, "expense")
]
receivers = []
counts = []

def calculate_totals(transactions):
    total=0
    for trans in transactions:
        if trans[4]=="expense":
            print(f"Expense: {trans[3]}")
            total+= trans[3]
        # if trans[2] not in receivers:
        #     receivers.append(trans[2])
        #     counts.append(1)
        # else:
        #     counts[receivers.index(trans[2])]+=1
    return total

def get_large_transactions(transactions):
    large_Transactions=[]
    total=0
    for trans in transactions:
        if trans[3] >1000:
            large_Transactions.append(trans[3])
            total+=trans[3]
            print(f"Large transaction to {trans[2]}: {trans[3]}")
            print("Total:",total)
    return large_Transactions

def count_receiver_frequency(transactions):
    receiver_frequency=[]
    counts=[]
    for trans in transactions:
        if trans[2] not in receiver_frequency:
            receiver_frequency.append(trans[2])
            counts.append(1)
        else:
            counts[receiver_frequency.index(trans[2])]+=1
    for i in range(len(receiver_frequency)):
        print(f'Receiver: {receiver_frequency[i]}, Count: {counts[i]}')
    return receiver_frequency,counts

def detect_suspicious_names(transactions):
    suspicious_names=[]
    for trans in transactions:
        if trans[2][-1] == "X" or trans[2][-4:]=="Corp":
            suspicious_names.append(trans[2])
            print(f"Suspicious transaction: {trans[3]} from {trans[1]} to {trans[2]}")
    return suspicious_names

def detect_bursts(transactions):
    bursts=[]
    prev_receiver = None
    count = 0
    for i in range(len(transactions)-1):
        receiver = transactions[i][2]
        prev_receiver = transactions[i+1][2]
        if receiver == prev_receiver:
            count += 1
        else:
            if count > 2:
                bursts.append(prev_receiver)
            count = 1
            prev_receiver = receiver
    print(dir(bursts))
        
    return bursts
        
# print(f'Total expenses: {calculate_totals(transactions)}')
# print(f'Receivers: {receivers}')
# print(f'Counts: {counts}')
# print(f'Large transactions: {get_large_transactions(transactions)}')
# print(f'Suspicious names: {detect_suspicious_names(transactions)}')
print(f'Receiver frequency: {count_receiver_frequency(transactions)}')
print(f'Bursts: {detect_bursts(transactions)}')
