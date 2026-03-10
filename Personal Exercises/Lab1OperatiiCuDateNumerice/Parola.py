goodPassord=int("7710")
attempts=3
for i in range(attempts):
    parolaUtilizator=input("Introdu parola: ")
    if not parolaUtilizator.isdigit():
        print("Error: Parola trebuie sa fie un numar pozitiv.")
        continue
    parolaUtilizator=int(parolaUtilizator)

    if parolaUtilizator==goodPassord:
        print("Parola corecta")
        break

    else:
        print("Diferenta dintre parola introdusa si cea corecta:", goodPassord-parolaUtilizator)
    
    if i == attempts - 1:
        print("Ati epuizat toate incercarile")
        break