# Dictionaries in Python 

person = {
    "name": "Alex Jones",
    "age": 35,
    "email": "alex@jones.com"
}

print("Person Dictionary:", person)

# Accessing elements of dictionary
print("Name:", person["name"])
print("Age:", person["age"])
print("Email:", person["email"])

# Adding new field
person["occupation"] = "Software Developer"
print("\nAfter adding occupation:", person)

# Updating values
person["age"] = 31
print("New age:", person)

person["occupation"] = "Electrical Engineer"
print("New occupation:", person)

# Deleting an element
del person["email"]
print("After removing email:", person)

# Cycling through a dictionary
for key, value in person.items():
    print(f"{key}: {value}")

# Check if a key exists
print("\nIs 'name' key present?", "name" in person)


print("Occupation:", person.get("occupation", "Not Specified"))

# Another way to create dictionaries (storing squares with each index)
squares = {x: x*x for x in range(6)}
print("\nSquares dictionary:", squares)