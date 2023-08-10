from tarfile import LinkOutsideDestinationError


numero=-1

#if (numero > 0):
    #print("numero es positivo")
#elif(numero == 0):
     #print("numero es cero")
#else:
     #print("numero es negativo")

i=0
while i < 5:
     print("Vamoooooos")
     i += 1

#funciones
def miFuncion():
     nombre = "Luis"
     return("Hola " + nombre + "!")

resultado = miFuncion()
print(resultado)

def sumaNum(numero1, numero2):
     return numero1 + numero2
total = sumaNum(15, 5)
print(total)

#listas
miLista = [1,2,3,4,5,6,7]

i=0
for elemento in miLista:
     miLista[i] += 5
     i += 1

print(miLista)


