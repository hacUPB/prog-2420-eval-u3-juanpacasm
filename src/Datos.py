
def main():
    #Tu código va aquí. Mantén la indentación
    pass # borra esta línea cuando con inicies tu código


if __name__ == "__main__":
    main()

mensajes = ["Trabajo listo","Trabajo en proceso","Trabajo revisado","Trabajo corregido"]

def elegir_mensaje():
    print("Bienvenido al chat, estas son las opciones de mensajes: ")
    print("")
    print("1. Trabajo listo \n2. Trabajo en proceso \n3. Trabajo revisado \n4.Trabajo corregido ")
    opcion = int(input("Seleccione el mensaje:  "))
    print(mensajes[opcion-1])

elegir_mensaje()