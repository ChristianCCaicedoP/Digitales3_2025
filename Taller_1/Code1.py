#Funciones
def menu():
    print("\n--- Directorio Telefónico ---")
    print("1. Agregar persona")
    print("2. Mostrar directorio")
    print("3. Salir")

def agregar_persona(directorio):
    nombre = input(textos[1])
    telefono = input(textos[2])
    cumpleanos = input(textos[3])
    correo = input(textos[4])
    
    persona = {
        "Nombre": nombre,
        "Teléfono": telefono,
        "Cumpleaños": cumpleanos,
        "Correo": correo
    }
    directorio.append(persona)
    print("Persona agregada exitosamente.")

def mostrar_directorio(directorio):
    if not directorio:
        print("\nEl directorio está vacío.")
    else:
        print("\n--- Directorio Telefónico ---")
        for i, persona in enumerate(directorio, start=1):
            print(f"{i}. {persona['Nombre']} - Teléfono: {persona['Teléfono']} - Cumpleaños: {persona['Cumpleaños']} - Correo: {persona['Correo']}")

#Variables
textos = [
    "\nBienvenido al directorio telefónico.",
    "\nIngrese el nombre y apellido de la persona: ",
    "\nIngrese el teléfono celular: ",
    "\nIngrese la fecha de cumpleaños (DD/MM): ",
    "\nIngrese el correo electrónico: "
]

directorio = []

# Ejecución de código
print(textos[0])
while True:
    menu()
    opcion = input("Por favor seleccione una opción: ")
    
    if opcion == '1':
        agregar_persona(directorio)
    elif opcion == '2':
        mostrar_directorio(directorio)
    elif opcion == '3':
        print("Saliendo del directorio. ¡Gracias!")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")