import os
import shutil
cale='C:/Users/Laurentiu/Downloads'
lista_fisiere=os.listdir(cale)
for i in range(len(lista_fisiere)):
    nume=lista_fisiere[i][str(lista_fisiere[i]).rfind('.')::]
    try:
        if str(nume[1:]) not in os.listdir(cale):
            path = os.path.join(cale,str(nume[1:])) 
            os.mkdir(path) 
        shutil.move(f"{cale}/{str(lista_fisiere[i])}",f"{cale}/{str(nume[1:])}/{str(lista_fisiere[i])}")
    except:
        print("Se cauta fisiere noi..")
