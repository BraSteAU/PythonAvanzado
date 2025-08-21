def par(x):
    es_par = (lambda x:x%2==0)(x)
    if es_par:
         print(f"{x} es par")
    else:
         print(f"{x} es impar")


x=int(input("Ingresa un numero"))
par(x)
