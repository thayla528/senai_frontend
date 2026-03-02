import math

from datetime import datetime

from flask import Flask, render_template, url_for, flash, redirect, request
from sqlalchemy.exc import SQLAlchemyError

from database import db_session, Funcionario, Usuario

from sqlalchemy import select, and_, func
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
app = Flask(__name__)
app.config['SECRET_KEY'] = '2'

# Adicione estas linhas:
login_manager = LoginManager()
login_manager.init_app(app)
# em qual lugar vou autenticar
login_manager.login_view = 'login'

#se na tiver logado joga para a tela de login

@app.route('/cadastrar_funcionario', methods=['POST'])
@login_required
def cadastrar_funcionario():
    nome = request.form.get('nome')
    data_nasc = request.form.get('data_nascimento')
    cpf = request.form.get('cpf')
    email = request.form.get('email')
    senha = request.form.get('senha')
    cargo = request.form.get('cargo')
    salario = request.form.get('salario')

    novo_f = Funcionario(nome=nome, data_nascimento=data_nasc, cpf=cpf, email=email, senha=senha, cargo=cargo,
                         salario=salario)

    try:
        db_session.add(novo_f)
        db_session.commit()
        flash("Funcionário cadastrado!", "success")
    except Exception as e:
        db_session.rollback()
        flash("Erro ao salvar no banco", "danger")

    return redirect(url_for('funcionarios'))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você saiu do sistema!', 'info')
    return redirect(url_for('login'))

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@login_manager.user_loader
def load_user(user_id):
    # Remova o .first()
    user = select(Usuario).where(Usuario.id == int(user_id))
    return db_session.execute(user).scalar_one_or_none()



@app.route('/')
def home():
    return render_template("home.html")

@app.route('/calculos')
def calculos():
    return render_template("calculos.html")

@app.route('/operacoes')
def operacoes():
    return render_template("operacoes.html")

@app.route('/geometria')
def geometria():
    return render_template("geometria.html")


@app.route('/funcionarios')
@login_required
def funcionarios():
    # Busca todos os registros da tabela 'funcionarios'
    query = select(Funcionario)
    lista = db_session.execute(query).scalars().all()

    # Envia a lista para o HTML através da variável 'funcionarios'
    return render_template("funcionarios.html", funcionarios=lista)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('form-email')
        senha = request.form.get('form-senha')
        if not email or not senha:
            flash('Por favor preencher os campos!', 'danger')
            return render_template('login.html')

        if email and senha:
            verificar_email = select(Usuario).where(Usuario.email == email)
            resultado_email = db_session.execute(verificar_email).scalar_one_or_none()
            if resultado_email:
                # se encontrado
                if resultado_email.check_password(senha):
                    # login correto
                    login_user(resultado_email)
                    flash(f'Login Sucesso!', 'success')
                    # chama a função
                    return redirect(url_for('home'))
                else:
                    #  senha invalida
                    flash(f'Senha incorreta!', 'danger')
                    return render_template('login.html')

            else:
                flash('Email não encontrado!', 'danger')
                # chama o html
                return render_template('login.html')
    else:
        return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro_usuario():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        if not nome or not email or not senha:
            flash('Por favor preencher os campos!', 'danger')
            return render_template('cadastro.html')
        verificar_email = select(Usuario).where(Usuario.email == email)
        exists_email = db_session.execute(verificar_email).scalar_one_or_none()
        if exists_email:
            flash(f'Email {email} já cadastrado! ', 'danger')
            return render_template('cadastro.html')
        try:
            novo_usuario = Usuario(nome=nome, email=email)
            novo_usuario.set_password(senha)
            db_session.add(novo_usuario)
            db_session.commit()
            flash(f'Usuario{nome} cadastrado com sucesso!', 'success')
            return redirect(url_for('login'))
        except SQLAlchemyError as e:
            flash(f'erro na base de dados: ', 'danger')
            print(f"Erro na base de dados: ", )
            return redirect(url_for('login'))
        except Exception as e:
            flash(f'erro ao cadastrar: ', 'danger')
            print(f"Erro ao cadastrar: ", )
            return redirect(url_for('cadastro_usuario'))
    return render_template('cadastro.html')

@app.route('/somar', methods=['GET', 'POST'])
def somar():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            soma = n1 + n2
            flash("Campo preenchido com sucesso", 'alert-success')
            return render_template("operacoes.html", n1=n1, n2=n2, soma=soma)
        else :
            # passo 1 : emetir a mensagem e a categoria do flash
            flash("Preencha o campo", 'alert-danger')

    return render_template("operacoes.html")

@app.route('/subtrair', methods=['GET', 'POST'])
def subtrair():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            subtracao = n1 - n2
            flash("Campo preenchido com sucesso", 'alert-success')
            return render_template("operacoes.html", n1=n1, n2=n2, subtracao=subtracao)
        else :
            # passo 1 : emetir a mensagem e a categoria do flash
            flash("Preencha o campo", 'alert-danger')


    return render_template("operacoes.html")

@app.route('/multiplicar', methods=['GET', 'POST'])
def multiplicar():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            multiplicacao = n1 * n2
            flash("Campo preenchido com sucesso", 'alert-success')
            return render_template("operacoes.html", n1=n1, n2=n2, multiplicacao=multiplicacao)
        else :
            # passo 1 : emetir a mensagem e a categoria do flash
            flash("Preencha o campo", 'alert-danger')


    return render_template("operacoes.html")

@app.route('/dividir', methods=['GET', 'POST'])
def dividir():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            divisao = n1 / n2
            flash("Campo preenchido com sucesso", 'alert-success')
            return render_template("operacoes.html", n1=n1, n2=n2, divisao=divisao)
        else :
            # passo 1 : emetir a mensagem e a categoria do flash
            flash("Preencha o campo", 'alert-danger')


    return render_template("operacoes.html")

# TRIÂNGULO
@app.route('/area', methods=['GET','POST'])
def area():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = float(request.form['form-n1'])
            vez = (n1 * n1) / 2
            flash("Campo preenchido com sucesso", 'alert-success')
            return render_template("geometria.html", n1=n1, vez=vez)
        else :
            # passo 1 : emetir a mensagem e a categoria do flash
            flash("Preencha o campo", 'alert-danger')

    return render_template("geometria.html")



@app.route('/perimetro_triangulo', methods=['GET','POST'])
def perimetro_triangulo():
    if request.method == 'POST':
        if request.form['form-n1'] :
            n1 = float(request.form['form-n1'])
            pt = 3 * n1
            flash("Campo preenchido com sucesso", 'alert-success')
            return render_template("geometria.html", n1=n1, pt=pt)
        else:
            # passo 1 : emetir a mensagem e a categoria do flash
            flash("Preencha o campo", 'alert-danger')

    return render_template("geometria.html")



# CÍRCULO
@app.route('/area_circulo', methods=['GET', 'POST'])
def area_circulo():
    if request.method == 'POST':
        if request.form['form-n1'] :
            n1 = float(request.form['form-n1'])
            arc = math.pi * (n1 ** 2)
            flash("Subtração realizada", 'alert-success')
            return render_template("geometria.html", n1=n1, arc=arc)
        else :
            # passo 1 : emetir a mensagem e a categoria do flash
            flash("Preencha o campo", 'alert-danger')
    return render_template("geometria.html")
@app.route('/perimetro_circulo', methods=['GET', 'POST'])
def perimetro_circulo():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = float(request.form['form-n1'])
            cr = 2 * math.pi * n1
            flash("Campo preenchido com sucesso", 'alert-success')
            return render_template("geometria.html", n1=n1, cr=cr)
        else:
            # passo 1 : emetir a mensagem e a categoria do flash
            flash("Preencha o campo", 'alert-danger')

    return render_template("geometria.html")

# QUADRADO
@app.route('/area_quadrado', methods=['GET', 'POST'])
def area_quadrado():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = float(request.form['form-n1'])
            qd = n1 * n1
            flash("Campo preenchido com sucesso", 'alert-success')
            return render_template("geometria.html", n1=n1, qd=qd)

        else:
            # passo 1 : emetir a mensagem e a categoria do flash
            flash("Preencha o campo", 'alert-danger')

    return render_template("geometria.html")
@app.route('/perimetro_quadrado', methods=['GET', 'POST'])
def perimetro_quadrado():
    if request.method == 'POST':
        if request.form['form-n1'] :
            n1 = float(request.form['form-n1'])
            pl = 4 * n1
            flash("Campo preenchido com sucesso", 'alert-success')
            return render_template("geometria.html", n1=n1, pl=pl)

        else:
            # passo 1 : emetir a mensagem e a categoria do flash
            flash("Preencha o campo", 'alert-danger')

    return render_template("geometria.html")



# HEXÁGONO
@app.route('/area_hexagono', methods=['GET', 'POST'])
def area_hexagono():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = float(request.form['form-n1'])
            ah = (3 * math.sqrt(3) / 2) * (n1 ** 2)
            flash("Campo preenchido com sucesso", 'alert-success')
            return render_template("geometria.html", n1=n1, ah=ah)
        else :
            # passo 1 : emetir a mensagem e a categoria do flash
            flash("Preencha o campo", 'alert-danger')

    return render_template("geometria.html")

@app.route('/perimetro_hexagono', methods=['POST'])
def perimetro_hexagono():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = float(request.form['form-n1'])
            ph = 6 * n1
            flash("Campo preenchido com sucesso", 'alert-success')
            return render_template("geometria.html", n1=n1, ph=ph)

        else :
            # passo 1 : emetir a mensagem e a categoria do flash
            flash("Preencha o campo", 'alert-danger')

    return render_template("geometria.html")


if __name__ == '__main__':
    app.run(debug=True)