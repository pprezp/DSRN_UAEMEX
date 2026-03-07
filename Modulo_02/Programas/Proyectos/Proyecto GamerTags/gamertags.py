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
          
                                                 ¡Crea tu identidad como Gamer!                          
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

def __main__():
    cabecera()
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")

    print(tagBasico(nombre))
    print(nombreInvertido(nombre))

if __name__=="__main__":
    __main__()