import time
import random
from Node import LinkedList

# # Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10)
# # y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado
# # y su cubo.
#
#
# # CÓDIGO DE EJEMPLO USANDO LISTAS DE PYTHON
#
# start_time = time.perf_counter()
# lista_numeros = []
#
# for indice in range(1,11):
# 	lista_numeros.append(random.randint(1,10))
#
# for numero in lista_numeros:
# 	print(numero," ",numero ** 2," ",numero ** 3)
#
# end_time = time.perf_counter()
# execution_time = (end_time - start_time)
#
# print(f"Ejecución con listas de python: {execution_time} nanosegundos")#"Ejecución con listas de python: 0.00014479993842542171 nanosegundos"


# CÓDIGO REALIZADO POR MÍ IMPLEMENTANDO LAS CLASES (NODE Y LINKEDLIST) JUNTO A SUS MÉTODOS


start_time = time.perf_counter()
number_list = LinkedList()
for i in range(1,11):
    number_list.add_at_front(random.randint(1,10))

current = number_list.head
while current is not None:
    print(current.data, current.data ** 2, current.data ** 3)
    current = current.next

end_time = time.perf_counter()
execution_time = (end_time - start_time)
print(f"Ejecución con mis métodos: {execution_time} nanosegundos")#Ejecución con mis métodos: 0.0001121999230235815 nanosegundos

#El tiempo de ejecución de mi solución es menor, lo que indica que es más rápida