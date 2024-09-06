# Definimos la agenda como un diccionario
agenda = {}

# Funciones para manejar la agenda

def agregar_contacto(nombre, telefono):
    agenda[nombre] = telefono
    print(f"Contacto {nombre} agregado con éxito.")

def mostrar_contactos():
    if agenda:
        print("\nLista de contactos:")
        for nombre, telefono in agenda.items():
            print(f"Nombre: {nombre}, Teléfono: {telefono}")
    else:
        print("La agenda está vacía.")

def buscar_contacto(nombre):
    if nombre in agenda:
        print(f"Contacto encontrado - Nombre: {nombre}, Teléfono: {agenda[nombre]}")
    else:
        print(f"El contacto {nombre} no está en la agenda.")

def editar_contacto(nombre):
    if nombre in agenda:
        nuevo_telefono = input(f"Coloca el nuevo teléfono para {nombre}: ")
        agenda[nombre] = nuevo_telefono
        print(f"Teléfono de {nombre} actualizado.")
    else:
        print(f"El contacto {nombre} no está en la agenda.")

def eliminar_contacto(nombre):
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto {nombre} eliminado con éxito.")
    else:
        print(f"El contacto {nombre} no está en la agenda.")

# Menú de opciones
while True:
    print("\n--- Agenda de Contactos ---")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Buscar contacto")
    print("4. Editar contacto")
    print("5. Eliminar contacto")
    print("6. Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == '1':
        nombre = input("Nombre del contacto: ")
        telefono = input("Teléfono del contacto: ")
        agregar_contacto(nombre, telefono)
        
    elif opcion == '2':
        mostrar_contactos()
        
    elif opcion == '3':
        nombre = input("Nombre del contacto a buscar: ")
        buscar_contacto(nombre)
        
    elif opcion == '4':
        nombre = input("Nombre del contacto a editar: ")
        editar_contacto(nombre)
        
    elif opcion == '5':
        nombre = input("Nombre del contacto a eliminar: ")
        eliminar_contacto(nombre)
        
    elif opcion == '6':
        print("Saliendo de la agenda...")
        break
        
    else:
        print("Opción no válida. Inténtalo de nuevo.")
