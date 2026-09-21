"""
Create
Read
Update
Delete
Registrar un listado de edades:
"""

edades = []

def agregarEdad (edad):
    edades.append(edad)

def mostrarEdades():
    return edades

def actualizarEdad(edad, index):
    edades[index] = edad

def eliminarEdad(edad):
    edades.remove(edad)

def menu():
    print("""1. Agregar
    2. Editar
    3. Eliminar
    4. Mostrar
    0. Salir
    Digite su opcion [0 - 4]:
    """)
    op = int(input())
    return op

def pedirDato():
    edad = 0
    while True:
        try:
            edad = int(input("Digite la edad: "))
            return edad
        except ValueError:
            print("Escriba un valor valido.")

def seleccionarOpcion():
    op = menu()
    if op == 1:
        print("Dime una edad: ")
        pedirDato()
        edad = pedirDato()
        agregarEdad(edad)
    elif op == 2:
        print("Dime en que posicion se encuentra: ")
        pos = pedirDato()
        print("Dime la nueva edad: ")
        edad = pedirDato()
        actualizarEdad(edad, pos)
    elif op == 3:
        print("Dime la edad a eliminar: ")
        edad = pedirDato()
        eliminarEdad()
    elif op == 4:
        mostrarEdades()
    elif op == 0:
        print("Adios.")

    else:
        print("opcion invalida")
    



seleccionarOpcion()