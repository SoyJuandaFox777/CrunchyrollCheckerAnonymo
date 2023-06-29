#!/usr/bin/env python3
"""
  ¸,ø¤º°`°º¤ø,¸¸,ø¤º° ᒎ𝐃_Ⓐ𝓷𝐎ภƳ𝓜ⓞ °º¤ø,¸¸,ø¤º°`°º¤ø,¸
"""

### Importing
# Importing Inbuilt-Packages
import os

# Importing Dev Defined Script
import src.checker

tag = """
  ¸,ø¤º°`°º¤ø,¸¸,ø¤º° ᒎ𝐃_Ⓐ𝓷𝐎ภƳ𝓜ⓞ °º¤ø,¸¸,ø¤º°`°º¤ø,¸
"""

def main():
    print(tag)
    if not os.path.exists('result'):
        os.makedirs('result')
        
    filename = input("Ingresa el nombre del archivo: ")
    if os.path.isfile(filename):
        src.checker.CrunchyrollChecker.create(filename)
    else:
        print("Archivo no encontrado.")


### yeaaahhhh!!!!
if __name__ == "__main__":
    main()

