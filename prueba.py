"""Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la función
len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio."""

"""
def calcularLongitud(palabra):
    a = len(palabra)
    print(a)
#principal
cadena = input("INTRODUCE UN PALABRA : ")
calcularLongitud(cadena)
"""
"""
Ejercicio 4
Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene que evaluar la cadena y decir
cuantas letras mayúsculas tiene. 
"""
"""
import re
def contar_mayusculas(texto):
    textoSoloMayusculas = re.sub('[^A-Z]', '', texto)
    print("Mayusculas: " + str(len(textoSoloMayusculas)))

texto = input("Texto Con Mayusculas y minusculas y num")
contar_mayusculas(texto)
"""
"""
laSuma = 0
    for i in listaNumeros:
        laSuma = laSuma + i
    return laSuma
"""