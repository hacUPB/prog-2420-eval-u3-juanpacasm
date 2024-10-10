mensajes = ["Trabajo listo", "Trabajo en proceso", "Trabajo revisado", "Trabajo corregido"]  # lista de mensajes predeterminados
usuarios = ["Juan", "Maria", "Pedro", "Ana"]  # lista de usuarios
historial_mensajes = []



def elegir_usuario():
    print("Bienvenido al chat, estos son los usuarios: ")
    print("")
    print("1. Juan \n2. Maria \n3. Pedro \n4. Ana")
    opcion1 = int(input("Seleccione el usuario:  "))
    print("Ha seleccionado a: ", usuarios[opcion1 - 1])
    return opcion1 - 1

def elegir_mensaje(usuario_index):
    print(f"Bienvenido al chat {usuarios[usuario_index]}, estas son las opciones de mensajes: ")
    print("")
    print("1. Trabajo listo \n2. Trabajo en proceso \n3. Trabajo revisado \n4.Trabajo corregido ")
    opcion = int(input("Seleccione el mensaje:  "))
    mensaje = f"{mensajes[opcion - 1]} enviado por {usuarios[usuario_index]}"
    historial_mensajes.append(mensaje)
    print(mensaje)
    return mensaje

def crear_historial(mensaje):
    with open("historial1.txt", "a") as archivo:
        archivo.write(mensaje + "\n")

def mostrar_historial():
    print("Historial de mensajes: ")
    with open("historial1.txt", "r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            print(linea)





def main():


    usuario_index = elegir_usuario()
    mensaje = elegir_mensaje(usuario_index)
    crear_historial(mensaje)
    mostrar_historial()


if __name__ == "__main__":
    main()