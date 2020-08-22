thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")  # creating tuple
print(thistuple)

print(thistuple[1])  # accessing tuple items

print(thistuple[-2])  # negative indexing

print(thistuple[2:5])  # accessing range of items

x = list(thistuple)  # for changing a value, convert the tuple into a list change value and then change it back to tuple
x[1] = "grape"
y = tuple(x)
print(y)

for i in y:  #looping through the tuple
    print(i)

if "apple" in thistuple:     # checking for an item
    print("yes apple is there")

del y # deleting a tuple.Since tuple is unchangable items from tuple is cannot be removed.we can delete an entire tuple.

y = (1,2,3)
tup = thistuple+y # joining two tuples
print(tup)

print(tup.count('apple')) # returns count of specific item

print(tup.index('cherry')) # returns index of specified items
