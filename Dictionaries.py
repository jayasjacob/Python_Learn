thisdict = {
    "brand": "Hyundai",
    "Model": "Creta",  # creating dictionary
    "Year": "2018"
}
print(thisdict)

print(thisdict["Model"])  # You can access the items of a dictionary by referring to its key name, inside square
# brackets

print(thisdict.get("brand"))  # same as before to get values

thisdict["Year"] = 2019  # You can change the value of a specific item by referring to its key name:
print(thisdict)

for x in thisdict:  # will return keys of the dictionary
    print(x)

for y in thisdict:  # return values from dict
    print(thisdict[y])

for z in thisdict.values():  # You can change the value of a specific item by referring to its key name
    print(z)

for a, b in thisdict.items():  # Loop through both keys and values, by using the items() method
    print(a, b)
if "Model" in thisdict:  # checking key is there or not
    print("Yes model is there")

thisdict["Color"] = "White"  # Adding new ite,
print(thisdict)

thisdict.pop("Model")  # The pop() method removes the item with the specified key name
print(thisdict)

thisdict.popitem()  # The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead)
print(thisdict)

del thisdict['Year']  # The del keyword removes the item with the specified key name
print(thisdict)

thisdict.clear()
print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

mydict = thisdict.copy()  # Make a copy of a dictionary with the copy() method:
print(mydict)

# nested dictionaries

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)

dict_1 = dict(brand = "Hyundai", model = "creta", year = 2019)  # using dict constructor
print(dict_1)
