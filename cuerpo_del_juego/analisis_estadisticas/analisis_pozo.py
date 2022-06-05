

def analisis_pozo():
    a = int(input("\nIngrese el monto deseado para inciar el juego:\t "))
    if 1 < a < 100000:
        cancelar = True
        pozo = a

    else:
        cancelar = False
        pozo = a

    return cancelar, pozo
