from flask import Flask, redirect, render_template, request

from tareas import agregar_tarea, completar_tarea, eliminar_tarea, tareas

app = Flask(__name__)


@app.route("/")
def index():
    # Ordenar tareas: incompletas primero, luego completadas
    tareas_ordenadas = sorted(tareas, key=lambda t: t["hecho"])
    return render_template("index.html", tareas=tareas_ordenadas)


@app.route("/agregar", methods=["POST"])
def agregar():
    texto_tarea = request.form.get("texto_tarea")
    if texto_tarea:
        agregar_tarea(texto_tarea)
    return redirect("/")


@app.route("/completar/<int:id>", methods=["POST"])
def completar(id):
    completar_tarea(id)
    return redirect("/")


@app.route("/eliminar/<int:id>", methods=["POST"])
def eliminar(id):
    eliminar_tarea(id)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
