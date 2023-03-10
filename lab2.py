# Tehnica greedy

def masini_reparatie():
    T = input('Timp total de lucru')
    M = [5, 4, 20, 2, 2, 3, 4, 6]
    m_reparate = []
    M.sort()
    T_ramas = int(T)
    i = 0
    while T_ramas > 0 and i < len(M):
        if M[i] <= T_ramas:
            T_ramas = T_ramas - M[i]
            m_reparate.append(M[i])
        i+=1
    print(m_reparate)
    print(T_ramas)



#Recursivitate

def suma(lista, st, dr):
    if st == dr:
        return lista[st]
    else:
        mij = (st + dr )//2
        return suma(lista, st, mij) + suma(lista, mij +1, dr)

def suma2():
    mij = len(lista)//2
    if len(lista)==1:
        return int(lista[0])
    else:
        return suma2(lista[:mij]) + suma2(lista[mij:])



if __name__=="__main__":
    masini_reparatie()