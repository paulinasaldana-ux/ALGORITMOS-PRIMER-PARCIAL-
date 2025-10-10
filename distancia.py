import math

# Solicitar las coordenadas del primer punto
x1 = float(input("Ingrese x1: "))
y1 = float(input("Ingrese y1: "))

# Solicitar las coordenadas del segundo punto
x2 = float(input("Ingrese x2: "))
y2 = float(input("Ingrese y2: "))

# Calcular la distancia usando la fórmula
distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"La distancia entre los puntos es: {distancia}")
