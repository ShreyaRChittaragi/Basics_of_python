#For loops in python are used to iterate over a sequence (like a list, tuple, dictionary, set, or string) or other iterable objects.
#The for loop in Python is used to execute a block of code a fixed number of times.
#Basic for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit is:", fruit)
print("Finished iterating over fruits!")

#Nested for loop
for i in range(3):
    for j in range(2):
        print("Outer loop i:", i, "Inner loop j:", j)
print("Finished nested loops!")

#For loop with else
for num in range(3):
    print("Number is:", num)
else:
    print("Loop ended, all numbers have been printed.")

#Using break statement in for loop
for i in range(10):
    if i == 5:
        print("Breaking the loop at i =", i)
        break
    print("i is:", i)
print("Exited the loop.")

#Using continue statement in for loop
for j in range(5):
    if j == 3:
        print("Skipping the iteration at j =", j)
        continue
    print("j is:", j)
print("Finished continue example.")

#Using pass statement in for loop
for k in range(3):
    if k == 1:
        pass  # Placeholder for future code
    print("k is:", k)
print("Finished pass example.")

#Using range() function in for loop
for num in range(1, 6):  # Generates numbers from 1 to
    print("Number from range is:", num)
print("Finished range example.")

#Iterating over a string
for char in "hello":
    print("Character is:", char)
print("Finished iterating over string.")

#Iterating over a dictionary
my_dict = {"a": 1, "b": 2, "c": 3}
for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
print("Finished iterating over dictionary.")

#Using enumerate() in for loop
my_list = ['x', 'y', 'z']
for index, value in enumerate(my_list):
    print("Index:", index, "Value:", value)
print("Finished enumerate example.")

#Using zip() in for loop
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for num, char in zip(list1, list2):
    print("Number:", num, "Character:", char)
print("Finished zip example.")

#for loops with Range and step
for i in range(0, 10, 2):  # From 0 to 10 with step of 2
    print("i with step is:", i)
print("Finished range with step example.")

#Double lists with for loop
doubles = [x * 2 for x in range(5)]
print("Doubled values are:", doubles)

#List comprehension with for loop
l=[1,2,3,4,5]
dl=[item * 2 for item in l]
print("List comprehension doubled values are:", dl)

#double only even numbers
deven=[item ** 2 for item in l if item % 2 == 0]
print("Doubled even numbers are:", deven)

#Dictionary comprehension with for loop
names=['Alice', 'Bob', 'Charlie']
d = {name: len(name) for name in names}
print("Dictionary comprehension result is:", d)

cp={
    "Bengaluru" : 84,
    "Mysuru" : 57,
    "Hubbali": 18,
    "Shimoga": 85
}

lc=[city for city in cp if cp[city]>50]
print("Cities with postal code greater than 50 are:", lc)