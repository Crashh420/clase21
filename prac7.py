#abrir archivo en modo binario
with open('imagen.png', 'rb') as archivo:
    variable=archivo.read()

with open("copiamintic.png", "wb") as copiadearchivo:
    copiadearchivo.write(variable)

print("Clonacion very good")