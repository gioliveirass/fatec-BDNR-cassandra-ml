<h1 align="center"> Manipulação de dados no Cassandra utilizando Python </h1>

<p align="center"> 
<a href="#sobre"> Sobre o projeto </a> • <a href="#tecnologias"> Tecnologias utilizadas </a> • <a href="#comoRodar"> Como rodar o projeto </a>
</p>

## <a id="sobre"> 🎲 Sobre o projeto </a>

Atividade desenvolvida durante a aula de Banco de Dados Não Relacional da Fatec, que consiste em armazenar no Cassandra certos dados armazenados no Redis na [atividade de modelagem com Redis](https://github.com/gioliveirass/fatec-BDNR-redis-ml). Também é válido desenvolver novas funcionalidades.

## <a id="tecnologias"> 🎲 Tecnologias utilizadas </a>

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?&style=for-the-badge&logo=redis&logoColor=white)
![Cassandra](https://img.shields.io/badge/Cassandra-1287B1?style=for-the-badge&logo=apache%20cassandra&logoColor=white)

## <a id="comoRodar"> 🎲 Como rodar o projeto </a>

Antes de tudo, baixe as dependências do projeto com o comando `pip install -r requirements.txt`.

Para autenticar com os bancos de dados utilizados, certifique-se de criar um arquivo config.py dentro da pasta src/ (baseado no arquivo config.example.py já existente) e adicionar os dados corretos dos bancos de dados.

Para autenticar com o Redis também é necessário ter o arquivo .zip do SECURE CONNECT BUNDLE instalado na pasta src/.

Uma vez que os dados estiverem corretos, execute o arquivo `src/main.py`.
