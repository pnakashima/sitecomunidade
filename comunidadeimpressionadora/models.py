from comunidadeimpressionadora import database, login_manager   # como estao dentro do __init__ só precisa colocar o nome da pasta, comunidadeimpressionadora
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))   # como id é a chave primária, podemos usar o get


class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    foto_perfil = database.Column(database.String, default='default.jpg')
    cursos = database.Column(database.String, nullable=False, default='Não informado')
    posts = database.relationship('Post', backref='autor', lazy=True)

    def contar_posts(self):
        return len(self.posts)

class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    titulo = database.Column(database.String, nullable=False)
    corpo = database.Column(database.Text, nullable=False)
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)  # ATENÇÃO! utcnow sem (), pq senao todos os posts vão ficar com o mesmo horário
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)  # ATENÇÃO! se passar Usuario.id dá pau, tem q ser minúsculo

