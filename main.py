from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/usuarios')
@app.route('/usuarios/<string:usuario>')
def usuarios(usuario="Seu Nome aqui"):
    return render_template('usuarios.html', usuario=usuario)






if __name__ == '__main__':
    app.run(port=3001, debug=True)