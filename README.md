# Libroteca Digital

## Descripción
**Libroteca Digital** es una aplicación web desarrollada con Flask que permite a los usuarios buscar, reservar y revisar una amplia gama de libros electrónicos. La aplicación ofrece una variedad de géneros para todos los gustos, desde ficción hasta no ficción, pasando por ciencia ficción, fantasía, terror, y más. Además, los usuarios pueden dejar sus opiniones y calificaciones sobre los libros que han leído, contribuyendo así a la comunidad de lectores.

## Características
- **Registro y autenticación de usuarios**: Los usuarios pueden registrarse y autenticarse para acceder a las funcionalidades de la aplicación.
- **Gestión de libros**: Los administradores pueden agregar, editar y eliminar libros de la librería.
- **Reservas de libros**: Los usuarios pueden reservar libros para leerlos más tarde.
- **Descarga de libros**: Los usuarios pueden descargar los libros en formato PDF.
- **Dashboard personalizado**: Los usuarios tienen un dashboard donde pueden ver sus reservas y descargar los libros reservados.

## Estructura del Proyecto
La aplicación está estructurada en módulos para facilitar el mantenimiento y la escalabilidad:
- **app_flask**: Contiene la aplicación Flask principal y sus componentes.
- **models**: Define los modelos de datos utilizados en la aplicación.
- **routes**: Contiene las rutas y vistas de la aplicación.
- **templates**: Almacena los archivos HTML utilizados para renderizar las vistas.
- **utils**: Contiene utilidades como la generación de PDFs.
- **venv**: Directorio virtual de Python para manejar las dependencias.
- **config.py**: Configuración de la aplicación, incluyendo la cadena de conexión a la base de datos.
- **run.py**: Punto de entrada de la aplicación.

## Configuración
Para configurar la aplicación, sigue estos pasos:
1. Clona el repositorio.
2. Crea un entorno virtual con `python -m venv venv`.
3. Activa el entorno virtual:
   - En Windows: `venv\Scripts\activate`
   - En Unix o MacOS: `source venv/bin/activate`
4. Instala las dependencias con `pip install -r requirements.txt`.
5. Configura la variable de entorno FLASK_APP para apuntar al archivo run.py.
6. Ejecuta `flask run` para iniciar la aplicación.

## Uso
Una vez que la aplicación esté en ejecución, puedes acceder a ella a través de un navegador web en `http://localhost:5000`. Desde allí, podrás registrarte, iniciar sesión, explorar los libros disponibles, reservarlos y descargarlos.

## Contribuciones
Las contribuciones son bienvenidas. Por favor, sigue el flujo de trabajo de GitHub para contribuir con cambios o nuevas características.

## Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.