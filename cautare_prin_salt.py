
def cautare_prin_salt(tab,val):
    ls=l.sort()
    n = len(l)
    salt = int(math.sqrt(n))
    val = int(input())
    #identificam zona din lista unde sse gasetste elem pe care eu il preiau de la tastatura
    for i in range(0, n, salt):
        if l[i]<val:
            start_lista_viitoare = i
        elif l[i] == val:
            print(i)
        else:
            break
    #am gasit zona din lista unde se gaseste elementul meu
    #pot sa efectuez o cautare secventiala
    flg = 0
    for i in range(len(start_lista_viitoare, start_lista_viitoare + salt)):
        if l[i]== val:
            print(i)
            flg = 1
    if flg == 0:
        print("Nu am gasit elementul")
















if __name__=="__main__":
    cautare_prin_salt()