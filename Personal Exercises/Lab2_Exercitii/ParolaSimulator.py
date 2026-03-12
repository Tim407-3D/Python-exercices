parola_buna = "7788"
parola = input("Introdu parola: ")

while parola != parola_buna:
    if parola.isdigit():
        print("Parola gresita")
        parola = input("Introdu parola: ")
    else:
        print("Parola trebuie sa fie cifre")
        parola = input("Introdu parola: ")
print("Parola corecta")