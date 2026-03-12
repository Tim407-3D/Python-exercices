#Desen 1
# sir01 = [
#     "/","-","\\",
#     "//","_","\\\ ",
#     "--------",
#     "\\\ ","_","//",
#     "\\","-","/"
# ]
# print(f"{sir01[0]}{sir01[1]}{sir01[2]}".center(24))
# print(f"{sir01[3]}{sir01[4]}{sir01[5]}".center(24))
# print(sir01[6].center(24))
# print(f"{sir01[7]}{sir01[8]}{sir01[9]}".center(24))
# print(f"{sir01[10]}{sir01[11]}{sir01[12]}".center(24))

#Desen 2

# sir02=["----",
# "/     \\",
# "/------\\",
# ]

# print(sir02[0].center(24).replace(' ', '_'))
# print(sir02[1].center(24).replace(' ', '_'))
# print(sir02[2].center(24).replace(' ', '_'))


#Desen 3

# sir03=['*',
# '***',
# '*****',
# '*******']
# print(sir03[0].center(24))
# print(sir03[1].center(24))
# print(sir03[2].center(24))
# print(sir03[3].center(24))

string1="/-\\"
string2="//-\\\\"
string3="-------"
#Create an output variable that you can use in order to print the strings centered
output = f"{string1.center(24)}\n{string2.center(24)}\n{string3.center(24)}\n{string2[::-1].center(24)}\n{string1[::-1].center(24)}\n"
print(output)
