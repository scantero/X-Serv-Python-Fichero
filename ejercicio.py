#!/usr/bin/python
# -*- coding: utf-8 -*-

fichero = open("/etc/passwd", "r")

usuarios = fichero.readlines()

for linea in usuarios:
    contenido = linea.split(":")
    print "usuario:", contenido[0], "-> shell:", contenido[-1],
    
print "Número de usuarios:",len(usuarios),
    
fichero.close()
