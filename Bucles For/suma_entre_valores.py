#!/usr/bin/python
# -*-coding: utf-8-*-

print("SUMA ENTRE VALORES")
numero_1 = int(input("Escriba un número entero: "))
numero_2 = int(input(f"Escriba un número entero mayor que {numero_1}: "))

if numero_2 <= numero_1:
    print(f"¡Le he pedido un número entero mayor o igual que {numero_1}!")
else:
    suma = 0
    for i in range(numero_1, numero_2 + 1):
        suma = suma + i
    print(f"La suma desde {numero_1} hasta {numero_2} es {suma}")

    for i in range(numero_1, numero_2):
        print(f"{i} + ", end="")
    print(f"{numero_2} = {suma}")
