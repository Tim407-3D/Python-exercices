# nr= int(input("Introduceti un numar mai mare decat 0: "))
# # in range de la 0 la nr+1 cu pas de 2 (doar nr pare )
# for i in range(0,nr+1,2):
#     print(i,end="")

cuv=str(input("Introduceti un cuvant: "))
word=cuv.lower()
print(word.count(word[0]))