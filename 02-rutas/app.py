from flask import Flask

app = Flask(__name__)


@app.route("/")
def inicio():
    return "<h1>Bienvenido a mi aplicación Flask</h1>"


@app.route("/contacto")
def contacto():
    return "<h2>Página de contacto</h2>"


@app.route("/cursos")
def cursos():
    return "<h3>Lista de cursos</h3>"


if __name__ == "__main__":
    app.run(debug=True)