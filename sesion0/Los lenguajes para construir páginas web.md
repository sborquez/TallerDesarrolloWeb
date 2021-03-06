# Páginas web

Para crear una página web, por lo general usamos tres tecnologías.

# HTML

HTML es el lenguaje con el que se define el contenido de las páginas web. Utiliza un conjunto de etiquetas que sirven para definir _elementos_ y sus _atributos_. Los elementos pueden ser texto, imágenes, formularios, entre otros. Nos referiremos a un objecto HTML como un documento, este sigue una estructura predefinida para que nuestro navegador pueda traducirlo a una página web.

Podemos utilizar este [editor](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_default) en linea, para poder visualizar a tiempo real un documento en html.


## Estructura básica

La estructura básica de un documento html posee al menos 3 etiquetas básicas:

```html
<html>
    <head>
        <!--este es un comentario-->
    </head>
    <body>
        <!--este es un comentario-->    
    </body>
</html>
```
<table>
    <tr> 
        <th>Elemento</th> <th>Función</th>
    </tr>
    <tr> 
        <td>html</td><td>Define al documento del tipo html</td>
    </tr>
    <tr>
        <td>head</td><td>Define información de la página, para temas de indexación y metadata.</td>
    </tr>
    <tr>
        <td>body</td><td>Define el cuerpo de la página, lo que se mostrará al usuario</td>
    </tr>
</table>

## Etiquetas de contenido

Podemos utilizar las siguentes etiquetas para definir contenido de texto.

```html
<html>
    <head>
        <title>Hello world!</title>
    </head>
    <body>
        <h1>Titulo</h1>
        <p>Este es un párrafo</p>
    </body>
</html>
```

<table>
    <tr> 
        <th>Elemento</th> <th>Función</th>
    </tr>
    <tr>
        <td>h1 a h6</td><td>Define títulos</td>
    </tr>
    <tr>
        <td>p</td><td>Define un párrafo</td>
    </tr>
</table>

## Organización

Etiquetas para organizar como mostramos los elementos.

### Listas Ordenadas
```html
<ol>
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ol>
```

### Listas No Ordenadas
```html
<ul>
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ul>
```

### Tablas
```html
<table>
    <tr> 
        <th>Company</th> <th>Country</th>
    </tr>
    <tr> 
        <td>Alfreds Futterkiste</td><td>Germany</td>
    </tr>
    <tr>
        <td>Island Trading</td><td>UK</td>
    </tr>
</table>
```

### Formularios

Usamos los [formularios](https://www.w3schools.com/html/html_forms.asp) para ingresar datos por parte de un usuario a través del navegador.

```html
<form action="/">
  Primer nombre:<br>
  <input type="text" name="nombre">
  <br>
  Edad:<br>
  <input type="number" name="edad">
  <br>
  Fecha de nacimiento: <br>
  <input type="datetime-local" name="nacimiento">
  <br>
  Ciudad:<br>
  <select name="ciudad">
    <option value="valparaiso">Valparaiso</option>
    <option value="santiago">Santiago</option>
    <option value="vina">Viña del mar</option>
  </select>
  
  <input type="submit" value="Submit">

</form>
```


Para seguir leyendo [Tutorial](https://www.w3schools.com/html/html_basic.asp) y [Referencia](https://www.w3schools.com/tags/default.asp) de html.

# CSS

Usamos CSS para definir el estilo de una página web, definimos el diseño, fuentes, layout de los elementos de la página. 

## Como usar

Podemos usar dos formas de incluir las definiciones de estilo en un documento _html_.

### Archivos externos

```html
<link rel="stylesheet" type="text/css" href="mystyle.css">
```

Podemos incluir archivos local o usar links a servidores externos.

### Etiqueta style

Podemos definir nuestro estilo dentro de las etiquetas **style** de hmtl.

```html
<style>

</style>
```

## Sintaxis

[<img src="https://www.w3schools.com/css/selector.gif">](https://www.w3schools.com/css/css_syntax.asp)

Para seguir leyendo [Tutorial](https://www.w3schools.com/css/default.asp) y [Referencia](https://www.w3schools.com/cssref/default.asp) de css.

Usamos selectores para ''buscar'' los elementos en la página, este selector puede ser:
*   Tipo de etiqueta
*   Atributo id
*   Atributo class

```html
<style>
    h1 {
        color: navy;
        margin-left: 20px;
    }

    #main {
       background-color: lightblue;
    }

    .center {
        text-align: center;
    }
</style>
<div id="main">
<h1>Titulo</h1>
<p class="center">Texto centrado</p>
</div>

```

## Atributos

Esta es una lista de algunos de los atributos de CSS, una lista completa la puede encontrar [aquí](https://www.w3schools.com/css/css_colors.asp)

### Colores

Para usar colores podemos identificarlos tanto por su nombre en inglés como en su representación en RGB u otras representaciones como HEX, HSL, HLSA y RGBA

Por ejemplo

* rgb(200,120,40)
* red
* #ff6347

Atributos de color:

* background-color : Define el color de fondo
* color:    Define el color del texto
* border:   Define el borde y su color.
 
### Fondos

Atributos para fondos:
* background-color: Para el color de fondo 
* background-image: Para cargar una imagen de fondo


### Bordes

Podemos definir atributos para su borde
* border-style: Estilo del borde, este puede ser:
    * dotted
    * solid
    * double
    * none
    * hidden
* border-left-style, border-right-style, border-top-style, border-bottom-style: Define bordes para cada dirección.
* border-width: Andcho del borde en pixeles.
* border-color: Color del borde.

### Marging

Especifica el margen entre cada elemento de la página.

* margin-top
* margin-right
* margin-bottom
* margin-left

### Padding

Para generar espacio alrededor del elemento.

* padding-top
* padding-right
* padding-bottom
* padding-left


### Dimensiones

Especificar tamaños para los elementos

* height
* width
* max-height, min-height 
* max-width, min-width  

## Frameworks

Existe estilos reutilizables disponibles, son faciles de incluir en nuestra página. Algunos ejemplos son:

* [Bootstrap](https://getbootstrap.com/docs/4.1/getting-started/introduction/)
* [Materials](https://www.muicss.com/)

# JavaScript

Javascript es un lenguaje de programación que corre del lado del cliente en el navegador.

Puede completar este [curso](https://www.codecademy.com/learn/introduction-to-javascript) de introducción al lenguaje impoartido por codecademy

<center><a href="https://github.com/sborquez/TallerDesarrolloWeb/tree/master/sesion0/Python%20y%20la%20orientación%20a%20objetos.md">Siguiente</a></center>