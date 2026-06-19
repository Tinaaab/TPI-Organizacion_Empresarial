import csv

def buscar_empleado(legajo):

    with open("empleados.csv", "r", encoding="utf-8") as archivo:

        lector = csv.DictReader(archivo)

        for fila in lector:

            if fila["legajo"] == legajo:
                return fila

    return None


print("=== SISTEMA DE VACACIONES ===")

legajo = input("Ingrese su legajo: ")

empleado = buscar_empleado(legajo)

if empleado is None:

    print("Empleado no encontrado")

else:

    print("Bienvenido:", empleado["nombre"])

    saldo = int(empleado["saldo"])

    try:

        dias = int(input("Ingrese cantidad de dias solicitados: "))

        if dias <= saldo:

            nuevo_saldo = saldo - dias

            print("Solicitud aprobada")
            print("Saldo restante:", nuevo_saldo)

        else:

            print("Solicitud rechazada")
            print("Saldo insuficiente")

    except ValueError:

        print("Debe ingresar un numero valido")