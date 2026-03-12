cuv=input("Introduceti cuvantul: ")
for letter in cuv.lower():
    if cuv.count(letter) > 1:
        print(letter + " apare de " + str(cuv.count(letter)) + " ori")
    