import requests

class BuscaEndereco:
    def __init__(self, cep):
        cep = str(cep)
        if self.valida_cep(cep):
            self.cep = cep
        else:
            raise ValueError("O CEP é inválido!!!")

    def __str__(self):
        return (
            self.formata_cep(),
            self.acessa_via_api()
        )

    def valida_cep(self, cep):
        self.cep = cep
        if len(cep) == 8:
            return True
        else:
            return False

    def formata_cep(self):
        return "{}-{}".format(self.cep[:5], self.cep[5:])

    def acessa_via_api(self):
        url = "https://ws.apicep.com/cep/{}.json".format(self.cep)
        requisicao = requests.get(url)
        dados = requisicao.json()
        return (
            dados['city'],
            dados['state'],
            dados['district'],
            dados['address']
        )
