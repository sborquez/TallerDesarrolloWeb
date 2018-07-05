# Blog


Crear las siguientes vistas para nuestra aplicación.

<table class="standard-table">
 <thead>
  <tr>
   <th scope="col">Pagina</th>
   <th scope="col">URL</th>
   <th scope="col">Requisitos</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>Home page</td>
   <td><code>/</code> and <code>/blog/</code></td>
   <td>Una página inicial que describa el sitio</td>
  </tr>
  <tr>
   <td>Lista de todos las publicaciones del blog</td>
   <td><code>/blog/posts/</code></td>
   <td>
    <p>Lista de todos las publicaciones&nbsp;del blog:</p>
    <ul>
     <li>Titulo de cada post</li>
     <li>Contenido de cada post</li>
     <li>Blogger de cada post y link a sus perfiles</li>
    </ul>
   </td>
  </tr>
<tr>
   <td>Blog post</td>
   <td><code>/blog/post/<em>&lt;post-id&gt;</em></code></td>
   <td>
    <p>Detalles del post.</p>
    <ul>
     <li>Titulo, contenido y blogger.</li>
    </ul>
   </td>
  </tr>
   <tr>
   <td>Lista de todos los bloggers</td>
   <td><code>/blog/bloggers/</code></td>
   <td>
    <p>Lista de todos los bloggers:</p>
    <ul>
     <li>Nombres, apellido y un link a su página</li>
    </ul>
   </td>
  </tr>
  <tr>
   <td>Blog autor (blogger) pagina de detalles</td>
   <td><code>/blog/blogger/<em>&lt;author-id&gt;</em></code></td>
   <td>
    <p>Información sobre el blogger</p>
    <ul>
     <li>nombre, apellido y ciudad</li>
     <li>lista de sus posts</li>
    </ul>
   </td>
  </tr>
 </tbody>
</table>