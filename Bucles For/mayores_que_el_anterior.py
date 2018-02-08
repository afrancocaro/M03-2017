#!/usr/bin/python
# -*-coding: utf-8-*-

print("MAYORES QUE EL ANTERIOR")
valores = int(input("¿Cuántos valores quiere introducir? "))
if valores < 1:
    print("¡No se puede, imposible!")
else:
    primero = int(input("Escriba un número: "))
    for i in range(valores - 1):
        numero = int(input(f"Escriba un número más grande que {primero}: "))
        if numero <= primero:
            print(f"¡{numero} no es mayor que {primero}!")
        primero = numero
    print("Hasta otra, Adiós!!")
