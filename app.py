from flask import Flask, redirect, render_template, request, url_for

from tareas import agregar_tarea, completar_tarea, tareas

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", tareas=tareas)


@app.route("/agregar", methods=["POST"])
def agregar():
    texto = request.form.get("texto", "")
    if texto.strip():
        agregar_tarea(texto)
    return redirect(url_for("index"))


@app.route("/completar/<int:id>", methods=["POST"])
def completar(id):
    completar_tarea(id)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
