#apertura de archivo en modo solo lectrura
with open('prac.txt','r') as archivo:
    var=archivo.read()

print("El contenido del archivo es: ")
print(var)