def organizaFiesta(nInvitados,temaFiesta="Python", lugarFiesta="Aula de Informatica" ):
    print(f"Preparando una fiesta para {nInvitados} invitados")
    print(f"Tema de la fiesta: {temaFiesta} ")
    print(f"Lugar de la celebración:{lugarFiesta} ")
    print()
    return

#Ejecución solo con nInvitados
organizaFiesta(50)

#Ejecución solo con nInvitados y temaFiesta
organizaFiesta(50, "Star Wars")

#Ejecución solo con todos los parametros
organizaFiesta(50, "Cruz Azul", "Estadio Ciudad de los Deportes")