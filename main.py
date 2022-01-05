import requests
from buscaEndereco import BuscaEndereco

cep = "66083180"

cep1 = BuscaEndereco(cep)
cidade, estado, bairro, endereco = cep1.acessa_via_api()
print(f"Cidade: {cidade},\nEstado: {estado},\nBairro: {bairro},\nEndereço: {endereco}")



url = "https://ws.apicep.com/cep/{}.json".format(cep)
requisicao = requests.get(url)
dados = requisicao.json()
print(dados)