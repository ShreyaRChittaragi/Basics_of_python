#Nested functions : Functions defined inside other functions are called nested functions or inner functions. They can access variables from the enclosing function's scope.
def outer_function(text):  #outer function
    def inner_function():  #inner function
        print(text)  #inner function accessing variable from outer function
    inner_function()  #calling inner function
outer_function("Hello from nested function!")  #calling outer function

#Example of nested function to calculate square and cube
def calculate_power(num):  #outer function
    def square():  #inner function to calculate square
        return num * num
    def cube():  #inner function to calculate cube
        return num * num * num
    sq = square()  #calling inner function square
    cu = cube()  #calling inner function cube
    return sq, cu  #returning results
number = 3
squared, cubed = calculate_power(number)  #calling outer function
print(f"Square of {number} is: {squared}")  #printing square
print(f"Cube of {number} is: {cubed}")  #printing cube
