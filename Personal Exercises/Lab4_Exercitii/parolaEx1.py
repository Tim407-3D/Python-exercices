username=input("Enter username: ")
def parola_valida():
    if len(password) < 7:
        print("Parola trebuie sa aiba cel putin 7 caractere")
        return False
    if not password[0].isupper():
        print("Parola trebuie sa inceapa cu o litera mare")
        return False
    if not any(char in {"!", "@", "%"} for char in password):
        print("Parola trebuie sa contina cel putin unul dintre urmatoarele caractere: !, @, %")
        return False
    if not any(char.isdigit() for char in password):
        print("Parola trebuie sa contina cel putin un numar")
        return False
    return True

while True:
    password=input("Enter password: ")
    if parola_valida():
        print("Parola este in regula.")
        break
    continue
