# Using if-else statements to make decisions based on conditions
#if statement : thus is used to test a specific condition. If the condition evaluates to True, the block of code within the if statement is executed
num=int(input("Enter a number: "))
if num%2==0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")

# elif statement : used to test multiple conditions sequentially. If the initial if condition is False, the program checks the elif condition. If it evaluates to True, the corresponding block of code is executed. You can have multiple elif statements to handle various conditions
marks=int(input("Enter your marks: "))
if marks>=90:
    print("Grade: A")
elif marks>=80:
    print("Grade: B")
elif marks>=70:
    print("Grade: C")
elif marks>=60:
    print("Grade: D")
else:
    print("Grade: F")

# nested if-else : An if-else statement can be nested within another if or else block. This allows for more complex decision-making by creating a hierarchy of conditions
age=int(input("Enter your age: "))
if age>=18:
    print("You are eligible to vote.")
    citizenship=input("Are you a citizen? (yes/no): ").lower()
    if citizenship=="yes":
        print("You can register to vote.")
    else:
        print("You must be a citizen to vote.")
else:
    print("You are not eligible to vote yet.")
    