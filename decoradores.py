import time

def medir_tiempo(funcion):
    def wrapper(*args, **kwargs):
        inicio = time.time()             # Tiempo antes de ejecutar
        resultado = funcion(*args, **kwargs)  # Ejecutamos la función
        fin = time.time()                # Tiempo después
        print(f"La función tardó {fin - inicio:.5f} segundos")
        return resultado
    return wrapper

@medir_tiempo
def calcular():
    suma = 0
    for i in range(1, 1000000):
        suma += i
    return suma

print(calcular())
