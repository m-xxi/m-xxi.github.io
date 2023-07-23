
# If using plugin more categories:
# in .md:
# category: foo/bar, foo/b#az/quux
# Using this plugin only to have the attribute categories in article

from inflect import engine
p = engine()

def PLURALIZE(mlist):
    return [p.plural(item) for item in mlist]

KW_TYPES_SING=['category','tag','author'] 
KW_TYPES_SING=[]
KW_TYPES=PLURALIZE(KW_TYPES_SING)
KW_HASH=['\&','#','@']


#When you don’t specify a category in your post metadata, set this setting to True, and organize your articles in subfolders, the subfolder will become the category of your post. If set to False, DEFAULT_CATEGORY will be used as a fallback.

USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = ''
# LABELS['src']['posts']
# category is given by de first folder of the article file:
# PATH_METADATA = r'(?P<category>.*?)/(?P<fpath>.*)/.*'

#Only landing articles have more than one category in the categories attribute