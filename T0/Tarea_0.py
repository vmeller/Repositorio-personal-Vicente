import parametros
import tablero
import random
from math import ceil
import funciones
###########################################################################   Menu de inicio
simbolos = "qQwWeErRtTyYuUiIoOpPaAsSdDfFgGhHjJkKlLñÑzZxXcCvVbBnNmM,.-<{ +}'¿|"
print(""" STAR ADVANCED! 

Seleccione una opcion:
[1] Crear partida
[2] Cargar partida
[3] Ver ranking
[0] Salir""")
tablero_juego_jugador = []
tablero_juego_admin = []
eleccion_inicio = input("Indique su opcion (0, 1, 2 o 3): ")
x = eleccion_inicio.isdigit()
while x == False or  int(eleccion_inicio) > 3:
    print("Opcion no valida, por favor ingresar un numero valido")
    print("""Seleccione una opcion:
[1] Crear partida
[2] Cargar partida
[3] Ver ranking
[0] Salir""")
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
        print("""Antes de comenzar el juego, debemos armar el tablero,
dime las medidas con las que deseas jugar: """)
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
        cantidad_de_bestias = ceil(int(largo_tablero) * int(ancho_tablero) * float(parametros.PROB_BESTIA))
        tablero_juego_admin = funciones.bestias_en_tablero(cantidad_de_bestias, \
            tablero_juego_admin, int(ancho_tablero), int(largo_tablero))
        while continuacion_juego == "s":
            tablero.print_tablero(tablero_juego_jugador) 
            print("""Seleccione una opcion:
[1] Descubrir un sector
[2] Guardar partida
[3] Salir de la partida""")
            menu_juego = input("Indique su opcion (1, 2 o 3): ")
            letras = menu_juego.isdigit()
            while int(menu_juego) <= 3 and menu_juego not in simbolos:
                    if int(menu_juego) == 1:
                        sector_fila = input("seleccione una fila (numeros): ")
                        if sector_fila in simbolos or int(sector_fila) > int(ancho_tablero)-1:
                            print("El valor ingresado no se encuentra dentro del tablero, \
                                ingrese un valor que se encuentre en la tabla")
                            sector_fila = input("seleccione una fila (numeros): ")
                            while sector_fila in simbolos or int(sector_fila) > int(ancho_tablero)-1:
                                print("El valor ingresado no se encuentra dentro del tablero, \
                                    ingrese un valor que se encuentre en la tabla")
                                sector_fila = input("seleccione una fila (numeros): ")
                                if sector_fila <= int(ancho_tablero):
                                    break
                                break            
                        sector_columna = input("seleccione una columna (letras): ")
                        letra = funciones.convertidor_columna_en_numero(sector_columna)
                        if letra > int(largo_tablero)-1:
                            print("El valor ingresado no se encuentra dentro del tablero, \
                                ingrese un valor que se encuentre en la tabla")
                            sector_columna = input("seleccione una columna (letras): ")
                            letra = funciones.convertidor_columna_en_numero(sector_columna)
                            while letra > int(largo_tablero)-1:
                                print("El valor ingresado no se encuentra dentro del tablero, \
                                    ingrese un valor que se encuentre en la tabla")
                                sector_columna = input("seleccione una columna (letras): ")
                                if letra <= int(largo_tablero)-1:
                                    break               
                        numero_bestias = funciones.surrounding(tablero_juego_admin, \
                            int(letra), int(sector_fila))
                        if tablero_juego_admin[int(sector_fila)][int(letra)] != "N":
                            tablero_juego_jugador[int(sector_fila)][int(letra)] = numero_bestias
                        elif tablero_juego_admin[int(sector_fila)][int(letra)] == "N":
                            tablero_juego_jugador[int(sector_fila)][int(letra)] = "N"
                            tablero.print_tablero(tablero_juego_jugador)
                            print("Perdiste...")
                            termino_de_juego = 1
                            break            
                    elif int(menu_juego) == 2:
                        casillas_no_descubiertas = 0
                        for linea in tablero_juego_jugador:
                            for lugar in linea: 
                                if lugar == " ":
                                    casillas_no_descubiertas += 1
                        casillas_descubiertas = (int(largo_tablero) * int(ancho_tablero)) - casillas_no_descubiertas
                        nueva_partida_guardada = "\n"
                        puntaje_jugador = str(cantidad_de_bestias * casillas_descubiertas * parametros.POND_PUNT)
                        nueva_partida_guardada += ";"+(nueva_partida)
                        nueva_partida_guardada += ";"+(puntaje_jugador)
                        nueva_partida_guardada += ";"+str(tablero_juego_admin)
                        nueva_partida_guardada += ";"+str(tablero_juego_jugador)                                
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
                            casillas_no_descubiertas = 0
                            for linea in tablero_juego_jugador:
                                for lugar in linea: 
                                    if lugar == " ":
                                        casillas_no_descubiertas += 1
                            casillas_descubiertas = (int(largo_tablero) * int(ancho_tablero)) - casillas_no_descubiertas
                            nueva_partida_guardada = "\n"
                            puntaje_jugador = str(cantidad_de_bestias * casillas_descubiertas * parametros.POND_PUNT)
                            nueva_partida_guardada += ";"+(nueva_partida)
                            nueva_partida_guardada += ";"+(puntaje_jugador)
                            nueva_partida_guardada += ";"+str(tablero_juego_admin)
                            nueva_partida_guardada += ";"+str(tablero_juego_jugador)                
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
                    print("""Seleccione una opcion:
[1] Descubrir un sector
[2] Guardar partida
[3] Salir de la partida""")
                    menu_juego = input("Indique su opcion (1, 2 o 3): ")

                    while letras == False or  int(menu_juego) > 3:
                        print("Opcion no valida, por favor ingresar un numero valido")
                        print("""Seleccione una opcion:
[1] Descubrir un sector
[2] Guardar partida
[3] Salir de la partida""")
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
            tablero_juego_admin_c = j[3]
            tablero_juego_jugador_c =  j[4]
            partida = []
            partida.append(nombre)
            partida.append(puntaje)
            partida.append(tablero_juego_admin_c)
            partida.append(tablero_juego_jugador_c)
            partidas_ordenadas.append(partida)
        funciones.cargar_partida(partidas_ordenadas)
        eleccion_partida = input("""Con que partida deseas continuar: (ingrese el numero correspondiente) 
Si desea iniciar una nueva partida ingrese el numero 0
""")
        if int(eleccion_partida) == 0:
            eleccion_inicio = 1
            termino_de_juego = 0
        elif int(eleccion_partida) > 0:
            print("Usted selecciono:")
            print("-----------------------------------")
            print(partidas_ordenadas[int(eleccion_inicio)][0],"=",partidas_ordenadas[int(eleccion_inicio)][1],"puntos")
            eleccion_inicio = 1
            termino_de_juego = 0
            continuacion_juego = "f"
            eleccion_inicio = 1
            nueva_partida = partidas_ordenadas[int(eleccion_inicio)+1][0]
            tablero_juego_admin = eval(partidas_ordenadas[int(eleccion_inicio)][2])
            tablero_juego_jugador = eval(partidas_ordenadas[int(eleccion_inicio)+1][3])
            while continuacion_juego == "f":
                tablero.print_tablero(tablero_juego_jugador) 
                print("""Seleccione una opcion:
[1] Descubrir un sector
[2] Guardar partida
[3] Salir de la partida""")
                menu_juego = input("Indique su opcion (1, 2 o 3): ")
                letras = menu_juego.isdigit()
                ancho_tablero = len(tablero_juego_jugador)
                largo_tablero = len(tablero_juego_jugador[1])
                while int(menu_juego) <= 3 and menu_juego not in simbolos:
                        if int(menu_juego) == 1:
                            sector_fila = input("seleccione una fila (numeros): ")
                            if sector_fila in simbolos or int(sector_fila) > int(ancho_tablero)-1:
                                print("El valor ingresado no se encuentra dentro del tablero, \
                                    ingrese un valor que se encuentre en la tabla")
                                sector_fila = input("seleccione una fila (numeros): ")
                                while sector_fila in simbolos or int(sector_fila) > int(ancho_tablero)-1:
                                    print("El valor ingresado no se encuentra dentro del tablero, \
                                        ingrese un valor que se encuentre en la tabla")
                                    sector_fila = input("seleccione una fila (numeros): ")
                                    if sector_fila <= int(ancho_tablero):
                                        break
                                    break       
                            sector_columna = input("seleccione una columna (letras): ")
                            letra = funciones.convertidor_columna_en_numero(sector_columna)
                            if letra > int(largo_tablero)-1:
                                print("El valor ingresado no se encuentra dentro del tablero, \
                                    ingrese un valor que se encuentre en la tabla")
                                sector_columna = input("seleccione una columna (letras): ")
                                letra = funciones.convertidor_columna_en_numero(sector_columna)
                                while letra > int(largo_tablero)-1:
                                    print("El valor ingresado no se encuentra dentro del tablero, \
                                        ingrese un valor que se encuentre en la tabla")
                                    sector_columna = input("seleccione una columna (letras): ")
                                    if letra <= int(largo_tablero)-1:
                                        break               
                            numero_bestias = funciones.surrounding(tablero_juego_admin, int(letra), int(sector_fila))
                            if tablero_juego_admin[int(sector_fila)][int(letra)] != "N":
                                tablero_juego_jugador[int(sector_fila)][int(letra)] = numero_bestias
                            elif tablero_juego_admin[int(sector_fila)][int(letra)] == "N":
                                tablero_juego_jugador[int(sector_fila)][int(letra)] = "N"
                                tablero.print_tablero(tablero_juego_jugador)
                                print("Perdiste...")
                                termino_de_juego = 1
                                break            
                        elif int(menu_juego) == 2:
                            cantidad_de_bestias = ceil(int(largo_tablero) * int(ancho_tablero) * \
                                float(parametros.PROB_BESTIA))
                            casillas_no_descubiertas = 0
                            for linea in tablero_juego_jugador:
                                for lugar in linea: 
                                    if lugar == " ":
                                        casillas_no_descubiertas += 1
                            casillas_descubiertas = (int(largo_tablero) * int(ancho_tablero)) - casillas_no_descubiertas
                            nueva_partida_guardada = "\n"
                            puntaje_jugador = str(cantidad_de_bestias * casillas_descubiertas * parametros.POND_PUNT)
                            nueva_partida_guardada += ";"+(nueva_partida)
                            nueva_partida_guardada += ";"+(puntaje_jugador)
                            nueva_partida_guardada += ";"+str(tablero_juego_admin)
                            nueva_partida_guardada += ";"+str(tablero_juego_jugador)  
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
                                casillas_no_descubiertas = 0
                                for linea in tablero_juego_jugador:
                                    for lugar in linea: 
                                        if lugar == " ":
                                            casillas_no_descubiertas += 1
                                casillas_descubiertas = (int(largo_tablero) * int(ancho_tablero)) - casillas_no_descubiertas
                                nueva_partida_guardada = "\n"
                                puntaje_jugador = str(cantidad_de_bestias * casillas_descubiertas * parametros.POND_PUNT)
                                nueva_partida_guardada += ";"+(nueva_partida)
                                nueva_partida_guardada += ";"+(puntaje_jugador)
                                nueva_partida_guardada += ";"+str(tablero_juego_admin)
                                nueva_partida_guardada += ";"+str(tablero_juego_jugador)                
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
                        print("""Seleccione una opcion:
[1] Descubrir un sector
[2] Guardar partida
[3] Salir de la partida""")
                        menu_juego = input("Indique su opcion (1, 2 o 3): ")
                        while letras == False or  int(menu_juego) > 3:
                            print("Opcion no valida, por favor ingresar un numero valido")
                            print("""Seleccione una opcion:
[1] Descubrir un sector
[2] Guardar partida
[3] Salir de la partida""")
                            menu_juego = input("Indique su opcion (1, 2 o 3): ")
                            k = menu_juego.isdigit()
                            if k == True:
                                if int(menu_juego) <= 3:
                                    break           
    elif int(eleccion_inicio) == 3:
        print("Cargando ranking...")
        with open("partidas/puntajes.txt", "r") as file:
            lista_puntajes = file.readlines()
            file.close()
            puntajes = []
        for linea in lista_puntajes:
            puntajes.append(linea.strip().split("="))
        x = 1 
        for juego in puntajes[:10]:
            print(x,")",juego[0],"=",juego[1])
            x += 1
        volver = input("""
[0] Volver atras: 
[1] Salir:
""")
        f = volver.isdigit()
        while f == False or int(volver) > 1:
            print("Por favor ingresar un numero valido")
            volver = input("""
[0] Volver atras: 
[1] Salir:
""")
        if int(volver) == 0:
            print(""" STAR ADVANCED! 

Seleccione una opcion:
[1] Crear partida
[2] Cargar partida
[3] Ver ranking
[0] Salir""")
            tablero_juego_jugador = []
            tablero_juego_admin = []
            eleccion_inicio = input("Indique su opcion (0, 1, 2 o 3): ")
            x = eleccion_inicio.isdigit()
            while x == False or  int(eleccion_inicio) > 3:
                print("Opcion no valida, por favor ingresar un numero valido")
                print("""Seleccione una opcion:
[1] Crear partida
[2] Cargar partida
[3] Ver ranking
[0] Salir""")
                eleccion_inicio = input("Indique su opcion (0, 1, 2 o 3): ")
                y = eleccion_inicio.isdigit()
                if y == True:
                    if int(eleccion_inicio) == 0 or int(eleccion_inicio) == 1 or \
                        int(eleccion_inicio) == 2 or int(eleccion_inicio) == 3:
                        break
                termino_de_juego = 0
        elif int(volver) == 1:
            termino_de_juego = 1
    elif int(eleccion_inicio) == 0:                             
        print("Hasta la proxima...")
        termino_de_juego = 1
        break

