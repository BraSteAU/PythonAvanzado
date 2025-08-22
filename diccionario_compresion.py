#Crea un diccionario por comprensión donde:
#La clave sea el nombre.
#El valor sea "Largo" si el nombre tiene más de 4 letras, o "Corto" si tiene 4 o menos.

nombres = ["Ana", "Pedro", "Isabela", "Juan", "Camila", "Sofía", "Leo"]
diccionario = {nombre: ("Largo" if len(nombre)>4 else "Corto") for nombre in nombres}
print(diccionario)