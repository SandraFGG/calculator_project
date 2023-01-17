from operaciones import *


def mostrar_menu(opciones):
    print ('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()

def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion,opciones)
        print()

def menu_principal():
    opciones = {
        '1': ('Sumar', suma),
        '2': ('Restar', resta),
        '3': ('Multiplicar', multiplicacion),
        '4': ('Dividir', division),
        '5': ('Raíz n', raiz),

        '8': ('Salir', salir)
    }
    generar_menu(opciones, '8')