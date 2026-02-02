from flask import Flask, render_template, request

app = Flask(__name__)

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

@app.route('/somar', methods=['GET', 'POST'])
def somar():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            soma = n1 + n2
            return render_template("operacoes.html", n1=n1, n2=n2, soma=soma)

    return render_template("operacoes.html")

@app.route('/subtrair', methods=['GET', 'POST'])
def subtrair():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            subtracao = n1 - n2
            return render_template("operacoes.html", n1=n1, n2=n2, subtracao=subtracao)

    return render_template("operacoes.html")

@app.route('/multiplicar', methods=['GET', 'POST'])
def multiplicar():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            multiplicacao = n1 * n2
            return render_template("operacoes.html", n1=n1, n2=n2, multiplicacao=multiplicacao)

    return render_template("operacoes.html")

@app.route('/dividir', methods=['GET', 'POST'])
def dividir():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            divisao = n1 / n2
            return render_template("operacoes.html", n1=n1, n2=n2, divisao=divisao)

    return render_template("operacoes.html")

@app.route('/area', methods=['GET', 'POST'])
def area():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            n3 = int(request.form['form-n3'])
            vez = n1 * n2 / n3
            return render_template("geometria.html", n1=n1, n2=n2, vez=vez)

    return render_template("geometria.html")

@app.route('/perimetro_triangulo', methods=['GET', 'POST'])
def perimetro_triangulo():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2'] and request.form['form-n3']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            n3 = int(request.form['form-n3'])
            pt = n1 + n2 + n3
            return render_template("geometria.html", n1=n1, n2=n2, n3=n3, pt=pt)
        return render_template("geometria.html")

@app.route('/area_circulo', methods=['GET', 'POST'])
def area_circulo():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2'] and request.form['form-n3']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            n3 = int(request.form['form-n3'])
            arc = n1 + n2 + n3
            return render_template("geometria.html", n1=n1, n2=n2, n3=n3, arc=arc)
        return render_template("geometria.html")

@app.route('/perimetro_circulo', methods=['GET', 'POST'])
def perimetro_circulo():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2'] and request.form['form-n3']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            n3 = int(request.form['form-n3'])
            cr = n1 + n2 + n3
            return render_template("geometria.html", n1=n1, n2=n2, n3=n3, cr=cr)
        return render_template("geometria.html")


@app.route('/area_quadrado', methods=['GET', 'POST'])
def area_quadrado():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2'] and request.form['form-n3']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            n3 = int(request.form['form-n3'])
            qd = n1 + n2 + n3
            return render_template("geometria.html", n1=n1, n2=n2, n3=n3, qd=qd)
        return render_template("geometria.html")

@app.route('/perimetro_quadrado', methods=['GET', 'POST'])
def perimetro_quadrado():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2'] and request.form['form-n3']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            n3 = int(request.form['form-n3'])
            pl = n1 + n2 + n3
            return render_template("geometria.html", n1=n1, n2=n2, n3=n3, pl=pl)
        return render_template("geometria.html")




if __name__ == '__main__':
    app.run(debug=True)