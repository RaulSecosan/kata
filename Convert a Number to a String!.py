''''
We need a function that can transform a number (integer) into a string.

What ways of achieving this do you know?

Examples (input --> output):
123  --> "123"
999  --> "999"
-100 --> "-100"
'''

def number_to_string(num):
    return str(num)

number_to_string(67)
number_to_string(-67)

# sau
def number_to_string(num):
    # Return a string of the number here!
    # return "%s" % num          # %-formatting
    # return str(num)            # int to string
    # return "{n}".format(n=num) # str.format()
    return f"{num}"              # f-strings