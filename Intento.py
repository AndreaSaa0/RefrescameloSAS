usuarios = {
    "usuario1": {"rol": "administrador", "areas": ["produccion", "almacen"]},
    "usuario2": {"rol": "operario", "areas": ["produccion"]},
}

roles = {
    "administrador": {"permisos": ["crear_rol", "editar_rol", "eliminar_rol", "ver_todos_los_datos"]},
    "operario": {"permisos": ["ver_propios_datos"]},
}

areas = {
    "produccion": ["crear_producto", "editar_producto"],
    "almacen": ["ver_inventario", "solicitar_material"]
}

def validar_acceso(usuario, area):
    if usuario in usuarios:
        rol_usuario = usuarios[usuario]["rol"]
        permisos_rol = roles[rol_usuario]["permisos"]
        if area in areas and any(permiso in permisos_rol for permiso in areas[area]):
            return True
        else:
            print("Acceso denegado. No tienes permisos para esa área.")
    else:
        print("Usuario no encontrado.")
    return False

while True:
    usuario = input("Ingrese su usuario: ")
    area = input("Ingrese el área a la que desea acceder: ")

    if validar_acceso(usuario, area):
        print("Acceso concedido.")
    else:
        print("Acceso denegado.")