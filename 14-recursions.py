#Recursion - a function calling itself is called recursion 
# example: Factorial function
def factorial(n):
    if n == 0 or n == 1:  #base case
        return 1
    else:
        return n * factorial(n - 1)  #recursive case
number = 5
result = factorial(number)  #calling the recursive function
print(f"Factorial of {number} is: {result}")  #printing the result

#Recursion example: Fibonacci series
def fibonacci(n):
    if n <= 0:  #base case
        return 0
    elif n == 1:  #base case
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  #recursive case
terms = 10
print(f"Fibonacci series up to {terms} terms:")
for i in range(terms):
    print(fibonacci(i), end=" ")  #printing Fibonacci series
print()

#Recursion example: Sum of natural numbers
def sum_natural(n):
    if n == 1:  #base case
        return 1
    else:
        return n + sum_natural(n - 1)  #recursive case
num = 5
total = sum_natural(num)  #calling the recursive function
print(f"Sum of first {num} natural numbers is: {total}")  #printing the result

#Recursion example: Reverse a string
def reverse_string(s):
    if len(s) == 0:  #base case
        return s
    else:
        return s[-1] + reverse_string(s[:-1])  #recursive case
string = "Hello"
reversed_str = reverse_string(string)  #calling the recursive function
print(f"Reversed string of '{string}' is: '{reversed_str}'")  #printing the result
