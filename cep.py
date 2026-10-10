import requests

cep = input("Digite seu CEP: ")

url = f"https://viacep.com.br/ws/{cep}/json/"

dados = requests.get(url)
resposta = dados.json()

print(resposta ["logradouro"])

print(f"voce mora na rua {resposta ["logradouro"]}. no bairro {resposta ["bairro"]}. na cidade de {resposta ["localidade"]}")



