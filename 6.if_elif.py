## Mas de una opcion
'''
En los anteriores ejemplos se observo que
es posible tomar al menos una decision; o mas de una
decision mediante el anidamiento de condicionales.
Existe una tercera posibilidad, y esto es el: "else if"
que plantea mayor numero de posibilidades independientes al
primer "if"
'''
numero = "45"

if type(numero) == int:
    print "numero, es un entero"
elif type(numero) == float:
    print "numero es un decimal"
elif type(numero) == str:
    print "numero es una cadena: " + numero
else:
    print "Entonces que es?"
