from colorama import Fore
from functions import time
class MM1:
    def __init__(self, lambdaa, mu):
        self.lambdaa = lambdaa
        self.mu = mu
    def factorDeUtilizacion(self):
        self.p = self.lambdaa/self.mu
        text = "El factor de utilización es: \t\t\t\t\t"
        nomenclatura = Fore.RED+"(p): "+Fore.RESET
        return text+nomenclatura+str(round(self.p,3))
    def promedioClientesSistema(self):
        self.ls = (self.p)/(1-self.p)
        text = "El número promedio de clientes en el sistema \t\t\t"
        nomenclatura = Fore.RED+"(Ls): "+Fore.RESET
        return text+nomenclatura+str(round(self.ls,3))
    def promedioClientesCola(self):
        self.lq = (self.p**2)/(1-self.p)
        text = "El número promedio de clientes en la cola \t\t\t"
        nomenclatura = Fore.RED+"(Lq): "+Fore.RESET
        return text+nomenclatura+str(round(self.lq,3))
    def tiempoPersonaSistema(self):
        self.ws = time(self.ls/self.lambdaa)
        text = "El tiempo promedio que una persona permanece en el sistema es \t"
        nomenclatura = Fore.RED+"(Ws): "+Fore.RESET
        return text+nomenclatura+self.ws
    def tiempoPersonaCola(self):
        self.wq = time(self.lq/self.lambdaa)
        text = "El tiempo promedio que una persona permanece en la cola es \t"
        nomenclatura = Fore.RED+"(Wq): "+Fore.RESET
        return text+nomenclatura+self.wq
    def printDate(self):
        print(self.factorDeUtilizacion())
        print(self.promedioClientesSistema())
        print(self.promedioClientesCola())
        print(self.tiempoPersonaSistema())
        print(self.tiempoPersonaCola())
