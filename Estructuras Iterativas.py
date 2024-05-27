# TECNICATURA SUPERIOR DE CIENCIAS DE DATOS E INTELIGENCIA ARTIFICIAL
#Modulo Programación - Introducion a la Programación
# Estudiante: Raúl Moreno

#ACTIVIDAD ESTRUCTURAS ITERATIVAS

# 1. Mostrar los números desde el 0 al número solicitado al usuario (input)
num1 = int(input("Ingrese un número para mostrar los números hasta ese valor: "))
print("Números del 0 hasta", num1, ":")
for i in range(num1 + 1):
    print(i)

print("\n")  # Salto de línea para separar los ejercicios

# 2. Mostrar sólo los números pares desde 0 hasta el número ingresado (input)
num2 = int(input("Ingrese un número para mostrar los números pares hasta ese valor: "))
print("Números pares del 0 hasta", num2, ":")
for i in range(num2 + 1):
    if i % 2 == 0:
        print(i)

print("\n")  # Salto de línea para separar los ejercicios

# 3. Pedir que el usuario ingrese (input) nombre de personas y mostrarlos hasta que el valor de lo que ingresa sea "fin"
nombres = []
print("Ingrese nombres (o 'fin' para terminar):")
while True:
    nombre = input()
    if nombre.lower() == "fin":
        break
    nombres.append(nombre)

print("\nLos nombres ingresados son:")
for nombre in nombres:
    print(nombre)