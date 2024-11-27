#escrituras de listas en archivos
lista=["lista1", "lista2", "lista3", "lista4", "lista5"]
with open("prac5.txt", "w") as archivo:
    for i in lista:
        archivo.write(i + "\n")