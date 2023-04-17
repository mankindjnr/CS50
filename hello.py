# accepting input and displaying the input - chaining the methods on the string
name = input("What's your name? ").strip().title()

# splitting users name into first and last name, whats in the " "is the delimeter
first, last = name.split(" ")

#output the first name
print(f"first name is, {first}")

# strip removes whitespaces from the string
#name = name.strip()

#capitalizing a string very first character
# name = name.capitalize()

# this capitalizes every word in the string
#name = name.title()

# format string
print(f"hello, {name}")


#or
"""
print("hello", name)
print("hello " + name)
print("hello", end=' ')
print(name)
"""
