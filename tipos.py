#name, numero = "harold", 100
#print(name, numero)
#print(dir(name))
# print(name.upper()) 
# print(name.lower())
# print(name.swapcase())
# print(name.replace("harold", "a"))
# print(name.count("a"))
# print(name.startswith("h"))
# print(name.endswith("d"))
# print(name.split())
# print(name.find("o"))
# print(len(name))
# print(name.index("l"))
#print(name[4])

#---------------------------------------------------------------------

#la f sirve para que interprete lo que está entre llaves como variable
#print(f"mi nimbre es {name}")

#listas 
# mi_lista = ["maria","pepe","jorge","marta"]
# print(mi_lista[0:2])
#el signo * en listas sirve como repetidor 
#el primer numero hace referencia al numero donde se empieza y el segundo en donde termina
#number_list = list((1, 2, 3, 4))
#colors = ["blue", "red", "green"]
#r = list(range(1, 100))
#print(r)
#colors[1] = "yellow"
#print(number_list)
#print("green" in colors)
#print(colors[0])
#print(len(colors))
#print(dir(number_list))
#colors.extend(["violet", "purple"])
#colors.insert(1, "violet")
#colors.append("orange")
#colors.insert(len(colors), "violet")
#.pop sirve para remover el elemento mas reciente, asi como remove elimina un elemento especifico
#colors.pop()
#colors.remove("red")
# colors.sort(reverse=True) #de esta forma los ordena demanera inversa
# print(colors)
# colors.clear()

#-------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------
#TUPLAS
# x = (1, 2, 3)
# print(x)
# y = tuple((4, 5, 6))
# del y # del sirve para borrar una variable
# print(y)
# mitupla = ("yo",13,2,"dos")
# print(mitupla)
# milista = list(mitupla)
# print(milista)
#tambien se puede convertir una lista a una tupla usando tuple()
#-------------------------------------------------------------------------------------
#DICTIONARY
# midiccionario = {"Alemania":"berlin",
# "Francia":"paris",
# "UK":"londres"
# }
# midiccionario["italia"]="roma"
# print(midiccionario)
# del midiccionario["UK"]
# print(midiccionario)

#  productos = {
#      "playera": 30,
#      "pantaloneta":20,
#      "sueter": 60,
#      "pans": 40
#  }
#  print(productos)

#juntar los valores de una dupla y un diccionario
# mitupla = ("españa","alemania","francia","EEUU")
# midiccionario={mitupla[0]:"madrid",mitupla[1]:"berlin",mitupla[2]:"paris",mitupla[3]:"washington"}
# print(midiccionario)
#METODOS PARA LOS DICCIONARIOS: 
#.keys() .len() .values()
#------------------------------------------------------------------------------------------
#CONDICIONALES
nota_alumno=input("ingresa la nota del alumno  ")

def evaluacion(nota): 
    valoracion="aprobado"
    if nota<5: 
        valoracion="suspendido por esta vez"
    return valoracion 

print(evaluacion(int(nota_alumno)))

