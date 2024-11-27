#abro y edito un archivo

with open('prac.txt', 'r') as fichero:
    contenido = fichero.read()

contenido=contenido+"\nEsta es una nueva cadena de texto"

with open('prac.txt', 'w') as fichero:
    fichero.write(contenido)