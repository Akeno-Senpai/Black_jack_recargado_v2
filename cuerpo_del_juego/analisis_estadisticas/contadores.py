

def Contadores(Victorias_jugador, Partidas_jugadas, validacion, apuesta_actual):
    if validacion == 0 or validacion == 1 or validacion == 2:

        Partidas_jugadas += 1

        if validacion == 1:

            racha_crupier = 0

            racha_crupier += 1

            return racha_crupier

        elif validacion == 0:

            racha_crupier = 0

            Victorias_jugador += 1

        if Partidas_jugadas == 1:

            apuesta_inicial = apuesta_actual

            return apuesta_inicial

    validacion = 0

    return Victorias_jugador, Partidas_jugadas, validacion
