#manejo de excepciones

try:
    with open('nohay.txt', 'r') as fichero:
        contenido = fichero.read()
        print(contenido)


except FileNotFoundError:
    print("El archivo no existe")

except IOError:
    print("Ocurrio un error de lectrura")