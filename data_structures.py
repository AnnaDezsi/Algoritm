def functie(lista): #[[0,1],[0,2],[1,2],[1,3],[3,4]]
    max=maxim(lista)+1
    m=[]
    for i in range(max):
        rand=[]
        for j in range(max):
            rand.append(0)
        m.append(rand)
    print(m) #vizualizam matricea noastra, ar trebui sa contina el 0
    for el in lista:
        x=el[0]
        y=el[1]
        m[x][y]=1
        m[y][x]=0
    print(m)


def genf(matrice):
    lista_finala=[]
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if matrice[i][j]==1:
                l=[i,j]
                lista_finala.append(l)



def maxim(lista):
    max=0
    for rand in lista:
        for el in rand:
            if el> max:
                max=el
    return max