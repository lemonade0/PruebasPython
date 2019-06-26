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
Ejercicio 1
Escriba una función que tome una lista de números y devuelva la suma acumulada, es decir, una nueva lista donde el
primer elemento es el mismo, el segundo elemento es la suma del primero con el segundo, el tercer elemento es la suma
del resultado anterior con el siguiente elemento y así sucesivamente. 
Por ejemplo, la suma acumulada de [1,2,3] es [1, 3, 6].

"""
def sumalista(listaNumeros):
    laSuma = 0
    for i in listaNumeros:
        laSuma = laSuma + i
        lista += [laSuma]
        return laSuma

print(sumalista([1,2,3]))