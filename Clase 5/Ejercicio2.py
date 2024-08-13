"""
Ejercicio 2: Verificar si un número está en una lista. Solicita al usuario que ingrese un número. Luego, define
una lista con varios números enteros. Utiliza un ciclo for para verificar si el número ingresado por el usuario está en
la lista. Si está, muestra un mensaje que diga "El número se encuentra en la lista", si no, muestra "El número no
está en la lista".
"""
ingresado = int(input("Ingrese un numero entero: "))

numeros_enteros = [1, 3, 4, 5, 6, 8, 9, 10, 20]

encontrado = False
for i in numeros_enteros:
    if ingresado == i:
        encontrado = True
        break
if encontrado:
    print(f"El numero {ingresado} esta en la Lista")
else:
    print(f"El numero {ingresado} no esta en la Lista")


