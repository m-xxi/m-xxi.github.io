from jinja2 import Template, Environment,FileSystemLoader
from pathlib import Path

import sys
sys.path.append('.')

# from catalog import set_catalog

def main():
	import pelicanconf as xx
	# Pongo el reload porque para que vuelva a buscar el archivo conf si llamo a main varias veces, e.g. si lo modifico al conf.py con otra configuración en el medio
	import importlib
	# importlib.reload(xx)

	import my.pelicanconf_ES as ES
	import my.pelicanconf_EN as EN	

	sites=[ES,EN]
	template_dirs = xx.THEME + '/templates'


	j2_env = Environment(autoescape=True,
		trim_blocks=True,
		loader=FileSystemLoader(template_dirs)
		)
############# HOME ############
	j2_template = j2_env.get_template('/landing.html')

	home_html=j2_template.render(sites=sites, 
		SITENAME=xx.SITENAME,
		DISPLAY_MENU=False,
		THEME_STATIC_DIR=xx.THEME_STATIC_DIR,
		ICON_DIR=xx.ICON_DIR)
	with open(xx.OUTPUT_PATH+'/index.html', "w", encoding="utf-8-sig") as report:
		report.write(home_html)	
############# DRAFTS ############

	# j2_template = j2_env.get_template('/drafts.html')

	# draft_html=j2_template.render( SITENAME=xx.SITENAME)
	# with open(xx.OUTPUT_PATH+'drafts/index.html', "w", encoding="utf-8-sig") as report:
	# 	report.write(drafts_html)	
