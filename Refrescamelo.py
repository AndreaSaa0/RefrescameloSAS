import datetime

# Clase Empleado
class Empleado:
    def __init__(self, id, nombre, apellido, cargo, area, turno, uniforme):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.cargo = cargo
        self.area = area
        self.turno = turno
        self.uniforme = uniforme
        self.rol = None  # El empleado inicialmente no tiene rol asignado

    def asignarRol(self, rol):
        self.rol = rol
        print(f"Rol asignado a {self.nombre} {self.apellido}: {rol.nombre}")

    def actualizarDatos(self, nombre=None, apellido=None, cargo=None, area=None, turno=None, uniforme=None):
        if nombre:
            self.nombre = nombre
        if apellido:
            self.apellido = apellido
        if cargo:
            self.cargo = cargo
        if area:
            self.area = area
        if turno:
            self.turno = turno
        if uniforme:
            self.uniforme = uniforme
        print(f"Datos de {self.nombre} actualizados.")

    def registrarAcceso(self, control_acceso):
        control_acceso.registrarAcceso(self)

# Clase Rol
class Rol:
    def __init__(self, id, nombre, descripcion):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.permisos = []

    def asignarPermisos(self, permisos):
        self.permisos.extend(permisos)
        print(f"Permisos asignados al rol {self.nombre}: {permisos}")

    def editarRol(self, nuevo_nombre=None, nueva_descripcion=None):
        if nuevo_nombre:
            self.nombre = nuevo_nombre
        if nueva_descripcion:
            self.descripcion = nueva_descripcion
        print(f"Rol {self.id} editado. Nuevo nombre: {self.nombre}, Nueva descripción: {self.descripcion}")

    def eliminarRol(self):
        print(f"Rol {self.nombre} eliminado.")

# Clase ControlAcceso
class ControlAcceso:
    def __init__(self):
        self.registros = []

    def validarAcceso(self, empleado, area):
        if empleado.rol and area in empleado.rol.permisos:
            print(f"Acceso concedido a {empleado.nombre} {empleado.apellido} para el área {area}.")
            return True
        else:
            print(f"Acceso denegado a {empleado.nombre} {empleado.apellido} para el área {area}.")
            return False

    def registrarAcceso(self, empleado):
        now = datetime.datetime.now()
        control = {
            "empleado": empleado.nombre,
            "area": empleado.area,
            "fecha_hora": now,
            "ingreso": "entrada"  # Suponiendo que es un acceso de entrada
        }
        self.registros.append(control)
        print(f"Acceso registrado para {empleado.nombre} {empleado.apellido} en el área {empleado.area}.")

    def generarReporte(self):
        print("Generando reporte de accesos...")
        for registro in self.registros:
            print(f"{registro['empleado']} accedió a {registro['area']} el {registro['fecha_hora']}.")

# Clase Auditoria
class Auditoria:
    def __init__(self):
        self.registros = []

    def registrarCambio(self, empleado, detalles):
        now = datetime.datetime.now()
        cambio = {
            "empleado": empleado.nombre,
            "detalles": detalles,
            "fecha_hora": now
        }
        self.registros.append(cambio)
        print(f"Cambio registrado para {empleado.nombre}: {detalles}.")

    def consultarRegistros(self):
        print("Consultando registros de auditoría...")
        for registro in self.registros:
            print(f"{registro['empleado']} hizo un cambio: {registro['detalles']} el {registro['fecha_hora']}.")

    def filtrarRegistros(self, empleado):
        print(f"Filtrando registros de auditoría para {empleado.nombre}...")
        for registro in self.registros:
            if registro['empleado'] == empleado.nombre:
                print(f"{registro['empleado']} hizo un cambio: {registro['detalles']} el {registro['fecha_hora']}.")

# Clase SeguridadAcceso
class SeguridadAcceso:
    def __init__(self):
        self.usuarios = {}

    def agregarUsuario(self, usuario, contraseña, permisos):
        self.usuarios[usuario] = {
            "contraseña": contraseña,
            "permisos": permisos
        }

    def autenticarUsuario(self, usuario, contraseña):
        if usuario in self.usuarios and self.usuarios[usuario]["contraseña"] == contraseña:
            print(f"Usuario {usuario} autenticado correctamente.")
            return True
        else:
            print(f"Autenticación fallida para {usuario}.")
            return False

    def autorizarAcceso(self, usuario, area):
        if usuario in self.usuarios:
            permisos = self.usuarios[usuario]["permisos"]
            if area in permisos:
                print(f"Acceso autorizado a {usuario} para el área {area}.")
                return True
            else:
                print(f"Acceso denegado a {usuario} para el área {area}.")
                return False
        return False

# Función para crear un nuevo rol
def crearRol():
    id_rol = input("Ingrese el ID del nuevo rol: ")
    nombre_rol = input("Ingrese el nombre del nuevo rol: ")
    descripcion_rol = input("Ingrese la descripción del rol: ")
    rol = Rol(id_rol, nombre_rol, descripcion_rol)
    print(f"Rol {nombre_rol} creado con éxito.")
    return rol

# Función para registrar un empleado
def registrarEmpleado():
    id_empleado = input("Ingrese el ID del empleado: ")
    nombre = input("Ingrese el nombre del empleado: ")
    apellido = input("Ingrese el apellido del empleado: ")
    cargo = input("Ingrese el cargo del empleado: ")
    area = input("Ingrese el área del empleado: ")
    turno = input("Ingrese el turno del empleado: ")
    uniforme = input("Ingrese el uniforme del empleado: ")
    empleado = Empleado(id_empleado, nombre, apellido, cargo, area, turno, uniforme)
    return empleado

# Función para asignar permisos a un rol
def asignarPermisos(rol):
    permisos = input("Ingrese las áreas de acceso permitidas para este rol (separadas por comas): ")
    permisos = permisos.split(",")
    rol.asignarPermisos(permisos)

# Función para gestionar el registro y asignación de roles
def gestionarRoles():
    # Crear roles
    rol_admin = crearRol()
    asignarPermisos(rol_admin)

    rol_operario = crearRol()
    asignarPermisos(rol_operario)

    # Registrar empleados
    empleado1 = registrarEmpleado()
    empleado1.asignarRol(rol_admin)

    empleado2 = registrarEmpleado()
    empleado2.asignarRol(rol_operario)

    # Ejemplo de acceso
    control_acceso = ControlAcceso()
    empleado1.registrarAcceso(control_acceso)
    empleado2.registrarAcceso(control_acceso)

    # Generación de reporte de acceso
    control_acceso.generarReporte()

# Iniciar el sistema
def iniciarSistema():
    print("Bienvenido a Refrescamelo SAS")
    gestionarRoles()

# Ejecutar el sistema
if __name__ == "__main__":
    iniciarSistema()
    
    