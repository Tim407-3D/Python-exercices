sales = ["apple", "banana", "apple", "orange", "banana", "apple", "strawbery", "ananas"]

# define the variable as the dictionary "={}"
count = {}
# for the existing items in the list, we store them inside of the dictionary
for fruits in sales: 
    # create a statement that will allow the loop to access the items inside the list and update it accordingly
   if fruits in count:
      count [fruits] = count [fruits] +1
      # if items in the list are not duplicating but they are existing define the number of items
   else:
       count[fruits]= 1 
print (count)