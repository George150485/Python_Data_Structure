#Lists and Tuples
#Tuples are ordered sequence
#allowing multiple types of variables
tuple = (19, 2, 33,343,12,4)
print(tuple)
print(type(tuple))
#like a dictionary a tuple has a key that is
#the index and the value
#slice a tuple
print(tuple[1:3])
print(len(tuple))
#sorted tuple but it has to have the same
#datatype in the tuple
print(sorted(tuple))
#lists
#ordered squence
list = [10,3,5, "string", ("tuple_member0", "tuple_member1")]
print(list)
print(list[4][1])
#lists are mutable but tuples are not
#Deleting a member using the delete frunction
del(list[4])
print(list)
#Dictionary
#Key and Value
dictionary = {"key1":10, "key1":10}
print(dictionary["key1"])
print(dictionary)
print(dictionary.keys())
#Sets
list=["Pop", "Pop", "NotPop"]
set = set(list)
print(list)
print(set)
print("Pop" in set)