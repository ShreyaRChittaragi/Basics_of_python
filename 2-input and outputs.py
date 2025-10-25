# input : int input , output : Print 
print("Shreya R Chittaragi")
age=input("Enter your age :")
print(age)

bname=input("enter the boy's name :")
bage=input("enter the boy age :")
gname=input("enter the girl's name :")
gage=input("enter the Girl's age :")
#concatenation : concating the strings that is : Adding the things together
print(bname + " hates " + gname)
age_diff=int(bage)-int(gage)
print("The age difference is : ", age_diff)

#Formatted string: f
print(f"{bname} hates {gname}")
print(f"The age difference is : {age_diff}")

#abs: absolute value : when you want the positive value of a negative number
print("The absolute value of -45 is :",abs(-45))
print("The real value of :",abs(45))

# : Commenting in python
# This is a single line comment
'''This is a 
multi line comment      ----> This is a multi line comment 
'''
"""This is also a
multi line comment      ----> This is also a multi line comment 
"""

# Control slash : \, this is for selecting multiple lines and commenting them at once
# Ctrl + / : for commenting and uncommenting the selected lines