from itertools import count

# #
# def aparitionNumber(arr):
#     count = 0
#     withoutDup = []
#     aparitions = []
#     for i in arr:
#         if i not in withoutDup:
#             withoutDup.append(i)
#
#     # print(withoutDup)
#     for element in withoutDup:
#         for element1 in arr:
#             if element == element1:
#                 count += 1
#         aparitions.append(f"{element} de {count}")
#         count = 0
#
#     return f"original: {aparitions}"


# ##merge bine dar mai jos cred ca e nul mai bun, aparition
# def aparitionNumber(arr):
#     dict = {}
#     newArr = []
#     # key_for_delete = []
#     for i in arr:
#
#         if type(i) is not int:
#             if len(i) > 1:
#                 dict_for_bigger = {} # pentru mai mari mai multe elemente ["aaa1abrbbcccc1cdddd","aaa1",'aaab']
#                 for char in i:
#                     if char not in dict_for_bigger:
#                         dict_for_bigger[char] = 1
#                     else:
#                         dict_for_bigger[char] += 1
#                 newArr.append(dict_for_bigger)
#
#         #daca e int il adaugam direct [1,2,1,5,8,6,1,5,9,9,8]
#         if i not in dict:
#             dict[i] = 1
#         else:
#             dict[i] += 1
#
#     #in dict s-au bagat si elementele pe care le-am tratat mai sus in dict_for_bigger dar s-au bagat incorect si acum le scoatem "aaa1abrbbcccc1cdddd" :1 ,"aaa1":1 ,'aaab':1
#     key_for_delete = [key for key in dict if type(key) is not int and len(key) > 1]
#     # for key in dict:
#     #     if type(key) is not int:
#     #         if len(key) > 1:
#     #             key_for_delete.append(key)
#
#     for keyDel in key_for_delete:
#         del dict[keyDel]
#
#
#     if len(dict) >0:
#         print('dict... ', dict)
#         return dict
#
#     if len(newArr) > 0:
#         print('pentru ', arr)
#         for i in newArr:
#             print(i)
#     # return dict, newArr
#     return ''

# print(aparitionNumber(["a","h","b","u","h","h","k","s","l","a"]))
# print(aparitionNumber([1,2,1,5,8,6,1,5,9,9,8]))
#
# print(aparitionNumber("aaa1abrbbcccc1cdddd"))
# print(aparitionNumber(["hmmm"]))
# print(aparitionNumber(["aaa1abrbbcccc1cdddd","aaa1",'aaab']))
# #


####mai simplu dar nu cuprinte majoritatea cazurilor
# def aparition(arr):
#     result = []  # Inițializează o listă goală pentru a stoca dicționarele individuale
#
#     for word in arr:  # Iterează prin fiecare cuvânt din listă
#         dictt = {}  # Creează un dicționar nou pentru fiecare cuvânt
#         for char in word:  # Iterează prin fiecare caracter din cuvântul curent
#             if char in dictt:  # Dacă caracterul există deja în dicționar
#                 dictt[char] += 1  # Incrementează valoarea asociată acestui caracter
#             else:  # Dacă caracterul nu există încă în dicționar
#                 dictt[char] = 1  # Inițializează valoarea la 1
#         result.append(dictt)  # Adaugă dicționarul curent în lista `result`
#
#     return result  # Returnează lista de dicționare

def aparition(arr):
    result = []  # Inițializează o listă goală pentru a stoca dicționarele individuale
    _newDict = {}
    for word in arr:  # Iterează prin fiecare cuvânt din listă
        dictt = {}  # Creează un dicționar nou pentru fiecare cuvânt
        if isinstance(word, str) and len(word) > 1:
            for char in word:  # Iterează prin fiecare caracter din cuvântul curent
                if char in dictt:  # Dacă caracterul există deja în dicționar
                    dictt[char] += 1  # Incrementează valoarea asociată acestui caracter
                else:  # Dacă caracterul nu există încă în dicționar
                    dictt[char] = 1  # Inițializează valoarea la 1
            result.append(dictt)  # Adaugă dicționarul curent în lista `result`
        #pentru numere si litere
        else:
            if word in _newDict:
                _newDict[word] += 1
            else:
                _newDict[word] = 1
    if _newDict:
        result.append(_newDict)
    # print(_newDict)
    return result  # Returnează lista de dicționare


print(aparition(['sasf', 'ooksf']))
print(aparition([1,2,1,5,8,6,1,5,9,9,8]))
print(aparition(["a","h","b","u",'a',"h","h","k","s","l","a"]))

print(aparition("aaa1abrbbcccc1cdddd"))
print(aparition(["hmmm"]))
print(aparition(["aaa1abrbbcccc1cdddd","aaa1",'aaab']))
# #

# def aparitionN umber(arr):
#     dict = {}
#     niceLook = []
#     print(arr)
#     for i in arr:
#         if len(arr) == 1:
#             for j in i:
#                 if j not in dict:
#                     dict[j] = 1
#                 else:
#                     dict[j] += 1
#         else:
#             if i not in dict:
#                 dict[i] = 1
#             else:
#                 dict[i] += 1
#
#     for item in dict:
#         niceLook.append(f"{item} apare de {dict[item]} \n")
#
#     return str(niceLook)
