'''
#PYTHON FUNCTION
def nama(name):
    print("Hello " + name)

nama("John")

#Masukin nilai parameter dalam fungsi

def my_function(child3, child2, child1):
    print("The youngest child is " + child3)
my_function(child1="Emil", child2="Tobias", child3="Linus")

def my_function(x):
    return 5 * x

print(my_function(3)) #15
print(my_function(5)) #25
print(my_function(9)) #45
'''

'''
#PYTHON DICTIONARY

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

# Accessing items:
x = thisdict["model"]

# Change value:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2018

# Loop through a dictionary:
for x in thisdict:
    print(x)

'''