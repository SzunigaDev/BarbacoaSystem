# BarbacoaSystem

BarbacoaSystem es un sistema de gestión para una empresa de barbacoa que utiliza Django y Django REST Framework para su backend.

## Características

- Gestión de productos
- Gestión de proveedores
- API RESTful para integración con otros sistemas
- Autenticación y autorización de usuarios
- Sistema de manejo de sesiones

## Instalación

### Requisitos previos

- Python 3.11.2
- PostgreSQL
- Virtualenv

### Pasos de instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/SzunigaDev/barbacoasystem.git
   cd barbacoasystem
   ```

2. Crea y activa un entorno virtual:

   ```bash
   python -m venv myenv
   source myenv/bin/activate  # En Windows usa `myenv\Scripts\ctivate`
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Configura las variables de entorno:

   - Crea un archivo `.env` en la raíz del proyecto.
   - Añade las variables necesarias (ver `.env.example` para más detalles).

5. Aplica las migraciones:

   ```bash
   python manage.py migrate
   ```

6. Ejecuta el servidor de desarrollo:

   ```bash
   python manage.py runserver
   ```

7. Accede al sistema:
   - URL: `http://127.0.0.1:8000/`
   - Credenciales: Crea un superusuario con `python manage.py createsuperuser`.

## Uso

- Puedes gestionar productos y proveedores desde la interfaz web.
- Las API RESTful están disponibles en los endpoints `/api/`.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue antes de enviar un pull request.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más información.
