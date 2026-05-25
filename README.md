# 📝 Gestor de Tareas

![Estado del Proyecto](https://img.shields.io/badge/Estado-Completado-success)
![Stack](https://img.shields.io/badge/Stack-Python%20%7C%20Flask%20%7C%20Jinja2-blue)

## 📖 Descripción del Proyecto

**Curso:** [Cursor con Python: desarrollo inteligente con IA](https://www.santanderopenacademy.com/) — **Santander Open Academy**

Este repositorio contiene una aplicación web desarrollada con **Flask** para gestionar tareas pendientes (to-do list). El proyecto forma parte del itinerario formativo del curso y pone en práctica los fundamentos del desarrollo web con Python: rutas, plantillas HTML, formularios y despliegue local.

### 🎯 Objetivo

Desarrollar una pequeña aplicación web que permita a los usuarios gestionar tareas de manera sencilla. Se utiliza **Flask**, un micro-framework web de Python muy popular y fácil de aprender.

La aplicación permite:

* ✅ Agregar nuevas tareas mediante un formulario.
* ✅ Marcar tareas como completadas.
* ✅ Ver la lista actual ordenada (pendientes primero, completadas después).

Este proyecto cubre conceptos de desarrollo web como **rutas**, **plantillas HTML**, **formularios** y **despliegue local**.

---

## 🛠️ Requerimientos Técnicos

Este proyecto cumple con los objetivos del módulo formativo:

* ✅ **Micro-framework Flask**: Configuración de aplicación y servidor de desarrollo.
* ✅ **Rutas y vistas**: Decoradores `@app.route` con métodos GET y POST.
* ✅ **Plantillas Jinja2**: `render_template`, bucles, condicionales y `url_for`.
* ✅ **Formularios web**: Captura de datos con `request.form` y redirección POST-redirect-GET.
* ✅ **Lógica en Python**: Lista global en memoria y funciones `agregar_tarea` / `completar_tarea`.
* ✅ **Archivos estáticos**: Hoja de estilos CSS servida desde `static/`.
* ✅ **Código organizado**: Separación entre rutas (`app.py`) y lógica de negocio (`tareas.py`).

---

## 📂 Documentación Técnica

### 1. Stack Tecnológico

* **Python 3**: Lenguaje base del backend.
* **Flask 3**: Micro-framework para rutas, vistas y servidor local.
* **Jinja2**: Motor de plantillas integrado en Flask.
* **HTML5 / CSS3**: Interfaz de usuario y estilos.
* **Git / GitHub**: Control de versiones y publicación del código.

### 2. Estructura del Proyecto

```
gestor_tareas/
│
├── app.py                 # Rutas Flask y punto de entrada
├── tareas.py              # Lista global y funciones de negocio
├── requirements.txt       # Dependencias del proyecto
├── README.md              # Documentación
│
├── templates/
│   └── index.html         # Vista principal (Jinja2)
│
└── static/
    └── css/
        └── style.css      # Estilos de la interfaz
```

### 3. Modelo de Datos y Lógica

Cada tarea se representa como un diccionario en la lista global `tareas`:

| Campo   | Tipo | Descripción                                      |
|---------|------|--------------------------------------------------|
| `id`    | int  | Identificador único incremental                  |
| `texto` | str  | Descripción de la tarea                          |
| `hecho` | bool | `False` = pendiente, `True` = completada         |

**Funciones principales (`tareas.py`):**

```python
def agregar_tarea(texto):
    """Crea una tarea, la añade a la lista global y devuelve su id."""

def completar_tarea(id):
    """Marca hecho=True en la tarea indicada. Devuelve True si existe."""
```

### 4. Rutas de la Aplicación

| Método | Ruta               | Vista      | Descripción                              |
|--------|--------------------|------------|------------------------------------------|
| GET    | `/`                | `index`    | Lista tareas ordenadas por estado        |
| POST   | `/agregar`         | `agregar`  | Crea tarea desde el campo `texto_tarea`  |
| GET    | `/completar/<id>`  | `completar`| Marca la tarea como completada           |

### 5. Funcionalidades Principales

#### 📋 Gestión de Tareas

* **Alta de tareas**: Formulario POST con validación de texto no vacío.
* **Completar tareas**: Enlace GET que invoca `completar_tarea(id)`.
* **Listado ordenado**: `sorted(tareas, key=lambda t: t['hecho'])` — pendientes primero.

#### 🎨 Interfaz (UI)

* **Plantilla Jinja2**: Bucles `{% for %}`, condicionales `{% if %}` y `url_for` para enlaces dinámicos.
* **Estilos CSS**: Tareas completadas con texto tachado y color atenuado.
* **Diseño centrado**: Contenedor principal con sombra y tipografía del sistema.

---

## 🚀 Cómo ejecutar este proyecto

Para ejecutar la aplicación en local:

### 1. Clonar el repositorio:

```bash
git clone https://github.com/jltamayocabello-droid/gestor_tareas.git
cd gestor_tareas
```

### 2. Crear y activar el entorno virtual:

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

### 3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

### 4. Iniciar el servidor:

```bash
python app.py
```

### 5. Abrir en el navegador:

Visita **http://127.0.0.1:5000**

> ⚠️ Las tareas se almacenan **en memoria**. Al reiniciar el servidor, la lista se vacía.

### 6. Uso de la aplicación:

1. **Crear tarea**: Escribe el texto y pulsa «Agregar».
2. **Completar tarea**: Haz clic en «Completar» junto a una tarea pendiente.
3. **Ver listado**: Las pendientes aparecen arriba; las completadas, abajo.

---

## 🌐 Repositorio

* **Repositorio GitHub**: 🔗 [https://github.com/jltamayocabello-droid/gestor_tareas](https://github.com/jltamayocabello-droid/gestor_tareas)

---

## 💡 Justificación de Decisiones Técnicas

### Separación `app.py` / `tareas.py`

**Decisión:** Rutas Flask en un módulo y lógica de tareas en otro.

**Justificación:**

* **Separación de responsabilidades**: `app.py` gestiona HTTP; `tareas.py` gestiona datos.
* **Reutilización**: Las funciones de tareas pueden probarse sin levantar el servidor.
* **Mantenibilidad**: Facilita ampliar el proyecto (por ejemplo, persistencia en archivo o BD).

### Lista global en memoria

**Decisión:** Almacenamiento en una lista Python sin base de datos.

**Justificación:**

* **Simplicidad**: Adecuado para aprendizaje y prototipos del curso.
* **Enfoque en Flask**: Permite centrarse en rutas, plantillas y formularios.
* **Evolución futura**: La misma interfaz puede migrarse a SQLite o JSON.

### POST-redirect-GET en `/agregar`

**Decisión:** Tras crear una tarea, redirigir a `/` con `redirect('/')`.

**Justificación:**

* **Evita reenvío del formulario**: Al recargar la página no se duplica la tarea.
* **Patrón estándar web**: Buena práctica en aplicaciones con formularios.

### Campo `hecho` en lugar de strings de estado

**Decisión:** Booleano `hecho` para el estado de la tarea.

**Justificación:**

* **Ordenación simple**: `sorted(..., key=lambda t: t['hecho'])` agrupa pendientes y completadas.
* **Condicionales claros**: En Jinja2, `{% if not tarea.hecho %}` es legible y directo.

---

## 📱 Funcionalidades Destacadas

| Funcionalidad        | Descripción                                                |
| -------------------- | ---------------------------------------------------------- |
| 📝 Agregar tareas    | Formulario POST con campo `texto_tarea`                    |
| ✅ Completar tareas   | Ruta GET `/completar/<id>` con redirección al inicio       |
| 📋 Listar tareas     | Vista principal con `render_template` y Jinja2             |
| 🔢 IDs incrementales | Contador interno `_siguiente_id` en `tareas.py`            |
| 🎨 Estilos CSS       | Diferenciación visual entre tareas pendientes y completadas|

---

## 🧪 Testing Manual

Para verificar el correcto funcionamiento:

1. **Crear tarea**: Debe aparecer en la lista con un `id` nuevo.
2. **Marcar como completada**: Debe mostrarse tachada y sin botón «Completar».
3. **Orden del listado**: Las pendientes deben aparecer antes que las completadas.
4. **Campo vacío**: No debe crearse tarea si el texto está vacío.
5. **Reiniciar servidor**: La lista debe quedar vacía (datos en memoria).

---

## 📚 Recursos y Referencias

* [Documentación oficial de Flask](https://flask.palletsprojects.com/)
* [Jinja2 Template Designer Documentation](https://jinja.palletsprojects.com/)
* [MDN Web Docs - HTML Forms](https://developer.mozilla.org/es/docs/Learn/Forms)
* Proyecto relacionado (Front-End): [m5_abp_taskflow](https://github.com/jltamayocabello-droid/m5_abp_taskflow)

---

## ✒️ Autor

**Jorge Tamayo Cabello**

Desarrollador Front-End 

---

## 📄 Licencia

Este proyecto es parte de un trabajo formativo del curso **"Cursor con Python: desarrollo inteligente con IA"** de **Santander Open Academy** y está disponible con fines educativos.

---

## 🙏 Agradecimientos

* **Santander Open Academy** por la formación en desarrollo con Python e IA asistida.
* **Flask / Pallets** por la documentación del micro-framework.
* **Comunidad Python** por los recursos de aprendizaje del ecosistema web.
