
class BasicPlethy():
    """Recibe la señal de un peltismografo y es capaz de determinar la duracion de la señal,
    frencuencia cardiaca y momentos en que se produce un pico"""
    import matplotlib.pyplot as plt 
    from scipy.signal import find_peaks
    
    def _init_(self, signal:list, fm:float = 125.):
        """Señal"""      
        
        self.signal = signal #señal
        self.fm = fm #frecuencia de muestreo
        self.T = 1/fm
        self.signalDuration = round((len(signal)*self.T)/60,2)
        self.peaks = find_peaks(signal, height=0.45) #encuentra los picos por enciama de la altura mayor a 0.45
        self.numOfpeaks = len(self.peaks[0])
        firstTenseconds = int(10/self.T)
        plt.plot(signal[0:firstTenseconds])
        
    def duration(self):
        """Returna la duración de la señal"""
        return f"Duracion de la señal: %s min" % (self.signalDuration)
    
    def getHR(self)->float:
        """Calcula la frecuencia cardíaca en latidos por minutos (Heart Rate)..."""
        
        heartRate = round(self.numOfpeaks/self.signalDuration,1)
        return f"Frecuencia Cardiaca: %s ppm" % (heartRate)

    def getPeaks(self)->list:
        """Obtiene los momentos en que ocurren los picos en la señal"""
        peaksValue=[]
        for i in range (0,len(self.peaks[0])):
            peaksValue.append(round((self.peaks[0][i])*self.T,1)) 
               
        return f"Momento en el tiempo que se produce cada pico [seg]: %s " % (peaksValue)
 
import os

archivo=open("plethysmography.txt",'r')#abre el archivo 
vector = list(map(float,(archivo.read().split()))) #se asigna el contendio del archivo a una lista de enteros


señal1=BasicPlethy(vector,125.0)

print (señal1.duration())
print (señal1.getHR())
print (señal1.getPeaks())
