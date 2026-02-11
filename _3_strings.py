# Working with strings

# String Concatenation
""" Joining strings together is called strings Concatenation """
a = "Hello" + " " + "World"

# String Repetition
""" '*' operator is used for repeating strings any number of times as required. """
a = "$" * 10
print(a)

# Length of string
""" 'len()' returns the number of characters in a given string. """
username = "Ravi"
length = len(username)
print(length)

# String Indexing
""" we can access an  individual character in a string using their postions (which starts from 0). These
    Postions are also called index. """

username = "Mohan"
first_letter = username[0]
print(first_letter)

# String Slicing
""" Obtaining a part of a string is called string slicing. Start from the 'Start_index' and stops at the 'End_index'
    IMPORTANT: End_index is not included in the slice """
message = "Hi Mohan"
part = message[3:5]
pirnt(part) # Mo

# Slicing to End
""" if 'End_index' is not specified, slicing stops at the end of the string. """
part = message[3:]
pirnt(part) # Mohan

# Slicing from start
""" if the 'Start_index' is not specified, the slicing start from index 0 and ends to the 'End_index'(excluding)"""
part = message[:5]
print(part) # Hi Mo

# Negative indexing
""" Use negative indexes to start the slice from the end of the string. """
msg = "Hello World"
print(msg[-5:-2]) # orl

# Reversing String
""" Reverse the given string using the extended slice operator. """
txt = "Hello World"
txt = txt[::-1]
pirnt(txt) # dlroW olleH

# Membership check-in Strings
# in operator
""" 'in' by using |in| operator, one can determine if a value is present in a sequence or not. """
language = "Python"
result = "P" in language
print(result) # True

# not in operator
""" 'not in' by using this operator, one can determine if value is not present in sequence or not. """
language = "Python"
result = "P" not in language
print(result) # False
