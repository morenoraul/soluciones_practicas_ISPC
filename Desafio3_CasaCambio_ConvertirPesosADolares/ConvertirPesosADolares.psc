Algoritmo ConvertirPesosADolares
    Definir montoEnPesos, montoEnDolares, tasaDeCambio como Real
    
    Escribir "Ingrese el monto en pesos argentinos (ARS): "
    Leer montoEnPesos
    
    Escribir "Ingrese la tasa de cambio actual (ARS a USD): "
    Leer tasaDeCambio
    
    montoEnDolares = montoEnPesos / tasaDeCambio
    
    Escribir "El equivalente en dólares estadounidenses (USD) es: $", montoEnDolares
    
FinAlgoritmo