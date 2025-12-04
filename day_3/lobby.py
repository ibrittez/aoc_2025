def find_max(cadena):
    maximo = '0'
    idx = 0
    for i in range(0, len(cadena)):
        if cadena[i] > maximo:
            maximo = cadena[i]
            idx = i

    return idx


def get_jotage(ratings, bank_size):
    cadena = ratings.strip()
    largo = len(cadena)

    if largo <= bank_size:
        return int(cadena)

    indexes = ["0"] * bank_size
    joltage = ["0"] * bank_size

    indexes[0] = find_max(cadena[:largo-bank_size+1])
    joltage[0] = ratings[indexes[0]]
    for i in range(1, bank_size):
        start = indexes[i-1] + 1
        end = largo - bank_size + i
        if len(cadena[start:]) < bank_size - i:
            ret = cadena[indexes[0]] + cadena[start:]
            return int(ret)
        indexes[i] = indexes[i-1] + 1 + find_max(cadena[start:end+1])
        joltage[i] = ratings[indexes[i]]

    return int("".join(joltage))


def calc_total_joltage(banks, bank_size):
    joltage = 0
    for bank in banks:
        joltage += get_jotage(bank, bank_size)
    return joltage


f = open("./input")

print("total joltage: ")
print(f"\tpart 1:\t{calc_total_joltage(f.readlines(), 2)}")
