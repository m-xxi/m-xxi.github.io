
#########################
PLUGIN_PATHS = [REL_TO_CONFIG_PATH+'pelican-plugins']
PLUGINS = ['keyword_related','pelican-toc','tag_cloud-dict', 'readtime'] #,'subcategory']#,'i18n_subsites']
#'more_categories' , 'search','neighbors'
# Table of Content Plugin: pelican-toc
## runs on every article, does not use [TOC] command

# Table of Content Plugin: extract_toc
## uses [TOC] command per article

# Site search plugin
SEARCH_MODE = "output"
SEARCH_HTML_SELECTOR = "main"


# Table of Content Plugin: pelican-toc
TOC = {
    'TOC_HEADERS'       : '^h[1-1]', # What headers should be included in
                                     # the generated toc
                                     # Expected format is a regular expression
    'TOC_RUN'           : 'true',    # Default value for toc generation,
                                     # if it does not evaluate
                                     # to 'true' no toc will be generated
    'TOC_INCLUDE_TITLE': 'false',    # If 'true' include title in toc
}

# from mdx_include import mdx_include
import os

content_abs_path=os.path.abspath(REL_TO_CONFIG_PATH+'content')

## Python-Markdown extension configuration
MARKDOWN = {
    'extensions' : ['mdx_include'],
    "extension_configs": {
        # Needed for code syntax highlighting
        "markdown.extensions.codehilite": {
            "css_class": "highlight",
        },
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.admonition": {},
        # This is for enabling the TOC generation
        # Table of Content Plugin: extract-toc
        "markdown.extensions.toc": {
            # "title": "Contenido", 
            "toc_depth": "2-4",
            "toc_class":"toc"
        },
        'mdx_include': {
            'base_path': content_abs_path,
            'recurs_local': True,
        }
        # "markdown.extensions.mdx_include":{},
    },
    "output_format": "html5",
}



####################################
#TAGS:
# https://www.stefaanlippens.net/quick-and-easy-tag-cloud-in-pelican.html
# import math
# JINJA_FILTERS = {
#     'count_to_font_size': lambda c: '{p:.1f}%'.format(p=100 + 25 * math.log(c, 2)),
# }
TAG_CLOUD_STEPS=4 #number of different sizes of fonts in the tag cloud
TAG_CLOUD_MAX_ITEMS=100 #number of different tags that can appear in tag cloud
TAG_CLOUD_SORTING='size' #how tags will be ordered in the tag cloud. Valid values: random, alphabetically, alphabetically-rev, size and size-rev
TAG_CLOUD_BADGE=False #If True, displays the number of articles in each tag
