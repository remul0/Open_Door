import requests
from flask import Flask, render_template, request
from colorama import Fore, init
import os
from dotenv import load_dotenv
import json

init(autoreset=True)
load_dotenv()

app = Flask(__name__)

# Função para abrir a porta
def abrir_porta(ip, usuario, senha, nome_porta, user_id=1, tipo='Remote'):
    # ... (o resto da função é o mesmo)
    url = f"http://{ip}/cgi-bin/accessControl.cgi?action=openDoor&channel=1&UserID={user_id}&Type={tipo}"
    digest_auth = requests.auth.HTTPDigestAuth(usuario, senha)
    response = requests.get(url, auth=digest_auth, timeout=20, verify=False)

    if response.text.strip() == "OK":
        return f"Porta '{nome_porta}' aberta com sucesso!"
    else:
        return f"Falha ao abrir a porta '{nome_porta}'. Resposta do servidor: {response.text.strip()}"

# Obter o usuário e senha do .env
usuario = os.getenv('USUARIO_DISPOSITIVO')
senha = os.getenv('SENHA_DISPOSITIVO')

# Ler o dicionário de portas do arquivo JSON
with open('portas.json', 'r', encoding='utf-8') as f:
    portas = json.load(f)

# Converte as chaves do dicionário de string para int, já que o request.form retorna strings
portas = {int(k): v for k, v in portas.items()}

# Página inicial
@app.route('/')
def home():
    return render_template('index.html', portas=portas)

# Rota para abrir a porta
@app.route('/abrir_porta', methods=['POST'])
def abrir_porta_web():
    porta_id = int(request.form['porta_id'])
    ip_escolhido = portas[porta_id]['ip']
    nome_porta = portas[porta_id]['nome']
    mensagem = abrir_porta(ip_escolhido, usuario, senha, nome_porta)
    return render_template('index.html', portas=portas, mensagem=mensagem)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
