# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True



# Path to blog content
PATH = REL_TO_CONFIG_PATH+'content'
LANDING_PATH=SITENAME
ARTICLE_EXCLUDES = [LABELS['posts']+'/'+LABELS['src']['versions']]




#Reads title from filename
FILENAME_METADATA = '(?P<title>.*)'
#Reads category from path
# PATH_METADATA= '(?P<subcategory_path>.*)/.*'
# PATH_METADATA = '(?P<category>.*)/.*'
# PATH_METADATA = '(?P<fpath>.*)/.*'
# PATH_METADATA = 'articles/(?P<category>.*)/.*'
PATH_METADATA = r'(?P<category>.*?)/(?P<fpath>.*)/.*'

#*?, +?, ??
#The '*', '+', and '?' quantifiers are all greedy; they match as much text as possible. Sometimes this behaviour isn’t desired; if the RE <.*> is matched against '<a> b <c>', it will match the entire string, and not just '<a>'. Adding ? after the quantifier makes it perform the match in non-greedy or minimal fashion; as few characters as possible will be matched. Using the RE <.*?> will match only '<a>'.
#Pongo <type>.*? para que <type> sea el nombre de la primer carpeta

# FILENAME_METADATA = r'(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'
FILENAME_METADATA = r'(?P<title>.*)-(?P<lang>.*)'
# SLUGIFY_SOURCE = 'fpath' # no anda...
SLUGIFY_SOURCE = 'title'
# SLUGIFY_SOURCE = 'basename' #i.e. file's name



## Path to input static folders, relative to PATH
STATIC_PATHS = [
    "static/images", "static/icons",
]

ICON_DIR='static/icons'


THEME_STATIC_PATHS = ['static']#INPUT in the THEME PATH


