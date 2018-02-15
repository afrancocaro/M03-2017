#!/usr/bin/python
# -*-coding: utf-8-*-

print("MAYOR, MENOR Y MEDIA ARITMÉTICA")
numero = int(input("¿Cuántos valores quiere introducir? "))

if numero <= 0:
    print("¡No se puede, imposible¡")
else:
    valor = float(input("Escriba el número 1: "))
    minimo = maximo = suma = valor
    for i in range(2, numero + 1):
        valor = float(input(f"Escriba el número {i}: "))
        suma = suma + valor
        if valor < minimo:
            minimo = valor
        if valor > maximo:
            maximo = valor
    print(f"El número más pequeño de los introducidos es {minimo}")
    print(f"El número más grande de los introducidos es {maximo}")
    print(f"La media de los números introducidos es {suma / numero}")
