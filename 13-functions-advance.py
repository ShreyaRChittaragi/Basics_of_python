#variable length arguments : *args and **kwargs to accept a variable length of arguments .
def func(*args):  #function with variable length positional arguments
    for arg in args:
        print(arg)
func(1, 2, 3)  #calling function with multiple arguments
func('a', 'b', 'c', 'd')  #calling function with multiple string arguments

#variable length keyword arguments : kwargs
def func_kwargs(**kwargs):  #function with variable length keyword arguments
    for key, value in kwargs.items():
        print(f"{key}: {value}")
func_kwargs(name="Alice", age=25)  #calling function with keyword arguments
func_kwargs(city="New York", country="USA", profession="Engineer")  #calling function with more keyword arguments

#for args : you will use only one asterisk (*) before the parameter name to indicate that it can accept a variable number of positional arguments.
#for kwargs : you will use two asterisks (**) before the parameter name to indicate that it can accept a variable number of keyword arguments.

#Lambda functions : anonymous functions defined using the lambda keyword.
#syntax : lambda arguments: expression

#example of lambda function to add two numbers
add=lambda a,b: a+b  #lambda function to add two numbers
result=add(4,6)  #calling lambda function
print("Sum using lambda:", result)  #printing the result

double =lambda x: x*2  #lambda function to double a number
print("Double of 5 is:", double(5))  #calling lambda function

#lambda for dictionary sorting
data = {'apple': 3, 'banana': 1, 'cherry': 2}
sorted_data = dict(sorted(data.items(), key=lambda item: item[1]))  #sorting dictionary by values using lambda
print("Sorted dictionary by values:", sorted_data)  #printing sorted dictionary