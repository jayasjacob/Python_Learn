thisset = {'apple', 'banana', 'orange', 'cherry'}  # A set is a collection which is unordered and unindexed. In Python
# sets are written with curly brackets.
print(thisset)

for x in thisset:  # You cannot access items in a set by referring to an index, since sets are unordered the items has no index.
    print(x)

print('banana' in thisset)  # returns true is banana is present in the set

thisset.add("mango") # to add one item to set use add method
print(thisset)

thisset.update(['rambuttan','grape']) # Add multiple items to a set, using the update() method:
print(thisset)

thisset.remove('banana') # To remove an item in a set, use the remove(), or the discard() method.
print(thisset)

thisset.discard('apple')  # To remove an item in a set, use the remove(), or the discard() method.
print(thisset)     # If the item to remove does not exist, discard() will NOT raise an error.

thisset.pop()  #removes last item
print(thisset)