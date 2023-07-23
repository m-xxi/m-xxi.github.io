#=========
DELETE_OUTPUT_DIRECTORY = True # Delete output directory before build
OUTPUT_RETENTION = [".git"]
OUTPUT_PATH = REL_TO_CONFIG_PATH+'../'+GITHUB['url']+'/'+LANG_DIR
if not os.path.exists(OUTPUT_PATH):
    os.makedirs(OUTPUT_PATH)

#=========
# Path to theme's static css/imgs/js relative to the OUTPUT PATH
THEME_STATIC_DIR='../' if MULTI_SITE else ''; #Need to localte the theme's static dir in the home page: '../'
THEME_STATIC_DIR+='static/theme' 
#=========

URLS={}
SAVE_AS={}
URLS['top']='#'
URLS['bottom']='#'+LABELS['sink']['bottom']


fname='{category}/{slug}';  
ARTICLE_URL = fname;   #The URL to refer to an article.
ARTICLE_SAVE_AS = fname+'/index.html';  # The place where we will save an article.
# '{lang}/'+
ARTICLE_LANG_URL = fname if MULTI_SITE else '' #The URL to refer to an article which doesn’t use the default language.
ARTICLE_LANG_SAVE_AS = '' #we don't need to save it since we run main.py
STATIC_LANG_SAVE_AS='{path}'

ARTICLE_TRANSLATION_ID='fpath'

#{category}: el mismo para todos los idiomas, se saca de los directorios principales: 'content/<category>/<fpath>'
#{fpath}: solo sirve para ARTICLE_TRANSLATION_ID, i.e. unificar artículos con un mismo idioma
#{slug}: titulo



#Esto sería si quiero poner más archivos dentro de cada autor, post o tag
# e.g. fotos?
# ver {attach} sintax
# AUTHOR_SAVE_AS = SAVE_AS['author']+"/{slug}/index.html"
# TAG_SAVE_AS = SAVE_AS['tag']+"/{slug}/index.html"
# ARTICLE_SAVE_AS = SAVE_AS['post']+'{slug}/index.html' # The place where we will save an article.
# ARTICLE_LANG_SAVE_AS = SAVE_AS['post']+'{slug}-{lang}/index.html'


#=========
#Only articles

ARCHIVES_SAVE_AS='' 
AUTHOR_SAVE_AS = ''
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
PAGE_SAVE_AS = ''
PAGE_LANG_SAVE_AS = ''
#=========
#All keywords
PAGE_LANG_URL = ''
TAG_URL = ''
CATEGORY_URL = ''

#=========
FEED_ALL_ATOM='' #'feeds/all.atom.xml',
CATEGORY_FEED_ATOM='' #'feeds/{slug}.atom.xml',
AUTHOR_FEED_ATOM='' #'feeds/{slug}.atom.xml',
AUTHOR_FEED_RSS='' #'feeds/{slug}.rss.xml',
TRANSLATION_FEED_ATOM='' #'feeds/all-{lang}.atom.xml',

from datetime import date

COPYRIGHT={};
COPYRIGHT['label'] = '©'+USER+str(date.today().year)
COPYRIGHT['url']= LANG_DIR+'/' if MULTI_SITE else ''
COPYRIGHT['url']+=slugify(LABELS['site'])+'/'+slugify(LABELS['code'])

INFO={}
INFO['label'] = LABELS['about']
INFO['url']= LANG_DIR+'/' if MULTI_SITE else ''
INFO['url']+=slugify(LABELS['site'])+'/'+slugify(LABELS['about'])

HOME={};
HOME['label'] = LABELS['home'];
HOME['url']= LANG_DIR+'/' if MULTI_SITE else ''