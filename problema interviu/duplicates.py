
def againDuplicates(input_list):
    noDuplicates = [input_list[0]]

    for element in input_list:
        found = 0
        # print('prim for ',element)
        for i in noDuplicates:
            # print('second for ',i)
            #verificare daca e string
            if type(i) == str and type(element) == str:
                if i.lower() == element.lower():
                    # print('duplicate found ', i)
                    found = 1
                    break  # Odată ce l-am găsit, nu mai are sens să continuăm


            if i == element:
                # print('duplicate found ', i)
                found = 1
                break
        if found == 0:
            # print('Adaugare ', element )
            noDuplicates.append(element)

    return noDuplicates

print( againDuplicates([5,1,5,2,3,5,6,2,3]))
print( againDuplicates(["a","b","a","d","f","b"]))
print( againDuplicates(["andrei","raul","andreea","Andrei","ok","b",'b']))

