import ui
import services

def main():
    es_miembro = ui.preguntar_si_es_miembro()
    while es_miembro is None:
        es_miembro = ui.preguntar_si_es_miembro()
    if es_miembro:
        id_miembro = ui.pedir_id()
        miembro = services.buscar_miembro_por_id(id_miembro)
        while miembro is None:
            ui.mostrar_error()
            id_miembro = ui.pedir_id()
            miembro = services.buscar_miembro_por_id(id_miembro)

        edad = miembro["edad"]
        activo = miembro["activo"]
        nombre = miembro["nombre"]
        precio = services.calcular_precio_final(edad, activo)
        ui.mostrar_resultado(nombre, precio)

    else:
        activo = False
        edad = 1
        nombre = "No miembro"
        precio = services.calcular_precio_final(edad, activo)
        ui.mostrar_resultado(nombre, precio)
main()