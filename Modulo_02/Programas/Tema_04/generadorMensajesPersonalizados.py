def generar_mensaje(nombre, mensaje="Bienvenido al curso de python"):
    """ funcion que genera un mensaje personalizado a través de los valores ingresados
    Keyword arguments
    nombre -- Nombre propio a quien va dirigido
    mensaje -- Mensaje a imprimir

    Return mensaje personalizado
    """
    return f"¡Hola, {nombre}! {mensaje}"

print(generar_mensaje("Pablo"))
print(generar_mensaje("Pablo", mensaje="¿Como te encuentras hoy?"))