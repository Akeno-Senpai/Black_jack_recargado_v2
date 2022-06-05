

def analisis_resultado(valor_mano_final_jugador, valor_mano_final_croupier, monto_apostado, monto_pozo_actual, analisis_BJN_jugador, analisis_BJN_croupier):

    contador_BJN = 0

    if (valor_mano_final_jugador <= 21) and (valor_mano_final_croupier < valor_mano_final_jugador) or (valor_mano_final_jugador <= 21 and valor_mano_final_croupier > 21):

        if analisis_BJN_jugador == 21:
            contador_BJN += 1

        validacion = 0

        print ('\nHas ganado esta ronda', '\n\nTu puntaje es: ', valor_mano_final_jugador, '\n\ny el del Croupier es: ', valor_mano_final_croupier)

    elif (valor_mano_final_croupier > valor_mano_final_jugador) and (valor_mano_final_croupier <= 21) or (valor_mano_final_jugador > 21):

        if analisis_BJN_croupier == 21:
            contador_BJN += 1

        validacion = 1

        print ('\nHas perdido esta ronda', '\n\nTu puntaje es: ', valor_mano_final_jugador, '\n\ny el del Croupier es: ', valor_mano_final_croupier)

    elif (valor_mano_final_jugador == valor_mano_final_croupier) or (valor_mano_final_jugador and valor_mano_final_croupier == 21):

        if (valor_mano_final_jugador and valor_mano_final_croupier == 21) and (analisis_BJN_jugador == 21 and analisis_BJN_croupier != 21):
            print ("Has obtenido un Black Jack natural, por lo tanto has ganado.")
            contador_BJN += 1
        elif (valor_mano_final_jugador and valor_mano_final_croupier == 21) and (analisis_BJN_jugador != 21 and analisis_BJN_croupier == 21):
            print ("El croupier ha obtenido un Black Jack natural, por lo tanto el ha ganado." )
            contador_BJN += 1
        else:
            print('\nHa ocurrido un empate', '\n\nTu puntaje es: ', valor_mano_final_jugador, '\n\ny el del Croupier es: ',
                  valor_mano_final_croupier)

        validacion = 2

    if validacion == 0:
        monto_pozo_actual += monto_apostado
        print("\nApostaste: ", monto_apostado)
        print ("\nTras la apuesta, tu monto actual es es igual a:", monto_pozo_actual)
        print("")

    elif validacion == 1:
        monto_pozo_actual -= monto_apostado
        print("\nApostaste: ", monto_apostado)
        print("\nTras la apuesta, tu monto actual es es igual a:", monto_pozo_actual)
        print("")

    elif validacion == 2:
        monto_pozo_actual = monto_pozo_actual
        print("\nApostaste: ", monto_apostado)
        print("\nTras la apuesta, tu monto actual es es igual a:", monto_pozo_actual)
        print("")


    return validacion, monto_pozo_actual, contador_BJN
