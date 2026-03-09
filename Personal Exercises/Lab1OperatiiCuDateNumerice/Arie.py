date={"Baza":[],"Inaltime":[]}

def updateDate(arie):
    while True:
        newbaza = input("Enter base: ")
        if newbaza.isnumeric():
            break
        else:
            print("Error: Base must be a positive number. Try again.")
    
    while True:
        newinaltime = input("Enter height: ")
        if newinaltime.isnumeric():
            break
        else:
            print("Error: Height must be a positive number. Try again.")
    
    arie=1/2*(int(newbaza)*int(newinaltime))
    date["Baza"].append(newbaza)
    date["Inaltime"].append(newinaltime)
    
    return arie


print(updateDate(0))
print(date)