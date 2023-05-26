def parcurgere_lista():
    l=list()
    for i in range(len(l)):
        print(l[i])
    for element in l:
        print(element)



#fiecare litera a alfabetului primeste o valoare (key - value) , ex: a-200, b-300, c-1...
#sa se calculeze pt un cuvant valoarea generata prin adunarea valorilor fiecarei litere
#abc --> 501
def suma_cuvant(cuvant):
    ht = {"a" : 200, "b" : 300, "c" : 1, "d" : 40, "e" : 50, "f" : 60, "g" : 70, "h" : 80, "i" :90,
          "j" : 1, "k" : 2, "l" : 3, "m" : 4, "n" : 5, "o" : 6, "p" : 7, "q" : 8, "r" : 9, "s" : 10, "t" : 11,
          "u" : 12, "v" : 13, "w" : 14, "x" : 15, "y" : 16, "z" : 17}
    suma = 0
    for el in cuvant:
        suma += ht[el]
    return suma


#se da o lista de nume ex ["ion", "vasile", "gheorghe", "ioana", "maria", "ana"]
# sa se det care nume din aceasta lista genereaza valoarea cea mai mare conform problemei anterioare si sa se afiseze acel nume
def suma_nume(lista):
    max = 0
    maxN = " "
    for el in lista:
        vc = suma_cuvant(el)
        if vc > max :
            max=vc
            maxN = el
    return maxN


def generare_ht(tip = 0):
    ht = {}
    litere = ["a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j", "k" , "l" , "m" , "n" , "o" , "p" , "q" , "r" , "s" , "t" ,
          "u" , "v" , "w" , "x" , "y" , "z" ]
    lista_noua = []
    start = 6
    for i in range(start, len(litere)):
        lista_noua.append(litere[i])
    for i in range(0, start):
        lista_noua.append(litere[i])
    for i in range(len(litere)):
        if tip == 0:
            ht[litere[i]] = lista_noua[i]
        else:
            ht[lista_noua[i]] = litere[i]
    return ht



def crypt_text(propozitie, tip=0):
    litere = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
              "u", "v", "w", "x", "y", "z"]

    ht = generare_ht(tip)
    noua_propozitie= ""
    for el in propozitie:
        if el in litere:
            noua_propozitie += ht[el]
        else:
            noua_propozitie += el
    return  noua_propozitie






if __name__ == "__main__":
    prop = input("Propozitie: ")
    c = crypt_text(prop)
    print(c)
    d = crypt_text(c, 1)
    print(d)