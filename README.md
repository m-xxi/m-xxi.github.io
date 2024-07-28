# m-xxi.github.io
manuscript XXI

## Run
-	In /src/config/ run

>	$% python main.py

- Manually move folders from `/mxxi/m-xxi.github.io/`m-xxi.github.io/ to `/mxxi/m-xxi.github.io/gh-pages`. This is because there is a lot of junk in static folders

-	In /mxxi/m-xxi.github.io/ run 

>	$% ghp-import -p gh-pages

## git

### Update this repo

>	$% git add .
>	$% git commit -m 'message'
>	$% git push

### online or public_html

Three alternatives:

1. we could create the `docs` dir. It is like the regular `public_html` dir.

2. we could create a gh-pages branch and publish from there, e.g. using `ghp-import`. [1](https://github.com/getpelican/pelican/blob/master/docs/tips.rst), [2](https://gist.github.com/JosefJezek/6053301). [Docs](https://github.com/c-w/ghp-import), simplest command:
	
>	$% sudo pip install ghp-import

Inside your repository just run ghp-import $DOCS_DIR where $DOCS_DIR is the path to public_html (I call it gh-pages). -p option pushes to the gh-pages branch

>	$% ghp-import -p gh-pages


3. We could use a custom deployment workflow[1](https://github.com/orgs/community/discussions/23073),[2](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#publishing-with-a-custom-github-actions-workflow),[3](https://github.com/orgs/community/discussions/21853)