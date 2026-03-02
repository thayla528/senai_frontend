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
    senha = Column(String(255), nullable=False) # Hash Werkzeug
    cargo = Column(String(50), nullable=False)
    salario = Column(Float(), nullable=False) # Agora com Float importado

    def __repr__(self):
        return f'<Funcionarios {self.nome}>'

    def set_password(self, password):
        self.senha = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.senha, password)

    def save(self): # Removi a necessidade de passar db_session se ele já for global
        try:
            db_session.add(self)
            db_session.commit()
        except SQLAlchemyError:
            db_session.rollback()
            raise

class Usuario(base, UserMixin):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)  # Adicione (100)
    senha = Column(String(255), nullable=False) # Hash Werkzeug
    email = Column(String(100), nullable=False, unique=True) # Adicione (100)


    def __repr__(self):
        return f'<Usuario {self.nome}>'

    def set_password(self, password):
        self.senha = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.senha, password)

    def save(self):  # Removi a necessidade de passar db_session se ele já for global
        try:
            db_session.add(self)
            db_session.commit()
        except SQLAlchemyError:
            db_session.rollback()
            raise
