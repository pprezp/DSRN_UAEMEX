def calcular_Calorias(carbohidratos, proteinas, grasas):
    """
    Funcion que retorna el calculo de calorias totales con base a los gr de proterinas carbohidratos y grasas\n
        Args:
        carbohidratos: int
        proteinas: int
        grasas: int

    return
    caloriasTotales: int
    """
    return (carbohidratos *4) + ( proteinas * 4 ) + ( grasas * 9 )


calTotales = calcular_Calorias(10, 40, 5)
    
print(f"Calorias Totales: { calTotales }")