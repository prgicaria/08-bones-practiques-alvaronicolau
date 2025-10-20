#!/usr/bin/env python

'''Bones pràctiques. Es divideixen dos nombres enters 
i es mosta la divisió, el quocient i el residu.

Institut Icària
Programació  - 1r Batxillerat - Curs 2025-26

El programa demana a l'usuari dos nombres enters, dividend i divisor.
La sortida per pantalla mostra la divisió, el quocient i el residu.

'''

__author__ = "Álvaro"
__email__ = "anicolau@instituticaria.cat"
__date__ = "2025/10/17"

dividend = int(input("Entra el dividend: "))
divisor = int(input("Entra el divisor: "))

quocient = dividend // divisor
residu = dividend % divisor

print(f"La divisió és: {dividend}/{divisor}")
print(f"El quocient és: {quocient}")
print(f"El residu és: {residu}")
