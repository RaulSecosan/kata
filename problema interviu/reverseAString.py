
def reverseAString(name):
    # print(name)
    reversedName = ''
    for i in range(len(name)-1,-1,-1):
        # reversedName = name[0].upper()
        reversedName += name[i]

    return reversedName[0].upper() + reversedName[1:-1] + reversedName[-1].lower()
##sau
# def reverseAString(name):
#     reversedName = ''
#     for i in range(len(name)-1, -1, -1):
#         if i == len(name) - 1:  # Primul caracter (devine uppercase)
#             reversedName += name[i].upper()
#         elif i == 0:  # Ultimul caracter (devine lowercase)
#             reversedName += name[i].lower()
#         else:
#             reversedName += name[i]
#
#     return reversedName

# print(reverseAString("Raul"))