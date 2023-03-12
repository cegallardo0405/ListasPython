import time
from Node import LinkedList

# Queremos guardar los nombres y la edades de los alumnos de un curso.
# Realiza un programa que introduzca el nombre y la edad de cada alumno.
# El proceso de lectura de datos terminará cuando se introduzca como nombre
# un asterisco (*) Al finalizar se mostrar� los siguientes datos:
#  * Todos lo alumnos mayores de edad.
#  * Los alumnos mayores (los que tienen más edad)


# CÓDIGO DE EJEMPLO USANDO LISTAS DE PYTHON

# start_time = time.perf_counter()
# nombres = []
# edades = []
# # Inicializo las listas hasta que introduzca un "*"
# while True:
#     nombre = input("Dime el nombre de un alumno:")
#     if nombre != "*":
#         nombres.append(nombre)
#         edades.append(int(input("Dime su edad:")))
#     if nombre == "*": break;
#
# # Calcular la edad máxima
# edad_max = max(edades)
# # Alumnos mayores de edad
# print("Alumnos mayores de edad")
# print("=======================")
# for nombre, edad in zip(nombres, edades):
#     if edad >= 18:
#         print(nombre)
#
# # Alumnos mayores
#
# print("Alumnos mayores")
# print("===============")
# for nombre, edad in zip(nombres, edades):
#     if edad == edad_max:
#         print(nombre)
#
# end_time = time.perf_counter()
# execution_time = (end_time - start_time)
#
# print(f"Ejecución con listas de python: {execution_time} nanosegundos")#Ejecución con listas de python: 9.365859899902716 nanosegundos


# CÓDIGO REALIZADO POR MÍ IMPLEMENTANDO LAS CLASES (NODE Y LINKEDLIST) JUNTO A SUS MÉTODOS

start_time = time.perf_counter()
names_list = LinkedList()
ages_list = LinkedList()
name = input("Digita el nombre del estudiante: ")
while name != "*":
    age = int(input("Digita la edad del estudiante: "))

    names_list.add_to_end(name)
    ages_list.add_to_end(age)
    name = input("Digita el nombre del estudiante: ")


def max_age(ages_list):
    age_max = None
    current = ages_list.head
    while current is not None:
        if age_max is None or current.data > age_max:
            age_max = current.data
        current = current.next
    return age_max


max = max_age(ages_list)


print("Estudiantes mayores de edad :", )
current_name = names_list.head
current_age = ages_list.head
while current_name is not None and current_age is not None:
    if current_age.data >= 18:
        print(current_name.data)
    current_name = current_name.next
    current_age = current_age.next

print("Estudiantes con edad máxima:", end=" ")
current_name = names_list.head
current_age = ages_list.head
while current_name is not None and current_age is not None:
    if current_age.data == max:
        print(current_name.data, end=" ")
    current_name = current_name.next
    current_age = current_age.next
print()

end_time = time.perf_counter()
execution_time = (end_time - start_time)

print(f"Ejecución con mis métodos: {execution_time} nanosegundos")#Ejecución con mis métodos: 8.56076360004954 nanosegundos

#En este caso el tiempo de ejecución del código usando mis métodos es menor (más rápido), pero creo que
#el tiempo puede variar, incluso a ser menor o igual en ambos casos si se tiene un tiempo presiso en que el
#usuario ingresa los datos