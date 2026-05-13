# Jujutsu Kaisen — Character Showcase
### Aplicación web con Reflex (Python) · Guía de instalación desde cero

---

## Requisitos previos

Antes de empezar, instala lo siguiente en tu máquina:

**1. Python 3.11 o superior**
Descarga desde https://www.python.org/downloads/
> Durante la instalación marca la casilla **"Add Python to PATH"**

**2. Node.js 18 o superior**
Descarga desde https://nodejs.org/
> Requerido por Reflex para compilar el frontend

**3. Poetry** (gestor de dependencias)
Abre PowerShell y ejecuta:
```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```
Luego cierra y vuelve a abrir PowerShell para que los cambios surtan efecto.

---

## Crear el proyecto

### Paso 1 — Crear la carpeta del proyecto

```powershell
mkdir JujutsuKaisen
cd JujutsuKaisen
```

> Evita usar OneDrive como ubicación. Reflex advierte que puede causar problemas de rendimiento.
> Recomendado: `C:\Proyectos\JujutsuKaisen`

---

### Paso 2 — Inicializar Poetry

```powershell
poetry init
```

Cuando te pregunte los datos, puedes presionar Enter para aceptar los valores por defecto en todo. Al final preguntará si quieres agregar dependencias manualmente — responde **no**.

Esto crea el archivo `pyproject.toml`.

---

### Paso 3 — Agregar Reflex como dependencia

```powershell
poetry add reflex
```

Esto puede tardar unos minutos la primera vez.

---

### Paso 4 — Activar el entorno virtual

```powershell
poetry env activate
```

Copia el comando que te devuelve y ejecútalo. Se verá algo así:

```powershell
& "C:\Users\TuUsuario\...\JujutsuKaisen\.venv\Scripts\activate.ps1"
```

Sabrás que está activo porque el nombre del entorno aparecerá entre paréntesis al inicio de la línea.

---

### Paso 5 — Inicializar el proyecto Reflex

```powershell
poetry run reflex init
```

Esto crea la estructura base del proyecto:

```
JujutsuKaisen/
├── assets/                  ← aquí van las imágenes
├── JujutsuKaisen/
│   └── JujutsuKaisen.py     ← archivo principal (reemplazar)
├── rxconfig.py
└── pyproject.toml
```

---

### Paso 6 — Reemplazar el archivo principal

Borra el contenido de `JujutsuKaisen/JujutsuKaisen.py` y reemplázalo con el código del proyecto (`Actividad5DesarrolloWebconReflex.py`).

> El nombre del archivo debe coincidir exactamente con el nombre de la carpeta del proyecto.

---

### Paso 7 — Agregar las imágenes

Copia las imágenes de los personajes dentro de la carpeta `assets/` con estos nombres exactos (todo en minúscula):

```
assets/
├── megumi.png
├── sukuna.png
├── gojo.png
├── yuji.png
└── nobara.png
```

> Si las imágenes vienen de internet y Windows las bloquea, haz clic derecho → Propiedades → marca **"Desbloquear"** → Aplicar.

> Si un personaje no aparece, puedes incrustar la imagen directamente en el código como base64 para evitar problemas con archivos externos (ver sección al final).

---

### Paso 8 — Ejecutar la aplicación

```powershell
poetry run reflex run
```

La primera vez descargará dependencias de frontend (puede tardar 2-5 minutos).

Cuando veas el mensaje `App running at: http://localhost:3000`, abre el navegador en:

```
http://localhost:3000
```

---

## Estructura final del proyecto

```
JujutsuKaisen/
├── assets/
│   ├── megumi.png
│   ├── sukuna.png
│   ├── gojo.png
│   ├── yuji.png
│   └── nobara.png
├── JujutsuKaisen/
│   └── JujutsuKaisen.py
├── rxconfig.py
├── pyproject.toml
└── poetry.lock
```

---

## Solución de problemas frecuentes

### Error: `ForeachVarError` al iniciar
Asegúrate de que las clases `ClipData` y `CharData` heredan de `BaseModel` (de pydantic), no de `rx.Base`. El código ya incluye esta corrección.

### Error: `No reflex attribute Base`
Tu versión de Reflex no expone `rx.Base`. La solución es usar `from pydantic import BaseModel` y heredar desde ahí.

### Las imágenes no aparecen (ícono roto)
- Verifica que la carpeta `assets/` esté en la raíz del proyecto, al mismo nivel que `rxconfig.py`
- Verifica que los nombres sean exactamente `megumi.png`, `sukuna.png`, etc. (minúsculas, sin espacios)
- Abre `http://localhost:3000/megumi.png` en el navegador — si da 404, el archivo no está en el lugar correcto
- Reinicia el servidor con `Ctrl+C` y vuelve a ejecutar `poetry run reflex run` después de agregar imágenes nuevas

### Warning sobre OneDrive
Reflex funciona en OneDrive pero puede ser lento. Para mejor rendimiento, crea el proyecto en `C:\Proyectos\` en lugar del Escritorio o carpetas sincronizadas.

### Warning sobre WSL
Reflex recomienda WSL en Windows para mejorar los tiempos de instalación, pero no es obligatorio. La aplicación funciona sin él.

---

## Incrustar imágenes como base64 (opcional)

Si una imagen sigue sin cargar desde `assets/`, puedes incrustarla directamente en el código para que no dependa de archivos externos.

Ejecuta esto en Python:

```python
import base64

with open("assets/nobara.png", "rb") as f:
    data = base64.b64encode(f.read()).decode()

print(f"data:image/png;base64,{data}")
```

Luego reemplaza `"nobara.png"` en el diccionario del personaje con el resultado completo:

```python
"image": "data:image/png;base64,/9j/4AAQSkZJRgAB...",
```

---

## Comandos útiles

| Comando | Descripción |
|---|---|
| `poetry run reflex run` | Iniciar la app en modo desarrollo |
| `poetry run reflex run --env prod` | Iniciar en modo producción |
| `Ctrl+C` | Detener el servidor |
| `poetry add <paquete>` | Agregar una dependencia |
| `poetry env activate` | Activar el entorno virtual |

---

*Fan-made · No afiliado con MAPPA ni Gege Akutami*