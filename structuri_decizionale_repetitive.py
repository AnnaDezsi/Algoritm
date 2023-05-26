

# se da un sir de numere naturale, sa se calculeze numarul de aparitii ale cifrei 5

# se da o lista de numere naturale, sa se calculeze numarul de aparitii ale cifrei 5

#de realizat o functie care imi verifica apartenenta unui numar la un domeniu
# 0 --> 4000 mic
# 4000 -> 8000 mediu
# 8000 -> mare

# de realizat o functie care creeaza un meniu de forma
#Apasati 1 pt adunare, 2 pentru scadere, 3 pt inmultire, 4 pt impartire


def fib():
    # fib ex 0 1 1 2 3 5 8 13
    f1 = 0
    f2 = 1
    contor = 0
    while contor<10:
        f3 = f1 + f2
        f1= f2
        f2 = f3
        contor +=1
    print(f3)


def sir5():
    print("Introduceti sirul de numere naturale:")
    sir = input() # sir de [inceput, sfarsit, pas]
    contor = 0
    for index in range(0,len(sir),1):
        if sir[index] == "5":
            contor+= 1
    print("Numarul de aparitii al cifrei 5 este:", contor)


def lista5():
    print("Introduceti sirul de numere naturaledespartit de virgula:")
    l = input().split(",")
    contor = 0
    for index in range(len(l)):
        if l[index] == "5":
            contor += 1
    print("Numarul de aparitii al cifrei 5 este:", contor)



def incadrare():
    print("Va rog introduceti un numar pentru care dorim incadrarea in domeniile date:")
    nr = int(input())
    if nr <4000:
        print("mic")
    else:
        if nr<8000:
            print("mediu")
        else:
            print("mare")


def adunare():
    print("a=", end="")
    a = int(input())
    print("b=", end="")
    b = int(input())
    print("a+b=", a+b)


def scadere():
    print("a=", end="")
    a = int(input())
    print("b=", end="")
    b = int(input())
    print("a-b=", a - b)


def inmultire():
    print("a=", end="")
    a = int(input())
    print("b=", end="")
    b = int(input())
    print("a*b=", a * b)


def impartire():
    print("a=", end="")
    a = int(input())
    print("b=", end="")
    b = int(input())
    print("a/b=", a / b)


def meniu():
    print("Apasati 1 pt adunare, 2 pentru scadere, 3 pt inmultire, 4 pt impartire, 5 pentru incadrare, 6 pt sir ")
    option = input().strip() #elimina spatiile de la inceput sau sfarsit daca ele exista
    # if option == "1":
    #     print("adunare")
    #     adunare()
    # else:
    #     if option == "2":
    #         print("scadere")
    #         scadere()
    #     else:
    #         if option == "3":
    #             print("inmultire")
    #             inmultire()
    #         else:
    #             if option == "4":
    #                 print("impartire")
    #                 impartire()
    #             else:
    #                 if option == "5":
    #                     print("incadrare")
    #                     incadrare()
    #                 else:
    #                     if option == "6":
    #                         print("sir")
    #                         sir5()
    #                     else:
    #                         if option == "7":
    #                             print("sir")
    #                             lista5()
    #                         else:
    #                             print("Optiunile disponibile sunt 1, 2, 3, 4, 5, 6, 7")
    match option:
        case '1':
            print("adunare")
            adunare()
        case '2':
            print("scadere")
            scadere()
        case _:
            print('Nu exista')







if __name__ == "__main__":
    # exit = ""
    # while exit!= "0":
    #     meniu()
    #     print("Pentru iesire tastati 0 sau orice alta tasta pt continuare")
    #     exit = input().strip()
    meniu()