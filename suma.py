# Solicitar un número entero positivo
numero = int(input("Ingrese un número entero positivo: "))

# Calcular la suma de sus dígitos
suma = 0
for digito in str(numero):
    suma += int(digito)

# Imprimir el resultado
print(f"La suma de los dígitos es: {suma}")
