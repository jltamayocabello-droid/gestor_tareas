from flask import Flask, redirect, render_template, request, url_for

from tareas import agregar_tarea, completar_tarea, tareas

# Instancia principal de la aplicación web.
app = Flask(__name__)


@app.route("/")
def index():
    """Muestra la página principal con el listado de tareas."""
    return render_template("index.html", tareas=tareas)


@app.route("/agregar", methods=["POST"])
def agregar():
    """Recibe el texto del formulario y crea una tarea nueva."""
    texto = request.form.get("texto", "")
    if texto.strip():
        agregar_tarea(texto)
    # Tras guardar, volvemos al inicio (patrón POST-redirect-GET).
    return redirect(url_for("index"))


@app.route("/completar/<int:id>", methods=["POST"])
def completar(id):
    """Marca como completada la tarea cuyo id viene en la URL."""
    completar_tarea(id)
    return redirect(url_for("index"))


if __name__ == "__main__":
    # debug=True recarga el servidor al editar código (solo desarrollo).
    app.run(debug=True)
