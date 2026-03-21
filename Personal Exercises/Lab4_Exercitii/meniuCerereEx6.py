lista = []
print("Introduceti numere. Cand sunteti gata, introduceti x.")
while True:
    nr=input("Numar:")
    if nr == 'x':
        break
    lista.append(float(nr))
    
def suma(lista: list):
    total=0
    for nr in lista:
        total=total+nr
    return total
def medie(lista: list):
    return suma(lista) / len(lista)
def putere(lista: list):
    return suma(lista) ** 2
while True:
    meniu = {
"1": medie,
"2": suma,
"3": putere
}
    print("Meniu:")
    print("1. Media numerelor")
    print("2. Suma numerelor")
    print("3. Puterea numerelor")
    print("4. Iesire")
    optiune = input("Alegeti o optiune: ")
    if optiune == '4':
        break
    elif optiune == '1':
        print("Rezultatul medie:", medie(lista))
    elif optiune == '2':
        print("Rezultatul suma:", suma(lista))
    elif optiune == '3':
        print("Rezultatul putere:", putere(lista))
    else:
        print("Optiune invalida")


