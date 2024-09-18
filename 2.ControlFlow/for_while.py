numbers = [1, 2, 3, 4, 5, 6]
for i in numbers:
    print("AquÃ­ i es igual a:",i+1)

for i in range(3,10):
    print(i)

fruits = ["Manzana", "Pera", "Uva", "Naranja", "Tomate"]
for fruit in fruits:
    print(fruit)
    if fruit == "Naranja":
        print("Naranja encontrada")


#While Use
x = 0
while x<5:
    if x ==3:
        break
    print(x) 
    x +=1


# For use
numbers = [1, 2, 3, 4, 5, 6]
for i in numbers:
    if i ==3:
        break
    print("AquÃ­ i es igual a:",i)



def mostrar_menu():
    print("\nMenú:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")

while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        print("Has elegido la Opción 1")
    elif opcion == "2":
        print("Has elegido la Opción 2")
    elif opcion == "3":
        print("Has elegido la Opción 3")
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")