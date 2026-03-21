angajat1 = {
'nume': 'Ana-Maria Popescu',
'departament': 'IT',
'ID': 3409,
'Salar': 4560,
}
angajat2 = {
'nume': 'Marian Muntean',
'departament': 'IT',
'ID': 2235,
'Salar': 4556,
}
angajat3 = {
'nume': 'Maria Manea',
'departament': 'HR',
'ID': 1908,
'Salar': 6755}
angajat4 = {
'nume': 'Oana Popa','departament': 'HR',
'ID': 1977,
'Salar': 5400,
}
angajat5 = {
'nume': 'David Codru',
'departament': 'Management',
'ID': 1988,
'Salar': 12900}

lista_dict = [angajat1, angajat2, angajat3, angajat4, angajat5]

for angajat in lista_dict:
    # if angajat['Salar'] > 5000:
    #     print(angajat['nume'], "->", angajat['departament'],angajat['ID'])

    # if angajat['departament'] is not 'Management':
    #     print(angajat['nume'])

    if angajat['departament']=='HR':
        medie_salarii= sum([angajat['Salar'] for angajat in lista_dict if angajat['departament']=='HR']) \
                        / len([angajat for angajat in lista_dict if angajat['departament']=='HR'])
                        
        print("Medie salarii HR:", medie_salarii)