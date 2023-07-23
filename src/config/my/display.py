DIRECT_TEMPLATES=('index',)

DEFAULT_METADATA = {
   'status': 'draft',
}

#several typographical improvements will be incorporated into the generated HTML via the Typogrify library, which can be installed via: python -m pip install typogrify
TYPOGRIFY = True

LOAD_CONTENT_CACHE = False

TIMEZONE = 'America/Argentina/Buenos_Aires'
DEFAULT_DATE ='fs' #filesystem