lista = input("Introduceti lista de taskuri: ")
lista_taskuri = lista.split(",")
print (lista_taskuri)
for task in lista_taskuri:
    if lista_taskuri.count(task) > 1:
       lista_taskuri.remove(task)
print(f"{lista_taskuri}")
