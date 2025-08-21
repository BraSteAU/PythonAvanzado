#Usar map con lambda para convertir una lista de temperaturas en Celsius a Fahrenheit.

temperaturas = [25,14,5,30,28]
cel_far = list(map(lambda f: (f,f*1.8+32,),temperaturas))
print(cel_far)