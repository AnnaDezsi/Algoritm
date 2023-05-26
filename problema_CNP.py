def generator_CNP(gen, an, luna, zi, judet, nnn):
    CNP= ""
    if gen == "M" or gen=="m":
        if an<2000:
            CNP += "1"
        else:
            CNP += "5"
    else:
        if an < 2000:
            CNP += "2"
        else:
            CNP += "6"
    if an < 2000:
        CNP += str(an-1900)
    else:
        CNP += str(an-2000)
    if luna < 10:
        CNP += "0"
    CNP += str(luna)
    if zi<10:
        CNP +="0"
    CNP+= str(zi)
    if judet<10:
        CNP += "0"
    CNP += str(judet)
    if nnn<10:
        CNP += "00"
    elif nnn<100:
        CNP += "0"
    else:
        CNP += ""
    CNP += str(nnn)
    #cand programul ajunge in acest punct CNP are 12 digits
    CNP += str(generare_C(CNP))
    return CNP



def generare_C(CNP):
    c= None
    lista_control = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]
    suma = 0
    for i in range(len(CNP)):
        suma += int(CNP[i])* lista_control[i]
    if suma % 11 == 10:
        c =1
    else:
        c = suma % 11
    return c

print(generator_CNP("f", 2001, 3, 15, 4 , 294))
print(Hello world)