# Ejercicio 6 - Archivo estático (CSS)
# =====================================================

# Importar Flask, render_template y url_for
from flask import Flask, render_template

# Crear la aplicación Flask
app = Flask(__name__)


# Ruta principal
# -----------------------------------------------------
# Muestra una página HTML utilizando una plantilla
# y un archivo CSS almacenado en la carpeta static.
@app.route("/")
def inicio():

    titulo = "Archivo estático con CSS"
    mensaje = "Bienvenido a Flask utilizando archivos estáticos."

    return render_template(
        "inicio.html",
        titulo=titulo,
        mensaje=mensaje
    )


# Ejecutar la aplicación
# -----------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)