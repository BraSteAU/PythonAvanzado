nombres = ["Ana", "Pedro", "Isabela", "Juan", "Camila", "Sofía", "Leo"]
lista = [nombre.upper() for nombre in nombres if len(nombre)>4]
print(lista)