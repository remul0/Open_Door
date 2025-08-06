Projeto Open Door

Este é um projeto de controle de portas via web, desenvolvido em Python com o framework Flask. Ele oferece uma interface simples e segura para abrir portas de dispositivos de rede.

Funcionalidades
Interface Web: Uma interface web simples para selecionar e abrir portas usando leitor facial intelbras.

Controle de Dispositivos: O script se comunica com os dispositivos de rede usando requisições HTTP.

Segurança: As informações de login e a lista de portas são armazenadas em arquivos de configuração locais e não são versionadas no Git.

Requisitos
Para rodar este projeto, você precisa ter o Python 3.x e as seguintes bibliotecas instaladas:

Bash

pip install Flask requests python-dotenv
Como Rodar o Projeto
Configurar o Ambiente

O projeto requer dois arquivos de configuração que não devem ser enviados ao Git. Crie-os na pasta principal do seu projeto (open_door):

.env: Crie este arquivo para armazenar suas credenciais.

Snippet de código

USUARIO_DISPOSITIVO=seu_usuario
SENHA_DISPOSITIVO=sua_senha_secreta
portas.json: Crie este arquivo para listar as portas e seus IPs. Substitua os exemplos pelas suas informações reais.

JSON

{
    "1": {"nome": "Nome da Porta 1", "ip": "192.168.1.1"},
    "2": {"nome": "Nome da Porta 2", "ip": "192.168.1.2"}
}
Iniciar o Servidor

Abra o terminal na pasta do projeto e execute o seguinte comando:

Bash

python app.py
Acessar a Aplicação

Abra seu navegador e acesse a URL: http://127.0.0.1:5000/.

Estrutura do Projeto
open_door/
├── static/
│   ├── logo.ico
│   └── logo.png
├── templates/
│   └── index.html
├── .env           <- Arquivo de credenciais (IGNORADO PELO GIT)
├── .gitignore
├── app.py         <- Lógica principal e servidor Flask
├── portas.json    <- Lista de portas (IGNORADO PELO GIT)
└── README.md

Contribuições
Sinta-se à vontade para abrir uma issue para reportar bugs ou enviar um pull request para sugerir melhorias.