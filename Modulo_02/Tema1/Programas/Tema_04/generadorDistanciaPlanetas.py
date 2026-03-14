def generadorDistanciaPLanetas(nombrePlaneta, distanciaMillonesKM):
    return "Nombre del planeta: " + str(nombrePlaneta), "Distancia al planeta: " + str(distanciaMillonesKM) + " millones de km"


texto1, texto2 = generadorDistanciaPLanetas("Saturno", 1_200)

print(texto1)
print(texto2)