def calcular_area_rectangulo(base, altura):
    """Calcula el área de un rectángulo."""
    return base * altura

def calcular_area_circulo(radio, pi=3.14159):
    """Calcula el área de un círculo."""
    return pi * radio ** 2

# Llamadas a las funciones
area_rectangulo = calcular_area_rectangulo(5, 3)
area_circulo = calcular_area_circulo(2)

print(f"Área del rectángulo: {area_rectangulo}")  # Salida: Área del rectángulo: 15
print(f"Área del círculo: {area_circulo}")  # Salida: Área del círculo: 12.56636