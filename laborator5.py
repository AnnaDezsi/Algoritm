#se da o lista de numere naturale neg si poz. sa se calculeze maximul si minimmul produselor care se pot obtine folosind doua elemenete din lista respectiva.
#Metoda 1
def minSiMax1(list):
    max= l[0]
    min=l[0]
    for i in range(len(list)):
        if l[i]< min:
            min = l[i]
        if l[i]> max:
            max = l[i]
        if min>l[i]:
            l[i]= min2
        if max<l[i]:
            l[i]=max2
    produs_max = max * max2
    produs_min = min * min2
    print(produs_min)
    print(produs_max)




#Metooda2
def minSiMax2():
        list = [1, 20, 3, 4, 60, 10]
        list.sort()
        n = len(list)
        produs_max = list[n-1] * list[n-2]
        produs_min = list[0]* list[1]
        print(produs_min)
        print(produs_max)



def matrice_nume(matrice):
    lista= "abcd"
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            print(lista[i], end="")
            if matrice[i][j]==1:
                print(lista[j])

            else:
                print("-")











if __name__=="__main__":
    matrice_nume([[0,1,1,0],[1,0,1,0], [1,1,0,1], [0,0,0,1]])
