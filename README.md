# Práctica del curso de Python

---


**KeepBlog** es una aplicación desarrollada con en el lenguaje de programación *Python* con el Framework *Django*
La aplicación cuenta tanto con una aplicación web y una Api, Keepblog fue desarrollada con el propósito de gestionar blogs de usuario.
   
   La aplicación **WEB** cuenta con las siguientes funcionalidades
    <p align="center">
  	<img width="890" height="500" src="https://github.com/MichaelNode/Python-Entrega/blob/master/content/adm1.png?raw=true">
    </p>
   
   * Crear blog (Django admin)
   * Crear Categorías (Django admin)
	    <p align="center">
		<img width="860" height="500" src="https://github.com/MichaelNode/Python-Entrega/blob/master/content/adm2.png?raw=true">
	     </p>
   * Crear, detalle y listado Post (KeepBlog)
  1. Detalle
    <p><img width="890" height="500" src="https://github.com/MichaelNode/Python-Entrega/blob/master/content/main3.png?raw=true" >
	</p>
 2. Crear
	
   	 <p align="center">
  	<img width="890" height="500" src="https://github.com/MichaelNode/Python-Entrega/blob/master/content/main2.png?raw=true">
     	</p>
	
	
3. Listado
	
   	 <p align="center">
  	<img width="860" height="500" src="https://github.com/MichaelNode/Python-Entrega/blob/master/content/main1.png?raw=true">
     	</p>
	
   * listado de blog y post con filtros y paginación (KeepBlog)
   	<p align="center">
  	<img width="890" height="500" src="https://github.com/MichaelNode/Python-Entrega/blob/master/content/listblog.png?raw=true">
     	</p>
   * Sing In(KeepBlog)
   * Log in (KeepBlog)
   * Logout(KeepBlog)
   
   La **API** cuenta con las siguientes funcionalidades
   
   * Creaciòn, edicion , detalle y Eliminaciòn de usuario.
   * Creaciòn, edicion , detalle y Eliminaciòn de post(filtro en Get).
   * listado de blog(filtros).

Keepblog cuenta con algunas restricciones de autentican en la mayoría de las funcionalidad.
el url por defecto es <http://localhost:8000/>



## Proceso de instalación 

## INSTALACIÓN
Ejecuta el siguiente comando para instalar las dependencias y ejecución de **KeepBlog**
- Crear y activar entorno``` shell virtualenv env --python=python3 source env/bin/activate ```
NOTA: debes tener instalado *virtualenv* para poder crear el entorno virtual

* Instalar depdenceias del Keepblog:
```shell
pip install -r requirements.txt
```

* Crear superusuario:

	```shell
	python manage.py migrate
	python manage.py createsuperuser
	```
NOTA: se debe crear un super usuario para poder crear un blog y categoría en el administrador de Django

* Correr aplicación:
	```shell
	python manage.py runserver
	```


## IMPORTANTE


1) Se recomienda realizar registro de un blog y una categoria desde el administrado proporcionado por Django



## API

Las rutas de la API son

1. Usuarios: para los casos de DETAIL, POST Y DELETE se debe especificar la pk del usuario en la url, es importante saber
que solo podré ver detalles, actualizar y eliminar el dueño de la cuenta y el administrador del sistema, ya que cuenta con validación de autenticación.
    * GET
     <http://127.0.0.1:8000/api/1.0/users/>
    * DETAIL(GET)
     <http://127.0.0.1:8000/api/1.0/users/PK>
    * POST(GET)
     <http://127.0.0.1:8000/api/1.0/users/PK>
	  ```shell{
      { 
      "first_name": "prueba",
      "last_name": "user",
      "username": "userapi",
      "email": "prueba@example.com",
      "password": "prueba"
       }```

    * PUT(GET)
	    <http://127.0.0.1:8000/api/1.0/users/PK>
	 
	     ```shell{
	      "first_name": "userapi edit",
	      "last_name": "user edit",
	      "username": "userapi",
	      "email": "user@example.com",
	      "password": "userapi"
		}```

    * DELETE
   <http://127.0.0.1:8000/api/1.0/users/PK>


2. Blog: la url de blog permite agregar un filtro author__username para ver los blogs  del usuario en especio, en caso de no agregar el filtro se obtendrá todos los blogs

	* <http://127.0.0.1:8000/api/1.0/blogs/>
    * con filtro
	* <http://127.0.0.1:8000/api/1.0/blogs/?author__username=admin>

3. Post: para las peticiones de post, se debe tener en cuenta que el resultado será distinto tanto para un usuario logeado y no, en el caso del get, un usuario que no esté autenticado solo obtendrá los post publicado, y en cambio uno autenticado podrá ver todo los post de un blog en específico ,

**IMPORTANTE** : para la creación de un post se debe considerar los campos de cat_id y blog_id que son las calves foráneas, es por eso que es importante saber las pk del blog y categoría donde se creara el post:
    
      * GET
	    <http://127.0.0.1:8000/api/1.0/post/>
	    
     * DETAIL(GET)
     
	    <http://127.0.0.1:8000/api/1.0/post/pk>
	    
     * DELETE
     
	    <http://127.0.0.1:8000/api/1.0/post/pk>
     * POST
     
	    <http://127.0.0.1:8000/api/1.0/post/pk>
    
 
        {
         "title": "post desde api 22",
         "content": "de la prueba de api 22",
         "image": "/uploads/ip_1_QmBfxeI.jpeg",
         "pos_date": "2018-11-25T22:38:25.693465Z",
         "blog_id": 1,
         "cat_id": 1
	}

 

