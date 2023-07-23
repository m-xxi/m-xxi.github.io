# It is called from pelicanconf.py
# exec(open(THEME+"/paths.py").read())
# PATHS relative to index
# paths={
# 'direct':'direct',
# 'each':'each',
# 'funcs':'funcs',
# 'layouts':'layouts',
# 'partial':'layouts/partial'
# }

# html_files={
# 	'home':['languages'],
# 	'direct':['archives','articles','authors','homes','tags','times','translations'],
# 	'each':['article','author','page','tag'],
# 	'funcs':['translations'],
# 	'layouts':['algolia.search','base','footer','header','minimal','recourse','related','search'],
# 	'navagation':['navbar','rightnav','topnav']

htmldict={}

import os
from slugify import slugify
# for x in os.listdir(THEME+'/templates'):
# 	# if x.endswith(".html"):
# 		# Prints only text file present in My Folder
# 	print(x)

# pathtosearch=os.path.abspath(THEME+'/templates')
pathtosearch=THEME+'/templates'
blocklist=['copy','old']
whishlist=['']

for path, currentDirectory, files in os.walk(pathtosearch):
    for file in files:
    	# print(file)
    	# if any(i in file for i in wishlist) and  all(i not in file for i in blocklist):
    	if all(i not in os.path.join(path, file) for i in blocklist):
	        if file.endswith(".html"):
	        	# print(os.path.join(path, file))
	        	path_rel_to_index=path.split(pathtosearch,1)[1]

	        	slug=slugify(file[:-5])
	        	#dict keys in pelican can not have '-', need underscore
	        	slug=slug.replace('-','_')
	        	fname=os.path.join(path_rel_to_index, file)
	        	print(path_rel_to_index, file, slug)
	        	#se repite el nombre translations
	        	if 'funcs/translations' in fname:
	        		slug+='_funcs'

	        	htmldict[slug]={'name':file,'path':path_rel_to_index,'fname':fname}
        		# print('#####----',file,fname)

HTML=htmldict

# THEME_TEMPLATES_OVERRIDES=[os.path.abspath(THEME+'/templates/direct')]
# print(os.path.abspath(THEME+'/templates/direct'))


# MYTEMPLATE={
#     'html':htmldict
# }

# import pathlib
# templatefiles = pathlib.Path(THEME+'/templates')

# # [print(file) for file in list(templatefiles.glob("*"))]

# from glob import glob
# [print(file) for file in glob(os.path.abspath(THEME+'/templates')+'/**/*.html',recursive=True)]


