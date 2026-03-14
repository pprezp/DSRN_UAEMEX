def comparar_longitud(palabra1, palabra2):
    """
        Funcion que compara la longitud de 2 cadenas de texto

        Arg:
        palabra1: str
        palabra2: str

        return:
        longitudIgual: bool
    """
    return len(palabra1)==len(palabra2)



palabra1 = "Perro"
palabra2 = "Gato"

print(f"¿Son '{palabra1}' y '{palabra2}' iguales? {comparar_longitud(palabra1, palabra2)}")