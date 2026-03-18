from data import MIEMBROS, PRECIO_BASE

def buscar_miembro_por_id(id_buscado):

    for miembro in MIEMBROS:
        if miembro["id"] == id_buscado:
            return miembro
    return None

def calcular_precio_final(edad, activo):

    precio = PRECIO_BASE

    if not activo:
        return precio
    
    elif edad < 21:
        return precio - (PRECIO_BASE * 0.20)
    
    elif edad > 60:
        return precio - (PRECIO_BASE * 0.35)
    
    return precio