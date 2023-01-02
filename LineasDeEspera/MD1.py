from colorama import Fore
from functions import time
class MD1:
    def __init__(self, lambdaa, mu):
        self.lambdaa = lambdaa
        self.mu = mu
    def longitudCola(self):
        self.lq = (self.lambdaa**2)/(2*self.mu*(self.mu-self.lambdaa))
        text = "La longitud promedio de la cola es \t\t\t\t"
        nomenclatura = Fore.RED+"(Lq): "+Fore.RESET
        return text+nomenclatura+str(round(self.lq,3))
    def tiempoPromedioCola(self):
        self.wq = self.lambdaa/(2*self.mu*(self.mu-self.lambdaa))
        text = "El tiempo de espera en la cola es \t\t\t\t"
        nomenclatura = Fore.RED+"(Wq): "+Fore.RESET
        return text+nomenclatura+str(round(self.wq,3))
    def promedioClientesCola(self):
        self.ls = self.lq+self.lambdaa/self.mu
        text = "Número promedio de clientes en el sistema \t\t\t"
        nomenclatura = Fore.RED+"(Ls): "+Fore.RESET
        return text+nomenclatura+str(round(self.ls,3))
    def promedioEsperaSistema(self):
        self.ws = self.wq+1/self.mu
        text = "Tiempo promedio de espera en el sistema \t\t\t"
        nomenclatura = Fore.RED+"(Ws): "+Fore.RESET
        return text+nomenclatura+str(round(self.ws,3))
    def printDate(self):
        print(self.longitudCola())
        print(self.tiempoPromedioCola())
        print(self.promedioClientesCola())
        print(self.promedioEsperaSistema())