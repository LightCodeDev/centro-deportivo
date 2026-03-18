
def preguntar_si_es_miembro():
    print("Eres miembro? si/no")
    respuesta = input().strip().lower()
    if respuesta == "":
        print("Respuesta invalida")
        return
    elif respuesta == "no":
        return False
    elif respuesta == "si":
        return True
    else:
        print("Respuesta invalida")
        return
def pedir_id():
    while True:
        print("Cual es su ID de miembro?")
        id_miembro = input().strip().upper()
        if id_miembro == "":
            print("Respuesta invalida")
        else:
            return id_miembro
def mostrar_resultado(nombre,precio):
    print(f"Hola {nombre}, tu precio a pagar es: {precio}")
def mostrar_error():
    print("ID no encontrado")