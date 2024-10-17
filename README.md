[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/PehQeuqy)
# Unidad 3
---Red social
## Documentación del proyecto
Nombre:  Juan Pablo Castrillón M.
ID:  000554106
---

# HISTORIAL
## Pseudocodigo
Declarar Variables:
mensajes: Lista de mensajes predeterminados.
usuarios: Lista de nombres de usuarios.
historial_mensajes: Lista vacía para almacenar el historial de mensajes.
horaR: Almacena la fecha y hora actual.

Función elegir_usuario:
Imprimir lista de usuarios.
Pedir al usuario que seleccione uno de los usuarios (opciones 1 a 4).
Imprimir el nombre del usuario seleccionado.
Retornar el índice del usuario seleccionado (restando 1 al valor ingresado).
Función elegir_mensaje:

Imprimir lista de mensajes predeterminados.
Pedir al usuario que seleccione un mensaje (opciones 1 a 4).
Crear un mensaje con el formato: "mensaje seleccionado por usuario a la hora actual".
Añadir el mensaje al historial_mensajes.
Imprimir el mensaje y retornar el mensaje.
Función crear_historial:

Abrir el archivo historial1.txt en modo añadir.
Escribir el mensaje en el archivo y añadir un salto de línea.
Función mostrar_historial:

Abrir el archivo historial1.txt en modo lectura.
Leer todas las líneas del archivo.
Imprimir cada línea (cada mensaje del historial).
Función Principal main:

Llamar a elegir_usuario para seleccionar un usuario.
Llamar a elegir_mensaje para seleccionar un mensaje.
Llamar a crear_historial para guardar el mensaje en el archivo.
Llamar a mostrar_historial para mostrar el historial de mensajes.
Iniciar el Programa:

Llamar a la función main si el archivo se ejecuta directamente.

## Guía de usuario
1. Seleccionar un Usuario:
Después de iniciar el programa, verás la siguiente lista de usuarios en la consola:
-----
Bienvenido al chat, estos son los usuarios:
1. Juan
2. Maria
3. Pedro
4. Ana
-----
El programa te pedirá que ingreses un número correspondiente al usuario que quieres seleccionar. Por ejemplo, si eliges a "Juan", escribe 1 y presiona Enter.


2. Elegir un Mensaje:
Luego de seleccionar el usuario, el programa mostrará una lista de mensajes predeterminados:
-----
Bienvenido al chat Juan, estas son las opciones de mensajes:
1. Trabajo listo
2. Trabajo en proceso
3. Trabajo revisado
4. Trabajo corregido
-----
Elige un mensaje escribiendo el número correspondiente. Por ejemplo, si quieres enviar "Trabajo en proceso", ingresa 2 y presiona Enter.

3. Historial de Mensajes:
Después de enviar el mensaje, el programa lo guardará en un archivo llamado historial1.txt.
A continuación, el programa te mostrará el historial completo de mensajes almacenados hasta el momento.
El historial se verá similar a esto:
-----
Trabajo en proceso enviado por Juan 2024-10-17 12:45:30.345678
Trabajo corregido enviado por Maria 2024-10-17 12:50:00.123456
-----

4. Finalizar el Programa:
Después de que se muestre el historial de mensajes, el programa finaliza su ejecución automáticamente. Si deseas enviar más mensajes, puedes ejecutar nuevamente el programa siguiendo los pasos anteriores.
