def find_max(cadena):
    maximo = '0'
    idx = 0
    for i in range(0, len(cadena)):
        if cadena[i] > maximo:
            maximo = cadena[i]
            idx = i

    return idx


def get_jotage(cadena):
    cadena = cadena.strip()
    first_idx = find_max(cadena[:len(cadena)-1])
    second_idx = find_max(cadena[first_idx+1:])

    return int(cadena[first_idx] + cadena[first_idx + 1 + second_idx])


def calc_total_joltage(banks):
    joltage = 0
    for bank in banks:
        joltage += get_jotage(bank)
    return joltage


f = open("./input")

print("total joltage: ")
print(f"\tpart 1:\t{calc_total_joltage(f.readlines())}")
