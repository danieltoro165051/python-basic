'We can include list inside tuples'
numbers2 = (7,8,9,10,[11,12])
print(numbers2)
print(numbers2[4])
print(type(numbers2[4]))  # list
# numbers2[4] = [20,40] -----> Gives error since they are inmutable
numbers2[4][1] = 2
print(numbers2)

## '''No podemos cambiar la tupla pero si podemos modificar las variables que se  encuentran dentro de la lista que a su vez esta incluida en la tupla'''

##Listas de Dos Dimensiones: Se crea una lista que representa una matriz, se accede a sus elementos y se iteran.
##Listas de Tres Dimensiones: Se crea una lista que representa un tensor, se accede a sus elementos y se iteran.
## Tuplas: Se crean tuplas, se accede a sus elementos, se muestran ejemplos de concatenación, repetición, verificación de pertenencia, longitud y desempaquetado.

# Lista de dos dimensiones
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriz:")
for fila in matriz:
    for elemento in fila:
        print(elemento, end=' ')
    print()

# Lista de tres dimensiones
tensor = [
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
]

print("\nTensor:")
for bloque in tensor:
    for fila in bloque:
        for elemento in fila:
            print(elemento, end=' ')
        print()
    print()

# Tuplas
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

print("Tupla1:", tupla1)
print("Tupla2:", tupla2)

tupla_concatenada = tupla1 + tupla2
print("Tupla concatenada:", tupla_concatenada)

tupla_repetida = tupla1 * 2
print("Tupla repetida:", tupla_repetida)

print("¿Está 3 en la tupla1?", 3 in tupla1)
print("Longitud de tupla1:", len(tupla1))

print("Elementos de tupla1:")
for elemento in tupla1:
    print(elemento)

a, b, c = tupla1
print("Desempaquetado de tupla1:", a, b, c)