
* cambiar una letra del font family... la I


* no anda keyw_clouds option SelectArticlesFromSelectClass cuando estoy dentro de un artículo (i.e. cuando se usa el sidenav desde article.html). Si anda desde la página principal (index.html)
	* seguro tiene que ver qu son dos archivos diferentes
* sacar la variable URLS
* que al apretar sobre article-tags, muestre en violeta en el rightnav el tag apretado

* button: 'more'/'details' en la configuración dentro del rightnav

* distinto color a las categorias, tags y authors, jquery-grid-picker no me deja...


* 	templates/tags y authors son iguales, capaz hacer en extend o include, recordar el uso de {{super()}} para que use las variables anteriores o algo así

* que tags y authors muestren detalles de cada uno , así como articles muestra detalles de cada artículo
	el de tags es un glosario
	el de authors es una reseña biblio/CV...
	
*	nombre de templates repetidos en distintas carpetas...

* If you want to publish the website you probably want to minify assets to save bandwidth and reduce the loading time. Have a look at webassets (https://github.com/pelican-plugins/webassets), a plugin that makes assets management as easy as pie.

*  sitemap, which is very easy to setup and provides an important tool for search engines to discover your site.

## Images

### Specific folder
*	ver como incluir images dentro de la carpeta article-cat/article-slug/ en vez de todas juntas dentro de static/images

### Markdown
.md:
Image: post01.jpg

.jinja2
<a href="single.html" class="image featured"><img src="images/{{ article.image }}" alt="" /></a>
          {{ article.content }}


