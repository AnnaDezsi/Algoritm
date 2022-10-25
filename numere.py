def adunare2():
    print("Introduceti  un numar natural de 2 cifre:")
    x = int(input())
    z = x // 10
    u = x % 10
    print("Numarul rezultat prin adunarea cifrelor zecilor cu unitatilor", z +u)

def adunare3():
    print("Introduceti  un numar natural de 3 cifre:")
    x = int(input())
    s = x // 100
    z = x // 10 % 10
    u = x % 10
    print("Numarul rezultat prin adunarea cifrelor zecilor cu unitatilor", z + u + s )

def numarPicioareSiCapete():
    print("Introduceti numarul de gaini:")
    g = int(input())
    print("Numarul de picioare gaini este:", g * 2)
    print("Introduceti numarul de oi:")
    o = int(input())
    print("Numarul de picioare oi este:", o * 4 )
    print("Numarul total de picioare este : ", g * 2 + o * 4)
    print("Numarul total de capete este :", g + o)


def arieCub():
    print("Introduceti latura cubului:")
    l = int(input())
    print("Aria cubului este:", (l ** 2) * 6)

def volumCub():
    print("Introduceti latura cubului:")
    l = int(input())
    print("Volumul cubului este:", l ** 3)

def numarDeterminat():
    print("Introduceti  un numar natural de 3 cifre:")
    x = int(input())
    s = x // 100
    u = x % 10
    print("Numarul afisat obtinut prin eliminarea cifrei din mijloc:", s * 10 + u )

def ora():
    print("Introduceti ora :")
    o = int(input())
    print("Introduceti minutele:")
    m = int(input())
    print("Minutele pe care doriti sa le adaugati")
    x = int(input())
    on = o * 60 + m + x
    print("Ora noua este:", on // 60 , "minute" , on % 60)

def produscifre():
    print("Introduceti numarul n:")
    n = int(input())
    s = n // 100
    u = n % 10
    print("Produsul cifrelor unitatilor si al sutelor este:", s * u)

def numarGloburi():
    print("Numar globuri albe")
    a = int(input())
    r = a * 2
    v = r - 3
    print("Numar total globuri:", a + r + v)

def gauss():
    print("Numar natural")
    a = int(input())
    print("Suma lui Gauss:", a * (a + 1) // 2)

def numarAnimale():
    print("Numarul de pisici")
    p = int(input())
    c = p // 2
    g = p * 2
    print("Numarul total de animale este:", p + c + g)



if __name__ == "__main__":
    numarAnimale()



