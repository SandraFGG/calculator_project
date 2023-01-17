import numpy
import math

def suma():
    print('Elegiste la opción suma')
    primerNumero = int(input('Proporciona el primer número: '))
    segundoNumero = int(input('Proporciona el segundo número: '))
    print(f'{primerNumero} + {segundoNumero} = {primerNumero + segundoNumero}')

def resta():
    print('Elegiste la opción resta')
    primerNumero = int(input('Proporciona el primer número: '))
    segundoNumero = int(input('Proporciona el segundo número: '))
    print(f'{primerNumero} - {segundoNumero} = {primerNumero - segundoNumero}')

def multiplicacion():
    print('Elegiste la opción multiplicación')
    primerNumero = int(input('Proporciona el primer número: '))
    segundoNumero = int(input('Proporciona el segundo número: '))
    print(f'{primerNumero} * {segundoNumero} = {primerNumero * segundoNumero}')

def division():
    print('Elegiste la opción división')
    primerNumero = int(input('Proporciona el primer número: '))
    segundoNumero = int(input('Proporciona el segundo número: '))
    print(f'{primerNumero} / {segundoNumero} = {primerNumero / segundoNumero}')

def raiz():
    print('Elegiste la opción raíz n')
    indiceRaiz = int(input('Proporciona el índice de la raíz: '))
    radicandoRaiz = int(input('Proporciona el radicando: '))
    print(f'La raíz {indiceRaiz} del número {radicandoRaiz} es: {numpy.power(radicandoRaiz, (1/indiceRaiz))}')

def exponente():
    print('Elegiste la opción exponente n')
    exponente = int(input('Proporciona el exponente: '))
    numero = int(input('Proporciona el número: '))
    print(f'{numero}^{exponente}= {numpy.power(numero, (exponente))}')

def seno():
    print('Elegiste la opción seno')
    angulo = int(input('Proporciona el ángulo: '))
    print(f'El seno del ángulo es: {math.sin((angulo * math.pi)/180)}')




def salir():
    print('Hasta nunca')

