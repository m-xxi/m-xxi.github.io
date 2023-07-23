DEFAULT_LANG = 'es'
AUTHOR = 'lea'
USER='m-xxi'
SITENAME = USER.upper()
#'<img src="/images/mi.manuscrito.titulo.png" alt="screenshot" style="width:200px;" />'

GITHUB={'user':USER,'project':'project','url':'m-xxi.github.io'}

if 'SUBTITLE' not in locals():
    TITLE = '<mxxi>Manuscrito XXI</mxxi>' #'blog existencial'
    SUBTITLE = '<mxxi>Manuscrito XXI</mxxi>' #'blog existencial'
    SUBTEXT = 'Un recurso de un recursante cursando, en el siglo XXI, un curso recursivo.' #' en la existencia.'
    SUBTEXT = 'un recurso precursor a la excursión incursiva'

#Si hay dos sitios distintos para cada lenguaje se define LANG_DIR en el main.py
if 'LANG_DIR' not in locals():
    LANG_DIR='.'
    MULTI_SITE_DIR='.'
    # DEFAULT_LANG='en'
    MULTI_SITE=False
else:
    DEFAULT_LANG=LANG_DIR;
    MULTI_SITE=True

print(f"LANG:{LANG_DIR}")

BIND='127.0.0.1';PORT=8001
SITEURL = 'https://'+SITENAME.lower()+".com" if PUBLISH else "http://"+BIND+":"+str(PORT)

HOMEURL=SITEURL + '/'+LANG_DIR

print(f"SITEURL:{SITEURL}")
