from flask_restful import Resource, reqparse
from models.banco import banco
from models.pessoa import Pessoa
from datetime import datetime
from flask import request

class PessoasResource(Resource):
    def get(self):
        pessoas = Pessoa.query.all()
        response = []
        for pessoa in pessoas:
            response.append({
                'id_pessoa': pessoa.id_pessoa,
                'nome': pessoa.nome,
                'tipo_pessoa': pessoa.tipo_pessoa,
                'cpf_cnpj': pessoa.cpf_cnpj,
                'data_nascimento': str(pessoa.data_nascimento),
                'estado_civil': pessoa.estado_civil,
                'endereco': pessoa.endereco,
                'telefone': pessoa.telefone,
                'email': pessoa.email
            })
        return {"pessoas": response}, 200

class PessoaResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('nome', type=str, required=True)
    parser.add_argument('tipo_pessoa', type=str, required=True)
    parser.add_argument('cpf_cnpj', type=str, required=True)
    parser.add_argument('data_nascimento', type=str, required=True)
    parser.add_argument('estado_civil', type=str, required=True)
    parser.add_argument('endereco', type=str, required=True)
    parser.add_argument('telefone', type=str, required=True)
    parser.add_argument('email', type=str, required=True)
   
    def get(self, pessoa_id):
       pessoa = Pessoa.query.get(pessoa_id)
       if pessoa:
            return {
                'id_pessoa': pessoa.id_pessoa,
                'nome': pessoa.nome,
                'tipo_pessoa': pessoa.tipo_pessoa,
                'cpf_cnpj': pessoa.cpf_cnpj,
                'data_nascimento': str(pessoa.data_nascimento),
                'estado_civil': pessoa.estado_civil,
                'endereco': pessoa.endereco,
                'telefone': pessoa.telefone,
                'email': pessoa.email
            }, 200
       return {'message': 'Pessoa não encontrada'}, 404
  
    def delete(self, pessoa_id):
        pessoa = Pessoa.query.get(pessoa_id)
        if pessoa:
            banco.session.delete(pessoa)
            banco.session.commit()
            return {'message': 'Pessoa excluída com sucesso'}
        return {'message': 'Pessoa não encontrada'}, 404
    
    def put(self, pessoa_id):
        args = PessoaResource.parser.parse_args()
        #busca pessoa na base de dados 
        pessoa = Pessoa.query.get(pessoa_id)
        if not pessoa:
            return {'message': 'Pessoa não encontrada'}, 404

        pessoa.nome = args['nome']
        pessoa.tipo_pessoa = args['tipo_pessoa']
        pessoa.cpf_cnpj = args['cpf_cnpj']
        pessoa.data_nascimento = datetime.strptime(args['data_nascimento'], '%Y-%m-%d').date()
        pessoa.estado_civil = args['estado_civil']
        pessoa.endereco = args['endereco']
        pessoa.telefone = args['telefone']
        pessoa.email = args['email']
        banco.session.commit()
        return {
                'id_pessoa': pessoa.id_pessoa,
                'nome': pessoa.nome,
                'tipo_pessoa': pessoa.tipo_pessoa,
                'cpf_cnpj': pessoa.cpf_cnpj,
                'data_nascimento': str(pessoa.data_nascimento),
                'estado_civil': pessoa.estado_civil,
                'endereco': pessoa.endereco,
                'telefone': pessoa.telefone,
                'email': pessoa.email
            }, 200
    
    def post(self,pessoa_id):
        args = PessoaResource.parser.parse_args()
        nome = args['nome']
        tipo_pessoa = args['tipo_pessoa']
        cpf_cnpj = args['cpf_cnpj']
        data_nascimento = datetime.strptime(args['data_nascimento'], '%Y-%m-%d').date()
        estado_civil = args['estado_civil']
        endereco = args['endereco']
        telefone = args['telefone']
        email = args['email']
        pessoa = Pessoa(nome=nome, tipo_pessoa=tipo_pessoa, cpf_cnpj=cpf_cnpj, data_nascimento=data_nascimento,estado_civil=estado_civil, endereco=endereco, telefone=telefone, email=email)

        #busca pessoa na base de dados 
        if Pessoa.query.filter_by(cpf_cnpj=pessoa.cpf_cnpj).first():
            return {'message': 'Pessoa já existe na base de dados'}, 409
        banco.session.add(pessoa)
        banco.session.commit()
        return {
                'id_pessoa': pessoa.id_pessoa,
                'nome': pessoa.nome,
                'tipo_pessoa': pessoa.tipo_pessoa,
                'cpf_cnpj': pessoa.cpf_cnpj,
                'data_nascimento': str(pessoa.data_nascimento),
                'estado_civil': pessoa.estado_civil,
                'endereco': pessoa.endereco,
                'telefone': pessoa.telefone,
                'email': pessoa.email
            }, 201        
