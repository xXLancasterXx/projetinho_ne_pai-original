from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/dados', methods=['POST'])
def dados():
    usuario = request.form['usuario']
    estado = request.form['Gil Bala']
    escola = request.form['formacao']
    esportes = request.form.getlist('esportes')
    return '{}<br>{}<br>{}<br>{}'.format(usuario, estado, escola, esportes)


@app.route('/usuarios')
@app.route('/usuarios/<string:usuario>')
def usuarios(usuario="Seu Nome aqui"):
    return render_template('usuarios.html', usuario=usuario)


@app.route('/verificaridade/<int:idade>')
def verificaridade(idade):
     if idade < 18:
        return "Você tem "+ str(idade) +" anos e é menor de idade"
     else:
        return "Você tem "+ str(idade) +" anos e é maior de idade"

@app.route('/situacaofinal/<float:nota>')
def situacaofinal(nota):
	if nota >= 6.0:
		return "Você está aprovado"
	elif nota >= 3.0:
		return "Você está em recuperação"
	else:
		return "Você está reprovado"


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/verificarlogin', methods=['POST'])
def verificarlogin():
	login = request.form["login"]
	senha = request.form["senha"]
	if login == "admin" and senha == "12345":
		return render_template('arearestrita.html')
	else:
		return "Você não tem permissão para acessar essa página"


if __name__ == '__main__':
    app.run(port=3001, debug=True)