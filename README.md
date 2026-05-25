# Gestor de Tareas

Aplicación web sencilla para gestionar tareas pendientes (to-do list), desarrollada con **Flask**.

## Contexto del proyecto

Esta aplicación fue creada como parte del curso **"Cursor con Python: desarrollo inteligente con IA"** de **Santander Open Academy**.

### Objetivo del curso

Desarrollar una pequeña aplicación web para gestionar tareas pendientes. Los usuarios pueden:

- Agregar tareas
- Marcarlas como completadas
- Ver la lista actual de tareas

El proyecto utiliza **Flask**, un micro-framework web de Python muy popular y sencillo de aprender, y cubre conceptos de desarrollo web como **rutas**, **plantillas HTML**, **formularios** y **despliegue local**.

## Funcionalidades

- Listado de tareas ordenado (pendientes primero, completadas después)
- Alta de tareas mediante formulario POST
- Marcado de tareas como completadas
- Interfaz con plantillas Jinja2 y estilos CSS

## Tecnologías

- Python 3
- Flask 3
- Jinja2 (plantillas)
- HTML / CSS

## Estructura del proyecto

```
gestor_tareas/
├── app.py              # Rutas y aplicación Flask
├── tareas.py           # Lógica de tareas (lista global en memoria)
├── requirements.txt    # Dependencias
├── templates/
│   └── index.html      # Vista principal (Jinja2)
└── static/
    └── css/
        └── style.css   # Estilos
```

## Requisitos previos

- Python 3 instalado
- Entorno virtual recomendado (`venv`)

## Instalación

1. Clona o descarga el repositorio:

```bash
git clone https://github.com/jltamayocabello-droid/gestor_tareas.git
cd gestor_tareas
```

2. Crea y activa el entorno virtual:

**Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (Git Bash) / Linux / macOS:**

```bash
python -m venv venv
source venv/Scripts/activate   # Windows Git Bash
# source venv/bin/activate     # Linux / macOS
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución local

Con el entorno virtual activado:

```bash
python app.py
```

Abre el navegador en: **http://127.0.0.1:5000**

> Las tareas se guardan en memoria. Al reiniciar el servidor, la lista se vacía.

## Rutas de la aplicación

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/` | Muestra el listado de tareas |
| POST | `/agregar` | Crea una tarea nueva (`texto_tarea`) |
| GET | `/completar/<id>` | Marca una tarea como completada |

## Modelo de datos

Cada tarea es un diccionario con:

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | int | Identificador incremental |
| `texto` | str | Descripción de la tarea |
| `hecho` | bool | `False` pendiente, `True` completada |

Las funciones principales en `tareas.py` son `agregar_tarea(texto)` y `completar_tarea(id)`.

## Conceptos practicados

- **Rutas Flask**: decoradores `@app.route` y vistas
- **Plantillas HTML**: `render_template` con Jinja2 (`{% for %}`, `{% if %}`, `url_for`)
- **Formularios**: envío POST y redirección tras guardar
- **Despliegue local**: servidor de desarrollo con `app.run(debug=True)`

## Licencia

Proyecto educativo del curso Santander Open Academy.
