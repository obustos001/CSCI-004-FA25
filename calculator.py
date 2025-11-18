# Simple Calculator -- CSCI 004, Evan Drake

# Hard-coded values (you can change these to test each desired case)

x = 0
y = 5
o = "*"

# In the following function
def evaluate(x, y, o): # this is the function, which takes all inputs (that were predefined) x, y, o
    if o == "+": # addition if statement is true, it wont even consider going in here if o != to +
        return x + y
    elif o == "-": # substraction if statement is true, it wont even consider going here if o != to -
        return x - y
    elif o == "*": # multiplication if statement is true, it wont even consider going here if o != to *
        return x * y
    elif o == "/": # division if statement is true, it wont even consider going here if o != to /
        # we wanna handle devide-by-zero safely and efficiently
        if y == 0:
            return "Error: cannot divide by zero"
        return x / y
    else: # in case we input letters for the variabls x or y or o. letters cannot/shouldn't be added, divided, multipled, or subtracted (in this case)
        return "Invalid operator"
    
#print result
print(evaluate(x, y, o)) 