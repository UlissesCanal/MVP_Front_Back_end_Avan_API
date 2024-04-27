from flask import Flask,jsonify
from flask_restful import Api
from service.service_cep import CepService
from resources.pessoa import PessoasResource, PessoaResource
from models.banco import banco
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pessoas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
CORS(app)

banco.init_app(app)

# Registre os recursos da API
api.add_resource(PessoasResource, '/pessoas')
api.add_resource(PessoaResource, '/pessoa/<int:pessoa_id>')

@app.route('/endereco/<cep>', methods=['GET'])
def obter_endereco_por_cep(cep):
    endereco = CepService.buscar_endereco_por_cep(cep)
    if endereco:
        return jsonify(endereco), 200
    else:
        return jsonify({"mensagem": "CEP não encontrado"}), 404


if __name__ == '__main__':
    with app.app_context():
        banco.create_all()
    app.run()
