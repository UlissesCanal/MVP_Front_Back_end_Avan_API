from models.banco import banco

# Classe de modelo para a tabela "Pessoa"
class Pessoa(banco.Model):
    __tablename__ = 'pessoa'
        
    id_pessoa = banco.Column(banco.Integer, primary_key=True)
    nome = banco.Column(banco.String(100))
    tipo_pessoa = banco.Column(banco.String(50))
    cpf_cnpj = banco.Column(banco.String(20))
    data_nascimento = banco.Column(banco.Date)
    estado_civil = banco.Column(banco.String(50))
    endereco = banco.Column(banco.String(200))
    telefone = banco.Column(banco.String(20))
    email = banco.Column(banco.String(100))

    def __init__(self, nome, tipo_pessoa, cpf_cnpj, data_nascimento, estado_civil, endereco, telefone, email):
        self.nome = nome
        self.tipo_pessoa = tipo_pessoa
        self.cpf_cnpj = cpf_cnpj
        self.data_nascimento = data_nascimento
        self.estado_civil = estado_civil
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
