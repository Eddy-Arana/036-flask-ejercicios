# Ejercicio 4 - Formulario GET y POST

# Importar Flask y request
from flask import Flask, request

app = Flask(__name__)

# Ruta principal
@app.route("/", methods=["GET", "POST"])
def inicio():

    # Si el formulario fue enviado
    if request.method == "POST":

        # Obtener el nombre escrito por el usuario
        nombre = request.form["nombre"]

        # Mostrar un mensaje personalizado
        return f"<h2>Hola, {nombre}. Bienvenido a Flask en ¿Qué puedo ayudarte?.</h2>"
    
        # Mostrar el formulario
    return """
    
<h1>Ejercicio 4 Formulario GET y POST</h1>

<form method ="POST">

<label>Nombre:</label><br>

<input type="text" name="nombre" required><br><br>

<input type= "submit" value="Enviar">

</form>
"""

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run(debug=True)
