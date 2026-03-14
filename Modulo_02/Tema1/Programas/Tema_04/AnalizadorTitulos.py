tituloLibro1 = "Gregorio y el mar"
tituloLibro2 = "La llamada de Cthulu"
tituloLibro3 = "El horror de Dunwich"


def analizadorTitulos(tituloLibro):
    return len(tituloLibro)

print(f"La longitud del título del libro 1({tituloLibro1}) es: {analizadorTitulos(tituloLibro1)}")
print(f"La longitud del título del libro 2({tituloLibro2})  es: {analizadorTitulos(tituloLibro2)}")
print(f"La longitud del título del libro 3({tituloLibro3})  es: {analizadorTitulos(tituloLibro3)}")