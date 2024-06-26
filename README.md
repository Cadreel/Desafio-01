# desafio_01

### Documentação do Projeto: Desafio 01
### Descrição
Este projeto consiste em uma aplicação web desenvolvida com Flask, um framework web em Python, para realizar uma pesquisa com clientes da empresa Bem Promotora. A pesquisa coleta informações sobre a faixa etária dos clientes, o convênio, a faixa salarial e o motivo do empréstimo. Os dados são armazenados em um banco de dados SQLite.
### Tecnologias Utilizadas
Python 3.x
Flask
SQLite
O projeto possui os seguintes arquivos e diretórios:
pesquisa.py: Arquivo principal contendo o código da aplicação Flask.
templates/: Diretório contendo os arquivos HTML para as páginas da aplicação.
form.html: Página de formulário para coletar as respostas da pesquisa.
thanks.html: Página de agradecimento exibida após o envio do formulário.
pesquisa.db: Arquivo do banco de dados SQLite onde as respostas da pesquisa são armazenadas.
database.py: Arquivo para criação do banco de dados
### Como Utilizar
Certifique-se de ter o Python 3.x instalado em seu sistema.
Instale o Flask executando o comando pip install Flask.
Baixe os arquivos do projeto para o seu computador.
Abra um terminal e navegue até o diretório onde os arquivos do projeto estão localizados.
Execute o comando python pesquisa.py para iniciar a aplicação Flask.
Abra um navegador web e acesse o endereço http://localhost:5000.
Preencha o formulário com as informações solicitadas e clique em "Enviar".
Após o envio do formulário, você será redirecionado para uma página de agradecimento.
### Observações:
Este projeto utiliza um banco de dados SQLite para armazenar as respostas da pesquisa. O arquivo pesquisa.db será criado automaticamente quando a aplicação for executada pela primeira vez.
Este é um exemplo simples de uma aplicação web utilizando Flask e SQLite. Ele pode ser expandido e customizado conforme necessário.
Caso não haja o diretório ‘templates’, crie-o na pasta raiz ‘.venv’(library root)
Os arquivos serão enviados como arquivos textos comuns.

### Install

$ pip install -r requirements.txt

### Run

$ flask --app pesquisa.py run