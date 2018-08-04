# W3.CSS

## Introducción

Hasta el momento solo hemos creado la estructura de la página, utilizando Django como nuestro framework para el manejo de solicitudes, interacciones con la base de datos y generar documentos HTML para mostrar en el navegador. Pero una página web no es nada sin un buen diseño.

Al igual que existen frameworks para la construcción del servidor como lo es Django, también existen frameworks para el diseño web.

(W3.CSS)[https://www.w3schools.com/w3css/default.asp] es un framework sencillo, ligero, fácil de aprender y enfocado al diseño responsivo (adaptable a diferentes tamaños de pantallas) y por supuesto, gratis.

## Como usar

Al igual que cualquier documento de CSS, debe ser incluido utilizando en la cabecera de un documento HTML con la etiqueta __link__. Además es necesario incluir una etiqueta __meta__ para hacer nuestra página responsiva.

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
```

También podemos optar por cargarlo localmente, para esto tendriamos que (descargarlo)[https://www.w3schools.com/w3css/w3css_downloads.asp] y luego incluirlo al documento HTML.


```html
<link rel="stylesheet" href="w3.css">
```

Luego, bastaria con utilizar las clases entregadas por el framework en las etiquetas de nuestro documento HTML.


## Un ejemplo sensillo

Para demostrar algunos ejemplos de como utilizar W3.CSS vamos a crear un documento HTML llamado __w3.html__

En este creamos la estructura básica de cualquier documento HTML e incluimos el framework W3.CSS

```html
<!DOCTYPE html>
<html>
    <title>W3.CSS</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<body>

</body>
</html>
```

### La clase básica

La clase que probablemente más se repita es el __w3-container__. Su función es agregar un relleno a ambos lados de 16px, además de proveer igualar de margenes, alineamiento, fuentes y color entre las diferentes elementos de nuestra contenedor.

Generalmente se utiliza en los siguientes elementos:

* div
* header
* footer
* form

Agregagmos el siguiente código dentro de body

```html

<header class="w3-container">
    <h1> Esto es un título </h1>
    <h2> Esto es un subtótulo </h2>
</header>

<div class="w3-container">
  <p>Este es un contenedor.</p>
</div>


<footer class="w3-container">
   <h5> Pie de pagina </h5>
</footer>
```

### Colores

W3.CSS dispone de una paleta de colores básados en ´materials, ampliamente usado en el diseño web. La lista de colores se puede encontrar [aquí](https://www.w3schools.com/w3css/w3css_colors.asp).

Para utilizarlo disponemos de cinco clases, debemos reemplazar la palabra _color_ por el color que queramos usar:

* w3-color  : para asignarle color de fondo a un container.
* w3-text-color : para asignarle el color del text de un container.
* w3-border-color: para asignarle el color del borde a un container.
* w3-hover-color: para asignarle un color para cuando el mouse esté encima del container.
* w3-hover-text-color: para asignale un color al texto para cuando el mouse esté encima del container.

Modifiquemos el ejemplo anterior y agreguemosle colores

```html
<header class="w3-container w3-deep-orange">
    <h1> Esto es un título </h1>
    <h2> Esto es un subtótulo </h2>
</header>

<div class="w3-container w3-light-gray">
  <p>Este es un contenedor.</p>
</div>


<footer class="w3-container w3-deep-orange">
   <h5> Pie de pagina </h5>
</footer>

```

### El sistema de grillas (grid)

El sistema de grillas nos permite dividir de manera equitativa la página web en 12 columnas adaptable al tamaño de la pantalla.

Para esto se nos da dos clases:
* w3-row para crear un contendedor que tendrá las columnas
* w3-col para una columna, se debe especificar su tamaño con:
    * s1 - s12 para pantallas pequeñas
    * m1 - m12 para pantallas medianas
    * l1- l12 para pantallas grandes

podemos usar diferentes tamaños de columnas para el mismo contenedor, siempre que sean para diferentes pantallas, en este caso se mostrará el tamaño correspondiente a la pantalla.

Ejemplo

```html
<div class="w3-row">
  <div class="w3-col s6 w3-green w3-center"><p>s6</p></div>
  <div class="w3-col s6 w3-dark-grey w3-center"><p>s6</p></div>
</div>
<div class="w3-row">
  <div class="w3-col s3 w3-green w3-center"><p>s3</p></div>
  <div class="w3-col s9 w3-dark-grey w3-center"><p>s9</p></div>
</div>
<div class="w3-row">
  <div class="w3-col s4 w3-green w3-center"><p>s4</p></div>
  <div class="w3-col s4 w3-dark-grey w3-center"><p>s4</p></div>
  <div class="w3-col s4 w3-red w3-center"><p>s4</p></div>
</div>
<div class="w3-row">
  <div class="w3-col m3 w3-green w3-center"><p>m3</p></div>
  <div class="w3-col m6 w3-dark-grey w3-center"><p>m6</p></div>
  <div class="w3-col m3 w3-red w3-center"><p>m3</p></div>
</div>
<div class="w3-row">
  <div class="w3-col m2 w3-green w3-center"><p>m2</p></div>
  <div class="w3-col m2 w3-red w3-center"><p>m2</p></div>
  <div class="w3-col m2 w3-blue w3-center"><p>m2</p></div>
  <div class="w3-col m2 w3-dark-grey w3-center"><p>m2</p></div>
  <div class="w3-col m2 w3-black w3-center"><p>m2</p></div>
  <div class="w3-col m2 w3-purple w3-center"><p>m2</p></div>
</div>
```

### Sistema responsivo

Finalmente podemos mostrar y ocultar elementos dependiendo del tamaño de la pantalla. Para esto usamos las clases:

```html
<div class="w3-container w3-hide-small w3-red">
  <p>w3-hide-small will be hidden on small screens (phones)</p>
</div>

<div class="w3-container w3-hide-medium w3-green">
  <p>w3-hide-medium will be hidden on medium screens (tablets)</p>
</div>

<div class="w3-container w3-hide-large w3-blue">
  <p>w3-hide-large will be hidden on large screens (laptops/desktop)</p>
</div>
```

### Y más

Lo anterior es solo una pequeña parte de las clases disponibles en W3.CSS. Otras clases disponibles nos pueden ayudar para los formularios, listas, tablas, navegación, imagenes, alertas, animaciones, entre otras más. Además, existe una lista de templates disponibles que utilizan al máximo las capacidades de W3.CSS en el siguiente [link](https://www.w3schools.com/w3css/w3css_templates.asp), son gratuitos por lo que pueden utilizarse como base para contruir nuestros propios diseños.
