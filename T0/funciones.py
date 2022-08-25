import random

def posicion(tablero1, tablero2, fila, columna):
    tablero1[fila][columna] = tablero2[fila][columna]
    return tablero1

def bestias_en_tablero(cantidad_bestias, tablero, ancho, largo):
    c = 0
    for i in range(cantidad_bestias):
        if tablero[random.randint(0,ancho-1)][random.randint(0,largo-1)] == 0:
            tablero[random.randint(0,ancho-1)][random.randint(0,largo-1)] = "N"
            c += 1
        else:
            c += 0
    if c < cantidad_bestias:
        return bestias_en_tablero
    else:
        return tablero

def convertidor_columna_en_numero(letra):
    numero = 0
    if letra == "a" or letra == "A":
        numero = 0
        return numero
    elif letra == "b" or letra == "B":
        numero = 1
        return numero
    elif letra == "c" or letra == "C":
        numero = 2
        return numero
    elif letra == "d" or letra == "D":
        numero = 3
        return numero
    elif letra == "e" or letra == "E":
        numero = 4
        return numero 
    elif letra == "f" or letra == "F":
        numero = 5
        return numero
    elif letra == "g" or letra == "G":
        numero = 6
        return numero
    elif letra == "h" or letra == "H":
        numero = 7
        return numero
    elif letra == "i" or letra == "I":
        numero = 8
        return numero
    elif letra == "j" or letra == "J":
        numero = 9
        return numero
    elif letra == "k" or letra == "K":
        numero = 10
        return numero
    elif letra == "l" or letra == "L":
        numero = 11
        return numero
    elif letra == "m" or letra == "M":
        numero = 12
        return numero
    elif letra == "n" or letra == "N":
        numero = 13
        return numero
    elif letra == "o" or letra == "O":
        numero = 14
        return numero
    else:
        numero = "valor no valido"
        return numero
################################################### Crearla
def ordenar_puntajes(lista):
    lista2 = []
    for l in lista:
        for j in lista:
            if j[1] >= l[1]:
                lista2.append(j)
    return lista2
        

def contador_de_bestias(tablero, ancho_total, largo_total):

    for i in range(ancho_total):
        if i == 0:
            for j in range(largo_total):
                if j == 0:                     #esquina superior izq tablero
                    if tablero[i][j] == "N":
                        if tablero[i][j+1] != "N" and tablero[i+1][j] != "N" and tablero[i+1][j+1] != "N":
                            e_s_i_d = int(tablero[i][j+1]) + 1
                            tablero[i][j+1] = e_s_i_d
                            e_s_i_a = int(tablero[i+1][j]) + 1
                            tablero[i+1][j] = e_s_i_a
                            e_s_i_ad = int(tablero[i+1][j+1]) + 1
                            tablero[i+1][j+1] = e_s_i_ad

                        elif tablero[i][j+1] == "N" and tablero[i+1][j] != "N" and tablero[i+1][j+1] != "N":
                            e_s_i_a = int(tablero[i+1][j]) + 1
                            tablero[i+1][j] = e_s_i_a
                            e_s_i_ad = int(tablero[i+1][j+1]) + 1
                            tablero[i+1][j+1] = e_s_i_ad

                        elif tablero[i][j+1] != "N" and tablero[i+1][j] == "N" and tablero[i+1][j+1] != "N":
                            e_s_i_d = int(tablero[i][j+1]) + 1
                            tablero[i][j+1] = e_s_i_d
                            e_s_i_ad = int(tablero[i+1][j+1]) + 1
                            tablero[i+1][j+1] = e_s_i_ad
                        
                        elif tablero[i][j+1] != "N" and tablero[i+1][j] != "N" and tablero[i+1][j+1] == "N":
                            e_s_i_d = int(tablero[i][j+1]) + 1
                            tablero[i][j+1] = e_s_i_d
                            e_s_i_a = int(tablero[i+1][j]) + 1
                            tablero[i+1][j] = e_s_i_a
              
                elif j == (largo_total-1):  #esquina superior der tablero
                    if tablero[i][j] == "N":
                        if tablero[i][j-1] != "N" and tablero[i+1][j] != "N" and tablero[i+1][j-1] != "N":
                            e_s_d_i = int(tablero[i][j-1]) + 1
                            tablero[i][j-1] = e_s_d_i
                            e_s_d_a = int(tablero[i+1][j]) + 1
                            tablero[i+1][j] = e_s_d_a
                            e_s_d_ai = int(tablero[i+1][j-1]) + 1
                            tablero[i+1][j-1] = e_s_d_ai

                        elif tablero[i][j-1] == "N" and tablero[i+1][j] != "N" and tablero[i+1][j-1] != "N":
                            e_s_d_a = int(tablero[i+1][j]) + 1
                            tablero[i+1][j] = e_s_d_a
                            e_s_d_ai = int(tablero[i+1][j-1]) + 1
                            tablero[i+1][j-1] = e_s_d_ai
                        
                        elif tablero[i][j-1] != "N" and tablero[i+1][j] == "N" and tablero[i+1][j-1] != "N":
                            e_s_d_i = int(tablero[i][j-1]) + 1
                            tablero[i][j-1] = e_s_d_i
                            e_s_d_ai = int(tablero[i+1][j-1]) + 1
                            tablero[i+1][j-1] = e_s_d_ai
                        
                        elif tablero[i][j-1] != "N" and tablero[i+1][j] != "N" and tablero[i+1][j-1] == "N":
                            e_s_d_i = int(tablero[i][j-1]) + 1
                            tablero[i][j-1] = e_s_d_i
                            e_s_d_a = int(tablero[i+1][j]) + 1
                            tablero[i+1][j] = e_s_d_a

                else:                          # otro punto primera fila
                    if tablero[i][j] == "N":

                        if tablero[i][j-1] != "N" and tablero[i][j+1] != "N" and tablero[i+1][j] != "N" and \
                            tablero[i+1][j-1] != "N" and tablero[i+1][j+1] != "N":
                            s_i = int(tablero[i][j-1]) + 1
                            tablero[i][j-1] = s_i
                            s_d = int(tablero[i][j+1]) + 1
                            tablero[i][j+1] = s_d
                            s_a = int(tablero[i+1][j]) + 1
                            tablero[i+1][j] = s_a
                            s_ai = int(tablero[i+1][j-1]) + 1
                            tablero[i+1][j-1] = s_ai
                            s_ad = int(tablero[i+1][j+1]) + 1
                            tablero[i+1][j+1] = s_ad

                        elif tablero[i][j-1] == "N" and tablero[i][j+1] != "N" and tablero[i+1][j] != "N" and \
                            tablero[i+1][j-1] != "N" and tablero[i+1][j+1] != "N":

                            s_d = int(tablero[i][j+1]) + 1
                            tablero[i][j+1] = s_d
                            s_a = int(tablero[i+1][j]) + 1
                            tablero[i+1][j] = s_a
                            s_ai = int(tablero[i+1][j-1]) + 1
                            tablero[i+1][j-1] = s_ai
                            s_ad = int(tablero[i+1][j+1]) + 1
                            tablero[i+1][j+1] = s_ad

                        elif tablero[i][j-1] != "N" and tablero[i][j+1] == "N" and tablero[i+1][j] != "N" and \
                            tablero[i+1][j-1] != "N" and tablero[i+1][j+1] != "N":
                            s_i = int(tablero[i][j-1]) + 1
                            tablero[i][j-1] = s_i
                            s_a = int(tablero[i+1][j]) + 1
                            tablero[i+1][j] = s_a
                            s_ai = int(tablero[i+1][j-1]) + 1
                            tablero[i+1][j-1] = s_ai
                            s_ad = int(tablero[i+1][j+1]) + 1
                            tablero[i+1][j+1] = s_ad

                        elif tablero[i][j-1] != "N" and tablero[i][j+1] != "N" and tablero[i+1][j] == "N" and \
                            tablero[i+1][j-1] != "N" and tablero[i+1][j+1] != "N":
                            s_i = int(tablero[i][j-1]) + 1
                            tablero[i][j-1] = s_i
                            s_d = int(tablero[i][j+1]) + 1
                            tablero[i][j+1] = s_d
                            s_ai = int(tablero[i+1][j-1]) + 1
                            tablero[i+1][j-1] = s_ai
                            s_ad = int(tablero[i+1][j+1]) + 1
                            tablero[i+1][j+1] = s_ad

                        elif tablero[i][j-1] != "N" and tablero[i][j+1] != "N" and tablero[i+1][j] != "N" and \
                            tablero[i+1][j-1] == "N" and tablero[i+1][j+1] != "N":
                            s_i = int(tablero[i][j-1]) + 1
                            tablero[i][j-1] = s_i
                            s_d = int(tablero[i][j+1]) + 1
                            tablero[i][j+1] = s_d
                            s_a = int(tablero[i+1][j]) + 1
                            tablero[i+1][j] = s_a
                            s_ad = int(tablero[i+1][j+1]) + 1
                            tablero[i+1][j+1] = s_ad
                        
                        elif tablero[i][j-1] != "N" and tablero[i][j+1] != "N" and tablero[i+1][j] != "N" and \
                            tablero[i+1][j-1] != "N" and tablero[i+1][j+1] == "N":
                            s_i = int(tablero[i][j-1]) + 1
                            tablero[i][j-1] = s_i
                            s_d = int(tablero[i][j+1]) + 1
                            tablero[i][j+1] = s_d
                            s_a = int(tablero[i+1][j]) + 1
                            tablero[i+1][j] = s_a
                            s_ai = int(tablero[i+1][j-1]) + 1
                            tablero[i+1][j-1] = s_ai

        elif i == (ancho_total-1):
            for j in range(largo_total):
                if j == 0:                     #esquina inferior izq tablero
                    if tablero[i][j] == "N":
                        if tablero[i-1][j] != "N" and tablero[i-1][j+1] != "N" and tablero[i][j+1] != "N":
                            e_i_i_a = int(tablero[i-1][j]) + 1
                            tablero[i-1][j] = e_i_i_a
                            e_i_i_ad = int(tablero[i-1][j+1]) + 1
                            tablero[i-1][j+1] = e_i_i_ad
                            e_i_i_d = int(tablero[i][j+1]) + 1
                            tablero[i][j+1] = e_i_i_d

                        elif tablero[i-1][j] == "N" and tablero[i-1][j+1] != "N" and tablero[i][j+1] != "N":
                            e_i_i_ad = int(tablero[i-1][j+1]) + 1
                            tablero[i-1][j+1] = e_i_i_ad
                            e_i_i_d = int(tablero[i][j+1]) + 1
                            tablero[i][j+1] = e_i_i_d

                        elif tablero[i-1][j] != "N" and tablero[i-1][j+1] == "N" and tablero[i][j+1] != "N":
                            e_i_i_a = int(tablero[i-1][j]) + 1
                            tablero[i-1][j] = e_i_i_a
                            e_i_i_d = int(tablero[i][j+1]) + 1
                            tablero[i][j+1] = e_i_i_d

                        elif tablero[i-1][j] != "N" and tablero[i-1][j+1] != "N" and tablero[i][j+1] == "N":
                            e_i_i_a = int(tablero[i-1][j]) + 1
                            tablero[i-1][j] = e_i_i_a
                            e_i_i_ad = int(tablero[i-1][j+1]) + 1
                            tablero[i-1][j+1] = e_i_i_ad

                
                elif j == (largo_total-1):  #esquina inferior der tablero
                    if tablero[i][j] == "N":
                        if tablero[i][j-1] != "N" and tablero[i-1][j] != "N" and tablero[i-1][j-1] != "N":
                            e_i_d_i = int(tablero[i][j-1]) + 1
                            tablero[i][j-1] = e_i_d_i
                            e_i_d_a = int(tablero[i-1][j]) + 1
                            tablero[i-1][j] = e_i_d_a
                            e_i_d_ai = int(tablero[i-1][j-1]) + 1
                            tablero[i-1][j-1] = e_i_d_ai

                        elif tablero[i][j-1] == "N" and tablero[i-1][j] != "N" and tablero[i-1][j-1] != "N":
                            e_i_d_a = int(tablero[i-1][j]) + 1
                            tablero[i-1][j] = e_i_d_a
                            e_i_d_ai = int(tablero[i-1][j-1]) + 1
                            tablero[i-1][j-1] = e_i_d_ai

                        elif tablero[i][j-1] != "N" and tablero[i-1][j] == "N" and tablero[i-1][j-1] != "N":
                            e_i_d_i = int(tablero[i][j-1]) + 1
                            tablero[i][j-1] = e_i_d_i
                            e_i_d_ai = int(tablero[i-1][j-1]) + 1
                            tablero[i-1][j-1] = e_i_d_ai

                        elif tablero[i][j-1] != "N" and tablero[i-1][j] != "N" and tablero[i-1][j-1] == "N":
                            e_i_d_i = int(tablero[i][j-1]) + 1
                            tablero[i][j-1] = e_i_d_i
                            e_i_d_a = int(tablero[i-1][j]) + 1
                            tablero[i-1][j] = e_i_d_a

                else:                          # otro punto ultima fila
                    if tablero[i][j] == "N":
                        if tablero[i][j-1] != "N" and tablero[i][j+1] != "N" and tablero[i-1][j] != "N" and \
                            tablero[i-1][j-1] != "N" and tablero[i-1][j+1] != "N":
                            i_i = int(tablero[i][j-1]) + 1
                            tablero[i][j-1] = i_i
                            i_d = int(tablero[i][j+1]) + 1
                            tablero[i][j+1] = i_d
                            i_a = int(tablero[i-1][j]) + 1
                            tablero[i-1][j] = i_a
                            i_ai = int(tablero[i-1][j-1]) + 1
                            tablero[i-1][j-1] = i_ai
                            i_ad = int(tablero[i-1][j+1]) + 1
                            tablero[i-1][j+1] = i_ad
                        
                        elif tablero[i][j-1] == "N" and tablero[i][j+1] != "N" and tablero[i-1][j] != "N" and \
                            tablero[i-1][j-1] != "N" and tablero[i-1][j+1] != "N":
                            i_d = int(tablero[i][j+1]) + 1
                            tablero[i][j+1] = i_d
                            i_a = int(tablero[i-1][j]) + 1
                            tablero[i-1][j] = i_a
                            i_ai = int(tablero[i-1][j-1]) + 1
                            tablero[i-1][j-1] = i_ai
                            i_ad = int(tablero[i-1][j+1]) + 1
                            tablero[i-1][j+1] = i_ad
                        
                        elif tablero[i][j-1] != "N" and tablero[i][j+1] == "N" and tablero[i-1][j] != "N" and \
                            tablero[i-1][j-1] != "N" and tablero[i-1][j+1] != "N":
                            i_i = int(tablero[i][j-1]) + 1
                            tablero[i][j-1] = i_i
                            i_a = int(tablero[i-1][j]) + 1
                            tablero[i-1][j] = i_a
                            i_ai = int(tablero[i-1][j-1]) + 1
                            tablero[i-1][j-1] = i_ai                            
                            i_ad = int(tablero[i-1][j+1]) + 1
                            tablero[i-1][j+1] = i_ad

                        elif tablero[i][j-1] != "N" and tablero[i][j+1] != "N" and tablero[i-1][j] == "N" and \
                            tablero[i-1][j-1] != "N" and tablero[i-1][j+1] != "N":
                            i_i = int(tablero[i][j-1]) + 1
                            tablero[i][j-1] = i_i
                            i_d = int(tablero[i][j+1]) + 1
                            tablero[i][j+1] = i_d
                            i_ai = int(tablero[i-1][j-1]) + 1
                            tablero[i-1][j-1] = i_ai                            
                            i_ad = int(tablero[i-1][j+1]) + 1
                            tablero[i-1][j+1] = i_ad
                        
                        elif tablero[i][j-1] != "N" and tablero[i][j+1] != "N" and tablero[i-1][j] != "N" and \
                            tablero[i-1][j-1] == "N" and tablero[i-1][j+1] != "N":
                            i_i = int(tablero[i][j-1]) + 1
                            tablero[i][j-1] = i_i
                            i_d = int(tablero[i][j+1]) + 1
                            tablero[i][j+1] = i_d
                            i_a = int(tablero[i-1][j]) + 1
                            tablero[i-1][j] = i_a
                            i_ad = int(tablero[i-1][j+1]) + 1
                            tablero[i-1][j+1] = i_ad
                        
                        elif tablero[i][j-1] != "N" and tablero[i][j+1] != "N" and tablero[i-1][j] != "N" and \
                            tablero[i-1][j-1] != "N" and tablero[i-1][j+1] == "N":
                            i_i = int(tablero[i][j-1]) + 1
                            tablero[i][j-1] = i_i
                            i_d = int(tablero[i][j+1]) + 1
                            tablero[i][j+1] = i_d
                            i_a = int(tablero[i-1][j]) + 1
                            tablero[i-1][j] = i_a
                            i_ai = int(tablero[i-1][j-1]) + 1
                            tablero[i-1][j-1] = i_ai
        else:
            for j in range(largo_total-1):
                if tablero[i][0] == "N":         #columna izquierda
                    if tablero[i-1][j] != "N" and tablero[i+1][j] != "N" and tablero[i][j+1] != "N" and \
                        tablero[i-1][j+1] != "N" and tablero[i+1][j+1] != "N":
                        cd_s = int(tablero[i-1][j]) + 1
                        tablero[i-1][j] = cd_s
                        cd_i = int(tablero[i+1][j]) + 1
                        tablero[i+1][j] = cd_i
                        cd_d = int(tablero[i][j+1]) + 1
                        tablero[i][j+1] = cd_d
                        cd_i_i = int(tablero[i-1][j+1]) + 1
                        tablero[i-1][j+1] = cd_i_i
                        cd_s_i = int(tablero[i+1][j+1]) + 1
                        tablero[i+1][j+1] = cd_s_i
                    
                    elif tablero[i-1][j] == "N" and tablero[i+1][j] != "N" and tablero[i][j+1] != "N" and \
                        tablero[i-1][j+1] != "N" and tablero[i+1][j+1] != "N":
                        cd_i = int(tablero[i+1][j]) + 1
                        tablero[i+1][j] = cd_i
                        cd_d = int(tablero[i][j+1]) + 1
                        tablero[i][j+1] = cd_d
                        cd_i_i = int(tablero[i-1][j+1]) + 1
                        tablero[i-1][j+1] = cd_i_i
                        cd_s_i = int(tablero[i+1][j+1]) + 1
                        tablero[i+1][j+1] = cd_s_i

                    elif tablero[i-1][j] != "N" and tablero[i+1][j] == "N" and tablero[i][j+1] != "N" and \
                        tablero[i-1][j+1] != "N" and tablero[i+1][j+1] != "N":
                        cd_s = int(tablero[i-1][j]) + 1
                        tablero[i-1][j] = cd_s
                        cd_d = int(tablero[i][j+1]) + 1
                        tablero[i][j+1] = cd_d
                        cd_i_i = int(tablero[i-1][j+1]) + 1
                        tablero[i-1][j+1] = cd_i_i
                        cd_s_i = int(tablero[i+1][j+1]) + 1
                        tablero[i+1][j+1] = cd_s_i
                    
                    elif tablero[i-1][j] != "N" and tablero[i+1][j] != "N" and tablero[i][j+1] == "N" and \
                        tablero[i-1][j+1] != "N" and tablero[i+1][j+1] != "N":
                        cd_s = int(tablero[i-1][j]) + 1
                        tablero[i-1][j] = cd_s
                        cd_i = int(tablero[i+1][j]) + 1
                        tablero[i+1][j] = cd_i
                        cd_i_i = int(tablero[i-1][j+1]) + 1
                        tablero[i-1][j+1] = cd_i_i
                        cd_s_i = int(tablero[i+1][j+1]) + 1
                        tablero[i+1][j+1] = cd_s_i

                    elif tablero[i-1][j] != "N" and tablero[i+1][j] != "N" and tablero[i][j+1] != "N" and \
                        tablero[i-1][j+1] == "N" and tablero[i+1][j+1] != "N":
                        cd_s = int(tablero[i-1][j]) + 1
                        tablero[i-1][j] = cd_s
                        cd_i = int(tablero[i+1][j]) + 1
                        tablero[i+1][j] = cd_i
                        cd_d = int(tablero[i][j+1]) + 1
                        tablero[i][j+1] = cd_d
                        cd_s_i = int(tablero[i+1][j+1]) + 1
                        tablero[i+1][j+1] = cd_s_i

                    elif tablero[i-1][j] != "N" and tablero[i+1][j] != "N" and tablero[i][j+1] != "N" and \
                        tablero[i-1][j+1] != "N" and tablero[i+1][j+1] == "N":
                        cd_s = int(tablero[i-1][j]) + 1
                        tablero[i-1][j] = cd_s
                        cd_i = int(tablero[i+1][j]) + 1
                        tablero[i+1][j] = cd_i
                        cd_d = int(tablero[i][j+1]) + 1
                        tablero[i][j+1] = cd_d
                        cd_i_i = int(tablero[i-1][j+1]) + 1
                        tablero[i-1][j+1] = cd_i_i
                    
                elif tablero[i][largo_total-1] == "N":     #columna derecha
                    if tablero[i-1][j] != "N" and tablero[i+1][j] != "N" and tablero[i][j-1] != "N" and \
                        tablero[i-1][j-1] != "N" and tablero[i+1][j-1] != "N":
                        ci_s = int(tablero[i-1][j]) + 1
                        tablero[i-1][j] = ci_s
                        ci_i = int(tablero[i+1][j]) + 1
                        tablero[i+1][j] = ci_i
                        ci_d = int(tablero[i][j-1]) + 1
                        tablero[i][j-1] = ci_d
                        ci_i_i = int(tablero[i-1][j-1]) + 1
                        tablero[i-1][j-1] = ci_i_i
                        ci_s_i = int(tablero[i+1][j-1]) + 1
                        tablero[i+1][j-1] = ci_s_i

                    elif tablero[i-1][j] == "N" and tablero[i+1][j] != "N" and tablero[i][j-1] != "N" and \
                        tablero[i-1][j-1] != "N" and tablero[i+1][j-1] != "N":
                        ci_i = int(tablero[i+1][j]) + 1
                        tablero[i+1][j] = ci_i
                        ci_d = int(tablero[i][j-1]) + 1
                        tablero[i][j-1] = ci_d
                        ci_i_i = int(tablero[i-1][j-1]) + 1
                        tablero[i-1][j-1] = ci_i_i
                        ci_s_i = int(tablero[i+1][j-1]) + 1
                        tablero[i+1][j-1] = ci_s_i

                    elif tablero[i-1][j] != "N" and tablero[i+1][j] == "N" and tablero[i][j-1] != "N" and \
                        tablero[i-1][j-1] != "N" and tablero[i+1][j-1] != "N":
                        ci_s = int(tablero[i-1][j]) + 1
                        tablero[i-1][j] = ci_s
                        ci_d = int(tablero[i][j-1]) + 1
                        tablero[i][j-1] = ci_d
                        ci_i_i = int(tablero[i-1][j-1]) + 1
                        tablero[i-1][j-1] = ci_i_i
                        ci_s_i = int(tablero[i+1][j-1]) + 1
                        tablero[i+1][j-1] = ci_s_i

                    elif tablero[i-1][j] != "N" and tablero[i+1][j] != "N" and tablero[i][j-1] == "N" and \
                        tablero[i-1][j-1] != "N" and tablero[i+1][j-1] != "N":
                        ci_s = int(tablero[i-1][j]) + 1
                        tablero[i-1][j] = ci_s
                        ci_i = int(tablero[i+1][j]) + 1
                        tablero[i+1][j] = ci_i
                        ci_i_i = int(tablero[i-1][j-1]) + 1
                        tablero[i-1][j-1] = ci_i_i
                        ci_s_i = int(tablero[i+1][j-1]) + 1
                        tablero[i+1][j-1] = ci_s_i

                    elif tablero[i-1][j] != "N" and tablero[i+1][j] != "N" and tablero[i][j-1] != "N" and \
                        tablero[i-1][j-1] == "N" and tablero[i+1][j-1] != "N":
                        ci_s = int(tablero[i-1][j]) + 1
                        tablero[i-1][j] = ci_s
                        ci_i = int(tablero[i+1][j]) + 1
                        tablero[i+1][j] = ci_i
                        ci_d = int(tablero[i][j-1]) + 1
                        tablero[i][j-1] = ci_d
                        ci_s_i = int(tablero[i+1][j-1]) + 1
                        tablero[i+1][j-1] = ci_s_i

                    elif tablero[i-1][j] != "N" and tablero[i+1][j] != "N" and tablero[i][j-1] != "N" and \
                        tablero[i-1][j-1] != "N" and tablero[i+1][j-1] == "N":
                        ci_s = int(tablero[i-1][j]) + 1
                        tablero[i-1][j] = ci_s
                        ci_i = int(tablero[i+1][j]) + 1
                        tablero[i+1][j] = ci_i
                        ci_d = int(tablero[i][j-1]) + 1
                        tablero[i][j-1] = ci_d
                        ci_i_i = int(tablero[i-1][j-1]) + 1
                        tablero[i-1][j-1] = ci_i_i
    #################        
                elif tablero[i][j] == "N":     # para todo
                    if tablero[i][j-1] != "N" and tablero[i][j+1] != "N" and tablero[i-1][j] != "N" and \
                        tablero[i+1][j] != "N" and tablero[i-1][j-1] != "N" and tablero[i-1][j+1] != "N" and \
                            tablero[i+1][j-1] != "N" and tablero[i+1][j+1] != "N":
                        izq = int(tablero[i][j-1]) + 1
                        tablero[i][j-1] = izq
                        der = int(tablero[i][j+1]) + 1
                        tablero[i][j+1] = der
                        arr = int(tablero[i-1][j]) + 1
                        tablero[i-1][j] = arr
                        aba = int(tablero[i+1][j]) + 1
                        tablero[i+1][j] = aba
                        aba_izq = (tablero[i-1][j-1]) + 1
                        tablero[i-1][j-1] = aba_izq
                        aba_der = int(tablero[i-1][j+1]) + 1
                        tablero[i-1][j+1] = aba_der
                        arr_izq = int(tablero[i+1][j-1]) + 1
                        tablero[i+1][j-1] = arr_izq
                        arr_der = int(tablero[i+1][j+1]) + 1
                        tablero[i+1][j+1] == arr_der

                    elif tablero[i][j-1] == "N" and tablero[i][j+1] != "N" and tablero[i-1][j] != "N" and \
                        tablero[i+1][j] != "N" and tablero[i-1][j-1] != "N" and tablero[i-1][j+1] != "N" and \
                            tablero[i+1][j-1] != "N" and tablero[i+1][j+1] != "N":
                        der = int(tablero[i][j+1]) + 1
                        tablero[i][j+1] = der
                        arr = int(tablero[i-1][j]) + 1
                        tablero[i-1][j] = arr
                        aba = int(tablero[i+1][j]) + 1
                        tablero[i+1][j] = aba
                        aba_izq = (tablero[i-1][j-1]) + 1
                        tablero[i-1][j-1] = aba_izq
                        aba_der = int(tablero[i-1][j+1]) + 1
                        tablero[i-1][j+1] = aba_der
                        arr_izq = int(tablero[i+1][j-1]) + 1
                        tablero[i+1][j-1] = arr_izq
                        arr_der = int(tablero[i+1][j+1]) + 1
                        tablero[i+1][j+1] == arr_der

                    elif tablero[i][j-1] != "N" and tablero[i][j+1] == "N" and tablero[i-1][j] != "N" and \
                        tablero[i+1][j] != "N" and tablero[i-1][j-1] != "N" and tablero[i-1][j+1] != "N" and \
                            tablero[i+1][j-1] != "N" and tablero[i+1][j+1] != "N":
                        izq = int(tablero[i][j-1]) + 1
                        tablero[i][j-1] = izq
                        arr = int(tablero[i-1][j]) + 1
                        tablero[i-1][j] = arr
                        aba = int(tablero[i+1][j]) + 1
                        tablero[i+1][j] = aba
                        aba_izq = (tablero[i-1][j-1]) + 1
                        tablero[i-1][j-1] = aba_izq
                        aba_der = int(tablero[i-1][j+1]) + 1
                        tablero[i-1][j+1] = aba_der
                        arr_izq = int(tablero[i+1][j-1]) + 1
                        tablero[i+1][j-1] = arr_izq
                        arr_der = int(tablero[i+1][j+1]) + 1
                        tablero[i+1][j+1] == arr_der

                    elif tablero[i][j-1] != "N" and tablero[i][j+1] != "N" and tablero[i-1][j] == "N" and \
                        tablero[i+1][j] != "N" and tablero[i-1][j-1] != "N" and tablero[i-1][j+1] != "N" and \
                            tablero[i+1][j-1] != "N" and tablero[i+1][j+1] != "N":
                        izq = int(tablero[i][j-1]) + 1
                        tablero[i][j-1] = izq
                        der = int(tablero[i][j+1]) + 1
                        tablero[i][j+1] = der
                        aba = int(tablero[i+1][j]) + 1
                        tablero[i+1][j] = aba
                        aba_izq = (tablero[i-1][j-1]) + 1
                        tablero[i-1][j-1] = aba_izq
                        aba_der = int(tablero[i-1][j+1]) + 1
                        tablero[i-1][j+1] = aba_der
                        arr_izq = int(tablero[i+1][j-1]) + 1
                        tablero[i+1][j-1] = arr_izq
                        arr_der = int(tablero[i+1][j+1]) + 1
                        tablero[i+1][j+1] == arr_der

                    elif tablero[i][j-1] != "N" and tablero[i][j+1] != "N" and tablero[i-1][j] != "N" and \
                        tablero[i+1][j] == "N" and tablero[i-1][j-1] != "N" and tablero[i-1][j+1] != "N" and \
                            tablero[i+1][j-1] != "N" and tablero[i+1][j+1] != "N":
                        izq = int(tablero[i][j-1]) + 1
                        tablero[i][j-1] = izq
                        der = int(tablero[i][j+1]) + 1
                        tablero[i][j+1] = der
                        arr = int(tablero[i-1][j]) + 1
                        tablero[i-1][j] = arr
                        aba_izq = (tablero[i-1][j-1]) + 1
                        tablero[i-1][j-1] = aba_izq
                        aba_der = int(tablero[i-1][j+1]) + 1
                        tablero[i-1][j+1] = aba_der
                        arr_izq = int(tablero[i+1][j-1]) + 1
                        tablero[i+1][j-1] = arr_izq
                        arr_der = int(tablero[i+1][j+1]) + 1
                        tablero[i+1][j+1] == arr_der

                    elif tablero[i][j-1] != "N" and tablero[i][j+1] != "N" and tablero[i-1][j] != "N" and \
                        tablero[i+1][j] != "N" and tablero[i-1][j-1] == "N" and tablero[i-1][j+1] != "N" and \
                            tablero[i+1][j-1] != "N" and tablero[i+1][j+1] != "N":
                        izq = int(tablero[i][j-1]) + 1
                        tablero[i][j-1] = izq
                        der = int(tablero[i][j+1]) + 1
                        tablero[i][j+1] = der
                        arr = int(tablero[i-1][j]) + 1
                        tablero[i-1][j] = arr
                        aba = int(tablero[i+1][j]) + 1
                        tablero[i+1][j] = aba
                        aba_der = int(tablero[i-1][j+1]) + 1
                        tablero[i-1][j+1] = aba_der
                        arr_izq = int(tablero[i+1][j-1]) + 1
                        tablero[i+1][j-1] = arr_izq
                        arr_der = int(tablero[i+1][j+1]) + 1
                        tablero[i+1][j+1] == arr_der

                    elif tablero[i][j-1] != "N" and tablero[i][j+1] != "N" and tablero[i-1][j] != "N" and \
                        tablero[i+1][j] != "N" and tablero[i-1][j-1] != "N" and tablero[i-1][j+1] == "N" and \
                            tablero[i+1][j-1] != "N" and tablero[i+1][j+1] != "N":
                        izq = int(tablero[i][j-1]) + 1
                        tablero[i][j-1] = izq
                        der = int(tablero[i][j+1]) + 1
                        tablero[i][j+1] = der
                        arr = int(tablero[i-1][j]) + 1
                        tablero[i-1][j] = arr
                        aba = int(tablero[i+1][j]) + 1
                        tablero[i+1][j] = aba
                        aba_izq = (tablero[i-1][j-1]) + 1
                        tablero[i-1][j-1] = aba_izq
                        arr_izq = int(tablero[i+1][j-1]) + 1
                        tablero[i+1][j-1] = arr_izq
                        arr_der = int(tablero[i+1][j+1]) + 1
                        tablero[i+1][j+1] == arr_der

                    elif tablero[i][j-1] != "N" and tablero[i][j+1] != "N" and tablero[i-1][j] != "N" and \
                        tablero[i+1][j] != "N" and tablero[i-1][j-1] != "N" and tablero[i-1][j+1] != "N" and \
                            tablero[i+1][j-1] == "N" and tablero[i+1][j+1] != "N":
                        izq = int(tablero[i][j-1]) + 1
                        tablero[i][j-1] = izq
                        der = int(tablero[i][j+1]) + 1
                        tablero[i][j+1] = der
                        arr = int(tablero[i-1][j]) + 1
                        tablero[i-1][j] = arr
                        aba = int(tablero[i+1][j]) + 1
                        tablero[i+1][j] = aba
                        aba_izq = (tablero[i-1][j-1]) + 1
                        tablero[i-1][j-1] = aba_izq
                        aba_der = int(tablero[i-1][j+1]) + 1
                        tablero[i-1][j+1] = aba_der
                        arr_der = int(tablero[i+1][j+1]) + 1
                        tablero[i+1][j+1] == arr_der

                    elif tablero[i][j-1] != "N" and tablero[i][j+1] != "N" and tablero[i-1][j] != "N" and \
                        tablero[i+1][j] != "N" and tablero[i-1][j-1] != "N" and tablero[i-1][j+1] != "N" and \
                            tablero[i+1][j-1] != "N" and tablero[i+1][j+1] == "N":
                        izq = int(tablero[i][j-1]) + 1
                        tablero[i][j-1] = izq
                        der = int(tablero[i][j+1]) + 1
                        tablero[i][j+1] = der
                        arr = int(tablero[i-1][j]) + 1
                        tablero[i-1][j] = arr
                        aba = int(tablero[i+1][j]) + 1
                        tablero[i+1][j] = aba
                        aba_izq = (tablero[i-1][j-1]) + 1
                        tablero[i-1][j-1] = aba_izq
                        aba_der = int(tablero[i-1][j+1]) + 1
                        tablero[i-1][j+1] = aba_der
                        arr_izq = int(tablero[i+1][j-1]) + 1
                        tablero[i+1][j-1] = arr_izq

    return tablero
