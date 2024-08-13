"""
Ejercicio 3: Contar ocurrencias de un elemento en una tupla. Crea una tupla con varios elementos repetidos.
Solicita al usuario que ingrese un elemento. Luego, usa un ciclo while para contar cuántas veces aparece el
elemento en la tupla. Muestra el resultado.
"""
tupla = (1, 2, 3 , 3, 3, 4, 5, 3)  
ingresar = int(input(" Ingrese un elemento: "))

contador = 0
indice = 0

# Usa un ciclo while para contar cuántas veces aparece el elemento en la tupla
while indice < len(tupla):
    if tupla[indice] == ingresar:
        contador = contador + 1
    indice = indice + 1

# Muestra el resultado
print(f"El elemento {ingresar} aparece {contador} veces en la tupla.")
