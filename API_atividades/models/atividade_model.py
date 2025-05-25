from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Atividade(db.Model):
    id_atividade = db.Column(db.Integer, primary_key=True)
    id_professor = db.Column(db.Integer, nullable=False)
    enunciado = db.Column(db.String(255), nullable=False)
    resposta = db.Column(db.String(255), nullable=True)

def listar_atividades():
    return [a.serialize() for a in Atividade.query.all()]

def obter_atividade(id_atividade):
    atividade = Atividade.query.get(id_atividade)
    if not atividade:
        raise AtividadeNotFound()
    return atividade.serialize()

def criar_atividade(data):
    nova = Atividade(**data)
    db.session.add(nova)
    db.session.commit()
    return nova.serialize()

class AtividadeNotFound(Exception):
    pass

def serialize(self):
    return {
        'id_atividade': self.id_atividade,
        'id_professor': self.id_professor,
        'enunciado': self.enunciado,
        'resposta': self.resposta
    }

Atividade.serialize = serialize
