
def duplicate(list):
    newList = []

    for element in list:
        if type(element) == str:
            if element.lower() not in newList:
                newList.append(element.lower())
        #pentru numere
        elif element not in newList:
            newList.append(element)
    return newList

print(duplicate([5,1,5,2,3,5,6,2,3]))
print(duplicate(["a","b","a","d","f","b"]))
print(duplicate(["andrei","Raul","andreea","raul","Andrei","ok","2","b",'b','raul','2']))



def againDuplicates(input_list):
    noDuplicates = [input_list[0]]

    for element in input_list:
        found = 0
        for i in noDuplicates:
            #verificare daca e string
            if type(i) == str and type(element) == str:
                if i.lower() == element.lower():
                    found = 1
                    break  # Odată ce l-am găsit, nu mai are sens să continuăm

            if i == element:
                found = 1
                break
        #Adaugare element
        if found == 0:
            noDuplicates.append(element)

    return noDuplicates

# print( againDuplicates([5,1,5,2,3,5,6,2,3]))
# print( againDuplicates(["a","b","a","d","f","b"]))
# print( againDuplicates(["andrei","raul","andreea","Andrei","ok","b",'b']))

