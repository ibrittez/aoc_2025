import sys

IZQUIERDA = -1
DERECHA = 1


class Perilla:
    contador_ceros = 0

    def __init__(self, valor):
        self.valor = valor

    def rotar(self, direccion, pasos):
        self.valor = (self.valor + direccion*pasos) % 100

        if (self.valor == 0):
            self.contador_ceros += 1

    def rotar_contando_ceros(self, direccion, pasos):
        inicial = self.valor
        vueltas_extra = pasos // 100
        if vueltas_extra > 0:
            self.contador_ceros += vueltas_extra

        # Ya desafecte las vueltas, por lo que me quedo con el
        # desplazamiento neto:

        pasos = pasos % 100
        self.valor = (self.valor + direccion*pasos) % 100

        if (self.valor == 0):
            # si caigo en cero sumo uno
            self.contador_ceros += 1
        elif (inicial == 0):
            # si arranqué en cero ojo que va a parecer que
            # sumar pero no (pensar en 0 - 3 xej)
            # (no pasa de vuelta x cero)
            pass
        elif (direccion == IZQUIERDA and self.valor > inicial):
            self.contador_ceros += 1
        elif (direccion == DERECHA and self.valor < inicial):
            self.contador_ceros += 1


def main():
    if len(sys.argv) < 2:
        print("uso: python3 programa.py archivo_input")
        return

    archivo = sys.argv[1]

    with open(archivo, 'r') as f:
        lineas = f.readlines()

    perilla_parte1 = Perilla(50)
    perilla_parte2 = Perilla(50)

    for linea in lineas:
        val = int(linea[1:])

        if (linea[0] == 'L'):
            dir = IZQUIERDA
        else:
            dir = DERECHA

        perilla_parte1.rotar(dir, val)
        perilla_parte2.rotar_contando_ceros(dir, val)

    print(f"ceros parte 1: {perilla_parte1.contador_ceros}")
    print(f"ceros parte 2: {perilla_parte2.contador_ceros}")


if __name__ == "__main__":
    main()
