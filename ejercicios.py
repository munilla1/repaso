# programa que, recibe dos numeros enteros y calcula la suma, la resta y la multiplicacion de dichos numeros

def suma(a, b):
    resultado = a + b
    return resultado

def resta(a, b):
    resultado = a - b
    return resultado

def multiplicacion(a, b):
    resultado = a * b
    return resultado

print(suma(10, 5))
print(resta(10, 5))
print(multiplicacion(10, 5))


# programa que, recibe el coste de un articulo vendido y la cantidad de dinero entregada por el cliente. Se calcula:

# el cambio, si el dinero entregado por el cliente es mayor
# ¿que pasa si el dinero entregado es exacto?
# la cantidad de dinero que falta por pagar si es menor que el precio del producto

precio_articulo = 26
dinero_pagado = 26

if precio_articulo < dinero_pagado:
    print(dinero_pagado - precio_articulo)

if precio_articulo == dinero_pagado:
    print("el dinero pagado es exacto, no hay cambio")

if precio_articulo > dinero_pagado:
    print("falta por pagar: " + str(precio_articulo - dinero_pagado))