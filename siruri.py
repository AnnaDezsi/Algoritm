def schimbare():
    cuvant = input().strip()
    print(cuvant)
    index = 0
    for caracter in cuvant:
        if caracter in "aeiou":
            print(caracter.upper(),"Am gasit vocala", index)
        else:
            print(caracter, index)
        index = index + 1

def prima_ultima_litera():
    cuvant = input().strip()
    print(cuvant)
    index = 0
    for caracter in cuvant:
        if index == 0 or index == len(cuvant) -1 :
            print(caracter.upper(),"Prima sau ultima litera", index)
        else:
            print(caracter, index)
        index = index + 1

def sufix_prefix_adaug():
    cuvant = input().strip()
    sufix = "_"
    prefix = "#"
    cuvantn = prefix + cuvant + sufix
    print(cuvantn)


def sufix_prefix_extrag():
    cuvant = input().strip()
    nrsf = 2
    print(cuvant[:nrsf], cuvant[len(cuvant)-nrsf:])


def inserare_asterisc():
    cuvantn = ""
    cuvant = input().strip()
    print(cuvant)
    for caracter in cuvant:
        if caracter in "aeiou":
           cuvantn = cuvantn + caracter + "*"
        else:
            cuvantn = cuvantn + caracter
    print(cuvantn)

def numar_litera_a1():
    cuvant = input().strip()
    print(cuvant)
    print(cuvant.count("a"))


def numar_litera_a2():
    cuvant = input().strip()
    contor = 0
    print(cuvant)
    for caracter in cuvant:
        if caracter in "aA":
            contor +=1
    print(contor)


def lista():
    l = [234, 100, 90, 300, 111, 2, 3, 0]
    jumatate = len(l) // 2
    l1 = l[:jumatate:]
    l1.sort()
    print(l1)
    l2 = l[jumatate::]
    l2.sort(reverse= True)
    print(l2)
    l2.append(4)
    l2.append(8)
    l2.sort(reverse=True)
    print(l2)

if __name__== "__main__":
    lista()