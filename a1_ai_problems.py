# Complete your individualized AI problems here

def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"

#1. Basic Syntax and Variables
#Write a Python program that declares a few variables of different types (integer, float, string, and boolean). Print these variables and their types to the console.

def variables(var):
    if(type(var)==int):
        print(str(var) + " is an integer.")
    if(type(var)==str):
        print(var + " is a string.")
    if(type(var)==bool):
        print(str(var) + " is a boolean.")
    if(type(var)==float):
        print(str(var) + " is a float.")
variables(3)
variables("hello")
variables(True)
variables(3.14)

#2. Control Structures
#Write a Python program that checks if a number is even or odd using an if statement. Then, use a for loop to iterate through a range of numbers from 1 to 10 and print whether each number is even or odd.

def even_odd(num):
    if(num%2 == 0):
        print(str(num) + " is even.")
    else:
        print(str(num) + " is odd.")
even_odd(5)
even_odd(6)

#3. Lists and Slicing
#Create a Python list with 5 different elements. Use slicing to create a new list that contains only the first three elements. Then, print both the original and sliced lists.

my_list = [1, 2, 3, 4, 5]
def slice(lst):
    first_three = lst[:3]
    print(lst)
    print(first_three)
slice(my_list)
