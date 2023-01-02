from colorama import Fore
def banner():
    return """
    ██╗     ██╗███╗   ██╗███████╗ █████╗ ███████╗    ██████╗ ███████╗    ███████╗███████╗██████╗ ███████╗██████╗  █████╗ 
    ██║     ██║████╗  ██║██╔════╝██╔══██╗██╔════╝    ██╔══██╗██╔════╝    ██╔════╝██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗
    ██║     ██║██╔██╗ ██║█████╗  ███████║███████╗    ██║  ██║█████╗      █████╗  ███████╗██████╔╝█████╗  ██████╔╝███████║
    ██║     ██║██║╚██╗██║██╔══╝  ██╔══██║╚════██║    ██║  ██║██╔══╝      ██╔══╝  ╚════██║██╔═══╝ ██╔══╝  ██╔══██╗██╔══██║
    ███████╗██║██║ ╚████║███████╗██║  ██║███████║    ██████╔╝███████╗    ███████╗███████║██║     ███████╗██║  ██║██║  ██║
    ╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚══════╝    ╚═════╝ ╚══════╝    ╚══════╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ 
    """
def opciones():
    return Fore.GREEN+"""\n\n\t1. Modelo M/M/1
    \t2. Modelo M/M/S
    \t3. Modelo M/D/1"""+Fore.RESET
def datosMM1():
    print((Fore.YELLOW+"Ingresa el número promedio de arribos o llegadas por hora"+Fore.RESET))
    lambdaa = input(Fore.BLUE+"[lambda]: "+Fore.RESET)
    print((Fore.YELLOW+"Ingresa el número promedio de clientes servidos por hora"+Fore.RESET))
    mu = input(Fore.BLUE+"[mu]: "+Fore.RESET)
    return float(lambdaa), float(mu)
def datosMMS():
    print((Fore.YELLOW+"Ingresa el número promedio de arribos o llegadas por hora"+Fore.RESET))
    lambdaa = input(Fore.BLUE+"[lambda]: "+Fore.RESET)
    print((Fore.YELLOW+"Ingresa el número promedio de clientes servidos por hora"+Fore.RESET))
    mu = input(Fore.BLUE+"[mu]: "+Fore.RESET)
    print((Fore.YELLOW+"Ingresa el número servidores"+Fore.RESET))
    s = input(Fore.BLUE+"[mu]: "+Fore.RESET)
    return float(lambdaa), float(mu), float(s)
def datosMD1():
    print((Fore.YELLOW+"Ingresa el número promedio de arribos o llegadas por hora"+Fore.RESET))
    lambdaa = input(Fore.BLUE+"[lambda]: "+Fore.RESET)
    print((Fore.YELLOW+"Ingresa el número promedio de clientes servidos por hora"+Fore.RESET))
    mu = input(Fore.BLUE+"[mu]: "+Fore.RESET)
    return float(lambdaa), float(mu)
def time(_time):
    if (_time%1!=0):
        minutos=_time%1
        minutos*=60
        _time=int(_time)
        if (minutos%1!=0):
            segundos=(minutos%1)*60
            minutos=int(minutos)
            return str(round(_time,3)) + " h "+str(round(minutos,3))+" min "+str(round(segundos,3))+" s"
        else:
            return str(round(_time,3)) + " h "+str(round(minutos,3))+" min "
    return str(round(_time,3))