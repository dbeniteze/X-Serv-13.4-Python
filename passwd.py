#!usr/bin/python 

fich = open("/etc/passwd", "r")
lineas= fich.readlines()
for i in lineas:
    separada = i.split(":", len(lineas))
    user = separada[0]
    shell = separada[-1]
    print user, shell
