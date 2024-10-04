


#Problema data de mine
def reverseList(lst):
    reversedList = []
    # ex:    range(9, 0 , -1) --> de la index 9 la index 1 cu un pas de -1, adica scade (dar trebuie sa punem, adica sunt 9 cifre in total, dar indexul pleaca de la 0 nu de la 1 deci punem pana la 8 (9 - 1) adila len(lst) - 1
    # for i in range(len(lst)-1, -1, -1):
    #     reversedList.append(lst[i])


    # fara len(lst)
    count = 0
    #aflam lungimea listei
    for i in lst:
        count += 1

    count -=1
    while count >= 0:
        reversedList.append(lst[count])
        count = count - 1

    print(reversedList)


reverseList([1,2,3,4,5,6,7,8,9])