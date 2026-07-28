# Ejercicio 3 - Parámetro en la URL

# Importar la clase Flask
from flask import Flask

# Crear la aplicación Flask
app = Flask(__name__)


# Ruta principal
@app.route("/")
def inicio():
    return "<h1>Ejercicio 3 - Parámetro en la URL</h1>"


# Ruta con parámetro

# Recibe el nombre escrito en la URL.

# Ejemplo:
# http://127.0.0.1:5000/estudiante/Eddy
@app.route("/estudiante/<nombre>")
def estudiante(nombre):
    return f"<h2>Hola, {nombre}. Bienvenido a Flask.</h2>"

# Ejecutar la aplicación

if __name__ == "__main__":
    app.run(debug=True)