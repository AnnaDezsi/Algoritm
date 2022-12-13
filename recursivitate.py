def cautare_sir(sirprincipal, subsir):
    i=0
    n=len(sirprincipal) - len(subsir)
    while i<=n:
        j = 0
        flg=True
        while flg and j<len(subsir):
            if sirprincipal[i+j]!= subsir[j]:
                flg= False
            j+=1
        if flg and j == len(subsir):
            return i
        i+=j
    return -1



def adunare(n):
    s=0
    for i in range(1,n+1):
        s+=i
    return s


def adunare_recursiv(n):
    if n==1:
        return 1
    return n + adunare_recursiv(n-1)

def factorial_recursiv(n):
    if n==1:
        return 1
    return n * factorial_recursiv(n-1)


def fibonacci(n): #al n-lea termen al sirului lui fibonacci
    f=0
    termen1=0
    termen2=1
    for i in range(2,n+1):
        f=termen1 + termen2
        termen1=termen2
        termen2=f
    return f


def fib_recursiv(n): #F(n) = F(n-1)+F(n-2)
    if n == 0:
        return 0
    if n==1:
        return 1
    return fib_recursiv(n-1)+fib_recursiv(n-2)


#de realizat o f recursiva care imi det nr de aparitii al cifrei 0 intr un numar natural
def numarnatural_recursiv1(n):
    sir=str(n)
    c= 0
    if sir[len(sir)-1] == "0":
        c =1
    if len(sir)-1<=0:
        return c
    return c + numarnatural_recursiv(int(sir[:len(sir)-1]))


def numarnatural_recursiv2(n):
    c=0
    if n ==0:
        return 0
    if n%10==0:
        c=1
    return c + numarnatural_recursiv2(n//10)

#sa se faca o f care ia ca parametru un numar natural si il reintoarce in ordine inversa a digits-urilor numarului
#211001 --> 1 0 0 1 1 2
def spatiu_cifre_inverse(n):
    sir= str(n)
    c= sir[len(sir)-1] #extrag ult el
    if len(sir)-1<=0: #verific daca nu am ajuns la sfarsit
        return c
    return c + spatiu_cifre_inverse(int(sir[:len(sir)-1]))


if __name__=="__main__":
    print(spatiu_cifre_inverse(2000))