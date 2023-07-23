mandatory files inside the templates folder, which can not be in other subfolders:

index.html 	# supposed to show all articles together, like archives
article.html # run for each articles

bypass this by using include inside this files.


I call articles, posts.


I created the HTML dict in the paths.py file:
	from the templates dir structures it obtains the file names which are the keys of HTML
## File structure
direct: templates used to show a group, e.g. tags, posts
each: templates used to show a single element of the group