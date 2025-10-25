#operators in python - Arithmetic, Assignment, Comparison, Logical, Identity, Membership, Bitwise
# Arithmetic Operators
a=10
b=40
print("a + b=",a+b) #Addition
print("a - b=",a-b) #Subtraction
print("a * b=",a*b) #Multiplication
print("a / b=",a/b) #Division
print("a % b=",a%b) #Modulus
print("a ** b=",a**b) #Exponentiation
print("a // b=",a//b) #Floor Division

#Assignment oprators : +=, -=, *=, /=, %=, //=, **=
c=10
c+=5  #c=c+5
print("c after c+=5 is:",c)
c-=3  #c=c-3
print("c after c-=3 is:",c)
c*=2  #c=c*2
print("c after c*=2 is:",c)
c/=4  #c=c/4
print("c after c/=4 is:",c)
c%=3  #c=c%3
print("c after c%=3 is:",c)
c**=2 #c=c**2
print("c after c**=2 is:",c)
c//=2 #c=c//2
print("c after c//=2 is:",c)

#Comparison operator : ==,!=, >, <, >=, <=
x=10
y=20
print("x==y:",x==y)   #False
print("x!=y:",x!=y)   #True
print("x>y:",x>y)     #False
print("x<y:",x<y)     #True
print("x>=y:",x>=y)   #False
print("x<=y:",x<=y)   #True

#Logical operators : and, or, not
m=12
n=15
print("m>10 and n>10:",m>10 and n>10) #True
print("m>10 or n<10:",m>10 or n<10) #True
print("not(m>10):",not(m>10)) #False
print("not(n<10):",not(n<10)) #True

#Identity operators : is, is not
p=[1,2,3]
q=p
r=[1,2,3]
print("p is q:",p is q)       #True (same object)
print("p is r:",p is r)       #False (different objects with same content)
print("p is not r:",p is not r) #True
print("p is not q:",p is not q) #False
print("p==r:",p==r)           #True (same content)
print("p!=r:",p!=r)           #False (same content)
print("p==q:",p==q)           #True (same content)
print("p!=q:",p!=q)           #False (same content)
print("id(p):",id(p))         #Memory address of p
print("id(q):",id(q))         #Memory address of q (same as p)
print("id(r):",id(r))         #Memory address of r (different from p and q)
print("id(p)==id(q):",id(p)==id(q)) #True
print("id(p)==id(r):",id(p)==id(r)) #False

#Membership operators : in, not in
s="Shreya R Chittaragi"
s2="Shanya"
print("'Shreya' in s:",'Shreya' in s)       
print(("s" in s)and ("R" in s))
print("'Shanya' not in s:",'Shanya' not in s)

#bitwise operators : &, |, ^, ~, <<, >>
a=10  #Binary: 1010
b=4   #Binary: 0100
print("a & b:",a & b)   #Binary: 0000 (Decimal: 0)
print("a | b:",a | b)   #Binary: 1110 (Decimal: 14)
print("a ^ b:",a ^ b)   #Binary: 1110 (Decimal: 14)
print("~a:",~a)         #Binary: -1011 (Decimal: -11)
print("b << 1:",b << 1) #Binary: 1000 (Decimal: 8)
print("b >> 1:",b >> 1) #Binary: 0010 (Decimal: 2)