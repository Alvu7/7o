from cliente import Cliente
from node import Node

class ListaDobleClientes:
    def __init__(self):
        self.head = None
        self.tail = None

    def registrar_cliente(self, nombre, apellido, telefono):
        nuevo_cliente = Cliente(nombre, apellido, telefono)
        nuevo_nodo = Node(nuevo_cliente)

        if self.head is None:
            self.head = self.tail = nuevo_nodo
        else:
            self.tail.next = nuevo_nodo
            nuevo_nodo.prev = self.tail
            self.tail = nuevo_nodo

        print(f"Cliente '{nombre} {apellido}' registrado correctamente.")

    def listar_clientes(self):
        if self.head is None:
            print("No hay clientes registrados.")
            return

        actual = self.head
        print("\nLista de clientes")
        while actual:
            print(actual.data)
            actual = actual.next
        print("\n")

    def eliminar_cliente(self, telefono):
        actual = self.head
        while actual:
            if actual.data.telefono == telefono:
                if not actual.data.activo:
                    print("El cliente ya está inactivo.")
                    return
                actual.data.activo = False
                print(f"Cliente con teléfono {telefono} marcado como inactivo.")
                return
            actual = actual.next
        print("Cliente no encontrado.")
