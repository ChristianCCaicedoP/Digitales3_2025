# Descripción del Código del Taller_1

## Directorio Telefónico en Python

Este es un programa en Python que permite gestionar un directorio telefónico básico. Los usuarios pueden agregar contactos, ver la lista de contactos almacenados y salir del programa.

## Características
El directorio cuenta con los siguientes datos a solicitar y guardar:

- Nombre y apellido
- Teléfono celular
- Fecha de cumpleaños
- Correo electrónico

## Funciones
### Función "agregar_persona"
La función "agregar_persona" realiza la solicitud de datos necesarios para cada usuario agregado y lo almacena en el directorio telefónico, solicitando los datos que se mencionan en Características.

### Función "mostrar_directorio"
Realiza la impresión en pantalla de todo el directorio que se ha almacenado hasta el momento

### Menu
El menú se define para para poder imprimir en pantalla las opciones de las funciones y opciones que se cuentan y poder nevegar por ellas.

Interfaz sencilla basada en la terminal

## Vista previa
Menú principal

--- Directorio Telefónico ---
1. Agregar persona
2. Mostrar directorio
3. Salir

## Ejemplo
Agregar un contacto:
---
---
- Ingrese el nombre y apellido de la persona: Germán Moreno
- Ingrese el teléfono celular: 1234567890
- Ingrese la fecha de cumpleaños (DD/MM): 25/12
- Ingrese el correo electrónico: ejemplo@ecci.edu.co

"Persona agregada exitosamente".

Mostrar directorio
---
---
--- Directorio Telefónico ---
1. Germán Moreno - Teléfono: 1234567890 - Cumpleaños: 25/12 - Correo: ejemplo@ecci.edu.co

## Comentarios
- Revise el código anexo en este repositorio y ejecutelo en python o un entorno de desarrollo que lo pueda ejecutar.

- Mejoras futuras:
    - Guardar los contactos en un archivo JSON o CSV para conservar los datos al cerrar el programa.
    - Realizar una mejora de la interfaz de usuario
    - Agregar funciones de búsqueda y edición de contactos.

--- Muchas gracias ---