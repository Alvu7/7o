class Cliente:
    def __init__(self, nombre, apellido, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.activo = True 

    def __str__(self):
        estado = "Activo" if self.activo else "Inactivo"
        return f"{self.nombre} {self.apellido} | Tel: {self.telefono} | Estado: {estado}"
