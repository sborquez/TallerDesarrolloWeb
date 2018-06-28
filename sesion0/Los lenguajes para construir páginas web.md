# Páginas web

Para crear una página web, por lo general usamos tres componentes

# HTML

HTML es el lenguaje con el que se define el contenido de las páginas web. Utiliza un conjunto de etiquetas que sirven para definir _elementos_ y sus _atributos_, los elementos pueden ser  texto, imágenes, listas, vídeos, o canvas.

Este [editor](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_default) en linea, nos permite ir previsualizando nuestra página web.


## Estructura básica

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
        <td>html</td><td>Define la página</td>
    </tr>
    <tr>
        <td>head</td><td>Define información de la página</td>
    </tr>
    <tr>
        <td>body</td><td>Define el cuerpo de la página</td>
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
<ol>
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ol>

```html
<ol>
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ol>
```

### Listas No Ordenadas
<ul>
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ul>

```html
<ul>
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ul>
```

### Tablas
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

<form>
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
```html
<style>
    body {
       background-color: lightblue;
    }
    h1 {
        color: navy;
        margin-left: 20px;
    }
</style>
```



## Sintaxis

[<img src="https://www.w3schools.com/css/selector.gif">](https://www.w3schools.com/css/css_syntax.asp)

Para seguir leyendo [Tutorial](https://www.w3schools.com/css/default.asp) y [Referencia](https://www.w3schools.com/cssref/default.asp) de css.

Usamos selectores para ''buscar'' los elementos en la página, este selector puede ser:
*   Tipo de etiqueta
*   Atributo id
*   Atributo class

<style>
    h1.center {
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
<h1 class="center">Titulo</h1>
<p class="center">Texto centrado</p>
</div>


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

### Fondos

### Bordes

### Marging

### Padding

### Dimensiones


# JAVASCRIPT

Para seguir leyendo [Tutorial](https://www.w3schools.com/js/default.asp) de javascript.

<center><a href="https://github.com/sborquez/TallerDesarrolloWeb/tree/master/sesion0/Python%20y%20la%20orientación%20a%20objetos.md">Siguiente</a></center>