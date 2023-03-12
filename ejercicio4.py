from Node import LinkedList
import time

# Programa que declare una lista y la vaya llenando de números hasta que
# introduzcamos un número negativo. Entonces se debe imprimir el vector
# (sólo los elementos introducidos).


# CÓDIGO DE EJEMPLO USANDO LISTAS DE PYTHON

# start_time = time.perf_counter()
# lista = []
# numero = int(input("Introduce un número en la lista:"))
# while numero >= 0:
#     lista.append(numero)
#     numero = int(input("Introduce un número en la lista:"))
#
# for numero in lista:
#     print(numero, " ", end="")
# end_time = time.perf_counter()
#
# execution_time = (end_time - start_time)
# print(f"Ejecución con listas de python: {execution_time} nanosegundos")#3.462341299979016 nanosegundos


# CÓDIGO REALIZADO POR MÍ IMPLEMENTANDO LAS CLASES (NODE Y LINKEDLIST) JUNTO A SUS MÉTODOS


start_time = time.perf_counter()
number_list = LinkedList()
numero = input("Ingresa un número: ")

while numero.isnumeric() and int(numero) >= 0:
    number_list.add_at_front(numero)
    numero = input("Ingresa un número: ")

number_list.print_list()

end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Tiempo de ejecución: {execution_time} nanosegundos")#Tiempo de ejecución: 2.361330699874088 nanosegundos

#De nuevo el tiempo de ejecución del código usando mis métodos es menor (más rápido), pero creo que
#el tiempo puede variar dependiendo el tiempo en que se ingresen los datos




