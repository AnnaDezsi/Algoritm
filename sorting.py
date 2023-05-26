def selection_sort(itemslist):
    n=len(itemslist)
    for i in range(n):
        minValueIndex = i
        for j in range(i+1,n):
            if itemslist[j]<itemslist[minValueIndex]:
                minValueIndex = j
        if minValueIndex != i:
            temp = itemslist[i]
            itemslist[i]=itemslist[minValueIndex]
            itemslist[minValueIndex]= temp
    return itemslist


employee1 = {
    "id": 14,
    "name": "John Doe",
    "age": 36,
    "position": "Business Manager"
}


employee2 = {
    "id": 2,
    "name": "Jane Doe",
    "age": 20,
    "position": "N/A"
}

employee3 = {
    "id": 110,
    "name": "John Smith",
    "age": 40,
    "position": "Software Developer"
}

employee4 = {
    "id": 40,
    "name": "Jane Smith",
    "age": 35,
    "position": "Engineer"
}

lista=[employee1, employee2, employee3, employee4]

def cautareId(lista,idcautat):
    for i in range(len(lista)):
        element = lista[i]
        if element['id'] == idcautat:
            return lista[i]['position']
    return {}








if __name__ == "__main__":
    print(cautareId(lista, 2))