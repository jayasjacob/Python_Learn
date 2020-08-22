print(10<9) # returns false
print(10>9) # returns true

# Evaluate values and variables
print(bool(""))
print(bool(9))

class myclass():
    def __len__(self):
        return 0
myobj = myclass()
print(bool(myobj))

def myfucntion():
    return True
print(myfucntion())

def check():
    return True
if check():
    print("Yes")
else:
    print("no")


# check integer or  not
x =200
print(isinstance(x,int)) # if data type is right returns true



