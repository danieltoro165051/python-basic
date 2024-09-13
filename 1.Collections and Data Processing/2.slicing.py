a = [1,2,3,4,5]
b = a
# a and b are using the same memory position
print(a)
print(b)

# Borrar valor en la posicion 0
del b[0]
print((a))
print((b))

# Asignar todos los valores de la lista a en c
c = a[:]
# Id represents memory position
print(id(a))
print(id(b))
print(id(c))

# Append adds number in the last position.
a.append(6)
print(a)
print(b)
print(c)

# Another Way to do a copy of a list using different memory position or id's
lista1 = [1,2,3,4,5]
lista2 = lista1.copy()

lista2.append( 6 )

print( lista1 )
print( lista2 )

print("Practicing Slicing")

# Lista de ejemplo
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Ejemplos de slicing
sublista1 = lista[2:5]
# Print from position 2 to 5 without including 5  [2, 3, 4]
print("SubLista1",sublista1)

# Print from position 0 to 4 without including 4  [0, 1, 2, 3]
sublista2 = lista[:4]
print("sublista2",sublista2)

# Print from position 5 to the rest [5, 6, 7, 8, 9]
sublista3 = lista[5:]
print("sublista3", sublista3)

# Print between two positions
sublista4 = lista[::4]
print("sublista4",sublista4)

# Print 
sublista5 = lista[1:7:2]
print("sublista5", sublista5)

# Slicing con índices negativos
sublista6 = lista[-5:]
sublista7 = lista[:-5]
sublista8 = lista[-8:-2:2]