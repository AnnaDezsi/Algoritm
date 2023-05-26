denominations = [1, 2, 5, 10, 20, 50, 100]

def returnChange(change, denominations): #coin = value
    toGiveBack = [0]*len(denominations)
    for pos, coin in enumerate(reversed(denominations)): #pos = indice
        while coin <= change:
            change = change - coin
            toGiveBack[pos] +=1
    return(toGiveBack[::-1])

def fib1():
    if n <= 2:
        return 1
    mem = [None] * (n)
    mem[0]=1
    mem[1]=1
    for i in range(2, n):
        mem[i]=mem[i-1]+mem[i-2]
    return(mem[i])


def fib2():
    if n <= 2:
        return 1
    else:
        return fib2(n-1)+ fib2(n-2)


def fib3(n, mem):
    if n in mem:
        return mem[n]
    if n <= 2:
        return 1
    else:
        rez = fib3(n-1, mem) + fib3(n-2, mem)
        mem[n]= rez
    return rez


def lista_culori(list): #lista numere cu valori curprinse intre 0 si 255;  [100,234,5];  sa se returneze inversa listei obtinuta prin scaderea val din lista, din nr 255
    for i in range(len(list)):
        list= 255 - [i]
        print(lista[::-1])
    return list


def num():
    print("1" + "2")



















if __name__=="__main__":
    num()