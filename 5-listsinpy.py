#Collection of items in python - lists, tuples, sets, dictionaries
#1. Lists : ordered, mutable (changeable), allows duplicate elements

items=["Bru","Sugar","Milk","Soppu","Chicken"]
print(items)

#indexing 
print(items[0])
print(items[-1])

#Lists can contain whatever the data types you want : jaise ki string, int, float, boolean, list, tuple, set, dictionary
l=[1,"Bru",True,[1,2,3],34.78]
print(l)
 
#poping 
print("popping from the list:")
print(items)
items.pop()
print(items)
items.pop(1)
print(items)

#appending
print("appending to the list:")
items.append("Eggs")
print(items)
print("Indexing after appending:")
items.insert(1,"Bread")
print(items)

#removing
print("removing from the list:")
items.remove("Milk")
print(items)

#clearing : removes all elements from the list
l.clear()
print("cleared l: ",l)

items[0]="Coffee powder"
print(items)

#slicing
print("Slicing the list:")
print(items[1:4]) #index 1 to 3
print(items[:3])  #start to index 2
print(items[2:])  #index 2 to end
print(items[-3:]) #last 3 elements
print(items[::2]) #every second element
print(items[::-1])#reversed list
print(items[0:5:2]) #index 0 to 4, every second element

#length of the list
print("Length of items list is:",len(items))

#sorting the list
numbers=[5,2,9,1,5,6]
print("Original numbers list:",numbers)
numbers.sort()
print("Sorted numbers list:",numbers)

#sorted function : returns a new sorted list without modifying the original
unsorted_numbers=[3,8,1,4,7]
sorted_numbers=sorted(unsorted_numbers)
print("Original unsorted_numbers list:",unsorted_numbers)
print("New sorted_numbers list:",sorted_numbers)

