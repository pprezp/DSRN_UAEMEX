# ==========================================
# CALCULADORA DE FITNESS Y SALUD PERSONAL
# ==========================================


def calcular_imc(pesoKg, alturaM):
    """
        Calcular Índice de Masa Corporal (IMC)
        Fórmula: IMC = peso / (altura^2)

        Parámetros:
        pesoKg: float
        alturaM: float

        Return:
        float: result
    """
    return pesoKg / ( alturaM ** 2)


def peso_es_saludable(imc):
    """
        Determina si el IMC está en rango saludable (18.5 - 24.9).
    
        Parámetro:
        imc (float): Índice de Masa Corporal
    
        Retorna:
        bool: True si está en rango saludable, False si no
    """
    return imc >= 18.5 and imc <= 24.9


def tiene_sobrepeso(imc):
    """
        Determina si se cuenta con sobrepeso tomando como referencia el IMC
    
        Parámetro:
        imc (float): Índice de Masa Corporal
    
        Retorna:
        bool: True si tiene sobrepeso, False si no
    """
    return imc >= 25

def tiene_bajo_peso(imc):
    """
        Determina si se cuenta con bajo peso tomando como referencia el IMC
    
        Parámetro:
        imc (float): Índice de Masa Corporal
    
        Retorna:
        bool: True si tiene bajo peso, False si no
    """
    return imc < 18.5

def calcular_calorias_diarias(peso, altura, edad, esHombre):
    """
        Calcula las calorías diarias recomendadas usando Fórmula de Harris-Benedict.   
        Parámetros:
        peso_kg (float): Peso en kg
        altura_cm (float): Altura en cm
        edad (int): Edad en años
        es_hombre (bool): True si es hombre, False si es mujer
        
        Retorna:
        float: Calorías diarias recomendadas
    """
    calorias_hombre = 88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * edad)
    calorias_mujer = 447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * edad)
    return esHombre * calorias_hombre + (1 - esHombre) * calorias_mujer


def calcular_agua_diaria(peso):
    """
        Calcula litros de agua recomendados al día

        Parametros:
        peso: float
    """

    return peso * 35

def calcular_ritmo_cardiaco_maximo(edad):
    """
        Calcula el ritmo cardiaco máximo

        Parametros:
        edad: int
    """
    return 220 - edad


def imprime_cabecero():
    print("==========================================================")
    print("=                                                        =")
    print("=              Calculadora fitness personal              =")
    print("=                                                        =")
    print("==========================================================")

def genera_calculos():

    imprime_cabecero()

    nombre = input("¿Cual es tu nombre? ")
    peso = float(input("¿Cual es tu peso(en kg)? "))
    edad = int(input("¿Cual es tu edad? "))
    altura = float(input("¿Cual es tu altura(en m)? "))

    imc = calcular_imc(peso, altura)

    print("==========================================================")
    print("                                                        ")
    print(f"              Resultados para: {nombre}              ")
    print("                                                        ")
    print("==========================================================")

    print(f"El peso es: {peso}")
    print(f"El edad es: {edad}")
    print(f"El altura es: {altura}")

    print(f"El IMC es de {imc}")
    print(f"¿Tiene sobrepeso? { tiene_sobrepeso(imc) }")
    print(f"¿Tiene bajo peso? { tiene_bajo_peso(imc) }")
    print(f"Calorias diarias recomendadas: { calcular_calorias_diarias(peso, (altura*100),edad, True )}")
    print(f"Agua diaria recomendada: { calcular_agua_diaria(peso)/100 } Lts")
    print(f"Calorias diarias recomendadas: { calcular_ritmo_cardiaco_maximo(edad)}")


if __name__ == "__main__":
    genera_calculos()