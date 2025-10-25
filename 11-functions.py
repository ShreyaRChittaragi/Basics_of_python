#Python , Functions are reusable blocks of code that perform a specific task. They help in organizing code, improving readability, and reducing redundancy
#Defining a function
def greet():
    print("Hello, Good morning!")   #defining a function named greet
    #calling the function 
greet()
greet()

#Function parameters : Parameters are variables that act as placeholders for the values that are passed to a function when it is called.
def greet(boy,girl):  #function with parameters
    print(f"{boy} said hello to {girl}")  #using parameters in function
greet("John","Alice")  #positional arguments
greet("Ashwin","Sonia")

#keyword arguments
greet(girl="Emma", boy="Liam")
#Default parameters
def greet(name="Guest"):  #function with default parameter
    print(f"Hello, {name}!")  #using parameter in function
greet()  #calling function without argument
greet("David")  #calling function with argument

#Real life example of function
def tables(num):  #function to print multiplication table
    for i in range(1, 11):
        print(f"{num}x{i}={num*i}")
tables(5)  #printing multiplication table of 5
tables(8)  #printing multiplication table of 8

#Default mutable parameters
def marriage(boy,girl="Girl"):
    print(f"{boy} is going to marry {girl}")
marriage("John","Emma")  #both arguments provided
marriage("Mike")  #only one argument provided, uses default

#Why return statements are used in functions
def add(a,b):
    return a+b  #returning the sum of a and b
result=add(3,5)  #calling function and storing return value
print("Sum is:", result)  #printing the result

#Local and global variables
x=10  #global variable
def func():
    y=5  #local variable
    print("Inside function, y is:", y)
    print("Inside function, x is:", x)  #accessing global variable
func()
print("Outside function, x is:", x)
# print("Outside function, y is:", y)  #this will raise an error as y is local to func()
#Using global keyword
def modify_global():
    global x  #declaring x as global
    x=20  #modifying global variable
    print("Inside function, modified x is:", x)
modify_global()
print("Outside function, modified x is:", x)
