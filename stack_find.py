stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)
print(stack.sort)
elemnt = int(input("Enter element to find"))
for i in stack:
    if elemnt == i:
        print("element found in ",stack.index(i))