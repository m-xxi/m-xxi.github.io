import sys

from pathlib import Path
home = str(Path.home())

sys.path.append('./')
# home+'/projects/catalogo.simple/src')


import my.funcs as my

def pelicanconf(lang):

	CONF_PATH='./'
	conf_original=my.join(CONF_PATH+'pelicanconf.py',CONF_PATH+'my/pelicanconf_'+lang+'.py')
	import subprocess
	# subprocess.run(["cd", "config"])
	subprocess.run(["pelican", "-s","pelicanconf.py"])
	with open (CONF_PATH+'pelicanconf.py', 'w') as fp:
		fp.write(conf_original)

def main():



	import render_home
	render_home.main()
	
	pelicanconf('EN')
	pelicanconf('ES')

if __name__ == "__main__":
	main()


	# original=join('config/jorge_conf.py','config/conf.py','config/conf.py')
	# main()

	# with open ('config/conf.py', 'w') as fp:
	# 	fp.write(original)
