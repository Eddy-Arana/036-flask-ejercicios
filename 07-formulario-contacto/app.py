# Ejercicio 7 - Formulario de Contacto
# =====================================================

# Importar Flask, request y render_template
from flask import Flask, request, render_template

# Crear la aplicación Flask
app = Flask(__name__)


# Ruta de contacto
# -----------------------------------------------------
# GET:
# Muestra el formulario.
#
# POST:
# Recibe los datos enviados por el usuario y
# muestra una página de agradecimiento.
@app.route("/contacto", methods=["GET", "POST"])

def contacto():

    # Verificar si el formulario fue enviado
    if request.method == "POST":

        # Obtener los datos del formulario
        nombre = request.form["nombre"]
        mensaje = request.form["mensaje"]

        # Mostrar la página de agradecimiento
        return render_template(
            "gracias.html",
            nombre=nombre,
            mensaje=mensaje
        )

    # Mostrar el formulario
    return render_template("contacto.html")


# Ejecutar la aplicación
# -----------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)