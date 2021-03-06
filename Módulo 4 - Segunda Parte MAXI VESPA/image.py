#ejercicio 5
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from utils import crearMatrix

#CLASES
class Image():
    """Documentación de Image"""

    def __init__(self, dimensiones:tuple = None, filename:str = ""):
        """Crea una imagen
        Paramas:
            - dimensiones: tupla con las dimensiones de la imágen a formar
            - filenme: nombre del archivo de imágen a cargar
        """
        if dimensiones:
            self.image = crearMatrix(dimensiones) #generamos una matriz de ceros
            self.filas = self.image.shape[0]
            self.columnas = self.image.shape[1]
            self.canales = self.image.shape[2]
        elif filename:
            self.image = self._loadImage(filename)
            self.filas = self.image.shape[0] #número de filas
            self.columnas = self.image.shape[1] #número de columnas
            self.canales = self.image.shape[2]
        else:
            raise ValueError("No se ha dado una dimensión ni un archivo")

    def _loadImage(self, filename:str):
        """Cargamos imágen"""
        return mpimg.imread(filename).astype(np.uint8)
        
    def show(self):
        """Mostramos imágen"""
        imgplot = plt.imshow(self.image) #.astype(np.uint8)

    def size(self):
        """Retorna una tupla de la forma (filas, columnas, canales)
        Si Image posee un solo canal, devuelve una tupla de la forma (filas, columnas)
        """
        return (self.filas,self.columnas,self.canales)

    def saveImage(self, filename:str):
        """Guarda la imágen en un archivo jpg"""
        
        return mpimg.imsave(filename,self.image)

#FUNCIONES
def ajustarContraste(image, alfa):
    """Ajusta el contraste de una imágen.
    
    Retorna una nueva imágen con las mismas dimensiones de la imágen original.
    """
    filas = image.image.shape[0] #cantidad de filas
    columnas = image.image.shape[1] #cantidad de columnas
    canales = image.image.shape[2]
    #Creo un nuevo objeto Image
    imagenProcesada = Image(dimensiones = (filas, columnas, canales))
    for canal in range(canales):
        for i in range(filas):
            for j in range(columnas):
                pixel = int(alfa*(image.image[i][j][canal]-128) + 128)
                if pixel < 0:
                    pixel = 0
                elif pixel > 255:
                    pixel = 255
                imagenProcesada.image[i][j][canal] = int(pixel)

    imagenProcesada.image = imagenProcesada.image.astype(np.uint8)
                
    return imagenProcesada
def ajustarBrillo(image, ajuste):
    """Doc..."""
    pass

def getHistograma(image):
    """Doc... Hacer documentación"""
    plt.hist(image.image.ravel(),bins=256)   
    plt.show() 

def getChannels(image):
    """Doc..."""
    pass
    #Arreglar con la función correcta

def ajustarGamma(image, gamma):
    """Doc..."""
    maximo=np.amax(image.image)
    c=(255/maximo)
    filas = image.image.shape[0] #cantidad de filas
    columnas = image.image.shape[1] #cantidad de columnas
    canales = image.image.shape[2]
    #Creo un nuevo objeto Image
    imagenProcesada = Image(dimensiones = (filas, columnas, canales))
    
    for canal in range(canales):
        for i in range(filas):
            for j in range(columnas):
                pixel = int(c*(image.image[i][j][canal])**gamma)
                if pixel < 0:
                    pixel = 0
                elif pixel > 255:
                    pixel = 255
                imagenProcesada.image[i][j][canal] = int(pixel)

    imagenProcesada.image = imagenProcesada.image.astype(np.uint8)
                
    return imagenProcesada

def aplicarKernel(image, kernel):
    """Doc..."""
    pass

def main():
    #Mostrar su implementación aquí
    ajustarGamma(ima)
    pass

if __name__ == '__main__':
    main()

