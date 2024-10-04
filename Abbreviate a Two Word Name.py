# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
#
# The output should be two capital letters with a dot separating them.
#
# It should look like this:
#
# Sam Harris => S.H
#
# patrick feeney => P.F

# def abbrev_name(name):
#     abbrevName = name.split(" ")
#     return abbrevName[0][0].upper() + " ." + abbrevName[1][0].upper()



# sau
# def abbrev_name(name):
#     abbrevName = ''
#     for name in name.split(" "):
#         abbrevName +=name[0].upper() + "."
#     return abbrevName[0:-1]

# sau
def abbrev_name(name):
    return '.'.join(name[0].upper() for name in name.split())
print(abbrev_name("Sam Harris"))

