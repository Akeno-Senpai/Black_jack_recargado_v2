

def jugar_una_mano():

    #IMPORTS#
    from generador_y_analisis_as.generador import generador
    from generador_y_analisis_as.analisis_as import analisis_as
    from cuerpo_del_juego.analisis_estadisticas.analisis_resultados import analisis_resultado
    #IMPORTS#

    #VARIABLES#
    valor_suma_inicial_jugador, valor_suma_carta_1_mas_carta_2_jugador, valor_suma_carta_1_mas_carta_2_mas_carta_jugador = 0, 0, 0
    valor_suma_inicial_croupier, valor_suma_carta_1_mas_carta_2_croupier, valor_suma_carta_1_mas_carta_2_mas_carta_croupier = 0, 0, 0
    black_jack_natural_jugador, black_jack_natural_croupier, black_jack_natural_total = 0, 0, 0
    opcion_jugador = 1
    #VARIABLES#

    #GENERACION_CARTAS#
    nombre_carta_jugador_1, palo_carta_jugador_1, valor_Carta_jugador_1 = generador()
    tupla_carta_jugador_1 = (nombre_carta_jugador_1, palo_carta_jugador_1)
    nombre_carta_jugador_2, palo_carta_jugador_2, valor_Carta_jugador_2 = generador()
    tupla_carta_jugador_2 = (nombre_carta_jugador_2, palo_carta_jugador_2)
    nombre_carta_jugador, palo_carta_jugador, valor_Carta_jugador = generador()
    tupla_carta_jugador = (nombre_carta_jugador, palo_carta_jugador)
    nombre_carta_croupier_1, palo_carta_croupier_1, valor_Carta_croupier_1 = generador()
    tupla_carta_croupier_1 = (nombre_carta_croupier_1, palo_carta_croupier_1)
    nombre_carta_croupier_2, palo_carta_croupier_2, valor_Carta_croupier_2 = generador()
    tupla_carta_croupier_2 = (nombre_carta_croupier_2, palo_carta_croupier_2)
    nombre_carta_croupier, palo_carta_croupier, valor_carta_croupier = generador()
    tupla_carta_croupier = (nombre_carta_croupier, palo_carta_croupier)
    #GENERACION_CARTAS#

    #MANO_SUMADA#
    valor_suma_inicial_jugador = valor_Carta_jugador_1
    valor_mano_jugador = valor_suma_inicial_jugador + valor_Carta_jugador_2
    valor_suma_inicial_croupier = valor_Carta_croupier_1
    #MANO_SUMADA#


    monto_apostado, monto_pozo_actual = 10, 10

    #CUERPO_DEL_CODIGO#
    print("\n", "Tu primera carta es: ", tupla_carta_jugador_1)

    print("\n", "Tu segunda carta es: ", tupla_carta_jugador_2)

    print("\n", "La primera carta del croupier es: ", tupla_carta_croupier_1)

    print("\n", "Tu puntaje actual en la mano es: ", valor_suma_carta_1_mas_carta_2_jugador)

    print("\n", "El puntaje actual en la mano del croupier es: ", valor_suma_inicial_croupier)

    if monto_apostado <= monto_pozo_actual and monto_apostado % 5 == 0 and monto_pozo_actual >= 5:

        while valor_suma_carta_1_mas_carta_2_jugador < 21 and opcion_jugador == 1:

            print("\n", "Seleccione una de las siguientes opciones: ")
            print("\n", "1- Pedir carta")
            print("\n", "2- Plantarse")

            opcion_jugador = input("\nIngrese aqui su opcion: ")

            if opcion_jugador == "1":

                print("\n", "Tu nueva carta es: ", tupla_carta_jugador)

                valor_Carta_jugador = analisis_as(valor_mano_jugador, valor_Carta_jugador)

                valor_mano_jugador = valor_mano_jugador + valor_Carta_jugador

                print("\n", "Tu puntaje actual en la mano es: ", valor_mano_jugador)

                while valor_mano_jugador >= 21 and valor_suma_carta_1_mas_carta_2_mas_carta_croupier < 17:

                    print("\n", "La nueva carta del croupier es: ", tupla_carta_croupier)

                    valor_mano_croupier = valor_suma_inicial_croupier + valor_carta_croupier

                    print("\n", "El puntaje actual en la mano del croupier es: ", valor_mano_croupier)

            elif opcion_jugador == "2":

                valor_mano_final_jugador = valor_mano_jugador

                print("\n", "Tu puntaje final es: ", valor_mano_final_jugador)

                print("\n", "La segunda carta del croupier es: ", tupla_carta_croupier_2)

                valor_Carta_croupier_2 = analisis_as(valor_suma_inicial_croupier, valor_Carta_croupier_2)

                valor_mano_croupier = valor_suma_inicial_croupier + valor_Carta_croupier_2

                while valor_mano_croupier < 17:

                    print("\n", "La nueva carta del croupier es", tupla_carta_croupier)

                    valor_carta_croupier = analisis_as(valor_mano_croupier, valor_carta_croupier)

                    valor_mano_croupier += valor_carta_croupier

                    print("\n", "El puntaje actual en la mano del croupier es: ", valor_mano_croupier)

                return

            else:

                print("Ingreso una opcion no valida")

        if valor_mano_jugador == 21:

            valor_mano_final_jugador = valor_mano_jugador
            valor_mano_final_croupier = valor_mano_croupier

            validacion, monto_pozo_actual, contador_bj_natural = analisis_resultado()


        elif valor_mano_jugador > 21:

            pvalor_mano_final_jugador = valor_mano_jugador
            valor_mano_final_croupier = valor_mano_croupier

        #CUERPO_DEL_CODIGO#

jugar_una_mano()
