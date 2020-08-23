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
