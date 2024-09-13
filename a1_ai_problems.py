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

1. Basic Syntax and Variables
Write a Python program that declares a few variables of different types (integer, float, string, and boolean). Print these variables and their types to the console.


Absolutely! Since you already have a background in JavaScript, you'll find that many programming concepts transfer over to Python, though there are some syntactical and idiomatic differences. Here are five questions that will help you get familiar with Python programming:

1. Basic Syntax and Variables
Write a Python program that declares a few variables of different types (integer, float, string, and boolean). Print these variables and their types to the console.



2. Control Structures
Write a Python program that checks if a number is even or odd using an if statement. Then, use a for loop to iterate through a range of numbers from 1 to 10 and print whether each number is even or odd.



3. Functions
Create a Python function that takes two arguments, adds them together, and returns the result. Then, call this function with different pairs of numbers and print the results.



4. Lists and Slicing
Create a Python list with 5 different elements. Use slicing to create a new list that contains only the first three elements. Then, print both the original and sliced lists.



5. Dictionaries and Loops
Create a Python dictionary with three key-value pairs where the keys are strings and the values are integers. Write a loop that iterates over the dictionary and prints each key along with its value.


