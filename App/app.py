"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista .
"""

import config as cf
import sys
import csv
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt
from Sorting import shellsort as sortshell
from Sorting import insertionsort as sortinsertion
from Sorting import selectionsort as sortselection
import copy

from time import process_time 


def loadCSVFile (file, sep=";"):
    """
    Carga un archivo csv a una lista
    """
    #lst = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    lst = lt.newList() #Usando implementacion linkedlist
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    with open(file, encoding="utf-8") as csvfile:
        spamreader = csv.DictReader(csvfile, dialect=dialect)
        for row in spamreader: 
            lt.addLast(lst,row)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return lst


def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
    print("3- Contar elementos filtrados por palabra clave")
    print("4- Consultar elementos a partir de dos listas")
    print('5- ordenar lista')
    print('6-verificar ordenamiento')
    print("0- Salir")

def countElementsFilteredByColumn(criteria, column, lst):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    """
    if lst['size']==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0
        iterator = it.newIterator(lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            if criteria.lower() in element[column].lower(): #filtrar por palabra clave 
                counter+=1           
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return counter

def countElementsByCriteria(criteria, column, lst):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    """
    return 0
def less(element1, element2):
        if int(element1['vote_count']) <  int(element2['vote_count']):
            return True
        return False
def greater(element1, element2):
        if int(element1['vote_average']) >  int(element2['vote_average']):
            return True
        return False
def sorting_shell(lst, compFunction):
    t1_start = process_time()
    sortshell.shellSort(lst, compFunction)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    
def sorting_insertion(lst, compFunction):
    t1_start = process_time()
    sortinsertion.insertionSort(lst, compFunction)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")

def sorting_selection(lst, compFunction):
    t1_start = process_time()
    sortselection.selectionSort(lst, compFunction)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos") 

def verifySorting(lista, compFunction):
        iterator = it.newIterator(lista)
        count=0
        prev_element=None
        while  it.hasNext(iterator):
            element = it.next(iterator)
            #result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
            #print (result)
            if count > 0:
                if compFunction(element, prev_element):
                    return False
            count+=1
            prev_element=copy.copy(element)
        return True
    
    


def main():
    lista = None 
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                lista = loadCSVFile("Data/Small.csv") #llamar funcion cargar datos
                print("Datos cargados, ",lista['size']," elementos cargados")
            elif int(inputs[0])==2: #opcion 2
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")    
                else: print("La lista tiene ",lista['size']," elementos")
            elif int(inputs[0])==3: #opcion 3
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:   
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    counter=countElementsFilteredByColumn(criteria, "nombre", lista) #filtrar una columna por criterio  
                    print("Coinciden ",counter," elementos con el crtierio: ", criteria  )
            elif int(inputs[0])==4: #opcion 4
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    counter=countElementsByCriteria(criteria,0,lista)
                    print("Coinciden ",counter," elementos con el crtierio: '", criteria ,"' (en construcción ...)")
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
            elif int(inputs[0])==5:
                tipo_ordenamiento= input('si desea ordenar por shell sort oprima 0,\nsi desea ordenar por inserionsort oprima 1,\nsi desea ordenar por selectionsort oprima 2,\n')
                if int(tipo_ordenamiento)==0:
                    comando= input('si desea ordenar la lista de menor a mayor cantidad de votos oprima 0, \nsi desea ordenar la lista  de mayor a menor Vote average oprima 1\n')
                    if int(comando)==0:
                        print('ordenando lista...')
                        sorting_shell(lista, less)
                        print('lista ordenada')
                    elif int(comando)==1:
                        print('ordenando lista...')
                        sorting_shell(lista, greater)
                        print('lista ordenada')
                elif int(tipo_ordenamiento)==1:
                    comando= input('si desea ordenar la lista de menor a mayor cantidad de votos oprima 0, \nsi desea ordenar la lista  de mayor a menor Vote average oprima 1\n')
                    if int(comando)==0:
                        print('ordenando lista...')
                        sorting_insertion(lista, less)
                        print('lista ordenada')
                    elif int(comando)==1:
                        print('ordenando lista...')
                        sorting_insertion(lista, greater)
                        print('lista ordenada')
                elif int(tipo_ordenamiento)==2:
                    comando= input('si desea ordenar la lista de menor a mayor cantidad de votos oprima 0, \nsi desea ordenar la lista  de mayor a menor Vote average oprima 1\n')
                    if int(comando)==0:
                        print('ordenando lista...')
                        sorting_selection(lista, less)
                        print('lista ordenada')
                    elif int(comando)==1:
                        print('ordenando lista...')
                        sorting_selection(lista, greater)
                        print('lista ordenada')
            elif int(inputs[0])==6:
                comando=input('si desea revisar la lista de menor a mayor cantidad de votos oprima 0, \nsi desea revisar la lista  de mayor a menor Vote average oprima 1\n')
                if int(comando)==0:
                    print(verifySorting(lista, less))
                elif int(comando)==1:
                    print(verifySorting(lista, greater))
                #print(lista['first'])
                #for element in lista:
                    #print(element)


                
                
                
if __name__ == "__main__":
    main()