# String operations in python 

# 1. String concatenation: Joining two or more strings using the + operator.
str1="Shreya"
str2="R Chittaragi"
full_name=str1+ " " +str2
print(full_name)

#Repition of strings : using * operator
Name="Dhanya "
print(Name*3)

#String methods : built in functions that perform specific operations on strings
#1. Uppercase : converts all the characters to the uppercase by using .upper()
print(full_name.upper())

#2. Lowercase : Converts all the characters to lowercase by using .lower()
print(full_name.lower())

#3. Strip : removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove) by using .strip()
str3="   Hello World!   "
print(str3.strip()) # returns "Hello World!"

#4. Replace : replaces a specified phrase with another specified phrase by using .replace()
print(Name.replace("Dhanya","Vani"))
print(Name.replace("a","o"))

# "''": this is for multi line strings 

#lenghth of the string : using len()
print(len("Shreya R Chittaragi"))

#Indexing of the string : accessing individual characters in a string using their index positions
#indexing starts from 0 and its position starts from 1
str1="Shreya"
print(str1[0]) #index=position-1