nrParticipanti=input("Introduceti numarul de participanti: ")
nrParticipanti=int(nrParticipanti)
listaVarste=[]
while True:
    for i in range(nrParticipanti):
        varsta=input(f"Introduceti varsta participantului {i+1}: ")
        if varsta.isdigit():
            listaVarste.append(int(varsta))
        else:
            print(f"Nu ati introdus un numar intreg pentru participantul {i+1}")
            varsta=input(f"Introduceti varsta participantului {i+1}: ")
            listaVarste.append(int(varsta))
            
    break
def medieParticipanti():
    return sum(listaVarste)/len(listaVarste)
    
       
print(f"Varste Introduse: {listaVarste}")
print(f"Media varstelor este: {medieParticipanti()}")    