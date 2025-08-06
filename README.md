# Projeto Open Door

Este é um projeto de controle de portas via web, desenvolvido em Python com o framework **Flask**. Ele oferece uma interface segura e intuitiva para abrir portas de dispositivos de rede.

---

### Funcionalidades

* **Interface Web:** Uma página simples e amigável para selecionar e abrir portas.
* **Controle de Dispositivos:** O script se comunica com os dispositivos de rede usando requisições HTTP.
* **Segurança:** Credenciais e dados de portas são armazenados em arquivos locais e **não são enviados para o Git**.

---

### Requisitos

Para rodar o projeto, você precisa ter o **Python 3.x** e as seguintes bibliotecas instaladas.

```bash
pip install Flask requests python-dotenv
Como Rodar o Projeto
1. Configurar o Ambiente
O projeto requer dois arquivos de configuração que devem ser criados localmente, pois não são enviados ao Git.

.env: Crie este arquivo para armazenar suas credenciais.

Snippet de código

USUARIO_DISPOSITIVO=seu_usuario
SENHA_DISPOSITIVO=sua_senha_secreta
portas.json: Crie este arquivo para listar as portas e seus IPs.

JSON

{
    "1": {"nome": "Nome da Porta 1", "ip": "192.168.1.1"},
    "2": {"nome": "Nome da Porta 2", "ip": "192.168.1.2"}
}
2. Iniciar o Servidor
Abra o terminal na pasta do projeto e execute:

Bash

python app.py
3. Acessar a Aplicação
Abra seu navegador e acesse a URL: http://127.0.0.1:5000/.

Estrutura do Projeto
open_door/

static/

aurora.ico

logo.png

templates/

index.html

.env (Ignorado pelo Git)

.gitignore

app.py

portas.json (Ignorado pelo Git)

README.md

Contribuições
Sinta-se à vontade para abrir uma issue ou enviar um pull request.