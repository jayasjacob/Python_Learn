a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua"""

b = "  Hellp, world!   "
print(a)
# strings are arrays of bytes representing unicode characters

print(a[2])  # getting characters using array
print(b[2:10])  # slicing getting range of characters
print(b[-5:-2])  # negative indexing, counting from the end of the string
print(len(a))  # getting the length

print(b.strip())  # strip function removes any whitespace from the beginning to the end
print(b.upper())  # upper function converts everything to uppercase
print(b.replace("lp", "ao"))  # replaces a string with another string
print(b.split())  # split the string into substring is if finds instances of the separator

# check string
txt = "hello are you there in the kitchen"
x = "abc" not in txt  # return true or false string is there or not
print(x)

# concatenation
a = "Hello"
b = "world"
print(a+b)

# format

x = 30
txt = "my name is jayas and i am {}"
print(txt.format(x))  # format place the passed argument in the place of {}

quantity = 20
itemno = 234
prince = 60.5
txt = "the quantity {} of item number {} with price {} is good"
print(txt.format(quantity,itemno,prince))

txt = "i want to pay {2} dollars for item {0} in the quantity {1}"
print(txt.format(itemno,quantity,prince))

# Escape Charchter
txt = "the group of peopls is called \"Vikings\" from the north"
print(txt)


