#Usa listas por comprensión para generar una nueva lista que:
#Si el número es par, guarde su cuadrado.
#Si el número es impar, guarde su cubo.

numeros = [5, 8, 13, 22, 7, 10]
lista = [num**2 if num%2==0 else num**3 for num in numeros ]
print(lista)