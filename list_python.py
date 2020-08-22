list_1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]  # creates a list
print(list_1)

print(list_1[1])  # accessing list item

print(list_1[-1])  # negative indexing

print(list_1[2:5])  # range of indexes When specifying a range,
# the return value will be a new list with the specified items.

print(list_1[:4])  # if leaves first value range will start from beginning

print(list_1[-4:-1])  # negative range

list_1[2] = "rambuttan"  # changing value of the list
print(list_1)

for i in list_1:  # looping through list
    print(i)

if "apple" in list_1:  # check if item exist
    print("yes, apple is there")
else:
    print("No")

print(len(list_1))  # return length of list

list_1.append("grapes")  # add item in the last
print(list_1)

list_1.insert(3, "guava")  # add item in a specified location
print(list_1)

list_1.remove("banana")  # removes an item
print(list_1)

list_1.pop()  # The pop() method removes the specified index, (or the last item if index is not specified):
print(list_1)

del list_1[0]  # The del keyword removes the specified index
print(list_1)

del list_1  # The del keyword can also delete the list completely:

list_1 = ['apple', 'banana', 'rambuttan', 'guava', 'orange', 'kiwi', 'melon', 'mango', 'grapes']
list_1.clear()  # he clear() method empties the list
print(list_1)

list_main = list_1 = ['apple', 'banana', 'rambuttan', 'guava', 'orange', 'kiwi', 'melon', 'mango', 'grapes']
list_2 = list_main.copy()  # copies list main to list 2
print(list_2)

list_3 = list(list_2)  # Another way to make a copy is to use the built-in method list().
print(list_3)

list_4 = ["a", "b", "c"]
list_5 = list_4 + list_3  # join two lists
print(list_5)

for x in list_4:  # Another way to join two lists are by appending all the items from list2 into list1, one by one:
    list_5.append(x)
print(list_5)

l = ['c','d','e']
a = [1,2,3,4]
a.extend(l)  # Use the extend() method to add list2 at the end of list1:
print(a)
