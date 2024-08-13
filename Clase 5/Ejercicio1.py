"""
Ejercicio 1: Sumar elementos de una lista. Crea una lista con 5 números enteros. Luego, recorre la lista con un
ciclo for y suma todos los elementos. Finalmente, muestra el resultado usando un print.
"""
enteros = []
suma = 0
for i in range (5):
    entero = int(input("Escriba 1 numero entero '(debera hacerlo hasta que sean 5)': "))
    enteros.append(entero)
print(f"Sus numeros son estos: {enteros}")

for i in enteros :
    suma = suma + entero
print(f"La suma total de sus 5 numeros es: {suma}")