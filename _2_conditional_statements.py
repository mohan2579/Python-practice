# Conditional statements

"""
Conditional statement allows you to execute a block of code only when a specific condition is true
"""
# If condition
if True:
    print("If block")
    print("Inside if")

# If Else

if False:
    pirnt() # it will not go inside if condition is false
else:
    print("It was else") # it will only enters into else when if condition is false

# Nested Condition
"""
The condition block inside |another| if/else conditional block is called as a nested conditional block.
"""
if condition A:
    if condition B:
        block of code
    else:
        block of code

# Or we can also write in else statement
if condition A:
    block of code
else:
    if Condition B:
        block of code

# Elif Statement
"""
use Elif statement when you have to apply multiple conditional statements between if and else. The Elif statement
is optional
"""
if Condition A:
    block of code
elif Condition B:
    block of code
else:
    block of code

# Indentation
"""
1. Spaces in front of the conditional block is called Indentation
2. Indentation(spacing) is used to identify the Conditional Blocks 
3. Standard practice is to use four spaces for indentation.
"""