
while True:   
    sir=input("Introduceti sirul: ")
    sir = sir.replace(" ", ",")
    sir=sir.split(",")
    for i in sir:
        if i.isnumeric():
            if int(i)>100 or int(i)<0:
                sir.remove(i)
        else:
            sir.remove(i)

    print(f"Numerele din sir sunt: {sir}")

    y=int(input("Introduceti y: "))
    #always initialize variables before adding them inside of a function
    rezultatadunare=0
    
    for numar in sir:
        rezultatPutere=int(numar)**y
        print(f"Rezultatul puterii {numar} la {y} este: {rezultatPutere}")
        rezultatadunare+=int(numar)
        rezultatInmultiriiY=int(numar)*y
        print(f"Rezultatul inmultirii numerelor din sir la {y} este: {rezultatInmultiriiY}\n")

    print(f"Suma numerelor din sir este: {rezultatadunare}")
    if input("Doriti sa continuati? (y/n): ") == "y":
        continue   
    else:
        exit()