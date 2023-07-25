def LIST2DICT(mkeys,mvals=None):
    mdict={}
    for i,key in enumerate(mkeys):
        if mvals!=None and len(mvals)==len(mkeys):
            mdict[key]=mvals[i];
        else: 
            mdict[key]=None;
    return mdict

def templates_dict(templ_sing,templ_plr):
    SINGULAR_DICT=LIST2DICT(templ_sing,templ_sing)
    PLURAL_DICT=LIST2DICT(templ_plr,templ_plr)
    ALL_DICT=dict(tuple(SINGULAR_DICT.items())+tuple(PLURAL_DICT.items()))
    return {'sing':SINGULAR_DICT,    'plr':PLURAL_DICT,    'all':ALL_DICT    }

def templates_dict_lang(templ_sing_key,templ_sing,templ_plr_key,templ_plr):
    SINGULAR_DICT=LIST2DICT(templ_sing_key,templ_sing)
    PLURAL_DICT=LIST2DICT(templ_plr_key,templ_plr)
    ALL_DICT=dict(tuple(SINGULAR_DICT.items())+tuple(PLURAL_DICT.items()))
    return {'sing':SINGULAR_DICT,    'plr':PLURAL_DICT,    'all':ALL_DICT    }

#=====================================#

SINGULAR_TEMPLATES=['type','tag', 'category', 'archive','author',
'post','character','home','time','translation','page',
'top','bottom','version']
PLURAL_TEMPLATES=PLURALIZE(SINGULAR_TEMPLATES)
PLURAL_TEMPLATES[0]='type';
# usually ARTICLES template is called index cause it is the landing page, here we call it home
# PLURAL_TEMPLATES=[w.replace('homes','index') for w in PLURAL_TEMPLATES]

SINGULAR_TEMPLATES_ES=['tipo','tag', 'categoría', 'archivo','autor',
'escrito','personaje','inicio','tiempo','traducción','página',
'arriba','abajo','vesión']

PLURAL_TEMPLATES_ES=['tipo','tags', 'categorías', 'archivos','autores',
'escritos','personajes','inicios','tiempos','traducciones','páginas',
'arriba','abajo','versiones']


TEMPLATES_ENGLISH=templates_dict(SINGULAR_TEMPLATES,PLURAL_TEMPLATES)

TEMPLATES_SPANISH=templates_dict_lang(SINGULAR_TEMPLATES,SINGULAR_TEMPLATES_ES,PLURAL_TEMPLATES,PLURAL_TEMPLATES_ES)


# Primero va el idioma, luego una tupla con: el locale y el formato de fecha
DATE_FORMATS = {
    'en': ('en_US','%a, %d %b %Y'),
    'es': ('es_ES','%a, %d de %b %Y'), #'%Y-%m-%d(%a)'),
}

SINGULAR_keys=['type','tag', 'category','author','post',]
PLURAL_keys=PLURALIZE(SINGULAR_keys)
PLURAL_keys[0]='type';
PLURAL_dict=LIST2DICT(SINGULAR_keys,PLURAL_keys)

print(PLURAL_keys)

#Tratar de que aquí estén solo las que se usan en más de un lugar, sino usar if/else en el template
ENGLISH_LABELS={
 'about':'about',
 'translation':'translation',
 'translations':'translations',
 'version':'version',
 'versions':'versions',
 'lang':'en',
 'languages':{'es':'spanish','en':'english'},
 'display':'display',
 'bright':'bright reading',
 'dark':'dark reading',
 'home':'home',
 'by':'by',
 'toc':{'title':'Table of Contents'},
 'sink':TEMPLATES_ENGLISH['all'],
 'templates':TEMPLATES_ENGLISH['all'],
 'src':dict(tuple(TEMPLATES_ENGLISH['all'].items())+tuple({'plr':PLURAL_dict}.items())),
 'plr':PLURAL_dict,
 'search':'search',
 'calendar':'calendar',
 'more':'more',
 'less':'less',
 'site':'situs',
 'filter':'filter',
 'clavis':'clavis', # para referirme a las tags, glosario, keywords
 'type':'type',
 'tag':'tag',
 'tags':'tags',
 'character':'character',
 'post':'scripta',
 'posts':'scripta',
 'author':'author',
 'authors':'authors',
 'category':'category',
 'categories':'categories',
 'code':'code'
 }

SINGULAR_keys=['type','tag', 'category','author','post']
PLURAL_keys=['tipo','tags','categorías','personajes','escritos']

SPANISH_LABELS={
 'about':'info',
 'translation':'traducción',
 'translations':'tranducciones',
 'version':'versión',
 'versions':'versiones',
 'lang':'es',
 'languages':{'es':'español','en':'inglés'},
 'display':'contraste',
 'bright':'lectura diurna',
 'dark':'lectura nocturna',
 'home':'inicio',
 'by':'x',
 'toc':{'title':'Índice'},
 'sink':TEMPLATES_SPANISH['all'],
 'templates':TEMPLATES_SPANISH['all'],
 # 'src':TEMPLATES_ENGLISH['all'],
 'src':dict(tuple(TEMPLATES_ENGLISH['all'].items())+tuple({'plr':PLURAL_dict}.items())),
 'plr':LIST2DICT(SINGULAR_keys,PLURAL_keys),
 'search':'buscar',
 'calendar':'calendario',
 'more':'más',
 'less':'menos',
 'site':'situs',
 'filter':'filtro', # binarios de los escritos
 'clavis':'clavis',
  'type':'tipo',
  'tag':'etiqueta',
  'tags':'etiquetas',
 'character':'personaje',
 'post':'scripta', 
  'posts':'scripta',
  'author':'personaje',
 'authors':'personajes',
'category':'categoría',
'categories':'categorías', 
'code':'código'
 }

MULTI_LANG_LABELS={
 'en':ENGLISH_LABELS,   
 'es':SPANISH_LABELS,
}

LABELS=MULTI_LANG_LABELS[DEFAULT_LANG]

print('labels[templates]:',LABELS['templates'],'\n')