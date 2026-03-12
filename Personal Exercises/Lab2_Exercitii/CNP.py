import datetime as date
# print(date.datetime.now())
cnp=input("Enter your CNP(7 cifre): ")
cnp_an=int(cnp[1:3])
cnp_gender=int(cnp[0])
#print(cnp_an , cnp_gender)   

if cnp_gender in [1,2]:
    cnp_gender=1900+cnp_an
elif cnp_gender in [3,4]:
    cnp_gender=1800+cnp_an
elif cnp_gender in [5,6]:
    cnp_gender=2000+cnp_an
else:
    print("CNP invalid")
    exit()

birth_date= cnp_gender
today= date.datetime.now().year
age= today - birth_date
print(age)

if age >=18:
    print("You are over 18")
else:
    print("You are under 18")

            
