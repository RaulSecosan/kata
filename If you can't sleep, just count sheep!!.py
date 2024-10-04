# If you can't sleep, just count sheep!!
#
# Task:
# Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.

def count_sheep(n):
    # your code
    sleep = ''
    if n > -1 :
        for i in range(1,n+1):
            sleep += f"{i} sheep..."
    else:
        n = -n
        for i in range(1, n + 1):
            sleep += f"{i} sheep..."

    return sleep
print(count_sheep(1))