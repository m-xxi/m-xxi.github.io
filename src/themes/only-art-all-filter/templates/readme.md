## File structure

### mandatory files 

inside the `templates` folder, which can not be in other subfolders:

-	index.html 	# supposed to show all articles together, like archives

-	article.html # run for each articles

bypass this by using `include` inside this files.

### File names

I created the `HTML dict` in the `paths.py` file:

from the templates dir structures it obtains the file names which are the keys of HTML



- **direct**: templates used to show a group, e.g. tags, posts
- **each**: templates used to show a single element of the group

### Fractal

We do not use index.html since the home page has the same structure than all other articles

We identify home pages with metadata: 

>	landing:True

since each one will be shown in a menu in the landing page

## Template code

in the .html templates we use in upper case python variables defined in src/config