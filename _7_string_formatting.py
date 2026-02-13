# String formatting
""" string formatting simplifies the concatenation. it increases the readability of code and type conversion is
    not required. """

# Add placeholder
""" Add placeholder '{}' where string needs to be formatted. """
name = "Raju"
age = 10
msg = "Hi {}. You are {} years old."
print(msg.format(name, age)) # Hi Raju. You are 10 years old.

# Numbering Placeholders
""" Numbering Placeholders, will fill values according to the postion of arguments. """
name = input("enter your name") # Mohan
age = int(input("enter your age")) # 22
msg = "Hi {1}. You are {0} years old."
print(msg.format(name, age)) # Hi 22. You are Mohan years old.

# Naming Placeholder
name = input() # Mohan
age = int(input()) # 22
msg = "Hi {name}. You are {age} years old."
print(msg.format(name=name, age=age)) # Hi Mohan. You are 22 years old.