import operator
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 10:26:28 2021

@author: Martínez Franco César Augusto & Noriega Domínguez Lisset
"""



class TablaLenguaje:
    def __init__(self, nombreArchivo, nombreLengua = "Ninguna"):
         self.cadena = self.archivoACadena(nombreArchivo)
         self.nombre = nombreLengua
         
         
    def obtenNGramas(self,listaPalabras, n):
        return [listaPalabras[i:i+n] for i in range(len(listaPalabras)-(n-1))]

    def frecuenciaRelativa(self,listaNgramas):
        longitudNgrama = len(listaNgramas)
        dict = {}
        for nGrama in listaNgramas:
            if(nGrama in dict.keys()):
                dict[nGrama] += 1/longitudNgrama
            else:
                dict[nGrama] = 1/longitudNgrama
        return dict
    def creaNGrama(self,cadena,n):
        p = self.obtenNGramas(cadena, n)
        return self.frecuenciaRelativa(p)
    def archivoACadena(self,nombreArchivo):
        archivo = open(nombreArchivo, encoding="utf8")
        return "".join(archivo.readlines())


def indiceJaccard(conjunto1,conjunto2):
    interseccion = conjunto1.intersection(conjunto2)
    union = conjunto1.union(conjunto2)
    return float(len(interseccion)/len(union))

def distanciaManhattan(dic_entrenamiento, dic_prueba):
    suma = 0
    for x in dic_entrenamiento:
        if x in dic_prueba.keys():
            suma += abs(dic_entrenamiento[x]-dic_prueba[x])
        else:
            suma += dic_entrenamiento[x]
    return suma

def distanciaEuclidiana(dic_entrenamiento, dic_prueba):
    suma = 0
    for x in dic_entrenamiento:
        if x in dic_prueba.keys():
            suma += (abs(dic_entrenamiento[x]-dic_prueba[x])) ** 2
        else:
            suma += dic_entrenamiento[x]
    return suma**(1/2)

def distanciaLevenshtein(dic_entrenamiento, dic_prueba):
    total = 0
    for x in dic_entrenamiento:
        for y in dic_prueba:
            total += letrasDiferentes(x, y)
    return total

def letrasDiferentes(cadena1, cadena2):
    total = 0
    i = 0
    for x in cadena1:
        if x != cadena2[i]:
            total += 1
        i += 1
    return total

def criterioDistancia(lenguas, prueba,funcion, n):
    min =  float('inf')
    nombreLengua = ""
    for lengua in lenguas:
        x = funcion(lengua.creaNGrama(lengua.cadena,n),prueba.creaNGrama(prueba.cadena,n))
        if(x<min):
            min = x
            nombreLengua = lengua.nombre
    return nombreLengua

def criterioJaccard(lenguas, prueba, n):
    max =  0
    nombreLengua = ""
    for lengua in lenguas:
        x = indiceJaccard(set(list(lengua.creaNGrama(lengua.cadena,n))),set(list(prueba.creaNGrama(prueba.cadena,n))))
        if(x>max):
            max = x
            nombreLengua = lengua.nombre
    return nombreLengua
        
        
    
tablaEspañol = TablaLenguaje("garcia_soledad.txt","Español")
tablaFinlandes = TablaLenguaje("Lönnrot_Kalevala.txt","Finlandés")
tablaIngles = TablaLenguaje("Twain_Sawyer.txt","Inglés")


pruebaClase = TablaLenguaje("prueba.txt")

arregloLenguas = [tablaEspañol,tablaFinlandes,tablaIngles]

for n in range(1,4):
    print("Levenstein ",n,"-grama",criterioDistancia(arregloLenguas,pruebaClase,distanciaLevenshtein,n))
    print("Euclidiana ",n,"-grama",criterioDistancia(arregloLenguas,pruebaClase,distanciaEuclidiana,n))
    print("Manhattan ",n,"-grama",criterioDistancia(arregloLenguas,pruebaClase,distanciaManhattan,n))
    print("Jaccard ",n,"-grama",criterioJaccard(arregloLenguas,pruebaClase,n))



