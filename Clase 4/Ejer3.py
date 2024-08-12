"""
Ejercicio3 : Comentarios y Variables
Escribe un programa que defina tres variables ‘a’, ‘b’ y ‘c’. Asigna a cada una un valor numérico y luego muestra la
suma de las tres utilizando una f-string. Escribe comentarios que expliquen cada parte del código.
"""
a = 10 #Defino la variable a
b = 20 #Defino la variable b
c = 99 #Defino la variable c

suma = a + b +c 
print(f"El resultado de la suma es {suma}")
while True:
    otra = input("Te gustaria hacer otra suma: V('SI') o F('NO'): ")
    if otra == "F":
        break
    else:
        a = int(input("Coloque el primer valor: "))
        b = int(input("Coloque el segundo valor: "))
        c = int(input("Coloque el tercer valor: "))
        suma = a + b +c 
        print(f"El resultado de la suma es {suma}")
print("Adios...")