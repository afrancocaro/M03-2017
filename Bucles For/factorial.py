#!/usr/bin/python
# -*-coding: utf-8-*-

print("FACTORIAL")
numero = int(input("Escriba un número entero mayor que cero: "))

if numero <= 0:
    print("¡Le he pedido un número entero mayor que cero!")
else:
    factorial = 1
    for i in range(1, numero + 1):
        factorial = factorial * i
    print(f"El factorial de {numero} es {factorial}")
