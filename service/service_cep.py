import requests

class CepService:
    @staticmethod
    def buscar_endereco_por_cep(cep):
        url = f"https://viacep.com.br/ws/{cep}/json/"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                endereco = {
                    "cep": data.get("cep"),
                    "logradouro": data.get("logradouro"),
                    "complemento": data.get("complemento"),
                    "bairro": data.get("bairro"),
                    "localidade": data.get("localidade"),
                    "uf": data.get("uf"),
                    "ibge": data.get("ibge"),
                    "gia": data.get("gia"),
                    "ddd": data.get("ddd"),
                    "siafi": data.get("siafi")
                }
                return endereco
            else:
                return None
        except Exception as e:
            print("Erro ao buscar endereço:", e)
            return None
