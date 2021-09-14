# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese dos palabras y arme combinaciones con ella
print('Ingrese palabra 1:')
palabra_1 = str(input())

print('Ingrese palabra 2:')
palabra_2 = str(input())
# De la primera palabra tome las primeras tres letras, utilice el operador :
recorte1 = palabra_1[:3]
# De la segunda palabra tome las primeras dos letras, utilice el operador :
recorte2 = palabra_2[:2]
# Formar una nueva palabra con los recortes solicitados
# Imprima en pantalla los resultados
print("Las 3 primeras letras de la palabra", palabra_1, "con las 2 primeras letras de la palabra", palabra_2,"forman la palabra", recorte1+recorte2)



