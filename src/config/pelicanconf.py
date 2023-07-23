# (base) ruiz@MacBook config % pelican -s pelicanconf.py -e "LANG_DIR='es'"
# All templates will receive the variables defined in your settings file, 
# as long as they are in all-caps. You can access them directly
# pelican --print-settings 

import os
PUBLISH = os.environ.get("PUBLISH"); print(f"PUBLISH: {PUBLISH}")
DEBUG = os.environ.get("DEBUG"); print(f"DEBUG: {DEBUG}")

# Because pelicanconf.py is in a folder different than the main src folder
# Maybe it should be better to run from the src folder..., but then instead of calling simply 'pelican' it would be 'pelican -s path/pelicanconf.py'
REL_TO_CONFIG_PATH='../';       

THEME_NAME='only-art-all-filter'; #Papyrus';mwe' #
THEME=REL_TO_CONFIG_PATH+'./themes/'+THEME_NAME; 
#https://github.com/aleylara/Papyrus/tree/a4ae976473ea7a36496b4f1196829f953fe0e303
# notmyidea'

pyfiles=["my/basic",'my/keywords', "my/languages",
THEME+"/templates/paths",
"my/display","my/paths_input","my/paths_output",
"my/plugins"]
# THEME+"/templates/landing",

for f in pyfiles:
    # This executes the .py code as copy paste in this file:
    exec(open("./"+f+".py").read()) 