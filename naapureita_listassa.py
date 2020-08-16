# tee ratkaisu tänne
def pisin_naapurijono(lista:list):
    pituus  = 0
    pisin = 0
    listanPaikka = 0
    apuri = 1
    if len(lista) <= 2:
        if lista[1]-lista[0]== 1 or lista[1]-lista[0]== -1:
            return 2
        else:
            return 1
    while apuri < len(lista):
        if lista[apuri] - lista[listanPaikka] == 1 or lista[apuri] - lista[listanPaikka]  == -1:
            pituus += 1
        else:
            if pituus > pisin:
                pisin = pituus
                pituus = 0
            else:
                pituus = 0
        listanPaikka += 1
        apuri+=1

        if apuri == len(lista):
            if pituus > pisin:
                pisin = pituus

    return pisin + 1


lista = [5, 3, 4, 2, 3, 1, 2, 3, 9, 8, 7, 8, 7, 6, 7, 6]
print(pisin_naapurijono(lista))
print(pisin_naapurijono([1, 2]))
print(pisin_naapurijono([5, 3, 4, 2, 3, 1, 2, 3, 9, 8, 7, 8, 7, 6, 7, 6]))