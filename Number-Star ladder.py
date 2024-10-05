# Task
# Using n as a parameter in the function pattern, where n>0, complete the codes to get the pattern (take the help of examples):
#
# Note: There is no newline in the end (after the pattern ends)
#
# Examples
# pattern(3) should return "1\n1*2\n1**3", e.g. the following:
#
# 1
# 1*2
# 1**3
# pattern(10): should return the following:
#
# 1
# 1*2
# 1**3
# 1***4
# 1****5
# 1*****6
# 1******7
# 1*******8
# 1********9
# 1*********10
# def pattern(n):
#     text = ""
#     if n == 1:
#         text = '1'
#
#     else:
#         for i in range(1,n+1):
#                 if i == 1:
#                     text = "1"
#                 else:
#                     text += "\n1" + "*" * (i-1) + str(i)
#     return text

# def pattern(n):
#     text = ""
#     for i in range(1,n+1):
#             text = "1" if i == 1 else text + "\n1" + "*" * (i-1) + str(i)
#     return text



def pattern(n):
    return  "".join(["1" if i == 1 else "\n1" + "*" * (i-1) + str(i)  for i in range(1,n+1)])


# print(pattern(1))
print(pattern(3))
# print(pattern(10))