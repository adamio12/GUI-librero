#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 15:39:08 2020

@author: danko
"""

class Librero():
    miLib=[]
    
    def __init__(self):
        print('esta instaniado')

    def sayhi(self):
        print("hloo")
    
    def mostrar(self):
        slibrero=""
        for libro in self.miLib:
            slibrero = slibrero + str(libro)+"\n"
            #print(str(libro))
        return slibrero
        #print(str(self.miLib[0])+"soy objeto")
    
    
    def cambioAutor(self,numLib,autorNv):
        self.miLib[numLib-1].autor=autorNv
    
    def cambioTitulo(self,numLib,TitNv):
        self.miLib[numLib-1].nombre=TitNv
        
    def baja(self,numLib):
        #se accede al elemento para eliminarlo
        self.miLib.remove(self.miLib[numLib-1])
    
    def altaLib(self,libro,autor):
        self.miLib.append(Libro(libro,autor))
        #print("alta")
    


class Cosa:
    "Clase que representa una cosa."
    def __init__(self, nombre):
        "Constructor de Cosa"
        self.nombre = nombre
            
            
class Libro(Cosa):
    def __init__(self,nombre,autor):
        self.autor = autor
        #llamada del constructor padre
        Cosa.__init__(self, nombre)
        # agregamos el nuevo atributo
    def __str__(self):
        return self.autor+"; "+self.nombre
    
    def cambioAutor(self,autorNv):
        self.autor = autorNv


#se inicializa el librero
miLibrero = Librero()
miLibrero.altaLib("harry 2","jk")
miLibrero.altaLib("harry 3","jk")
miLibrero.altaLib("harry 4","jk")
"""
print(miLibrero.mostrar())
miLibrero.cambioAutor(2, "J.K. rowling")
print(miLibrero.mostrar())
print((2).__class__.__name__)

print("//")
print(miLibrero.miLib[0])
print("//")
miLibrero.baja(1)
#miLibrero.mostrar()
miLibrero.mostrar()
"""

