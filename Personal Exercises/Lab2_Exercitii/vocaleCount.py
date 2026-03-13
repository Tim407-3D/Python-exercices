cuv= input("Introduceti cuvantul: ")
vocale= "aeiou"
count=0
for i in cuv.lower():
    if i in vocale:
        count+=1
print(f"Numarul de vocale din cuvantul {cuv} este {count}")