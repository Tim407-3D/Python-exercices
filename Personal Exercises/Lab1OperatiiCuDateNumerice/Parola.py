goodPassord=int("7710")

parolaUtilizator=int(input("Introdu parola: "))

if parolaUtilizator==goodPassord:
    print("Parola corecta")
else:
    print("Diferenta dintre parola introdusa si cea corecta:", goodPassord-parolaUtilizator)