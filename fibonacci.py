#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

n1 = 0
n2 = 1

terms = int(input("Type how many terms of the Fibonacci sequuence you want here (integers only):"))
if terms <=0:
  print("Please enter a positive number!")
elif terms ==1:
  print("With that many terms the sequence equals")
  print(n1)
else:
  print("The sequence is:")
  for _ in range(2, terms):
     nth = n1+n2
     print(nth)
     n1 = n2
     n2 =nth
