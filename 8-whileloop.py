#While loop : The while loop in Python is used to repeatedly execute a block of code as long as a specified condition is true.
count = 0
while count < 5:
    print("Count is:", count)
    count += 1  # Increment the count to avoid infinite loop
print("Finished counting!")

#Nested while loop
outer_count = 0
while outer_count < 3:
    inner_count = 0
    while inner_count < 2:
        print("Outer count:", outer_count, "Inner count:", inner_count)
        inner_count += 1
    outer_count += 1
print("Finished nested loops!")

#While loop with else
num = 0
while num < 3:
    print("Number is:", num)
    num += 1
else:
    print("Loop ended, number is no longer less than 3.")
#Infinite while loop (commented out to prevent actual infinite loop)
# while True:
#     print("This will run forever unless stopped.")
#Break statement in while loop
i = 0
while i < 10:
    if i == 5:
        print("Breaking the loop at i =", i)
        break
    print("i is:", i)
    i += 1
print("Exited the loop.")

#Continue statement in while loop
j = 0
while j < 5:
    j += 1
    if j == 3:
        print("Skipping the iteration at j =", j)
        continue
    print("j is:", j)
print("Finished continue example.")

#Pass statement in while loop
k = 0
while k < 3:
    if k == 1:
        pass  # Placeholder for future code
    print("k is:", k)
    k += 1
print("Finished pass example.")