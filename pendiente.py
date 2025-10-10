# Solicitar las coordenadas del primer punto
x1 = float(input("Ingrese x1: "))
y1 = float(input("Ingrese y1: "))

# Solicitar las coordenadas del segundo punto
x2 = float(input("Ingrese x2: "))
y2 = float(input("Ingrese y2: "))

# Calcular la pendiente
if x2 != x1:
    pendiente = (y2 - y1) / (x2 - x1)
    print(f"La pendiente es: {pendiente}")
else:
    print("La pendiente es indefinida (división por cero).")