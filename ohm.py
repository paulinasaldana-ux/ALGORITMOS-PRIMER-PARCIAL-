"""
Este programa calcula la Ley de Ohm
Opciones:
1 = Voltaje
2 = Corriente
3 = Resistencia
"""
print("Ley de Ohm")
print("Selecciona la opción:")
opcion = int(input("1 = Voltaje, 2 = Corriente, 3 = Resistencia: "))

try:
    if opcion == 1:
        resistencia = float(input("Ingresa la resistencia (Ohm): "))
        corriente = float(input("Ingresa la corriente (Amperios): "))
        voltaje = resistencia * corriente
        print("El voltaje es:", voltaje, "voltios")
    elif opcion == 2:
        voltaje = float(input("Ingresa el voltaje (Voltios): "))
        resistencia = float(input("Ingresa la resistencia (Ohm): "))
        corriente = voltaje / resistencia
        print("La corriente es:", corriente, "amperios")
    elif opcion == 3:
        voltaje = float(input("Ingresa el voltaje (Voltios): "))
        corriente = float(input("Ingresa la corriente (Amperios): "))
        resistencia = voltaje / corriente
        print("La resistencia es:", resistencia, "ohmios")
    else:
        print("Opción no válida.")
except Exception as e:
    print("Error en los datos ingresados:", e)
