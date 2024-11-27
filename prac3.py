#lectura linea por linea
import time
with open('prac3.txt', 'r') as fichero:
    for linea in fichero:
        print(linea.strip()) #imprime cada linea sin saltos de linea
        time.sleep(0.09)


print("Ejecucion finalizada")