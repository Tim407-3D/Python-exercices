date= {"Baze": [] ,"Height": [] }

def updateData(arie):

    while True:
        newBase= (input ("Enter the base of the Triangle:"))
        if newBase.isnumeric:
            break
        else:
            print ("Error the value is not numeric.Try again.")


    while True:
        newHeigth=(input("enter the Height of the Triangle:"))
        if newHeigth.isnumeric:
            break
        else:
            Print("Error the value is not numeric.Try again.")

    arie=1/2* newBase*newHeigth
    result=arie
    Print(result)
    return result


