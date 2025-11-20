from heap import HeapMax

cola_impresion = HeapMax()

#A prioridad 1
cola_impresion.arrive("Informe mensual", 1)
cola_impresion.arrive("Solicitud vacaciones", 1)  
cola_impresion.arrive("Reporte ventas", 1) 

#B imprima el primer documento de la cola
print('=== B ===')
if cola_impresion.size() > 0:
    documento = cola_impresion.attention()
    print(f"Imprimiendo: {documento[1]}")

#C cargue dos documentos del staff de TI (prioridad 2)
print('=== C ===')
cola_impresion.arrive("Analisis seguridad", 2)  
cola_impresion.arrive("Backup sistema", 2)  
print(f"Cola actual: {cola_impresion.elements}")

#D cargue un documento del gerente (prioridad 3)
print('=== D ===')
cola_impresion.arrive("Estrategia corporativa", 3)
print(f"Cola actual: {cola_impresion.elements}")

#E imprima los dos primeros documentos de la cola
print('=== E ===')
print("Primer documento:")
if cola_impresion.size() > 0:
    documento1 = cola_impresion.attention()
    print(f"  Imprimiendo: {documento1} ")

print("Segundo documento:")
if cola_impresion.size() > 0:
    documento2 = cola_impresion.attention()
    print(f"  Imprimiendo: {documento2}")
print(f"Cola despues de imprimir: {cola_impresion.elements}")

#F cargue dos documentos de empleados y uno de gerente
print('=== F ===')
cola_impresion.arrive("Formulario gastos", 1)  
cola_impresion.arrive("Evaluacion desempenio", 1)  
cola_impresion.arrive("Plan presupuestario", 3)  
print(f"Cola actual: {cola_impresion.elements}")

#G imprima todos los documentos de la cola de impresion
print('=== F ===')
while cola_impresion.size() > 0:
    documento = cola_impresion.attention()
    print(f"  Imprimiendo: {documento[1]} (Prioridad: {documento[0]})")

print()
print(f"Cola final: {cola_impresion.elements}")