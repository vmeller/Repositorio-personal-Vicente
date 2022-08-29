import parametros
import tablero
from math import ceil
import funciones
###########################################################################   Menu de inicio
simbolos = "qQwWeErRtTyYuUiIoOpPaAsSdDfFgGhHjJkKlLñÑzZxXcCvVbBnNmM,.-<{ +}'¿|"
print(""" STAR ADVANCED! \nSeleccione una opcion:\n[1] Crear partida \n[2] Cargar partida
[3] Ver ranking\n[0] Salir""")
tablero_juego_jugador = []
tablero_juego_admin = []
eleccion_inicio = input("Indique su opcion (0, 1, 2 o 3): ")
x = eleccion_inicio.isdigit()
while x == False or  int(eleccion_inicio) > 3:
    print("""Opcion no valida, por favor ingresar un numero valido\nSeleccione una opcion:\n[1] Crear partida
[2] Cargar partida\n[3] Ver ranking\n[0] Salir""")
    eleccion_inicio = input("Indique su opcion (0, 1, 2 o 3): ")
    y = eleccion_inicio.isdigit()
    if y == True:
        if int(eleccion_inicio) == 0 or int(eleccion_inicio) == 1 or \
            int(eleccion_inicio) == 2 or int(eleccion_inicio) == 3:
            break
termino_de_juego = 0
continuacion_juego = "s"
while termino_de_juego == 0 and continuacion_juego == "s":
    if int(eleccion_inicio) == 1:
        nueva_partida = input("Indiqueme su nombre: ")
        print("""Antes de comenzar el juego, debemos armar el tablero,\ndime las medidas con las que deseas jugar: """)
        largo_tablero = input("largo: ")
        ancho_tablero = input("ancho: ")
        while largo_tablero in simbolos or ancho_tablero in simbolos or int(largo_tablero) > 15 \
            or int(largo_tablero) < 3 or int(ancho_tablero) > 15 or int(ancho_tablero) < 3:
            print("valores no validos, por favor ingrese otros valores:")
            largo_tablero = input("largo (debe ser un numero entre 3 y 15): ")
            ancho_tablero = input("ancho (debe ser un numero entre 3 y 15): ")      
        for a in range(int(ancho_tablero)):
            tablero_juego_jugador.append([])
            tablero_juego_admin.append([])
        for tabla in tablero_juego_jugador:
            for l in range(int(largo_tablero)):
                tabla.append(" ")
        for tabla in tablero_juego_admin:
            for l in range(int(largo_tablero)):
                tabla.append(0)
##########################################################  Menu de juego
        cantidad_de_bestias = ceil(int(largo_tablero) * int(ancho_tablero) * float(parametros.PROB_BESTIA))#
        tablero_juego_admin = funciones.bestias_en_tablero(cantidad_de_bestias, \
            tablero_juego_admin, int(ancho_tablero), int(largo_tablero))
        while continuacion_juego == "s":
            tablero.print_tablero(tablero_juego_jugador) 
            print("""Seleccione una opcion:\n[1] Descubrir un sector\n[2] Guardar partida
[3] Salir de la partida""")
            menu_juego = input("Indique su opcion (1, 2 o 3): ")
            letras = menu_juego.isdigit()
            while int(menu_juego) <= 3 and menu_juego not in simbolos:
                    if int(menu_juego) == 1:
                        sector_fila = funciones.valor_fila(ancho_tablero)
                        sector_columna = funciones.valor_columna(largo_tablero)            
                        numero_bestias = funciones.surrounding(tablero_juego_admin, \
                            int(sector_columna), int(sector_fila))
                        if tablero_juego_admin[int(sector_fila)][int(sector_columna)] != "N":
                            tablero_juego_jugador[int(sector_fila)][int(sector_columna)] = numero_bestias
                        elif tablero_juego_admin[int(sector_fila)][int(sector_columna)] == "N":
                            tablero_juego_jugador[int(sector_fila)][int(sector_columna)] = "N"
                            tablero.print_tablero(tablero_juego_jugador)
                            print("Perdiste...")
                            termino_de_juego = 1
                            continuacion_juego = "f"
                            break            
                    elif int(menu_juego) == 2:
                        an = 0
                        an_b = 0
                        num = ""
                        best = ""
                        casillas_no_descubiertas = 0
                        for linea in tablero_juego_jugador:
                            la = 0
                            for lugar in linea: 
                                digito = str(lugar).isdigit()
                                if lugar == " ":
                                    casillas_no_descubiertas += 1
                                if digito == True:
                                    num += str(lugar)
                                    num += str(an)
                                    num += str(la)
                                la += 1
                            an += 1
                        for linea_b in tablero_juego_admin:
                            la_b = 0
                            for lugar_b in linea_b: 
                                if lugar_b == "N":
                                    best += lugar_b
                                    best += str(an_b)
                                    best += str(la_b)
                                la_b += 1
                            an_b += 1
                            casillas_descubiertas = (int(largo_tablero) * int(ancho_tablero)) - casillas_no_descubiertas#
                            nueva_partida_guardada = "\n"
                            puntaje_jugador = str(cantidad_de_bestias * casillas_descubiertas * parametros.POND_PUNT)#
                            nueva_partida_guardada += ";"+(nueva_partida)
                            nueva_partida_guardada += ";"+(puntaje_jugador)
                            nueva_partida_guardada += ";" + ancho_tablero
                            nueva_partida_guardada += ";" + largo_tablero 
                            nueva_partida_guardada += ";"+ num
                            nueva_partida_guardada += ";"+ best                            
                        with open("partidas/partidas.txt", "r") as file:
                            lista_partidas = file.readlines()
                            file.close()
                        lista_partidas_str = ""
                        for i in lista_partidas:
                            lista_partidas_str += str(i)
                        lista_partidas_str += nueva_partida_guardada
                        with open("partidas/partidas.txt", "w") as file:
                            file.write(lista_partidas_str)
                        print("Partida guardada")
                    elif int(menu_juego) == 3:
                        an = 0
                        an_b = 0
                        num = ""
                        best = ""
                        guardar = input("Desea guardar la partida antes de salir?: (Si o No) ")
                        if guardar == "si" or guardar == "Si":
                            casillas_no_descubiertas = 0
                            for linea in tablero_juego_jugador:
                                la = 0
                                for lugar in linea: 
                                    digito = str(lugar).isdigit()
                                    if lugar == " ":
                                        casillas_no_descubiertas += 1
                                    if digito == True:
                                        num += str(lugar)
                                        num += str(an)
                                        num += str(la)
                                    la += 1
                                an += 1
                            for linea_b in tablero_juego_admin:
                                la_b = 0
                                for lugar_b in linea_b: 
                                    if lugar_b == "N":
                                        best += lugar_b
                                        best += str(an_b)
                                        best += str(la_b)
                                    la_b += 1
                                an_b += 1
                            casillas_descubiertas = (int(largo_tablero) * int(ancho_tablero)) - casillas_no_descubiertas#
                            nueva_partida_guardada = "\n"
                            puntaje_jugador = str(cantidad_de_bestias * casillas_descubiertas * parametros.POND_PUNT)#
                            nueva_partida_guardada += ";"+(nueva_partida)
                            nueva_partida_guardada += ";"+(puntaje_jugador)
                            nueva_partida_guardada += ";" + ancho_tablero
                            nueva_partida_guardada += ";" + largo_tablero 
                            nueva_partida_guardada += ";"+ num
                            nueva_partida_guardada += ";"+ best                
                            with open("partidas/partidas.txt", "r") as file:
                                lista_partidas = file.readlines()
                                file.close()
                            lista_partidas_str = ""
                            for i in lista_partidas:
                                lista_partidas_str += str(i)
                            lista_partidas_str += nueva_partida_guardada
                            with open("partidas/partidas.txt", "w") as file:
                                file.write(lista_partidas_str)
                            print("Partida guardada")
                            termino_de_juego = 1
                            continuacion_juego = "f"
                            break
                        elif guardar == "no" or guardar == "No":
                            print("Cerrando el juego!")
                            termino_de_juego = 1
                            continuacion_juego = "f"
                            break

                    tablero.print_tablero(tablero_juego_jugador)
                    print("""Seleccione una opcion:\n[1] Descubrir un sector\n[2] Guardar partida
[3] Salir de la partida""")
                    menu_juego = input("Indique su opcion (1, 2 o 3): ")

                    while letras == False or  int(menu_juego) > 3:
                        print("""Opcion no valida, por favor ingresar un numero valido
Seleccione una opcion:\n[1] Descubrir un sector\n[2] Guardar partida\n[3] Salir de la partida""")
                        menu_juego = input("Indique su opcion (1, 2 o 3): ")
                        k = menu_juego.isdigit()
                        if k == True:
                            if int(menu_juego) <= 3:
                                break           
    elif int(eleccion_inicio) == 2:
        print("Cargando partidas...")
        with open("partidas/partidas.txt", "r") as file:
            lista_partidas = file.readlines()
        partidas_ordenadas = []
        for i in lista_partidas:
            j = i.split(";")
            nombre = j[1]
            puntaje = j[2]
            ancho_tablero_c = j[3]
            largo_tablero_c =  j[4]
            numeros_c = j[5]
            bestias_c = j[6]
            partida = []
            partida.append(nombre)
            partida.append(puntaje)
            partida.append(ancho_tablero_c)
            partida.append(largo_tablero_c)
            partida.append(numeros_c)
            partida.append(bestias_c)
            partidas_ordenadas.append(partida)
        funciones.cargar_partida(partidas_ordenadas)
        eleccion_partida = input("""Con que partida deseas continuar: (ingrese el numero correspondiente) 
Si desea iniciar una nueva partida ingrese el numero 0\n""")
        if int(eleccion_partida) == 0:
            eleccion_inicio = 1
            termino_de_juego = 0
        elif int(eleccion_partida) > 0:
            print("Usted selecciono:")
            print("-----------------------------------")
            print(partidas_ordenadas[int(eleccion_partida)-1][0],"=",partidas_ordenadas[int(eleccion_partida)-1][1],"puntos")#
            eleccion_inicio = 1
            termino_de_juego = 0
            continuacion_juego = "f"
            eleccion_inicio = 1
            nueva_partida = partidas_ordenadas[int(eleccion_partida)-1][0]
            tablero_juego_admin = funciones.creador_tablero_admin(partidas_ordenadas) 
            tablero_juego_jugador = funciones.creador_tablero_jugador(partidas_ordenadas)
            print(tablero_juego_admin)
            while continuacion_juego == "f":
                tablero.print_tablero(tablero_juego_jugador) 
                print("""Seleccione una opcion:\n[1] Descubrir un sector\n[2] Guardar partida\n[3] Salir de la partida""")
                menu_juego = input("Indique su opcion (1, 2 o 3): ")
                letras = menu_juego.isdigit()
                ancho_tablero = len(tablero_juego_jugador)
                largo_tablero = len(tablero_juego_jugador[1])
                while int(menu_juego) <= 3 and menu_juego not in simbolos:
                        if int(menu_juego) == 1:
                            sector_fila = funciones.valor_fila(ancho_tablero)
                            sector_columna = funciones.valor_columna(largo_tablero)              
                            numero_bestias = funciones.surrounding(tablero_juego_admin, int(sector_columna), int(sector_fila))#
                            if tablero_juego_admin[int(sector_fila)][int(sector_columna)] != "N":
                                tablero_juego_jugador[int(sector_fila)][int(sector_columna)] = numero_bestias
                            elif tablero_juego_admin[int(sector_fila)][int(sector_columna)] == "N":
                                tablero_juego_jugador[int(sector_fila)][int(sector_columna)] = "N"
                                tablero.print_tablero(tablero_juego_jugador)
                                print("Perdiste...")
                                termino_de_juego = 1
                                continuacion_juego = "k"
                                break            
                        elif int(menu_juego) == 2:
                            cantidad_de_bestias = ceil(int(largo_tablero) * int(ancho_tablero) * \
                                float(parametros.PROB_BESTIA))
                            an = 0
                            an_b = 0
                            num = ""
                            best = ""
                            casillas_no_descubiertas = 0
                            for linea in tablero_juego_jugador:
                                la = 0
                                for lugar in linea: 
                                    digito = str(lugar).isdigit()
                                    if lugar == " ":
                                        casillas_no_descubiertas += 1
                                    if digito == True:
                                        num += str(lugar)
                                        num += str(an)
                                        num += str(la)
                                    la += 1
                                an += 1
                            for linea_b in tablero_juego_admin:
                                la_b = 0
                                for lugar_b in linea_b: 
                                    if lugar_b == "N":
                                        best += lugar_b
                                        best += str(an_b)
                                        best += str(la_b)
                                    la_b += 1
                                an_b += 1
                            casillas_descubiertas = (int(largo_tablero) * int(ancho_tablero)) - casillas_no_descubiertas#
                            nueva_partida_guardada = "\n"
                            puntaje_jugador = str(cantidad_de_bestias * casillas_descubiertas * parametros.POND_PUNT)#
                            nueva_partida_guardada += ";"+(nueva_partida)
                            nueva_partida_guardada += ";"+(puntaje_jugador)
                            nueva_partida_guardada += ";" + ancho_tablero
                            nueva_partida_guardada += ";" + largo_tablero 
                            nueva_partida_guardada += ";"+ num
                            nueva_partida_guardada += ";"+ best  
                            with open("partidas/partidas.txt", "r") as file:
                                lista_partidas = file.readlines()
                                file.close()
                            lista_partidas_str = ""
                            for i in lista_partidas:
                                lista_partidas_str += str(i)
                            lista_partidas_str += nueva_partida_guardada
                            with open("partidas/partidas.txt", "w") as file:
                                file.write(lista_partidas_str)
                            print("Partida guardada")
                        elif int(menu_juego) == 3:
                            guardar = input("Desea guardar la partida antes de salir?: (Si o No) ")
                            if guardar == "si" or guardar == "Si":
                                an = 0
                                an_b = 0
                                num = ""
                                best = ""
                                casillas_no_descubiertas = 0
                                for linea in tablero_juego_jugador:
                                    la = 0
                                    for lugar in linea: 
                                        digito = str(lugar).isdigit()
                                        if lugar == " ":
                                            casillas_no_descubiertas += 1
                                        if digito == True:
                                            num += str(lugar)
                                            num += str(an)
                                            num += str(la)
                                        la += 1
                                    an += 1
                                for linea_b in tablero_juego_admin:
                                    la_b = 0
                                    for lugar_b in linea_b: 
                                        if lugar_b == "N":
                                            best += lugar_b
                                            best += str(an_b)
                                            best += str(la_b)
                                        la_b += 1
                                    an_b += 1
                                casillas_descubiertas = (int(largo_tablero) * int(ancho_tablero)) - casillas_no_descubiertas#
                                nueva_partida_guardada = "\n"
                                puntaje_jugador = str(cantidad_de_bestias * casillas_descubiertas * parametros.POND_PUNT)#
                                nueva_partida_guardada += ";"+(nueva_partida)
                                nueva_partida_guardada += ";"+(puntaje_jugador)
                                nueva_partida_guardada += ";" + ancho_tablero
                                nueva_partida_guardada += ";" + largo_tablero 
                                nueva_partida_guardada += ";"+ num
                                nueva_partida_guardada += ";"+ best                
                                with open("partidas/partidas.txt", "r") as file:
                                    lista_partidas = file.readlines()
                                    file.close()
                                lista_partidas_str = ""
                                for i in lista_partidas:
                                    lista_partidas_str += str(i)
                                lista_partidas_str += nueva_partida_guardada
                                with open("partidas/partidas.txt", "w") as file:
                                    file.write(lista_partidas_str)
                                print("Partida guardada")
                                termino_de_juego = 1
                                break
                            elif guardar == "no" or guardar == "No":
                                print("Cerrando el juego!")
                                termino_de_juego = 1
                                break
                        tablero.print_tablero(tablero_juego_jugador)
                        print("""Seleccione una opcion:\n[1] Descubrir un sector\n[2] Guardar partida\n[3] Salir de la partida""")
                        menu_juego = input("Indique su opcion (1, 2 o 3): ")
                        while letras == False or  int(menu_juego) > 3:
                            print("""Opcion no valida, por favor ingresar un numero valido
Seleccione una opcion:\n[1] Descubrir un sector\n[2] Guardar partida\n[3] Salir de la partida""")
                            menu_juego = input("Indique su opcion (1, 2 o 3): ")
                            k = menu_juego.isdigit()
                            if k == True:
                                if int(menu_juego) <= 3:
                                    break      
    elif int(eleccion_inicio) == 3:
        print("Cargando ranking...")
        with open("partidas/partidas.txt", "r") as file:
            lista_puntajes = file.readlines()
        puntajes_ordenadas = []
        for i in lista_puntajes:
            j = i.split(";")
            nombre = j[1]
            puntaje = j[2]
            puntos = []
            puntos.append(nombre)
            puntos.append(puntaje)
            puntajes_ordenadas.append(puntos)
        funciones.cargar_ranking(puntajes_ordenadas)    
        volver = input("""\n[0] Volver atras: \n[1] Salir:\n""")
        f = volver.isdigit()
        while f == False or int(volver) > 1:
            print("Por favor ingresar un numero valido")
            volver = input("""\n[0] Volver atras: \n[1] Salir:\n""")
        if int(volver) == 0:
            print(""" STAR ADVANCED! \nSeleccione una opcion:\n[1] Crear partida
[2] Cargar partida\n[3] Ver ranking\n[0] Salir""")
            tablero_juego_jugador = []
            tablero_juego_admin = []
            eleccion_inicio = input("Indique su opcion (0, 1, 2 o 3): ")
            x = eleccion_inicio.isdigit()
            while x == False or  int(eleccion_inicio) > 3:
                print("""Opcion no valida, por favor ingresar un numero valido\nSeleccione una opcion:
[1] Crear partida\n[2] Cargar partida\n[3] Ver ranking\n[0] Salir""")
                eleccion_inicio = input("Indique su opcion (0, 1, 2 o 3): ")
                y = eleccion_inicio.isdigit()
                if y == True:
                    if int(eleccion_inicio) == 0 or int(eleccion_inicio) == 1 or \
                        int(eleccion_inicio) == 2 or int(eleccion_inicio) == 3:
                        break
                termino_de_juego = 0
        elif int(volver) == 1:
            termino_de_juego = 1
            print("Hasta la proxima...")
    elif int(eleccion_inicio) == 0:                             
        print("Hasta la proxima...")
        termino_de_juego = 1
        break