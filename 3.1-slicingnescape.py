#String slicing : extracting a portion of a string by specifying a range of indices
#syntax : string[start:end] (includes start index but excludes end index)
str1="Shreya R Chittaragi"
print(str1[0:6]) #output: Shreya (index 0 to 5)
print(str1[7:])  #output: R Chittaragi (from index 7 to end)
print(str1[:6])  #output: Shreya (from start to index 5)
print(str1[-8:]) #output: Chittaragi (last 8 characters)
print(str1[::2]) #output: Seaa htaai (every second character)
print(str1[::-1])#output: igarattihC R ayerhS (reversed string)
#[start:end:step] (step specifies the interval between characters to include)
print(str1[0:12:3]) #output: Sya a (from index 0 to 11, every third character)
print(str1[::3])    #output: Sya a (from start to end, every third character)

#Escape sequences : special characters in strings that are preceded by a backslash (\) to represent certain whitespace or special characters
#Common escape sequences:
#\n : Newline- moves the cursor to the next line
#\t : Tab - adds a horizontal tab space
#\\ : Backslash - allows you to include a literal backslash in the string
#\' : Single quote - allows you to include a single quote in a string enclosed by single quotes
#\" : Double quote - allows you to include a double quote in a string enclosed by double quotes
print("Hello\nWorld")  #output: Hello (newline) World
print("Hello\tWorld")  #output: Hello (tab) World
print("This is a backslash: \\") #output: This is a backslash: \
print('It\'s a beautiful day!') #output: It's a beautiful day!
print("He said, \"Hello!\"") #output: He said, "Hello!"

# Homeworks : 
#1. greeting program with their age printed . 
name= str(input("enter your name"))
age= int(input("enter your age"))
print(f"{name} and their age is : {age}")

#2. string manipulations - uppercase, lowercase , replaces , stripped 

Branch="      Artificial intelligence and machine learning              "
print(Branch.upper())
print(Branch.lower())
print(Branch.replace("Artificial intelligence and machine learning","AIML"))
print(Branch.strip())

#3. Character counter .
Input="Shreya and Dhanya"
print(len(Input))

#4. Escape sequencing : 
print("Hi it's Shreya in here\n who are you ?")