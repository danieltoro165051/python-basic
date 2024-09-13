
# Print Function
print('Hola Mundo')

# Using separator in print function
print("Esto", "es", "un", "texto", sep=":")

# Concatening Strings
print("String 1"," ","String2")

# How to check type of the var
name = 'DANiel y daniel'
print(type(name)) # It's str or String and you can use diferents python function when is str

# Some Str Functions
print(name.lower())
print(name.upper())

# Using Count function
print("La i aparece: " , name.count('i'), "vez o veces")

mi_lista = [1, 5, 3, 5, 7, 5, 9]
cantidad_cinco = mi_lista.count(5)
print(f"El número 5 aparece {cantidad_cinco} veces en la lista.")

#Using title function - Capitaliza la primera letra de cada palabra.
texto = "hola mundo"
print(texto.title())  # "Hola Mundo"

#Using Strip function - Elimina los espacios en blanco al inicio y al final.
texto = "  hola  "
print(texto.strip())  # "hola"

#Using replace - Reemplaza partes de la cadena.
texto = "hola mundo"
print(texto.replace("mundo", "Python"))  # "hola Python"

#Using #split(sep) function - Divide la cadena en una lista según el separador.
texto = "hola,mundo,Python"
print(texto.split(","))  # ['hola', 'mundo', 'Python']


#Using Join Function - Une elementos de un iterable en una sola cadena.
lista = ["hola", "mundo"]
print(" ".join(lista))  # "hola mundo"


#Using Find function - Busca una subcadena y devuelve el índice de su primera aparición.
texto = "hola mundo"
print(texto.find("mundo"))  # 5

#Using startsWith and endsWith - Verifica si la cadena empieza o termina con una subcadena.
texto = "hola mundo"
print(texto.startswith("hola"))  # True
print(texto.endswith("mundo"))  # True

#Ejemplo Completo:
frase = "  Bienvenido a Python!  "
frase = frase.strip().replace("Python", "el mundo de Python").upper()
print(frase)  # "BIENVENIDO A EL MUNDO DE PYTHON!"

# Using EVAL function - Evalúa una expresión de Python contenida en una cadena y devuelve el resultado.
expression = "2 + 3 * 4"
result = eval(expression)  # result será 14
print(result)

# Using EXEC Function Ejecuta un bloque de código Python contenido en una cadena. A diferencia de eval, puede ejecutar declaraciones complejas, incluyendo definiciones de funciones, bucles, importaciones, etc.
code = """
def greet(name):
    print(f'Hello, {name}')
"""
exec(code)
greet('Alice')  # Output: Hello, Alice


# Using f-strings - Al anteponer una f a la cadena de texto, puedes incluir variables directamente dentro de las llaves {}
frase = "Nunca pares de aprender"
author = "Platzi"
print(f"Frase: {frase}, Autor: {author}")


# :.2f indica que el número debe mostrarse con dos decimales.
valor = 3.14159
print("Valor: {:.2f}".format(valor))


# Para imprimir una cadena que contenga comillas simples o dobles dentro de ellas, debes usar secuencias de escape
print('Hola soy \'Carli\'')


#Si necesitas imprimir una ruta de archivo en Windows, que incluya barras invertidas
print("La ruta de archivo es: C:\\Users\\Usuario\\Desktop\\archivo.txt")



