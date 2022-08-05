# Getting Started
##### Para poder darle uso a la API rest estos son los pasos a seguir:
1. El primer paso es clonar el proyecto

    `git clone https://github.com/IsidroEmirPelli/todo-challenge.git`

2.  Una vez que tengas repositorio clonado recomiendo crear un entorno virtual

    `python -m venv ./venv`

3. El siguente paso es entrar al venv en caso de haber creado el entorno virtual

    `/venv/scripts/activate`

4. Tienes que instalar los requeriments.txt

    `pip install -r requeriments.txt`

5. Lo siguente es abrir el servidor

    `python manage.py runserver`

## Urls
##### Para poder acceder a la api necesitas obtener una clave de autentificacion
Para ello vamos a acceder a http://127.0.0.1:8000/api/login/
Y vamos a ingresar las credenciales 

`Username:user` `Password:pass`

### Una vez que tenemos la clave de auth podremos acceder a los siguentes endpoints
##### Creacion  de tareas
-Post `http://127.0.0.1:8000/api/tasks?content="Tarea"`
##### Eliminar una tarea.
-Delete `http://127.0.0.1:8000/api/tasks/<pk>/`
##### Actualizar el estado de una tarea
-Patch  `http://127.0.0.1:8000/api/tasks/<pk>/`
##### Visualizar una lista de todas las tareas existentes
-Get `http://127.0.0.1:8000/api/tasks/`
##### Filtrar/buscar tareas por fecha de creación y/o por el contenido de la misma
-Get `http://127.0.0.1:8000/api/tasks/filter/?fecha=2022-08-05&content=tarea`
