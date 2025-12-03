def fraccionar_cadena(cadena, n):
    largo = len(cadena)

    if (largo % n != 0):
        return None

    ret = [None] * n

    for i in range(0, n):
        ret[i] = cadena[(largo//n)*i: (largo//n)*(i+1)]

    return ret


def encontrar_repeticiones(rango):
    extremos = rango.split("-")

    suma = 0
    for i in range(int(extremos[0]), int(extremos[1])+1):
        for j in range(len(str(i)), 2-1, -1):
            ret = fraccionar_cadena(str(i), j)
            if (ret):
                if len(set(ret)) <= 1:
                    suma += i
                    break
    return suma


def gift_shop_part_1(filename):
    f = open(filename, 'r')
    data = f.read().strip()
    data = data.split(",")

    suma = 0
    for rango in data:
        extremos = rango.split("-")

        for i in range(int(extremos[0]), int(extremos[1])+1):
            ret = fraccionar_cadena(str(i), 2)
            if (ret):
                if len(set(ret)) <= 1:
                    suma += i

    return suma


def gift_shop_part_2(filename):
    f = open(filename, 'r')
    data = f.read().strip()
    data = data.split(",")

    suma = 0
    for rango in data:
        suma += encontrar_repeticiones(rango)

    return suma


print("suma de IDs invalidas: ")
print(f"\tparte 1:\t{gift_shop_part_1("./input")}")
print(f"\tparte 2:\t{gift_shop_part_2("./input")}")
