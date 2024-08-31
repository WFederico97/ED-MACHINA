# ED-MACHINA Challenge

by Federico Wuthrich

## BACKEND

Se solicitó hacer una API CRUD basada en LEADS que registre y consulte personas que estén cursando una carrera y las materias que dicha carrera contenga. Se implementó un patrón de desarrollo MVC (Modelo-Vista-Controlador) con una arquitectura modular.

- **Modelo**: Representado por los archivos `.py` en la carpeta Models y Schemas.
- **Controlador**: Representado por aquellos archivos que se encuentran en la carpeta Routes.
- **Vista**: Representada por los JSON que son devueltos en las respuestas del SWAGGER de FastAPI.
- **Arquitectura Modular**: Todos los módulos fueron separados en capas, permitiendo una facilidad de aislación de responsabilidades y haciendo que el código sea escalable.

## CONTENEDORIZACIÓN

Realizada con Docker y compuesta con Docker-Compose.

## BASE DE DATOS

Se utilizó el motor de PostgreSQL. A su vez, en el archivo `database.py` se ejecuta un script con la creación de la base de datos para que se realice antes de inicializar la app. El script puede encontrarse en la carpeta `Scripts/init.sql`.

### WALKTHROUGH

1. Una vez inicializada la app, las tablas `carreras` y `materias` ya se encuentran con datos y su respectiva integridad referencial.
2. Para crear una nueva persona, hay que dirigirse al endpoint de método 'PUT'. Este mismo recibe un `id` como parámetro y luego un schema que contiene nombre, apellido, email y un campo booleano `active` que viene predeterminado como `True`.
3. Una vez creada la persona, puede ser consultada tanto por la consulta general como 'get all' y por `id`.
4. Si queremos agregar una carrera o modificar algún dato a una persona ya creada, deberemos volver al punto 2 y modificar los datos que haga falta en ese endpoint.
5. En el caso de que queramos eliminar a una persona de la base de datos, lo haremos a través de un borrado lógico para no afectar a la integridad de datos en la base de datos. Para esto, modificaremos el valor de la propiedad `active` a `False`.

---

## English

### BACKEND

The task was to create a CRUD API based on LEADS that registers and queries people who are studying a degree and the subjects that the degree contains. An MVC (Model-View-Controller) development pattern was implemented, with a modular architecture.

- **Model**: Represented by the `.py` files in the Models and Schemas folders.
- **Controller**: Represented by the files located in the Routes folder.
- **View**: Represented by the JSONs returned in the responses from FastAPI's SWAGGER.
- **Modular Architecture**: All modules were separated into layers to facilitate the isolation of responsibilities and make the code scalable.

### CONTAINERIZATION

Performed with Docker and composed using Docker-Compose.

### DATABASE

PostgreSQL was used as the engine, and a script with the database creation runs in the `database.py` file before initializing the app. The script can be found in the `Scripts/init.sql` folder.

### WALKTHROUGH

1. Once the app is initialized, the `carreras` (degrees) and `materias` (subjects) tables are already populated with data and their respective referential integrity.
2. To create a new person, you need to go to the 'PUT' method endpoint. This endpoint receives an `id` as a parameter and then a schema that includes the first name, last name, email, and a boolean field `active` which is set to `True` by default.
3. Once a person is created, they can be queried either through the general query like 'get all' or by `id`.
4. If we want to add a degree or modify some data for an already created person, we must go back to step 2 and modify the necessary data in that endpoint.
5. If we want to remove a person from the database, we will do so through a soft delete to avoid affecting data integrity in the database. For this, we will change the value of the `active` property to `False`.