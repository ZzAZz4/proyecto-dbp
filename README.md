# Kusa Store

## Integrantes
```
- Jose de Lama Zegarra
- Alex Loja Zumaeta
- Esteban Villacorta Garcia
- Gustavo Orosco Zavala
```

## Descripción

Kusa store es una aplicación web de tienda online en la que se ofrecen productos relacionados al anime, manga y la cultura otaku en Perú. 

El proyecto permite que existan tres tipos de usuario para la aplicación: administrador, cliente registrado y cliente no registrado. Cada uno tiene permisos incrementales dentro de la aplicación.

* Cliente no registrado:
  - Puede entrar a la pagina y ver los productos.
* Cliente registrado:
  - Puede añadir los productos que desea comprar a un carrito de compra.
  - Puede comprar estos productos.
* Administrador:
  - Puede hacer CRUD de los productos de manera sencilla, por medio de la interfaz.
## Objetivos Principales
```
- Venta legal de figuras coleccionables en Perú.
- Importación de artículos desde Japón.
- Impulso de la cultura otaku en Perú y América Latina.
```

## Mision

Ser la tienda virtual de manga, anime, artículos coleccionables más grande y reconocida en Perú.

## Vision

Ser referente en la construcción de la cultura otaku en sudámerica. "Una monita china en cada hogar".

## Tecnologias utilizadas

Para el desarrollo de Kusa Store se utilizó:
### FrontEnd
```
- HTML5 y CSS7
- Bootstrap
- Javascript 
- UIkit
```
### BackEnd
```
- SQLAlchemy para el manejo a alto nivel de los modelos de bases de datos.
- Flask como frameword para la creación rápida de la aplicación web.
- flask_wtf para el manejo de forms en la compra de articulos.
- Flask_login para el manejo y validación de usuarios y su acceso al sistema.
- flask_migrate para tener un log de los cambios a la estructura de la base de datos.
```
### Bases de datos
```
- MySQL / Postgresql a nivel interno en la creación de las Bases de datos
```

## Informacion de la aplicación
Dentro de las entidades en la aplicación (clases en el código y tablas en la base de datos) tenemos las siguientes:
```
- Usuario: representa a los usuarios registrados en la aplicación.
- Categoria: es la categoría a la que pertenece un producto.
- Subcategoría: similar a Categoría.
- Producto: un producto general disponible, con atributos como nombre, precio, descripcióń, etc.
- Compra: una compra hecha, con atributos como fecha, usuario y productos.
```
Además, existe un endpoint para cada vista de la página:
### Index
Es la vista principal de la página. Muestra todos los productos y, dependiendo de si eres un cliente o un administrador, se proveerán opciones para hacer CRUD de los productos.

### Signup Cliente
Es un formulario que crea un usuario a partir de los datos del cliente. Revisa si el username ya se encuentra registrado y, si no, lo añade a la base de datos con SQLAlchemy.

### Login Cliente
Es una vista que permite al usario loggearse. En el caso en el que el usuario ya se encuentre loggeado, este es redirigido a la página principal.

### Logout Cliente

### Single Product
Es una vista para obtener el detalle de un solo producto. 


### Create Product
Permite crear un producto en la base de datos si eres un administrador.

### Delete Product
Permite eliminar un producto de la base de datos si eres un administrador.

### Update Product
Permite actualizar la información de un producto ya existente si eres un administrador.

### Server error
Vista para mostrar lo que se muestra cuando ocurre un server error.
## Uso y Deployment
Para hacer uso de la aplicación, se deben seguir los siguientes pasos:

* Configurar las credenciales para la base de datos que se quiere usar en el archivo `config.py`.
* Instalar los requerimientos mostrados en el archivo `requirements.txt` dentro de este mismo repositorio.
* Ejecutar el comando:
```
python app.py
```

