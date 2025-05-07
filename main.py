from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<a href=''./alunos''>Hello, World!</a>'


@app.route('/alunos')
def alunos():
    return '<p>Alunos</p>'


if __name__ == '__main__':
    # Run the Flask app on port 3001
    app.run(port=3001, debug=True)