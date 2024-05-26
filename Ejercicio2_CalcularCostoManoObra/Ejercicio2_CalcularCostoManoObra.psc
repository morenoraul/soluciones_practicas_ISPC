Proceso CalcularCostoManoObra
	Definir largo, altura, areaPintada, costoMetroCuadrado, costoManoObra Como Real
	Escribir "Ingrese la longitud de la pared (en metros): "
	Leer largo
	Escribir "Ingrese la altura de la pared (en metros): "
	Leer altura
	areaPintada <- largo * altura
	Escribir "Ingrese el costo por metro cuadrado: "
	Leer costoMetroCuadrado
	costoManoObra <- areaPintada * costoMetroCuadrado
	Escribir "El costo de mano de obra para pintar la pared es: $", costoManoObra
	
FinProceso