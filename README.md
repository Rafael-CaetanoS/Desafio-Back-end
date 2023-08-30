# Desafio Back end

<p>Projeto realizado no dia 06/05</p>
<p>Sistema que permite calcular a média de um produto específico obtido de uma API, além de cadastrar todos os produtos presentes nessa API em um banco de dados. Ao final, o sistema exibe uma mensagem aleatória do Chuck Norris, obtida de outra API.</p>

## Linguagem e banco de dados utilizados
- Python
- mySQL

## Bibliotecas utilizadas
- requests
- pprint
- mysql.connector
 
## Como rodar o projeto
<p>Instalar as bibliotecas requests, pprint e a mysql.connector. </p>
<p> Para rodar o projeto basta baixar os arquivos, importar o banco de dados, abrir a sua IDE e executar o codigo phyton chamando as funçoes mediaCell() e cadastrarNoBanco().</p>
<p> Nessas funções, uma calcula a media de preço dos celulares e a outra cadastra os itens que a api fornece no banco de dados(produtos).</p>
<p>Na parte de conexão com o banco de dados no codigo, voce tera que alterar a senha do banco e usar a senha do banco da sua maquina. </p>
<p> Na funçao de cadastrar produtos, trato uma exceção se o id ja foi cadastrado ou nao.</p>
<p> A chamada dessas funções ja estao no codigo na linha 64 e 65.</p>
