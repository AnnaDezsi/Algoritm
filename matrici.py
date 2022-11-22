def suma_matrice() :
    n = 4
    sdp = 0
    sds = 0
    matrice = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrice[i][j] = int(input())
            if i < j:
                sdp += matrice[i][j]
            if i + j < n-1:
                sds += matrice[i][j]
    print("Suma diagoanala principala", sdp)
    print("Suma diagonala secundara", sds)



def patrat_elemente():
    m = 3 #randuri
    n = 2 #coloane
    matrice = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(n):
            matrice[i][j]=int(input())
            matrice[i][j] = matrice[i][j]**2
    print(matrice)


def element_10():
    m = 3  # randuri
    n = 2  # coloane
    matrice = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(n):
            matrice[i][j] = int(input())
            matrice[i][j] = matrice[i][j] +10
    print(matrice)


def lista_100():
    n = 10
    lista = []
    for i in range(len(lista)):
        lista.append(int(input()))
    for i  in range(len(lista)):
        if lista[i]== 100:
            print(i)

def matrice_100():
    m = 3
    n = 2
    matrice = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(n):
            matrice[i][j] = int(input())
            if matrice[i][j] == 100:
                print(i, j)


def  suma_matrice_par():
    m = 3
    n = 2
    suma = 0
    matrice = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(n):
            matrice[i][j] = int(input())
            if matrice[i][j] % 2 == 0:
                suma+= matrice[i][j]


def  suma_matrice_impar():
    m = 3
    n = 2
    suma = 0
    matrice = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(n):
            matrice[i][j] = int(input())
            if matrice[i][j] % 2 != 0 :
                suma+= matrice[i][j]


def  suma_matrice_par2():
    m = 3
    n = 2
    suma = 0
    matrice = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(n):
            matrice[i][j] = int(input())
            if matrice[i][j] % 2 == 0 and matrice[i][j] > 10:
                suma+= matrice[i][j]

if __name__ == "__main__":
    suma_matrice_impar()