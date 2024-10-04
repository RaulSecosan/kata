def sort(list):
    newList = [list[0]]

    for element in list:
        if element > newList[-1]:
            newList.append(element)

        for ind,elementFromNewList in enumerate(newList):
            if element  < elementFromNewList:
                newList.insert(ind,element)
                # print("newList++ ", newList)
                break
            #Elimina duplicatele
            elif element == elementFromNewList:
                break
    #elimina duplicatele
    # dup = []
    # for element in newList:
    #     if element not in dup:
    #         dup.append(element)
    return newList


# print(list(set(sort([1,0,6,1,22,4,5,2,3,4,10,9]))))
# print(list(set(sort([4, 3, 2, 1, 5, 0]))))
# print(sort([10,8, 5,-1,-3,22, 7,7, -3, 9, 6, 8, 2]))
#
# # Test fără set()
# print(sort([4, 3, 2, 1, 5, 0]))  # Așteptat: [0, 1, 2, 3, 4, 5]
# print(sort([10, 5, 7, 3, 9, 6, 8, 2]))  # Așteptat: [2, 3, 5, 6, 7, 8, 9, 10]
# print(sort([-1, -5, 0, 2, -3, 4]))  # Așteptat: [-5, -3, -1, 0, 2, 4]
# print(sort([3, 3, 3, 1, 1, 1]))  # Așteptat: [1, 1, 1, 3, 3, 3]
# print(sort([100, 100, 50, 75, 50, 100]))  # Așteptat: [50, 50, 75, 100, 100, 100]
#


# alta varianta dar nu am inteles acel sort
# def sort(array):
#     list = [array[0]]
#     for i in array[1:]:
#         for h, j in enumerate(list):
#             if j > i:
#                 list.insert(h, i)
#                 break
#         else:
#             list.append(i)
#     return list
#
# print(sort([4, 3, 2,8, 1, 5, 0]))  # Așteptat: [0, 1, 2, 3, 4, 5]
#
