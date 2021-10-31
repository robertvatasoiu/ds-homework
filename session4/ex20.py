"""
    Ex. 20: Deschideti fisierul .json creat la exercitiul anterior, cititi
    continutul si returnati un dictionar (dictionarul de acolo).

    Toate astea le veti face intr-o functie read_from_file(file), unde
    file este numele fisierului primit dat ca parametru.
"""
import json


def read_from_file(file):
    with open(file) as read_file:
        print(json.load(read_file))


read_from_file("ceva.json")
