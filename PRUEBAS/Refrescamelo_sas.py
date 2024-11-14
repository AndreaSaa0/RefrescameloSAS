from datetime import datetime

class Empleado:
    def __init__(self, id, nombre, apellido, cargo, area, turno, uniforme):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.cargo = cargo
        self.area = area
        self.turno = turno
        self.uniforme = uniforme
        self.roles = []

    def asignarRol(self, rol):
        self.roles.append(rol)
    
    def actualizarDatos(self, nombre=None, apellido=None, cargo=None, area=None, turno=None, uniforme=None):
        if nombre: self.nombre = nombre
        if apellido: self.apellido = apellido
        if cargo: self.cargo = cargo
        if area: self.area = area
        if turno: self.turno = turno
        if uniforme: self.uniforme = uniforme

    def registrarAcceso(self, area, ingreso):
        return ControlAcceso(id=len(ControlAcceso.registros) + 1, empleado=self, area=area, ingreso=ingreso)


class Rol:
    roles = []

    def __init__(self, id, nombre, descripcion, permisos):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.permisos = permisos
        Rol.roles.append(self)

    def editarRol(self, nombre=None, descripcion=None, permisos=None):
        if nombre: self.nombre = nombre
        if descripcion: self.descripcion = descripcion
        if permisos: self.permisos = permisos

    def eliminarRol(self):
        Rol.roles.remove(self)

    def asignarPermisos(self, nuevos_permisos):
        self.permisos.extend(nuevos_permisos)


class ControlAcceso:
    registros = []

    def __init__(self, id, empleado, area, ingreso):
        self.id = id
        self.empleado = empleado
        self.area = area
        self.fecha_hora = datetime.now()
        self.ingreso = ingreso  # Puede ser 'entrada' o 'salida'
        ControlAcceso.registros.append(self)

    @staticmethod
    def validarAcceso(empleado, area):
        for rol in empleado.roles:
            if area in rol.permisos:
                return True
        return False

    @staticmethod
    def generarReporte():
        reporte = []
        for registro in ControlAcceso.registros:
            reporte.append(f"{registro.fecha_hora} - {registro.empleado.nombre} {registro.ingreso} en {registro.area}")
        return reporte


class Auditoria:
    registros = []

    def __init__(self, id, empleado, ingreso, detalles):
        self.id = id
        self.empleado = empleado
        self.ingreso = ingreso
        self.fecha_hora = datetime.now()
        self.detalles = detalles
        Auditoria.registros.append(self)

    @staticmethod
    def registrarCambio(empleado, ingreso, detalles):
        return Auditoria(id=len(Auditoria.registros) + 1, empleado=empleado, ingreso=ingreso, detalles=detalles)

    @staticmethod
    def consultarRegistros():
        return Auditoria.registros

    @staticmethod
    def filtrarRegistros(criterio):
        return [registro for registro in Auditoria.registros if criterio in registro.detalles]


class SeguridadAcceso:
    def __init__(self, usuario, contraseña, permisos):
        self.usuario = usuario
        self.contraseña = contraseña
        self.permisos = permisos

    def autenticarUsuario(self, usuario, contraseña):
        return self.usuario == usuario and self.contraseña == contraseña

    def autorizarAcceso(self, area):
        return area in self.permisos




# Crear un rol
rol_admin = Rol(id=1, nombre="Administrador", descripcion="Acceso total", permisos=["Oficina", "Almacén"])

# Crear un empleado y asignarle un rol
empleado1 = Empleado(id=1, nombre="Julian", apellido="Daza", cargo="Supervisor", area="Oficina", turno="Mañana", uniforme="Formal")
empleado1.asignarRol(rol_admin)

# Actualizar datos del empleado (mostrando antes y después)
print(f"Datos antes de la actualización: {empleado1.nombre}, {empleado1.apellido}, {empleado1.cargo}")
empleado1.actualizarDatos(nombre="jhon ", cargo="Gerente")
print(f"Datos después de la actualización: {empleado1.nombre}, {empleado1.apellido}, {empleado1.cargo}")

# Registrar acceso del empleado
acceso = empleado1.registrarAcceso(area="Oficina", ingreso="entrada")
print(f"Acceso registrado para {empleado1.nombre} en el área {acceso.area} como {acceso.ingreso}")

# Validar el acceso
if ControlAcceso.validarAcceso(empleado1, "Oficina"):
    print(f"Acceso permitido a {empleado1.nombre} en Oficina.")
else:
    print(f"Acceso denegado a {empleado1.nombre} en Oficina.")

# Generar reporte de accesos
print("Reporte de accesos:")
reporte_accesos = ControlAcceso.generarReporte()
for registro in reporte_accesos:
    print(registro)

# Registrar auditoría de cambio
auditoria_registro = Auditoria.registrarCambio(empleado=empleado1, ingreso="entrada", detalles="Actualización de cargo")
print("Registro de auditoría:")
for registro in Auditoria.consultarRegistros():
    print(f"ID: {registro.id}, Empleado: {registro.empleado.nombre}, Detalles: {registro.detalles}, Fecha y hora: {registro.fecha_hora}")

# Autenticación de usuario
seguridad = SeguridadAcceso(usuario="Daniela, guañarita", contraseña="1234", permisos=["Oficina", "Almacén"])
if seguridad.autenticarUsuario("Daniela , guañarita", "1234"):
    print("Autenticación exitosa")
else:
    print("Autenticación fallida")