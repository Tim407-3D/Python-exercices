text = """In primavara anului 1894, toata Londra a fost interesata, iar lumea la moda a fost consternata de
uciderea onorabilului Ronald Adair in circumstante cele mai neobisnuite si inexplicabile...
Chiar si acum, dupa acest interval lung, ma trezesc emotionat cand ma gandesc la asta si simt din nou acel
potop brusc de bucurie, uimire si neincredere care mi-a cufundat cu totul mintea."""

litera = input("Introduceti o litera: ")

numartext = text.lower().count(litera.lower())
print(f"Litera '{litera}' apare de {numartext} ori in text.")

lista_cuvinte=text.split()
print(lista_cuvinte)

for cuvant in lista_cuvinte:
    if cuvant.startswith('s'):
        count = cuvant.count('s')
        print(f"Cuvantul '{cuvant}' contine {count} litera 's'")
    