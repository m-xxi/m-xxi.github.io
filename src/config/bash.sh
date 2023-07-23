pelican -help:
-l: listen
-r: autoreload
-s: settings file

pelican -l -s pelicanconf.py -e DEFAULT_LANG='"es"'

pelican -l -r -s pelicanconf.py -e DEFAULT_LANG='"es"'

sass -w style.scss style.css