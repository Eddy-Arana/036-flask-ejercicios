# =====================================================
# Ejercicio 5 - Plantilla con Jinja2
# =====================================================

# Importar Flask y render_template
from flask import Flask, render_template

# Crear la aplicación Flask
app = Flask(__name__)


# -----------------------------------------------------
# Ruta principal
# -----------------------------------------------------
# Muestra una plantilla HTML y envía una variable
# llamada mensaje.
@app.route("/")
def inicio():

    mensaje = "Bienvenido a Flask usando Jinja2"

    return render_template("inicio.html", mensaje=mensaje)


# -----------------------------------------------------
# Ejecutar la aplicación
# -----------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)