# Convert number to reversed array of digits
# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
#
# Example(Input => Output):
# 35231 => [1,3,2,5,3]
# 0 => [0]

def digitize(n):
    return  [int(str(n)[digit]) for digit in  range(len(str(n))-1,-1,-1) ]
    # num = []
    # for digit in range(len(str(n))-1,-1,-1):
    #     num.append(int(str(n)[digit]))
    # return num

print(digitize(35231))