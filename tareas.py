tareas = []
_siguiente_id = 1


def agregar_tarea(texto):
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
    for tarea in tareas:
        if tarea["id"] == id:
            tarea["completada"] = True
            return True
    return False
