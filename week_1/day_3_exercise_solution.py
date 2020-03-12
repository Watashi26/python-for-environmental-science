# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 09:51:33 2018

@author: Florian Ulrich Jehn
"""

# Exercise 1
def calc_base(vol, height):
    """
    Calculates the length of one side of the base of a rectangular pyramid,
    given the volume and height.
    """
    return math.sqrt((3 * vol) / height)

print(calc_base(1000, 18))


# Exercise 2
def largest_of_three(a,b,c):
    """
    Tells you which was the largest of the three numbers it is provided with
    """
    print("The largest of a, b and c is " + str(max(a,b,c)))
    
largest_of_three(1,3,4)


# Exercise 3
def in_range(a,b,c):
    """Checks if a is between b and c"""
    return (a < b and a > c) or (a > b and a < c)

print(in_range(5, 1, 10))
print(in_range(5, 10, 1))
print(in_range(5, 10, 12))


# Exercise 4
def reverse_string(word):
    """Reverses the given string and returns it"""   
    new_string = ""
    index = len(word)
    while index > 0:
        index -= 1
        new_string += word[index]
    return new_string

reverse_string("bla")


# Exercise 5
def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod
def a(x, y):
    x = x + 1
    return x * y
def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square
x = 1
y = x + 1
print(c(x, y+3, x+y))


# Exercise 6
def adder():
    """Adds all the numbers the user gives until "done" is typed."""
    print("Type a number or 'done' when finished")
    result = 0
    while True:
        try:
            val = input("Please give input: ")
            if val == "done":
                break
            else:
                result += float(val)
        except ValueError:
            print("Wrong input type")
    return result
print("The result is: " + str(adder()))


# Exercise 7
def collatz(number):
    """Creates the next number in a Collatz sequence"""
    if number % 2 == 0:
        return int(number / 2)
    else:
        return int(3 * number + 1)

def prompt_and_run():
    """
    Prompts the user for a starting number for the Collatz sequence and 
    prints the sequence.
    """
    number = int(input("Please provide a starting number (int): "))
    print(number)
    while number > 1:
        number = collatz(number)
        print(number)
        
prompt_and_run()


# Exercise 8
n = int(input("Which element of the Fibonacci sequence do you want to calculate?\nPut in here (int): "))

def fibonacci(n):
    """
    Calculates the Fibonacci sequence to the nth number
    """
    if n <= 2:
        print (1)
    last = next_to_last = 1
    for i in range(2, n):
        result = last + next_to_last
        next_to_last = last
        last = result
    print(last)

fibonacci(n)
      
    
# Exercise 9
import random
def random_num():
    """Creates a random number between 10 and 100"""
    return random.randint(10, 101)

def check_num(num):
    """Checks if num is smaller than 20"""
    return num < 20

def printer(bool_val):
    """Prints 1 or 0 depending on bool_val""" 
    if bool_val:
        print("1")
    else:
        print("0")
    
for i in range(10):
    printer(check_num(random_num()))
