# Importe o Float para o salário
from sqlalchemy import create_engine, String, Integer, func, Column, DateTime, Float
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# Base de dados
engine = create_engine('mysql+pymysql://root:senaisp@localhost:3306/empresa_db')
db_session = scoped_session(sessionmaker(bind=engine))
base = declarative_base()
base.query = db_session.query_property()


class Funcionario(base, UserMixin):
    __tablename__ = 'funcionarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    data_nascimento = Column(DateTime(), nullable=False)
    cpf = Column(String(14), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    senha_hash = Column(String(255), nullable=False)  # Aumentado para o hash
    cargo = Column(String(50), nullable=False)
    salario = Column(Float(), nullable=False)
    papel = Column(String(20), default='usuario')  # Adicionado para o admin_required

    # MANTENDO SUA LÓGICA DE MÉTODO
    def set_password(self, senha):
        self.senha_hash = generate_password_hash(senha)

    def check_password(self, senha):
        return check_password_hash(self.senha_hash, senha)

    def serialize(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "papel": self.papel,
        }


class Usuario(base, UserMixin):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    senha_hash = Column(String(255), nullable=False)
    papel = Column(String(20), default='usuario')  # Adicionado para o admin_required

    # MANTENDO SUA LÓGICA DE MÉTODO
    def set_password(self, senha):
        self.senha_hash = generate_password_hash(senha)

    def check_password(self, senha):
        return check_password_hash(self.senha_hash, senha)

    def serialize(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "papel": self.papel,
        }


# Garante a criação das tabelas
base.metadata.create_all(engine)
