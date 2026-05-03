print("Controle de níveis de água 💧")

from colorama import Fore, Style, init

# Inicializa o colorama
init(autoreset=True)

# Lista com os níveis
niveis = [
    "Nível 1 - Muito baixo (crítico)  💧 ",
    "Nível 2 - Baixo 💧 💧 ",
    "Nível 3 - Médio  💧 💧 💧 ",
    "Nível 4 - Alto  💧 💧 💧 💧 ",
    "Nível 5 - Muito alto (alerta)  💧 💧 💧 💧 💧"
]

# Função para definir a cor
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED # Vermelho
    elif nivel == 2:
        return Fore.YELLOW  # Amarelo
    elif nivel == 3:
        return Fore.GREEN  # Verde
    elif nivel == 4:
        return Fore.CYAN  # Ciano
    elif nivel == 5:
        return Fore.BLUE  # Azul
    else:
        return Fore.WHITE

#  Entrada do usuário
nivel_atual = int(input("Digite o nível do reservatório (1 a 5): "))

# Verificação para evitar erro
if 1 <= nivel_atual <= 5:
    cor = definir_cor(nivel_atual)
    mensagem = niveis[nivel_atual - 1]

    print("\nSituação do reservatório:")
    print(cor + mensagem + Style.RESET_ALL)
else:
    print("⚠️ Nível inválido! Digite um número de 1 a 5.")
