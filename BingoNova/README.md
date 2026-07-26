# BingoPro

Sistema web de Bingo desarrollado con Django como proyecto académico.

## Características

- Inicio de sesión de usuarios.
- Gestión de partidas de bingo.
- Generación de cartones.
- Interfaz moderna y responsive.
- Desarrollo bajo arquitectura MVC (MVT en Django).

---

## Requisitos

- Python 3.12 o superior
- pip
- Git (opcional)

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/BingoPro.git
```

### 2. Entrar al proyecto

```bash
cd BingoPro
```

### 3. Crear el entorno virtual

```bash
python -m venv venv
```

### 4. Activar el entorno virtual

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

### 5. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 6. Ejecutar migraciones

```bash
python manage.py migrate
```

### 7. Iniciar el servidor

```bash
python manage.py runserver
```

---

## Acceso

Abrir el navegador y acceder a:

```
http://bingopro:8000
```

Si no se ha configurado el archivo **hosts**, utilizar:

```
http://localhost:8000
```

---

## Tecnologías utilizadas

- Python
- Django
- HTML5
- CSS3
- JavaScript
- SQLite

---

## Autor

Proyecto desarrollado con fines académicos.