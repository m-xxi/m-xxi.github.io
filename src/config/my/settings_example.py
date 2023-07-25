PUBLISH: None
LANG:.
{
    'PATH': '/Users/ruiz/projects/mxxi/src/content',
    'ARTICLE_PATHS': [''],
    'ARTICLE_EXCLUDES': ['pages'],
    'PAGE_PATHS': ['pages'],
    'PAGE_EXCLUDES': [''],
    'THEME': '/Users/ruiz/projects/mxxi/src/themes/alexis',
    'OUTPUT_PATH': '/Users/ruiz/projects/mxxi/m-xxi.github.io',
    'READERS': {},
    'STATIC_PATHS': [
        'static/images',
        'static/icons',
        '.././themes/alexis/extra'
    ],
    'STATIC_EXCLUDES': [],
    'STATIC_EXCLUDE_SOURCES': True,
    'THEME_STATIC_DIR': 'theme',
    'THEME_STATIC_PATHS': ['static'],
    'FEED_ALL_ATOM': 'feeds/all.atom.xml',
    'CATEGORY_FEED_ATOM': 'feeds/{slug}.atom.xml',
    'AUTHOR_FEED_ATOM': 'feeds/{slug}.atom.xml',
    'AUTHOR_FEED_RSS': 'feeds/{slug}.rss.xml',
    'TRANSLATION_FEED_ATOM': 'feeds/all-{lang}.atom.xml',
    'FEED_MAX_ITEMS': '',
    'RSS_FEED_SUMMARY_ONLY': True,
    'SITEURL': 'http://127.0.0.1:8001',
    'SITENAME': 'M-XXI',
    'DISPLAY_PAGES_ON_MENU': False,
    'DISPLAY_CATEGORIES_ON_MENU': True,
    'DOCUTILS_SETTINGS': {},
    'OUTPUT_SOURCES': False,
    'OUTPUT_SOURCES_EXTENSION': '.text',
    'USE_FOLDER_AS_CATEGORY': True,
    'DEFAULT_CATEGORY': 'misc',
    'WITH_FUTURE_DATES': True,
    'CSS_FILE': 'main.css',
    'NEWEST_FIRST_ARCHIVES': True,
    'REVERSE_CATEGORY_ORDER': False,
    'DELETE_OUTPUT_DIRECTORY': True,
    'OUTPUT_RETENTION': [],
    'INDEX_SAVE_AS': 'index.html',
    'ARTICLE_URL': '{slug}.html',
    'ARTICLE_SAVE_AS': '{slug}.html',
    'ARTICLE_ORDER_BY': 'reversed-date',
    'ARTICLE_LANG_URL': '{slug}-{lang}.html',
    'ARTICLE_LANG_SAVE_AS': '{slug}-{lang}.html',
    'DRAFT_URL': 'drafts/{slug}.html',
    'DRAFT_SAVE_AS': 'drafts/{slug}.html',
    'DRAFT_LANG_URL': 'drafts/{slug}-{lang}.html',
    'DRAFT_LANG_SAVE_AS': 'drafts/{slug}-{lang}.html',
    'PAGE_URL': 'pages/{slug}.html',
    'PAGE_SAVE_AS': 'pages/{slug}.html',
    'PAGE_ORDER_BY': 'basename',
    'PAGE_LANG_URL': 'pages/{slug}-{lang}.html',
    'PAGE_LANG_SAVE_AS': 'pages/{slug}-{lang}.html',
    'DRAFT_PAGE_URL': 'drafts/pages/{slug}.html',
    'DRAFT_PAGE_SAVE_AS': 'drafts/pages/{slug}.html',
    'DRAFT_PAGE_LANG_URL': 'drafts/pages/{slug}-{lang}.html',
    'DRAFT_PAGE_LANG_SAVE_AS': 'drafts/pages/{slug}-{lang}.html',
    'STATIC_URL': '{path}',
    'STATIC_SAVE_AS': '{path}',
    'STATIC_CREATE_LINKS': False,
    'STATIC_CHECK_IF_MODIFIED': False,
    'CATEGORY_URL': 'category/{slug}.html',
    'CATEGORY_SAVE_AS': 'category/{slug}.html',
    'TAG_URL': 'tag/{slug}.html',
    'TAG_SAVE_AS': 'tag/{slug}.html',
    'AUTHOR_URL': 'author/{slug}.html',
    'AUTHOR_SAVE_AS': 'author/{slug}.html',
    'PAGINATION_PATTERNS': [
        PaginationRule(min_page=1, URL='{url}', SAVE_AS='{save_as}'),
        PaginationRule(min_page=2, URL='{base_name}/{number}/', 
SAVE_AS='{base_name}/{number}/index.html')
    ],
    'YEAR_ARCHIVE_URL': '',
    'YEAR_ARCHIVE_SAVE_AS': '',
    'MONTH_ARCHIVE_URL': '',
    'MONTH_ARCHIVE_SAVE_AS': '',
    'DAY_ARCHIVE_URL': '',
    'DAY_ARCHIVE_SAVE_AS': '',
    'RELATIVE_URLS': False,
    'DEFAULT_LANG': 'es',
    'ARTICLE_TRANSLATION_ID': 'slug',
    'PAGE_TRANSLATION_ID': 'slug',
    'DIRECT_TEMPLATES': (
        'index',
        'tags',
        'categories',
        'archives',
        'authors'
    ),
    'THEME_TEMPLATES_OVERRIDES': [],
    'PAGINATED_TEMPLATES': {
        'index': None,
        'tag': None,
        'category': None,
        'author': None,
        'archives': 24
    },
    'PELICAN_CLASS': 'pelican.Pelican',
    'DEFAULT_DATE_FORMAT': '%a %d %B %Y',
    'DATE_FORMATS': {
        'en': ('en_US', '%a, %d %b %Y'),
        'es': ('es_ES', '%a, %d de %b %Y')
    },
    'MARKDOWN': {
        'extension_configs': {
            'markdown.extensions.codehilite': {
                'css_class': 'highlight'
            },
            'markdown.extensions.extra': {},
            'markdown.extensions.meta': {},
            'markdown.extensions.admonition': {},
            'markdown.extensions.toc': {
                'toc_depth': '2-4',
                'toc_class': 'toc'
            }
        },
        'output_format': 'html5'
    },
    'JINJA_FILTERS': {},
    'JINJA_GLOBALS': {},
    'JINJA_TESTS': {},
    'JINJA_ENVIRONMENT': {
        'trim_blocks': True,
        'lstrip_blocks': True,
        'extensions': []
    },
    'LOG_FILTER': [],
    'LOCALE': [''],
    'DEFAULT_PAGINATION': 100,
    'DEFAULT_ORPHANS': 0,
    'DEFAULT_METADATA': {},
    'FILENAME_METADATA': '(?P<title>.*)',
    'PATH_METADATA': '',
    'EXTRA_PATH_METADATA': {},
    'ARTICLE_PERMALINK_STRUCTURE': '',
    'TYPOGRIFY': True,
    'TYPOGRIFY_IGNORE_TAGS': [],
    'TYPOGRIFY_DASHES': 'default',
    'SUMMARY_END_SUFFIX': '…',
    'SUMMARY_MAX_LENGTH': 50,
    'PLUGIN_PATHS': [
        '/Users/ruiz/projects/mxxi/src/pelican-plugins'
    ],
    'PLUGINS': [
        'pelican-toc',
        'tag_cloud',
        'readtime',
        'pelican.plugins.search',
        'pelican.plugins.neighbors',
        'more_categories'
    ],
    'PYGMENTS_RST_OPTIONS': {},
    'TEMPLATE_PAGES': {},
    'TEMPLATE_EXTENSIONS': ['.html'],
    'IGNORE_FILES': ['.#*'],
    'SLUG_REGEX_SUBSTITUTIONS': [
        ('[^\\w\\s-]', ''),
        ('(?u)\\A\\s*', ''),
        ('(?u)\\s*\\Z', ''),
        ('[-\\s]+', '-')
    ],
    'INTRASITE_LINK_REGEX': '[{|](?P<what>.*?)[|}]',
    'SLUGIFY_SOURCE': 'basename',
    'SLUGIFY_USE_UNICODE': False,
    'SLUGIFY_PRESERVE_CASE': False,
    'CACHE_CONTENT': False,
    'CONTENT_CACHING_LAYER': 'reader',
    'CACHE_PATH': 'cache',
    'GZIP_CACHE': True,
    'CHECK_MODIFIED_METHOD': 'mtime',
    'LOAD_CONTENT_CACHE': False,
    'WRITE_SELECTED': [],
    'FORMATTED_FIELDS': ['summary'],
    'PORT': 8001,
    'BIND': '127.0.0.1',
    'ARCHIVES_SAVE_AS': 'archives.html',
    'ARCHIVES_URL': 'archives',
    'AUTHOR': 'lea',
    'AUTHORS_SAVE_AS': 'autores.html',
    'AUTHORS_URL': 'autores',
    'CATEGORIES_SAVE_AS': 'categorías.html',
    'CATEGORIES_URL': 'categorías',
    'COPYRIGHT': '©m-xxi2023',
    'COURSES': {
        'python': {
            'cid': '822444',
            'tag': 'python',
            'title': 'Python and Django Full Stack Web Developer 
Bootcamp',
            'description': 'Learn to build websites with HTML, CSS, 
Bootstrap, Javascript, jQuery, Python 3, and Django!',
            'img': 'https://img-b.udemycdn.com/course/480x270/822444_a
6db.jpg?secure=K6tKj_8lsi_hfHPsKXup8A%3D%3D%2C1647332006',
            'link': 'https://click.linksynergy.com/link?id=zOWbNCBDzko
&offerid=1060092.822444&type=2&murl=https%3A%2F%2Fwww.udemy.com%2Fcour
se%2Fpython-and-django-full-stack-web-developer-bootcamp%2F',
            'pixel': 'https://ad.linksynergy.com/fs-bin/show?id=zOWbNC
BDzko&bids=1060092.822444&type=2&subid=0'
        },
        'linux': {
            'cid': '3371848',
            'tag': 'linux',
            'title': 'Linux Administration: The Complete Linux 
Bootcamp for 2022',
            'description': 'Linux Administration (Ubuntu and CentOS) 
for Beginners. Get the Linux skills to boost your career and get 
ahead.',
            'img': 
'https://img-c.udemycdn.com/course/480x270/3371848_9ea9_6.jpg',
            'link': 'https://click.linksynergy.com/link?id=zOWbNCBDzko
&offerid=1060092.3371848&type=2&murl=https%3A%2F%2Fwww.udemy.com%2Fcou
rse%2Fmaster-linux-administration%2F',
            'pixel': 'https://ad.linksynergy.com/fs-bin/show?id=zOWbNC
BDzko&bids=1060092.3371848&type=2&subid=0'
        },
        'ubuntu': {
            'cid': '1394254',
            'tag': 'ubuntu',
            'title': 'Ubuntu Linux Fundamentals Linux Server 
Administration Basics',
            'description': "Updated for Ubuntu 20.04 - The Latest! 
Gain essential skills with Linux Server in this 11 hour Beginner's 
course.",
            'img': 
'https://img-c.udemycdn.com/course/480x270/1394254_2eb5_6.jpg',
            'link': 'https://click.linksynergy.com/link?id=zOWbNCBDzko
&offerid=1060092.1394254&type=2&murl=https%3A%2F%2Fwww.udemy.com%2Fcou
rse%2Fubuntu-server-fundamentals-manage-linux-server-with-ubuntu%2F',
            'pixel': 'https://ad.linksynergy.com/fs-bin/show?id=zOWbNC
BDzko&bids=1060092.1394254&type=2&subid=0'
        },
        'aws': {
            'cid': '2196488',
            'tag': 'aws',
            'title': 'Ultimate AWS Certified Solutions Architect 
Associate 2022',
            'description': 'Full Practice Exam Learn Cloud Computing 
Pass the AWS Certified Solutions Architect Associate Certification 
SAA-C02!',
            'img': 
'https://img-c.udemycdn.com/course/480x270/2196488_8fc7_7.jpg',
            'link': 'https://click.linksynergy.com/link?id=zOWbNCBDzko
&offerid=1060092.2196488&type=2&murl=https%3A%2F%2Fwww.udemy.com%2Fcou
rse%2Faws-certified-solutions-architect-associate-saa-c02%2F',
            'pixel': 'https://ad.linksynergy.com/fs-bin/show?id=zOWbNC
BDzko&bids=1060092.2196488&type=2&subid=0'
        },
        'firebase': {
            'cid': '1247828',
            'tag': 'firebase',
            'title': 'The Complete Angular Course: Beginner to 
Advanced',
            'description': 'Learn Angular from scratch and build 
powerful web applications with the latest tools.',
            'img': 
'https://img-c.udemycdn.com/course/480x270/1247828_32bb.jpg',
            'link': 'https://click.linksynergy.com/link?id=zOWbNCBDzko
&offerid=1060092.1247828&type=2&murl=https%3A%2F%2Fwww.udemy.com%2Fcou
rse%2Fthe-complete-angular-master-class%2F',
            'pixel': 'https://ad.linksynergy.com/fs-bin/show?id=zOWbNC
BDzko&bids=1060092.1247828&type=2&subid=0'
        }
    },
    'DEFAULT_DATE': 'fs',
    'DISPLAY_MENU': True,
    'EXTRA': '.././themes/alexis/extra',
    'GITHUB': {'user': 'm-xxi', 'project': 'project'},
    'HOME_DIR': '.',
    'ICON_DIR': 'static/icons',
    'LABELS': {
        'about': 'info',
        'version': 'versión',
        'versions': 'versiones',
        'lang': 'español',
        'display': 'contraste',
        'bright': 'lectura diurna',
        'dark': 'lectura nocturna',
        'home': 'inicio',
        'by': 'x',
        'categories': 'categorías',
        'toc': {'title': 'Índice'},
        'author': 'author',
        'authors': 'autores'
    },
    'LANG_DIR': '.',
    'MULTI_LANG_LABELS': {
        'en': {
            'about': 'info',
            'version': 'versions',
            'lang': 'english',
            'display': 'display',
            'bright': 'bright reading',
            'dark': 'dark reading',
            'home': 'home',
            'by': 'by',
            'categories': 'categories',
            'toc': {'title': 'Table of Contents'},
            'author': 'author',
            'authors': 'authors'
        },
        'es': {
            'about': 'info',
            'version': 'versión',
            'versions': 'versiones',
            'lang': 'español',
            'display': 'contraste',
            'bright': 'lectura diurna',
            'dark': 'lectura nocturna',
            'home': 'inicio',
            'by': 'x',
            'categories': 'categorías',
            'toc': {'title': 'Índice'},
            'author': 'author',
            'authors': 'autores'
        }
    },
    'MULTI_SITE_DIR': '.',
    'PROFILE_PICTURE': 'mi.manuscrito.titulo.png',
    'PUBLISH': None,
    'REL_TO_CONFIG_PATH': '../',
    'SEARCH_HTML_SELECTOR': 'main',
    'SEARCH_MODE': 'output',
    'STATIC_PATH_ALEXIS': ['.././themes/alexis/extra'],
    'SUBTEXT': 'un recurso precursor a la excursión incursiva',
    'SUBTITLE': 'Manuscrito XXI',
    'TAGS_SAVE_AS': 'tags.html',
    'TAGS_URL': 'tags',
    'TAG_CLOUD_BADGE': True,
    'TAG_CLOUD_MAX_ITEMS': 100,
    'TAG_CLOUD_SORTING': 'size',
    'TAG_CLOUD_STEPS': 4,
    'TIMEZONE': 'America/Argentina/Buenos_Aires',
    'TOC': {
        'TOC_HEADERS': '^h[1-1]',
        'TOC_RUN': 'true',
        'TOC_INCLUDE_TITLE': 'false'
    },
    'UDEMY': {'aid': 'zOWbNCBDzko', 'pid': '1060092'},
    'USER': 'm-xxi',
    'DEBUG': False,
    'FEED_DOMAIN': 'http://127.0.0.1:8001'
}
