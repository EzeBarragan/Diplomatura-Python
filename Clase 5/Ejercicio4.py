"""
Ejercicio 4: Imprimir números pares. Crea una lista con los números del 1 al 20. Luego, usa un ciclo for y un
condicional if para imprimir solo los números pares. 
"""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for i in numeros:
    if i % 2 == 0:
        print(i)
