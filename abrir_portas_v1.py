# abrir_portas_v1.py

import requests
from colorama import Fore, init
import os
from dotenv import load_dotenv
import json

load_dotenv()
init(autoreset=True)

# Função para abrir a porta
def abrir_porta(ip, usuario, senha, nome_porta, user_id=1, tipo='Remote'):
    url = f"http://{ip}/cgi-bin/accessControl.cgi?action=openDoor&channel=1&UserID={user_id}&Type={tipo}"
    digest_auth = requests.auth.HTTPDigestAuth(usuario, senha)
    response = requests.get(url, auth=digest_auth, timeout=20, verify=False)
    if response.text.strip() == "OK":
        print(Fore.GREEN + f"Porta '{nome_porta}' aberta com sucesso!")
    else:
        print(Fore.RED + f"Falha ao abrir a porta '{nome_porta}'. Resposta do servidor: {response.text.strip()}")

# Obter o usuário e senha do .env
usuario = os.getenv('USUARIO_DISPOSITIVO')
senha = os.getenv('SENHA_DISPOSITIVO')

# Lê o dicionário de portas do arquivo JSON
with open('portas.json', 'r', encoding='utf-8') as f:
    portas_data = json.load(f)
portas = {k: v for k, v in portas_data.items()}

def exibir_menu():
    print(Fore.YELLOW + "=" * 60)
    print(Fore.CYAN + "Escolha uma porta para abrir?".center(60))
    print(Fore.YELLOW + "=" * 60)
    max_length = max(len(info['nome']) for info in portas.values())
    for i, info in portas.items():
        opcao_str = f"{i}. {info['nome']}"
        print(Fore.MAGENTA + opcao_str.center(60))
    print(Fore.YELLOW + "=" * 60)

# Exibe o menu para o usuário
exibir_menu()

# Solicita ao usuário que escolha uma porta
opcao_str = input(Fore.WHITE + "Digite o número da porta que deseja abrir: ")

# Verifica se a opção escolhida é válida
if opcao_str in portas:
    ip_escolhido = portas[opcao_str]['ip']
    nome_porta = portas[opcao_str]['nome']
    abrir_porta(ip_escolhido, usuario, senha, nome_porta)
else:
    print(Fore.RED + "Opção inválida! Tente novamente.")
