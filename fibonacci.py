#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

n1 = 0
n2 = 1

while True:
    user_input = input("Type how many terms of the Fibonacci sequence you want here (integers only): ")
    try:
        terms = int(user_input)
        if terms <= 0:
            print("Please enter a positive number!")
            continue
        break
    except ValueError:
        print("Invalid input! Please enter an integer.")

if terms == 1:
    print("The sequence is:")
    print(n1)
else:
    print("The sequence is:")
    print(n1)
    print(n2)
    for _ in range(2, terms):
        nth = n1 + n2
        print(nth)
        n1 = n2
        n2 = nth
