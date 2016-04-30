'''
Los bucles while nos permiten ejecutar una pieza/as de codigo durante
una cantidad de veces definidas.
Ejecuta el cuerpo del bucle, si es que la condicion que se evalua
es Verdadera (True), cuando esa condicion cambie a Falso (False)
el bucle terminara
'''
bandera = True
cont = 0
while bandera:
    print "Dentro del bucle"
    if cont < 10:
        cont += 1
    else:
        bandera = False
print "Fuera del bucle, cont: ", cont
