Algoritmo CalcularPrecioFinalConIVAPersonalizado
    Definir precioProducto, precioFinal, tasaIVA como Real
    
    Escribir "Ingrese el precio del producto: "
    Leer precioProducto
    
    Escribir "Ingrese el porcentaje de IVA (sin el s�mbolo %): "
    Leer tasaIVA
    
    tasaIVA = tasaIVA / 100  // Convertir el porcentaje a decimal
    precioFinal = precioProducto + (precioProducto * tasaIVA)
    
    Escribir "El precio final del producto incluyendo el IVA es: $", precioFinal
    
FinAlgoritmo