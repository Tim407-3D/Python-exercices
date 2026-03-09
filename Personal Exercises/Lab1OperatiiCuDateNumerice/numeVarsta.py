date={"Nume":[],"Varsta":[]}
def addPersoane():
    while True:
        numeNou=str(input("Introdu numele: "))
        if numeNou.isalpha():
            break
        else:
            print("Numele trebuie sa fie format doar din litere!")
    while True:
        varstaNoua=str(input("Introdu varsta: "))
        if varstaNoua.isdigit():
            break
        else:
            print("Varsta trebuie sa fie un numar!")

    anNastere = 2026 - int(varstaNoua)
    print(f"Ceau {numeNou} Deci te-ai nascut in {anNastere}")
    return anNastere

print(addPersoane())
