while True:
    number=input("Enter a number: ")

    def calculate_power(number):
        if number.isdigit():
            number = int(number)
            result = number ** number
            print(f"{number} la puterea {number} = {result}")
        else:
            print("Please enter a valid number")    

        if number == "q":
            print("Goodbye!")
            exit()
    calculate_power(number)
