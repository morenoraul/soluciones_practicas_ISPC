Algoritmo CalcularPrecioFinal
    Definir precioProducto, precioFinal como Real
    Definir tasaIVA como Real
    
    Escribir "Ingrese el precio del producto: "
    Leer precioProducto
    
    tasaIVA = 0.21 //o la tasa de IVA correspondiente
    precioFinal = precioProducto + (precioProducto * tasaIVA)
    
    Escribir "El precio final del producto incluyendo el IVA es: $", precioFinal
    
FinAlgoritmo