def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def division(a, b):
    return a / b

while True:
    opciones = input("Elija que quiere hacer 'S(suma)', 'R(resta)', 'M(multiplicar)', 'D(dividir)', o coloque 'salir' si desea salir: ")
    if opciones == "salir":
        break
    
    a = int(input("Coloque el primer número: "))
    b = int(input("Coloque el segundo número: "))
    
    if opciones == "S":
        print(f"El resultado de la suma es: {suma(a, b)}")
    elif opciones == "R":
        print(f"El resultado de la resta es: {resta(a, b)}")
    elif opciones == "M":
        print(f"El resultado de la multiplicación es: {multiplicar(a, b)}")
    elif opciones == "D":
        if b != 0:
            print(f"El resultado de la división es: {division(a, b)}")
        else:
            print("Error: No se puede dividir por 0.")
    else:
        print("Opción no válida. Intente de nuevo.")
