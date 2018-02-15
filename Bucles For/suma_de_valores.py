#!/usr/bin/python
# -*-coding: utf-8-*-

print("SUMA DE VALORES")
numero = int(input(f"¿Cuántos valores va a introducir? "))

if numero <= 0:
    print("¡Imposible!")
else:
    suma = 0
    for i in range(1, numero + 1):
        valor = float(input(f"Escriba el número {i}: "))
        suma = suma + valor
    print(f"La suma de los números que ha escrito es {suma}")
