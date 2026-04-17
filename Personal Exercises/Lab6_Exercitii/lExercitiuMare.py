import random

# Generate a list of random numbers
list_size = random.randint(5, 15)  # Random list size between 5 and 15
numbers = [random.randint(1, 100) for _ in range(list_size)]

def separate_even_odd(numbers):
    even_numbers = []
    odd_numbers = []
    
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    
    return even_numbers, odd_numbers

def bubble_sort(numbers):
    num = len(numbers)
    for i in range(num):
        for j in range(num-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

def minimum_number(numbers):
    min=numbers[0]
    for num in numbers:
        if num < min:
            min=num
    return min

def maximum_number(numbers):
    max=numbers[0]
    for num in numbers:
        if num > max:
            max=num
    return max

even_nums, odd_nums = separate_even_odd(numbers)
bubble= bubble_sort(numbers)
print("Even numbers:", even_nums)
print("Odd numbers:", odd_nums)
print("Bubble sorted:", bubble)
print("Minimum number:", minimum_number(numbers))
print("Maximum number:", maximum_number(numbers))
