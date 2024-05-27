def determinar_beneficio_estudiante():
  
  edad = int(input("Ingrese la edad del estudiante: "))
  promedio = float(input("Ingrese el promedio del estudiante: "))

  es_mayor_de_edad = edad >= 18
  es_estudiante_de_honor = promedio > 90
  tiene_beneficio_especial = es_mayor_de_edad or es_estudiante_de_honor

  if tiene_beneficio_especial:
    print("El estudiante tiene un beneficio especial.")
  else:
    print("El estudiante no tiene beneficios por el momento.")

determinar_beneficio_estudiante()
