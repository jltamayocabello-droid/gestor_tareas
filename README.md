# 📝 TaskManager Pro — Gestor de Tareas

![Estado del Proyecto](https://img.shields.io/badge/Estado-Completado-success)
![Stack](https://img.shields.io/badge/Stack-Python%20%7C%20Flask%20%7C%20Jinja2-blue)
![UI](https://img.shields.io/badge/UI-Bootstrap%205%20%7C%20Dark%20Mode-6f42c1)

## 📖 Descripción del Proyecto

**Curso:** [Cursor con Python: desarrollo inteligente con IA](https://www.santanderopenacademy.com/) — **Santander Open Academy**

Aplicación web **TaskManager Pro** desarrollada con **Flask** para gestionar tareas pendientes (to-do list). El proyecto forma parte del itinerario formativo del curso y pone en práctica los fundamentos del desarrollo web con Python: rutas, plantillas HTML, formularios, archivos estáticos y despliegue local.

### 🎯 Objetivo

Desarrollar una pequeña aplicación web que permita a los usuarios gestionar tareas de manera eficiente. Se utiliza **Flask**, un micro-framework web de Python muy popular y fácil de aprender.

La aplicación permite:

* ✅ Agregar nuevas tareas desde un modal Bootstrap.
* ✅ Marcar tareas como completadas (formulario POST seguro).
* ✅ Eliminar tareas pendientes o completadas.
* ✅ Ver un dashboard en tarjetas, ordenado (pendientes primero).
* ✅ Interfaz moderna en **modo oscuro** con paleta Slate.

Este proyecto cubre conceptos de desarrollo web como **rutas**, **plantillas HTML**, **herencia Jinja2**, **formularios POST**, **CDN Bootstrap** y **despliegue local**.

---

## 🛠️ Requerimientos Técnicos

Este proyecto cumple con los objetivos del módulo formativo:

* ✅ **Micro-framework Flask**: Configuración de aplicación y servidor de desarrollo.
* ✅ **Rutas y vistas**: Decoradores `@app.route` con métodos GET y POST.
* ✅ **Plantillas Jinja2**: Herencia (`extends`), bloques, bucles, condicionales y `url_for`.
* ✅ **Layout maestro**: `base.html` con Bootstrap 5 vía CDN.
* ✅ **Formularios web seguros**: POST para agregar, completar y eliminar; redirección POST-redirect-GET.
* ✅ **Lógica en Python**: Lista global en memoria y funciones CRUD en `tareas.py`.
* ✅ **UI responsive**: Grid de tarjetas, modal y tipografía Plus Jakarta Sans.
* ✅ **Modo oscuro**: Variables CSS con paleta Slate personalizada.
* ✅ **Código organizado**: Separación entre rutas (`app.py`) y lógica de negocio (`tareas.py`).

---

## 📂 Documentación Técnica

### 1. Stack Tecnológico

* **Python 3**: Lenguaje base del backend.
* **Flask 3**: Micro-framework para rutas, vistas y servidor local.
* **Jinja2**: Motor de plantillas integrado en Flask.
* **Bootstrap 5.3.2**: Componentes UI (CDN).
* **HTML5 / CSS3**: Dashboard, modal y tema oscuro.
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
│   ├── base.html          # Layout maestro (navbar, CDN Bootstrap)
│   └── index.html         # Dashboard de tareas (extiende base.html)
│
└── static/
    └── css/
        └── style.css      # Tema oscuro y estilos personalizados
```

### 3. Modelo de Datos y Lógica

Cada tarea se representa como un diccionario en la lista global `tareas`:

| Campo   | Tipo | Descripción                              |
|---------|------|------------------------------------------|
| `id`    | int  | Identificador único incremental          |
| `texto` | str  | Descripción de la tarea                  |
| `hecho` | bool | `False` = pendiente, `True` = completada |

**Funciones principales (`tareas.py`):**

```python
def agregar_tarea(texto):
    """Crea una tarea, la añade a la lista global y devuelve su id."""

def completar_tarea(id):
    """Marca hecho=True en la tarea indicada. Devuelve True si existe."""

def eliminar_tarea(id):
    """Elimina la tarea de la lista. Devuelve True si existía."""
```

### 4. Rutas de la Aplicación

| Método | Ruta               | Vista      | Descripción                              |
|--------|--------------------|------------|------------------------------------------|
| GET    | `/`                | `index`    | Dashboard con tareas ordenadas por estado|
| POST   | `/agregar`         | `agregar`  | Crea tarea desde el campo `texto_tarea`  |
| POST   | `/completar/<id>`  | `completar`| Marca la tarea como completada           |
| POST   | `/eliminar/<id>`   | `eliminar` | Elimina la tarea (pendiente o completada)|

### 5. Paleta de Colores — Modo Oscuro

| Elemento           | Color (Hex) | Propósito                                      |
|--------------------|-------------|------------------------------------------------|
| Fondo principal    | `#0f172a`   | Fondo de toda la aplicación (Slate 900)       |
| Tarjetas y modales | `#1e293b`   | Superficies elevadas con el contenido (800)   |
| Bordes e inputs    | `#334155`   | Separadores y fondo de campos de texto (700)  |
| Texto primario     | `#f8fafc`   | Títulos y descripciones principales (50)      |
| Texto secundario   | `#94a3b8`   | Subtítulos, estados y textos auxiliares (400)  |

Las variables se definen en `static/css/style.css` bajo la clase `app-dark` en `<html>`.

### 6. Funcionalidades Principales

#### 📋 Gestión de Tareas

* **Alta de tareas**: Modal Bootstrap con formulario POST y validación HTML5.
* **Completar tareas**: Botón POST por tarjeta; badge «Completada» al finalizar.
* **Eliminar tareas**: Disponible en pendientes y completadas.
* **Listado ordenado**: `sorted(tareas, key=lambda t: t['hecho'])` — pendientes primero.

#### 🎨 Interfaz (UI/UX)

* **Dashboard en tarjetas**: Grid responsive (`col-12` / `md-6` / `lg-4`).
* **Layout heredado**: `index.html` extiende `base.html` con bloques Jinja2.
* **Modo oscuro**: Tema Slate con `data-bs-theme="dark"` y CSS personalizado.
* **Estado vacío**: Mensaje amigable y acceso rápido al modal de creación.
* **Efectos visuales**: Hover en tarjetas, badges de estado y texto tachado en completadas.

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

1. **Crear tarea**: Pulsa «+ Nueva Tarea», escribe la descripción en el modal y guarda.
2. **Completar tarea**: En una tarjeta pendiente, pulsa «✔ Completar».
3. **Eliminar tarea**: Pulsa «Eliminar» en cualquier tarjeta.
4. **Ver listado**: Las pendientes se ordenan antes que las completadas en el grid.

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
* **Mantenibilidad**: Facilita ampliar el proyecto (por ejemplo, persistencia en SQLite).

### Formularios POST para completar y eliminar

**Decisión:** Acciones mutables solo por POST, no por enlaces GET.

**Justificación:**

* **Seguridad**: Evita cambios accidentales al prefetch de enlaces o recargas.
* **Buenas prácticas HTTP**: GET para leer, POST para modificar estado.

### Layout `base.html` + herencia Jinja2

**Decisión:** Plantilla maestra con Bootstrap CDN y vistas hijas con `{% extends %}`.

**Justificación:**

* **DRY**: Navbar, scripts y tema se definen una sola vez.
* **Escalabilidad**: Nuevas páginas reutilizan el mismo shell visual.

### Modo oscuro con variables CSS

**Decisión:** Paleta Slate fija mediante custom properties en `style.css`.

**Justificación:**

* **Legibilidad**: Contraste alto para títulos (`#f8fafc`) y metadatos (`#94a3b8`).
* **Coherencia**: Misma paleta en tarjetas, modal, inputs y navbar.
* **Mantenimiento**: Cambiar un color actualiza toda la interfaz.

### Lista global en memoria

**Decisión:** Almacenamiento en una lista Python sin base de datos.

**Justificación:**

* **Simplicidad**: Adecuado para aprendizaje y prototipos del curso.
* **Enfoque en Flask**: Permite centrarse en rutas, plantillas y formularios.
* **Evolución futura**: La misma interfaz puede migrarse a SQLite o JSON.

---

## 📱 Funcionalidades Destacadas

| Funcionalidad         | Descripción                                                   |
| --------------------- | ------------------------------------------------------------- |
| 📝 Agregar tareas     | Modal Bootstrap con POST a `/agregar`                         |
| ✅ Completar tareas    | POST seguro a `/completar/<id>`                               |
| 🗑️ Eliminar tareas    | POST a `/eliminar/<id>` (pendientes y completadas)            |
| 📋 Dashboard          | Grid de tarjetas con badges de estado                         |
| 🌙 Modo oscuro        | Paleta Slate (`#0f172a` → `#94a3b8`)                         |
| 🔢 IDs incrementales  | Contador interno `_siguiente_id` en `tareas.py`               |
| 📱 Diseño responsive  | Adaptable a móvil, tablet y escritorio                        |

---

## 🧪 Testing Manual

Para verificar el correcto funcionamiento:

1. **Crear tarea**: Debe aparecer una nueva tarjeta en el dashboard.
2. **Marcar como completada**: Badge verde, texto tachado y botón «Finalizada».
3. **Eliminar tarea pendiente**: La tarjeta desaparece del grid.
4. **Eliminar tarea completada**: Igual comportamiento que en pendientes.
5. **Orden del listado**: Las pendientes deben renderizarse antes que las completadas.
6. **Modal**: Abrir, cancelar y guardar sin errores visuales en tema oscuro.
7. **Campo vacío**: El navegador debe impedir enviar el formulario vacío (`required`).
8. **Reiniciar servidor**: La lista debe quedar vacía (datos en memoria).

---

## 📚 Recursos y Referencias

* [Documentación oficial de Flask](https://flask.palletsprojects.com/)
* [Jinja2 Template Designer Documentation](https://jinja.palletsprojects.com/)
* [Bootstrap 5 Documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
* [MDN Web Docs - HTML Forms](https://developer.mozilla.org/es/docs/Learn/Forms)
* Proyecto relacionado (Front-End): [m5_abp_taskflow](https://github.com/jltamayocabello-droid/m5_abp_taskflow)

---

## ✒️ Autor

**Jorge Tamayo Cabello**

_Desarrollador Front-End_

---

## 📄 Licencia

Este proyecto es parte de un trabajo formativo del curso **"Cursor con Python: desarrollo inteligente con IA"** de **Santander Open Academy** y está disponible con fines educativos.

---

## 🙏 Agradecimientos

* **Santander Open Academy** por la formación en desarrollo con Python e IA asistida.
* **Flask / Pallets** y **Bootstrap** por la documentación de sus herramientas.
* **Comunidad Python** por los recursos de aprendizaje del ecosistema web.
