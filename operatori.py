def suma():

    print("Suma")
    print("Introduceti primul numar de la tastatura (a)")
    a = input()
    print("a=", a)
    print("Introduceti al doilea numar de la tastatura (b)")
    b = input()
    print("b=", b)
    print("a+b=", int(a) + int(b))


def scadere():
    print("Scadere")
    print("Introduceti primul numar de la tastatura (a)")
    a = input()
    print("a=", a)
    print("Introduceti al doilea numar de la tastatura (b)")
    b = input()
    print("b=", b)
    print("a-b=", int(a) - int(b))

def inmultire():
    print("Inmultire")
    print("Introduceti primul numar de la tastatura (a)")
    a = input()
    print("a=", a)
    print("Introduceti al doilea numar de la tastatura (b)")
    b = input()
    print("b=", b)
    print("a*b=", int(a) * int(b))

def impartire():
    print("Impartire")
    print("Introduceti primul numar de la tastatura (a)")
    a = input()
    print("a=", a)
    print("Introduceti al doilea numar de la tastatura (b)")
    b = input()
    print("b=", b)
    print("a/b=", int(a) / int(b))

def arie():
        print("Arie")
        print("Introduceti prima cateta")
        a = input()
        print("c1=", a)
        print("Introduceti a doua cateta")
        b = input()
        print("c2=", b)
        print("aria=c1*c2/2 ->", int(a) * int(b) / 2)
def ariePatrat():
        print("AriePatrat")
        print("Introduceti latura patratului")
        a = input()
        print("a=", a)
        print("ariePatrat=a**2 ->",  int(a)**2)

def arieDreptunghi():
        print("ArieDreptunghi")
        print("Introduceti prima latura")
        a = input()
        print("a=", a)
        print("Introduceti a doua latura")
        b = input()
        print("b=", b)
        print("arieDreptunghi=a * b  ->", int(a) * int(b))



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("10%2 ->", 10%2)
    # suma()
    # scadere()
    # inmultire()
    # impartire()
    # arie()
    # ariePatrat()
    # arieDreptunghi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
