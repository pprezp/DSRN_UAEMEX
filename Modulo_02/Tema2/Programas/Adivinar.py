def palabra_adivinar(letra_palabra, palabra_intento):
    """
        Funcion para validar si se adivino la palabra
    """
    palabra_adivinar = "Pablo"
    letra_en_palabra = letra_palabra in palabra_adivinar

    resultado_adivinanza = ( len(palabra_intento) == len(palabra_adivinar) ) and palabra_adivinar == palabra_intento
    print(f"¿La letra de prueba se encuentra en la palabra? {letra_en_palabra}")
    print(f"El jugador gana: {resultado_adivinanza}")



letra = input("Ingresa la letra a buscar: ")
palabra = input("Ingresa la palabra que crees que pueda ser: ")

palabra_adivinar(letra, palabra)