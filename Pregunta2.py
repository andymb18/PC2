#Inicio
numeros = []

#Proceso
while len(numeros) < 5:
    n = int(input("Ingrese cualquier numero"))

    if numeros.count(n) == 0:
        numeros.append(n)

        
#Salida
print(numeros)