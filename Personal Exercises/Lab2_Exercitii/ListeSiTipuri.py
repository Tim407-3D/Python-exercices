lista=['abc',123,'1',1]
for i in lista:
    print(type(i))
    if type(i) == int:
        print(len(str(i)))
    elif type(i) == str:
        print(len(i))
    elif type(i) == list:
        print(len(i))
    else:
        print("Unknown type")