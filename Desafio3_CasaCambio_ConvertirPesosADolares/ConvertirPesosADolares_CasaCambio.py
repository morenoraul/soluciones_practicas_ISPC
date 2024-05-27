# Solicitar el monto en pesos argentinos
monto_en_pesos = float(input("Ingrese el monto en pesos argentinos (ARS): "))

# Solicitar la tasa de cambio actual
tasa_de_cambio = float(input("Ingrese la tasa de cambio actual (ARS a USD): "))

# Calcular el monto en dólares
monto_en_dolares = monto_en_pesos / tasa_de_cambio

# Mostrar el resultado
print(f"El equivalente en dólares estadounidenses (USD) es: ${monto_en_dolares:.2f}")