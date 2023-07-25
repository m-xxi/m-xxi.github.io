import os
import re
import subprocess

CLEANR = re.compile('<.*?>') 

INPUT_extension='.md'

def cleanhtml(raw_html):
  return re.sub(CLEANR, '', raw_html)

site_title=cleanhtml(TITLE)
pathtosearch=PATH

#Touch landing article so that it is always shown first
for path, currentDirectory, files in os.walk(pathtosearch):
	for file in files:
		if file.endswith(INPUT_extension) and len(file.split('-'))==2:
			#File name convention: {title}-{lang}.md
			name,lang=file.split('-')
			if name==site_title and lang==DEFAULT_LANG+INPUT_extension:
				subprocess.run(["touch", os.path.join(path, file)])
				print('BASH: touch '+file)