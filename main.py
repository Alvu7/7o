from lista_doble_clientes import ListaDobleClientes

def menu():
    lista = ListaDobleClientes()

    while True:
        print("""
--------MENÚ---------- 
1. Registrar cliente
2. Listar clientes
3. Eliminar cliente
4. Salir
""")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            telefono = input("Teléfono: ")
            lista.registrar_cliente(nombre, apellido, telefono)

        elif opcion == "2":
            lista.listar_clientes()

        elif opcion == "3":
            telefono = input("Ingrese teléfono del cliente a eliminar: ")
            lista.eliminar_cliente(telefono)

        elif opcion == "4":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    menu()
