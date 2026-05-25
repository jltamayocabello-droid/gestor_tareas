# Lista global en memoria: persiste mientras el proceso de Python siga activo.
tareas = []

# Contador interno para asignar ids únicos e incrementales.
_siguiente_id = 1


def agregar_tarea(texto):
    """Crea una tarea nueva, la añade a la lista global y devuelve su id."""
    global _siguiente_id

    tarea = {
        "id": _siguiente_id,
        "texto": texto.strip(),
        "completada": False,
    }
    tareas.append(tarea)
    _siguiente_id += 1
    return tarea["id"]


def completar_tarea(id):
    """Marca como completada la tarea con el id indicado. Devuelve True si existe."""
    for tarea in tareas:
        if tarea["id"] == id:
            tarea["completada"] = True
            return True
    return False
