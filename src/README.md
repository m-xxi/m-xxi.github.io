## Template structure

### Metadata

#### slug
no lo estoy usando, me hubiera gustado poner 
> SLUGIFY_SOURCE = 'fpath'

pero no lo toma, si lo hubiera tomado, no habría que poner los directorios como slug


#### keywords

*	DEFAULT_CATEGORY = LABELS['src']['posts'], i.e. posts

en el .md hay que poner category, luego el plugin more-categories crea la article attribute 'categories': las uso con mayor jerarquía que tags

* all keywords and authors should have a post with their name as a title

### structure

* Creo la variable `fpath` que indica el file path:
	*	PATH_METADATA = `'(?P<fpath>.*)/.*'`
	*   `fpath` tiene que estar escrito como slug
	*	Se usa para identificar a las traducciones:
		*	ARTICLE_TRANSLATION_ID='fpath'
* El nombre del archivo tienen el título y el lang
	*	FILENAME_METADATA = `r'(?P<title>.*)-(?P<lang>.*)'`

*	solo templates index.html y article.html, el index recorre sobre todos los articles

*	article incluye: posts, tags, authors, son los tres tipos de artículos
que están dados por 

> {% set type = article.fpath.split('/')[0] %}



### Translations

*	van en la misma carpeta, tienen el título y el basename en su idioma:
	*	FILENAME_METADATA = `r'(?P<title>.*)-(?P<lang>.*)'`

*	`fpath` se usa para identificar a las traducciones:
		*	ARTICLE_TRANSLATION_ID='fpath', por default es slug, pero no se puede hacer slug=fpath.

## BUGS

no anda pagination...

## Run
ir a la terminal a src/config

desde ahi correr
	% pelican 

por default pelican llama a pelicanconf.py
está hecho para un idioma.
este usa como index el template: homes.html

Si quiero más idiomas correr:

	% python main.py
este usa como index el template: languages.html

### style
Estoy usando sass para poder usar varibales y dividir en múltiples archivos

	% src/themes/static/css/ sass -w style.scss style.css

#### ToDo

* borrar los css y scss y dejar solo style.css y jquery-grid-picker.css


## Config

* All the setting identifiers must be set in all-caps, otherwise they will not be processed


* Unless otherwise specified, settings that refer to paths can be either absolute or relative to the configuration file. The **settings you define in the configuration file will be passed to the templates**, which allows you to use your settings to add site-wide content.

* `FORMATTED_FIELDS` = ['summary']
	* A list of metadata fields containing reST/Markdown content to be parsed and translated to HTML.


### Links

* `STATIC_CREATE_LINKS` = False
	* Create links instead of copying files. If the content and output directories are on the same device, then create hard links. Falls back to symbolic links if the output directory is on a different filesystem. If symlinks are created, don’t forget to add the -L or --copy-links option to rsync when uploading your site.

* `INTRASITE_LINK_REGEX` = '[{|](?P<what>.*?)[|}]'
	* Regular expression that is used to parse internal links. Default syntax when linking to internal files, tags, etc., is to enclose the identifier, say filename, in {} or ||. Identifier between { and } goes into the what capturing group. For details see Linking to internal content.



### Debug
ir a la terminal a src/config:

	% pelican --print-settings

muestra todas las variables fijadas y las defaults

