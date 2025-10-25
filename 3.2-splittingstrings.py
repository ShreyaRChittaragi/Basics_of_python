#Splitting a string into a list of words
s="this is a computer"
l=s.split()
print("Split string into list:", l)

print("List input practice")
x=input("enter list of integers separated by space:")
int_list=[int(i) for i in x.split()]
print("List of integers:", int_list)

#or
y=input("enter list of strings separated by space:")
str_list=y.split()
print("List of strings:", str_list)
