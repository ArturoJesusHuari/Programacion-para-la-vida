from colorama import Fore
from functions import time
class MMS:
    def __init__(self, lambdaa, mu, s):
        self.lambdaa = lambdaa
        self.mu = mu
        self.s = s
    def factorial(self, n):
        if n==0 or n==1:
            resultado=1
        elif n>1:
            resultado=n*self.factorial(n-1)
        return resultado
    def probabilidadCero(self):
        sumatoria = 0
        for i in range(0,int(self.s)):
            sumatoria += (1/self.factorial(i))*(self.lambdaa/self.mu)**i
        f1 = (1/self.factorial(self.s))*((self.lambdaa/self.mu)**self.s)
        f2 = (self.s*self.mu/(self.s*self.mu-self.lambdaa))
        sumandoDenominador = f1*f2
        self.p0 = 1/(sumatoria+sumandoDenominador)
        text = "La probabilidad de que existan 0 unidad en el sistema es \t"
        nomenclatura = Fore.RED+"(p0): "+Fore.RESET
        return text+nomenclatura+str(round(self.p0,3))
    def promedioClienteCola(self):
        factor = (self.lambdaa*self.mu*(self.lambdaa/self.mu)**self.s)/(self.factorial(self.s-1)*(self.s*self.mu-self.lambdaa)**2)
        self.lq = factor*self.p0
        text = "El número promedio de clientes en la cola \t\t\t"
        nomenclatura = Fore.RED+"(Lq): "+Fore.RESET
        return text+nomenclatura+str(round(self.lq,3))
    def promedioClienteSistema(self):
        self.ls = self.lq + self.lambdaa/self.mu
        text = "El número promedio de clientes en el sistema \t\t\t"
        nomenclatura = Fore.RED+"(Ls): "+Fore.RESET
        return text+nomenclatura+str(self.ls)
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
    def probabilidadOcupado(self):
        self.pw = (1/self.factorial(self.s))*((self.lambdaa/self.mu)**self.s)*(self.s*self.mu/(self.s*self.mu-self.lambdaa))*self.p0
        text = "La probabilidad de que el sistema esté ocupado es \t\t"
        nomenclatura = Fore.RED+"(Pw): "+Fore.RESET
        return text+nomenclatura+str(round(self.pw,3))
    def printDate(self):
        print(self.probabilidadCero())
        print(self.promedioClienteCola())
        print(self.promedioClienteSistema())
        print(self.tiempoPersonaSistema())
        print(self.tiempoPersonaCola())
        print(self.probabilidadOcupado())