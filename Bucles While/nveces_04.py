#!/usr/bin/python
# -*-coding: utf-8-*-

num = int(input("Escriba la cantidad de números positivos a solicitar: "))
while num < 1:
    num = int(input("La cantidad debe ser mayor que 0. Inténtelo de nuevo: "))

print()
numero = int(input("Escriba un número: "))
total = 1
if numero > 0:
    cantidad = 1
else:
    cantidad = 0

while cantidad < num:
    numero = int(input("Escriba otro número: "))
    if numero > 0:
        cantidad += 1
    total += 1

print()
if cantidad == 1:
    print("Ha escrito 1 número positivo.")
else:
    print("Ha escrito", total, "números,", num, "de ellos positivos.")
print("Programa terminado")
