#!/usr/bin/env python3
fib = 0
while (True):
  num = int(input("User input: "))
  if num >= 0:
    break
  else: print("Expected output: Please enter a positive integer.")

if num == 0:
  print("0")
if num == 1:
  print("1")

first, second = 0, 1
print(first, end=" ")
print(second, end=" ")
for i in range(2, num):
        total = first + second
        print(total, end=" ")
        first, second = second, total


# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.
