import requests
import pprint
import mysql.connector

#api dos produtos
site = requests.get("https://dummyjson.com/products")
#api no formato json
api = site.json()
#tamanho da api
tam = api['limit']

#api do chuck
chucksite = requests.get("https://api.chucknorris.io/jokes/random")
chuck = chucksite.json()

#fazendo conexão com o banco
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    #essa senha que coloquei é so um exemplo, vc vai ter que colocar a sua
    password='1234',
    database='desafio'
)
cursor = conexao.cursor()

#função para calcular a media dos smartphones
def mediaCell():
    total = 0
    media = 0
    qtdTel = 0
    i = 0

    while i < tam:
        if api['products'][i]['category'] == 'smartphones':
            valor = (api['products'][i]['price'])
            total += valor
            qtdTel += 1
        i += 1

    media = total / qtdTel

    print("## Resultado da coleta de dados ##")
    print(f"Preço médio dos smartphones: ${media}\n")

#função para cadastrar os produtos no banco de dados
def cadastrarNoBanco():
    i = 0
    while i < tam:
        id_api = api['products'][i]['id']
        title = (api['products'][i]['title'])
        category = (api['products'][i]['category'])
        price = (api['products'][i]['price'])

        try:
            comando = f'INSERT INTO produtos (id, title, category, price) VALUES ({id_api},"{title}","{category}", {price})'
            cursor.execute(comando)
            conexao.commit()
        except:
            print(f'id {id_api} ja cadastrado')
        i += 1


#chamando funções
mediaCell()
cadastrarNoBanco()
mensagem = chuck['value']

print("***********************************")
print(mensagem)
print("***********************************")

cursor.close()
conexao.close()
