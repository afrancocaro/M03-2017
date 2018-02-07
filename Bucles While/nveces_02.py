#!/usr/bin/python
# -*-coding: utf-8-*-

primero = float(input("Escriba un número: "))
segundo = float(input("Escriba un número mayor que " + str(primero) + ": "))

while segundo > primero:
    segundo = float(input("Escriba un número mayor que " + str(primero) + ": "))

print()
print(segundo, "no es mayor que", str(primero) + ".")
print("Programa terminado")
