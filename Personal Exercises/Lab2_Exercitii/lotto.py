listaNumere=[]
while True:
    #
    print(f"Numar {len(listaNumere) + 1}")
    numar=int(input("Introduceti un nr intre 1 si 49: "))
    isNumberValid=1 <= numar <= 49
    if isNumberValid and numar not in listaNumere:
        listaNumere.append(numar)
    else:
        print("Numarul trebuie sa fie intre 1 si 49 si sa nu fie deja introdus")
    
    if len(listaNumere) == 6:
        break
   
    

prize = 0
numereCastigatoare=[4,12,31,17,22,25]
matched_numbers = set(listaNumere).intersection(set(numereCastigatoare))

if len(matched_numbers) == 2:
    prize = 50
elif len(matched_numbers) == 3:
    prize = 500
elif len(matched_numbers) == 4:
    prize = 1000
elif len(matched_numbers) == 5:
    prize = 5000
elif len(matched_numbers) == 6:
    prize = 100000

print(f"Prize: {prize}")
print(f"Matched numbers: {matched_numbers}")
print(f"Numbers: {listaNumere}")
print(f"Winning numbers: {numereCastigatoare}")

