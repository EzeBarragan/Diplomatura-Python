"""
Ejercicio 5: Revertir una lista. Solicita al usuario que ingrese 5 palabras y guárdalas en una lista. Luego, utiliza un
ciclo for para imprimir la lista en orden inverso.
"""
palabras = []
for i in range(5):
    usuario = input("Ingrese una palabra: ")
    palabras.append(usuario)
    
for i in range(len(palabras) - 1, -1, -1):
    print(palabras[i])
    
    