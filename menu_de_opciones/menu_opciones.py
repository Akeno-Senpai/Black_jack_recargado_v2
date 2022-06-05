

def menu_opciones(valor_pozo_inicial, bandera):

    from menu_de_opciones.opciones.jugar_una_mano import jugar_una_mano
    from menu_de_opciones.opciones.apostar import apostar
    import time

    valor_pozo_actual = 0

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

              pozo_jugador, valor_pozo_inicial_constante = apostar(valor_pozo_inicial)


            elif opcion == 2:

                validacion, monto_pozo_actual, contador_bj_natural = jugar_una_mano(valor_pozo_inicial, valor_pozo_actual)

            elif opcion == 3:

                pass

            else:

                print("\nLea bien las opciones del menu. [Valor ingresado no valido]")

                time.sleep(1.5)

                print("Precione enter para volver al menu: ")

                input()
