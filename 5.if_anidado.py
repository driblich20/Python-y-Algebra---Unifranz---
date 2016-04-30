## If anidado ##
'''
Esta propiedad basica en la programacion indica que
es posible poner una condicional, dentro de otra condicional,
es de ahi que proviene el nombre "Anidado", que permite estructuras
mas complejas en cuanto a busquedas, ordenamiento y demas.
'''
x = 90
y = 43.5
if type(x) != type(y):
    y = int(x)
    if type(x) != type(y):
        print "Conversion fallida"
    else:
        print "Conversion exitosa"
else:
    print "No fue precisa la conversion"
