from flask import Blueprint, jsonify, request
from models.atividade_model import listar_atividades, obter_atividade, criar_atividade, AtividadeNotFound
from clients.professor_service_client import ProfessorServiceClient

atividade_bp = Blueprint('atividade_bp', __name__)

@atividade_bp.route('/', methods=['GET'])
def listar():
    return jsonify(listar_atividades())

@atividade_bp.route('/<int:id_atividade>', methods=['GET'])
def obter(id_atividade):
    try:
        return jsonify(obter_atividade(id_atividade))
    except AtividadeNotFound:
        return jsonify({'erro': 'Atividade não encontrada'}), 404

@atividade_bp.route('/', methods=['POST'])
def criar():
    data = request.get_json()
    if not ProfessorServiceClient.verificar_professor(data.get('id_professor')):
        return jsonify({'erro': 'Professor não encontrado'}), 404
    return jsonify(criar_atividade(data)), 201
