def cabecera():
    """Muestra la cabecera de la aplicación"""
    cabecero = """
         #####                              #######                         ######                              
        #     #   ##   #    # ###### #####     #      ##    ####   ####     #     #   ##   #####  #       ####  
        #        #  #  ##  ## #      #    #    #     #  #  #    # #         #     #  #  #  #    # #      #    # 
        #  #### #    # # ## # #####  #    #    #    #    # #       ####     ######  #    # #####  #      #    # 
        #     # ###### #    # #      #####     #    ###### #  ###      #    #       ###### #    # #      #    # 
        #     # #    # #    # #      #   #     #    #    # #    # #    #    #       #    # #    # #      #    # 
         #####  #    # #    # ###### #    #    #    #    #  ####   ####     #       #    # #####  ######  #### 
          
                                            👾¡Crea tu identidad como Gamer!👾                         
        """

    print(cabecero)


def tagBasico(nombre):
    """Funcion que crea un gamertag a partir de las primeras 4 letras de un string\n
    Parametro: \n
    nombre(str): username\n

    return\n
    str: basic gamertag
    """
    tag = nombre[0:4]
    return tag


def nombreInvertido(nombre):
    """Funcion que crea un gamertag a partir de linvertir el nombre completo del usuario\n
    Parametros:\n
    nombre(srt): nombre del usuario\n

    return:\n
    str: gamertag invertido

    """
    nombreInvertido = nombre[::-1]
    return nombreInvertido


def gamerTagIntercalado(nombre, apellido):
    """Funcion que crea un gamertag a partir de intercalar el nombre y apellido del usuario\n
    Parametros:\n
    nombre(srt): nombre del usuario\n
    apellido(srt): apellido del usuario\n

    return:\n
    str: gamertag intercalado

    """
    return nombre[0] + apellido[0] + nombre[1:] + apellido[1:]


def creaTagElite(nombre):
    """Funcion que crea un gamertag a partir de el nombre del usuario\n
    Parametros:\n
    nombre(srt): nombre del usuario\n

    return:\n
    str: gamertag elite

    """
    tag = nombre[0:2] + nombre[-2:]
    return tag


def creaTagConNumero(nombre, numero):
    """Funcion que crea un gamertag a partir de el nombre del usuario y un numero\n
    Parametros:\n
    nombre(srt): nombre del usuario\n
    numero(int): numero favorito del usuario\n

    return:\n
    str: gamertag con numero

    """
    return nombre[:5] + str(numero)


def imprimeGamerTags(nombre, apellido, numero):
    print(
        """
        ______________________________________________________
                        🎯¡Gamertags generados!
        ______________________________________________________
          """
    )
    print("1.- Gamertag básico:", tagBasico(nombre))
    print("2.- Gamertag invertido:", nombreInvertido(nombre))
    print("3.- Gamertag intercalado:", gamerTagIntercalado(nombre, apellido))
    print("4.- Gamertag elite:", creaTagElite(nombre))
    print("5.- Gamertag con número:", creaTagConNumero(nombre, numero))


def mostrarEstadisticas(nombre):
    """
    Muestra estadísticas del nombre proporcionado

    Parametros:\n
    nombre(srt): nombre del usuario\n

    return:\n
    None (Imprime directamente)
    """
    nLetras = str(len(nombre))
    primerLetra = nombre[0]
    ultimaLetra = nombre[-1]
    print("\n📊 ESTADÍSTICAS DE TU NOMBRE:\n")
    print("Nombre completo:", nombre)
    print("Longitud del nombre:", nLetras, "letras")
    print("Primera letra:", primerLetra)
    print("Última letra:", ultimaLetra)
    print()
    return


def __main__():
    cabecera()
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    numeroFavorito = int(input("Número favorito: "))
    mostrarEstadisticas(nombre)
    imprimeGamerTags(nombre, apellido, numeroFavorito)
    print("✨ Elige tu favorito y conquista el mundo gamer✨\n")
    return


if __name__ == "__main__":
    __main__()
 