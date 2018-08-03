# Django

[Django](https://www.djangoproject.com/) es un framework web de alto nivel que permite el desarrollo de sitios web de manera rapida, segura y mantenible.

Es gratuito y de código abierto, tiene una comunidad próspera y activa, una gran documentación y muchas opciones de soporte gratuito y de pago.

Django es

* Completo
* Versátil
* Seguro
* Escalable
* Mantenible
* Portable

## Arquitectura

En un sitio web tradicional basado en datos, una aplicación web espera peticiones HTTP del explorador web (o de otro cliente). Cuando se recibe una petición la aplicación elabora lo que se necesita basándose en la URL y posiblemente en la información incluida en los datos POST o GET. Dependiendo de qué se necesita quizás pueda entonces leer o escribir información desde una base de datos o realizar otras tareas requeridas para satisfacer la petición. La aplicación devolverá a continuación una respuesta al explorador web, con frecuencia creando dinámicamente una página HTML para que el explorador la presente insertando los datos recuperados en marcadores de posición dentro de una plantilla HTML.

Las aplicaciones web de Django normalmente agrupan el código que gestiona cada uno de estos pasos en ficheros separados:

<img src="https://mdn.mozillademos.org/files/13931/basic-django.png">

* urls: Procesar las diferentes peticiones y las redirige a las vistas correspondiente.
* views: Reciben peticiones y generan respuestas HTTP. Las vistas acceden a datos de los modelos para satisfacer la petición.
* models: Son objetos que definen la estructura de los datos, proporcionan acceso a las bases de datos y ejecutan la lógica del negocio.
* templates: Son plantillas, toman la respuesta generada por las vistas y les dan un formato.

En resumen el flujo de trabajo:

El usuario realiza una peticion HTTP al servidor. Esta petición es procesada por _urls_ y decide cual vista es la correspondiente a la solicitud. Esta _vista_ usará los modelos para obtener datos y operar sobre ellos para luego entregar los datos al _template_ el cual generará finalmente el documento _html_ que el usuario necesita.

## Otras herramientas

Django posee varios modulos para las diferentes requisitos que nuestra aplicación puede tener.

* Formularios
* Autentificación
* Serialización
* Sitio de admintrador

<center><a href="https://github.com/sborquez/TallerDesarrolloWeb/tree/master/sesion1/Primera%20aplicación.md">Siguiente</a></center>