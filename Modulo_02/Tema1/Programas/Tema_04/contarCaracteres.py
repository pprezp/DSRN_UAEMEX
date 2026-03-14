def contarCaracteres(frase = "Aprender Python es divertido"):
    """Funcion que cuenta el numero de caracteres e imprime el resultado\n
    Keyword arguments\n
    frase -- variable String para contar los caracteres
    """
    print("La frase", frase, "tiene", str(len(frase)), "caracteres")
    return

def convertirNumero(numero):
    """Funcion que realiza el casteo de un numero a String y Float\n
    Keyword arguments\n
    numero -- variable String para contar los caracteres
    """
    print(f"1.- Entero: {numero}, Tipo: {type(numero)}")
    print(f"2.- Cadena: {str(numero)}, Tipo: {type(str(numero))}")
    print(f"3.- Flotante: {float(numero)}, Tipo: {type(float(numero))}")

contarCaracteres()
contarCaracteres("¡El diplomado DSRNArtifiales es muy interesante!")

convertirNumero(10)