thisset = {'apple', 'banana', 'orange', 'cherry'}  # A set is a collection which is unordered and unindexed. In Python
# sets are written with curly brackets.
print(thisset)

for x in thisset:  # You cannot access items in a set by referring to an index, since sets are unordered the items has no index.
    print(x)

print('banana' in thisset)  # returns true is banana is present in the set

thisset.add("mango")  # to add one item to set use add method
print(thisset)

thisset.update(['rambuttan', 'grape'])  # Add multiple items to a set, using the update() method:
print(thisset)

thisset.remove('banana')  # To remove an item in a set, use the remove(), or the discard() method.
print(thisset)

thisset.discard('apple')  # To remove an item in a set, use the remove(), or the discard() method.
print(thisset)  # If the item to remove does not exist, discard() will NOT raise an error.

thisset.pop()  # removes last item
print(thisset)

set_1 = {"a", "b", "c"}
set_2 = {1, 2, 3, 4}
set_3 = set_1.union(set_2)  # The union() method returns a new set with all items from both sets
print(set_3)

set_1.update(set_2)  # The update() method inserts the items in set2 into set1
print(set_1)  # Both union() and update() will exclude any duplicate items.

print(set_1.difference(set_2))  # Returns a set containing the difference between two or more sets

print(set_1.intersection(set_3))  # Returns a set, that is the intersection of two other sets
