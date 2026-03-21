while True:
    utilizator1= input("Introduceti utilizatorul1: ")
    parola1= input("Introduceti parola1: ")

    utilizator2= input("Introduceti utilizatorul2: ")
    parola2= input("Introduceti parola2: ")

    utilizator3= input("Introduceti utilizatorul3: ")
    parola3= input("Introduceti parola3: ")

    # if utilizator1 == utilizator2 or utilizator1 == utilizator3 or utilizator2 == utilizator3:
    #     print("Utilizatorii trebuie sa fie diferiti")
    #     continue
    # if parola1 == utilizator1 or parola1 == utilizator2 or parola1 == utilizator3:
    #     print("Parolele trebuie sa fie diferite de utilizatori")
    #     continue
        
    dictionar_parole = {
        "utilizator 1": parola1,
        "utilizator 2": parola2,
        "utilizator 3": parola3
    }

    for key, value in dictionar_parole.items():
        print(f"{key}: {value}")
    break
