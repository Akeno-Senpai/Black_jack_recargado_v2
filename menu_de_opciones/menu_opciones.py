    from menu_de_opciones.opciones.jugar_una_mano import jugar_una_mano
    from menu_de_opciones.opciones.apostar import apostar
    from cuerpo_del_juego.analisis_estadisticas.contadores import contadores
    from cuerpo_del_juego.bienvenida import bienvenida
    import time

    valor_pozo_inicial, bandera = bienvenida()

    monto_pozo_actual = valor_pozo_inicial
    partidas_jugadas = 0
    victorias_jugador = 0
    monto_apostado = 0
    opcion = -1

    if bandera == True or valor_pozo_inicial != 0:

        while opcion != 0:

            validacion = -1

            print("\nMenu de opciones")

            print("\n1- Apostar")

            print("\n2- Jugar una mano")

            print("\n3- Salir")

            opcion = int(input("\nIngrese la opcion que quiere realizar: "))



            if opcion == 1:

              monto_pozo_actual, valor_pozo_inicial_constante = apostar(valor_pozo_inicial)


            elif opcion == 2:

                validacion, monto_pozo_actual, contador_bj_natural, monto_apostado = jugar_una_mano(valor_pozo_inicial, monto_pozo_actual)

            elif opcion == 3:

                pass

            else:

                print("\nLea bien las opciones del menu. [Valor ingresado no valido]")

                time.sleep(1.5)

                print("Precione enter para volver al menu: ")

                input()

            contadores(victorias_jugador, partidas_jugadas, validacion, monto_apostado)
