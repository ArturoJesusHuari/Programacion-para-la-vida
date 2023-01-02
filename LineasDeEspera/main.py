from MM1 import MM1
from MMS import MMS
from MD1 import MD1
from functions import banner, opciones, datosMM1, datosMMS, datosMD1, time
from colorama import Fore
def main():
    print(banner())
    print(opciones())
    op = input(Fore.BLUE+"[+]: "+Fore.RESET)
    if (int(op)==1):
        datos = datosMM1()
        sistema = MM1(datos[0],datos[1])
        sistema.printDate()
    elif (int(op)==2):
        datos = datosMMS()
        sistema = MMS(datos[0],datos[1], datos[2])
        sistema.printDate()
    elif (int(op)==3):
        datos = datosMD1()
        sistema = MD1(datos[0],datos[1])
        sistema.printDate()

if __name__ == "__main__":
    main()