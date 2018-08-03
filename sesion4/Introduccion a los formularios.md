# Introducción a los formularios

Los formularios de HTML son la manera más fácil de pedir información al usuario. Con esta información podemos crear, actualizar o borrar datos de nuestra base de datos, modificar el Modelo. Django incluye su propio módulo para la implementación sencilla de formularios en nuestra aplicación web, sin embargo es necesario conocer como son creados normalmente con etiquetas de HTML.

## Formularios de HTML

Los [HTML Forms](https://www.w3schools.com/html/html_forms.asp) son un conjuntos de campos de entrada y widgets en una página web, su función es recolectar diferentes datos por parte del usuario en el navegador y luego enviarlos al servidor para que pueda realizar las operaciones correspondientes.

Son una herramienta flexible, soportan una gran variedad de tipos de datos, cajas de texto, checkbox, droplist, ratio buttons, dates, numbers, etc. Además de ser un mecanismo relativamente seguro para el envio de información, ya que suelen utilizar el método de _POST_ para el envio de las solicitudes.

Hasta el momento no hemos construido ningún formulario por nosotros, sin embargo ya hemos vistos los formularios creados automaticamente por la vista del administrador, un ejemplo es el de [crear nuevo blogger](http://127.0.0.1:8000/admin/blog/blogger/add/).

Veremos como crear el mismo formulario usando la notación de HTML

### sintaxis

```html
<form action="/blogger_add/" method="post">
    <label for="name">Nombre: </label>
    <input id="name" type="text" name="name_field" placeholde="Ingrese su nombre">
    <label for="lastname">Apellido: </label>
    <input id="lastname" type="text" name="lastname_field" placeholde="Ingrese su apellido">
    <label for="city">Ciudad: </label>
    <input id="city" type="text" name="city_field" placeholde="Valparaiso">
    <label for="email">Correo: </label>
    <input id="email" type="email" name="email_field">
    <input type="submit" value="OK">
</form>
```

Puede utilizar este [editor](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_form_submit) para probar las difetentes etiquetas y tipos.

Explicación

1. __form__ especifica a un formulario, posee dos atributos _action_ y _method_.

    * __action__ indica quien se encargará de manipular la solicitud, esta puede ser una url o incluso puede ser una función de javascript, por ahora solo usaremos la url.

    * __method__ indica si la solicitud se hará usando POST o GET, la primera tiene la particularidad de que los datos enviados no son mostrados al usuario. Al contrario de GET, donde los datos enviados son incluidos en la url de la solicitud, por lo tanto visible.

2. __label__ espefica el texto que acompaña a cada input, debe usarse el atributo _for_ indicandole la _id_ del inputs correspondiente.

3. __input__ este es quien interactua con el usuario.
    * __id__ como cualquier elemento de HTML es utilizado para identificar a input para CSS o JS

    * __type__ el más importante, indica que tipo de input se espera, por ejemplo: texto plano, un número, fecha entre otras. La lista completa de los tipos de datos puede encontrarse [aquí](https://www.w3schools.com/tags/att_input_type.asp).

    * __value__ corresponde al valor predeterminado en caso de no ingresar valores.

    * __placeholder__ es el texto que se muestra antes de ingresar alguna entrada al input.

La construcción de un formulario puede volverse tediosa o complicada por el hecho de tener que validar datos, poner valores predefinidos, etc. En la siguiente sección aprenderemos a utilizar las herramientas de creación de formularios de Django.

