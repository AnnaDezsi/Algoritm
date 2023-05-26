#1).Sa se def o functie care prim ca parm o lista de nr naturale si un nr natural so reintaorce true daca imi gaseste nr in lista true,daca nu false
def numar_lista(l,n):
    for i in range(len(l)):
        if l[i]==n:
            return True
    return False


#2). Sa se def o functie cu param o matrice si un nr nat si reintaorce true daca gaseste nr in matrice ,daca nu false
def numar_matrice(matrice,nr):
    m=len(matrice)
    n=len(matrice[0])
    matrice = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if matrice[i][j]==nr:
                return True
    return False


#3). Sa se def o functie recursiva care calc factorialul unui nr natural n primit ca param
def factorial_nr_recursiv(n):
    if n==1:
        return 1
    return n * factorial_recursiv(n-1)


#4). Sa se def o functie rec care calc suma digitilor unui nr nat n primit ca param
def suma_digits(n):
    if n==0:
        return n
    return n%10 + suma_digits(n//10)


#5). Sa se def o functie rec care imi numara de cate ori apare cifra 0 in digitii lui n primit ca parametru
def aparitii_recursiv(n):

    c = 0
    if [len() - 1] == "0":
        c = 1
    if len() - 1 <= 0:
        return c
    return c + aparitii_recursiv(


#6). Sa se def o functie bubble-sort
def bubble_sort(l):
    flg=1
    while flg==1:
        flg=0
        for i in range(len(l)-1):
            if l[i]>l[i+1]:
                l[i+1], l[i]=l[i], l[i+1]
                flg=1


def Bubble_sort(l):
    n = len(l)
    swapped = False
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return









if__name__=="__main__":
