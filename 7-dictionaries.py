#dictionary: unordered, mutable (changeable), no duplicate elements, you can retrieve and manipulate data using keys
Birthday={
    "Shreya" : "25th febrauary",
    "Dhanya" : "3rd May",
    "Vani" : "20th september",
    "Rajashekhar": "7th october"
}
print(type(Birthday)) #prints the type of the data structure

print("Shreya's birthday is on:",Birthday["Shreya"])

#using get : if key not found, returns None instead of error
print("Sudeep's birthday is on:",Birthday.get("Sudeep","Not found"))
 
#Adding and updating the dictionary
Birthday["Sudeep"]="15th August" #adding new key-value pair
print("Birthday dictionary after adding Sudeep:",Birthday)
Birthday["Dhanya"]="4th May" #updating existing key-value pair
print("Birthday dictionary after updating Dhanya:",Birthday)

#Removinng elements from the dictionary : pop,popitem,delete,clear
Birthday.pop("Vani") #removes key "Vani"
print("Birthday dictionary after popping Vani:",Birthday)
Birthday.popitem() #removes last inserted key-value pair
print("Birthday dictionary after popping last item:",Birthday)
del Birthday["Rajashekhar"] #removes key "Rajashekhar"
print("Birthday dictionary after deleting Rajashekhar:",Birthday)
x= Birthday.clear() #removes all key-value pairs
print("Birthday dictionary after clearing all items:",x)
print(Birthday)

meanings={
    "Python":"A high-level programming language",
    "Dictionary":"A collection of key-value pairs",
    "List":"An ordered collection of items",
    "Tuple":"An immutable ordered collection of items"
}
print("meanings dictionary is :",meanings)
print(" The keys are :",meanings.keys()) #prints all keys
print(" The values are :",meanings.values()) #prints all values
print(" The items are :",meanings.items()) #prints all key-value pairs as tuples

#updating dictionary using update()
meanings.update({"Set":"An unordered collection of unique items"})
print("meanings dictionary after updating with Set:",meanings)

#why dictionaries are important ?
#1. Fast lookups : O(1) average time complexity for lookups using keys
#2. Flexible data representation : can represent complex data structures
#3. Easy to use : intuitive syntax for adding, updating, and retrieving data
#4. Widely used : used in various applications like databases, caching, configuration management, etc.
#5. Dynamic sizing : can grow and shrink as needed without predefined size
#6. Built-in methods : provides various built-in methods for easy manipulation of data
#you can create list of dictionaries . 

items1={
    "name":"Bru",
    "weight":500,
    "price":250,
}
print("Item details are :",items1)
items2={
    "name":"Sugar",
    "weight":1000,
    "price":40,
}
itemsn=[items1,items2]
print(f"Total weight of {itemsn[0]['name']} and {itemsn[1]['name']} is:",itemsn[0]['weight']+itemsn[1]['weight'])