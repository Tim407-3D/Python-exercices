optiuni={
    "1": "1. Cappuccino....4 lei",
    "2": "2. Espresso....3.50 lei"
}
print(optiuni["1"]+"\n"+optiuni["2"])
alegere=input("Alege optiunea: ")
bancnote=[5,10]
introducere_bani=int(input("Introduceti bancnota: "))
def calcul_rest(rest):  
    return rest

for o in optiuni:
    if o == alegere:
        if o == "1":
            pret=float(4)
            rest=float(introducere_bani-pret)
        elif o == "2":
            pret=float(3.50)
            rest=float(introducere_bani-pret)
        print("Rest:",calcul_rest(rest))

print("Produsul se livreaza...")