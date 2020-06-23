from urllib.request import urlopen
web = urlopen('https://tools.ietf.org/html/rfc1180')
archivoBackup=open("./dump.html","wb")

lectura=web.read()
archivoBackup.write(lectura)


archivoBackup.close()




