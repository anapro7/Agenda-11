from colorama import Fore, Style, init
init(autoreset=True)

#Lista com os níveis do reservatório
niveis = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]

#Função para definir cor de cada nível
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel ==2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

#Simulação dos níveis do reservatório
for nivel_atual in range(1,len(niveis) + 1):
    cor = definir_cor(nivel_atual)
    mensagem = niveis[nivel_atual - 1]

    print(cor + f"Nivel {nivel_atual}: {mensagem}")
    print(Style.RESET_ALL)

    