f = ["apple", "orange", "mango"]
for x in f:
    print(x)  # prints each fruit

for i in "banana":
    print(i)  # loop through letters

for x in f:
    print(x)
    if x == "orange":
        break  # With the break statement we can stop the loop before it has looped through all the items
for y in f:
    if x == "orange":
        break  # Exit the loop when x is "banana", but this time the break comes before the print
    print(x)

for z in f:
    if z == "orange":
        continue  # With the continue statement we can stop the current iteration of the loop, and continue with the next
    print(z)

for a in range(10):  # To loop through a set of code a specified number of times, we can use the range() function
    print(a)

for a in range(2, 10):
    print(a)  # giving starting number

for x in range(2,20,3):  # Increment the sequence with 3 (default is 1)
    print(x)

for x in range(6):
    print(x)
else:           # The else keyword in a for loop specifies a block of code to be executed when the loop is finished
    print("Done")

adj = ["red","big","tasty"]
fruits = ["apple","banana","cherry"]
for x in adj:
    for y in fruits:   # The "inner loop" will be executed one time for each iteration of the "outer loop
        print(x,y)