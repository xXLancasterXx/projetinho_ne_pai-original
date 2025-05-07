from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<a href=''./contatos''>Hello, World!</a>'


@app.route('/contatos')
def contatos():
    return render_template('contatos.html')


if __name__ == '__main__':
    app.run(port=3001, debug=True)