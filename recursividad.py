#TP 1 puntos 5 y 22 de recursividad
def romano_a_decimal(num):
    
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 
               'C': 100, 'D': 500, 'M': 1000}
    
   # caso base: cadena vacia
    if num == '':
        return 0
    
    # caso cuando quede un solo caracter
    if len(num) == 1:
        return valores[num[0]]
    
    # comparar el primer y segundo carácter
    primero = valores[num[0]]
    segundo = valores[num[1]]
    
    if primero < segundo:
        return segundo - primero + romano_a_decimal(num[2:])
    else:
        return primero + romano_a_decimal(num[1:])
    
print(romano_a_decimal('MDIV'))


def usar_la_fuerza(mochila,objetos_sacados):
    
    #caso base mochila basia
    if not mochila:
        return (False,objetos_sacados)
    
    objeto=mochila[0]
    
    if objeto=='sable de luz':
        return(True,objetos_sacados +1)
    return usar_la_fuerza(mochila[1:],objetos_sacados +1)

mochila1= ["radio", "mapa", "kit medico",
           "sable de lu", "pila"]

resultado, cantidad_objetos= usar_la_fuerza(mochila1,0)
if resultado:
    print('el sable de luz fue encontrado')
    print('la contidad de objetos sacados es: ', cantidad_objetos)
else:
    print('el sable de luz no fue encontrado')




