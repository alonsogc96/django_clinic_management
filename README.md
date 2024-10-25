# Clinic Management

Este proyecto es una aplicación de gestión de clínicas que permite manejar datos de pacientes, citas y médicos a través de una API RESTful.

## Tabla de Contenidos

- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Documentación de la API](#documentación-de-la-api)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Requisitos

- Python 3.x
- Django 5.x o superior
- Django Rest Framework
- Otras dependencias necesarias (listadas en `requirements.txt`)

## Instalación

Sigue estos pasos para configurar el proyecto:

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/tuusuario/clinic-management.git
   cd clinic-management
   ```

2. **Crea un entorno virtual:**

   ```bash
   python -m venv venv
   ```

3. **Activa el entorno virtual:**

   - En Windows:

     ```bash
     venv\Scripts\activate
     ```

   - En macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Instala las dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Realiza las migraciones de la base de datos:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Inicia el servidor de desarrollo:**

   ```bash
   python manage.py runserver
   ```

## Uso

Para interactuar con la API, puedes utilizar herramientas como Postman o cURL. Aquí tienes algunos ejemplos de uso:

- **Registrar un nuevo usuario:**
  - Método: POST
  - URL: `http://localhost:8000/usuario/registrar`
  - Cuerpo de la solicitud (JSON):

    ```json
    {
      "username": "nuevo_usuario",
      "password": "tu_contraseña",
      "first_name": "nombres", 
      "last_name":"apellidos", 
      "email": "email", 
      "tipo_documento": "dni", 
      "numero_documento": 01234567
    }
    ```

- **Iniciar sesión:**
  - Método: POST
  - URL: `http://localhost:8000/api/token/`
  - Cuerpo de la solicitud (JSON):

    ```json
    {
      "username": "tu_usuario",
      "password": "tu_contraseña"
    }
    ```

- **Obtener la lista de clínicas:**
  - Método: GET
  - URL: `http://localhost:8000/clinicas/`
  - Autenticación requerida: Sí (agregar token en el encabezado)

## Documentación de la API

- **Endpoints disponibles:**
  - `/usuario/registrar`: Registro de nuevos usuarios.
  - `/api/token`: Autenticación de usuarios.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.