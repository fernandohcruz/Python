def pangrama(lista):
    count = 0
    for x in "abcdefghijklmnopqrstuvwxyz":
        if x in lista:
            count += 1
    return count == 26

lista = "abcdefgasdosjdjaksda hijklmnopqrstuvwx"
print(pangrama(lista))