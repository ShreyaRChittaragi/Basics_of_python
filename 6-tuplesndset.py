#tuples : you can't change tuples one created (immutable)
name=("Bru","Sugar","Milk","Soppu","Chicken")
print(name)
print(name[0])

#tuple concatenation
t1=(1,2,3)
t2=("a","b","c")
t3=t1+t2
print("Tuple concatenation is :",t3)

#tuple repetition
t4=t1*3
print("Tuple repetition is:",t4)

#tuple membership test
print("Is 2 in t1?:",2 in t1)

#counting elements in tuple
t5=(1,2,2,3,4,2,5)
print("Count of 2 in t5 is:",t5.count(2))

#index of element in tuple
print("Index of element 3 in t5 is:",t5.index(3))

#you can create a tuple in n dimensions
t6=((1,2,3),(4,5,6),(7,8,9))
print("2D Tuple is:",t6)

#Sets : unordered collection of unique elements, mutable (can be changed) , so basically it doesn't have indexing and slicing
s={1,2,3,4,5}
print("Set s is:",s)
s.add(6)
print("Set s after adding 6 is:",s)
s.remove(3)
print("Set s after removing 3 is:",s)
s.discard(10) #doesn't raise error if element not found
print("Set s after discarding 10 is:",s)
s.pop() #removes and returns an arbitrary element i.e, removes a random element
print("Set s after popping an element is:",s)
s.clear() #removes all elements
print("Set s after clearing is:",s)

#sets union and intersection
s1={1,2,3}
s2={3,4,5}
print("Union of s1 and s2 is:",s1 | s2) #or s1.union(s2)
print("Intersection of s1 and s2 is:",s1 & s2) #or s1.intersection(s2)
print("Difference of s1 and s2 is:",s1 - s2) #or s1.difference(s2)
print("Symmetric difference of s1 and s2 is:",s1 ^ s2) #or s1.symmetric_difference(s2)
print("Is s1 a subset of s2?:",s1 <= s2) #or s1.issubset(s2)
print("Is s1 a superset of s2?:",s1 >= s2) #or s1.issuperset(s2)
print("Are s1 and s2 disjoint?:",s1.isdisjoint(s2))
print("s1 after updating with s2:",s1.update(s2)) #or s1|=s2
print(s1)
