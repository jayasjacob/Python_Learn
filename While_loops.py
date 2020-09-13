i = 1
while i < 6:
    print(i)
    i += 1    #print i as long as its less than 6

i = 1
while i <7:
    print(i)
    if i == 5:
        break  #breaking execution when i =3
    i += 1

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue  # With the continue statement we can stop the current iteration, and continue with the next
    print(i)

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")  # With the else statement we can run a block of code once when the condition no longer is true