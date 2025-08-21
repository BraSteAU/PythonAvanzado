#combinando map, filter y lambda.

nombres = ["Ana", "Pedro", "Isabela", "Juan", "Camila", "Sofía", "Leo"]
masletras = filter(lambda x: len(x)>4,nombres)
mayusculas = list(map(lambda x: x.upper(),masletras))
print(mayusculas)