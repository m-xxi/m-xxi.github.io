import datetime

from pelican import signals
from pelican.contents import Article
from pelican.readers import BaseReader


def addArticle(articleGenerator):
    settings = articleGenerator.settings

    # Author, category, and tags are objects, not strings, so they need to
    # be handled using BaseReader's process_metadata() function.
    baseReader = BaseReader(settings)

    content = "I am the body of an injected article!"

    newArticle = Article(content, {
        "fpath":'test',
        'status':'published',
        "title": "Injected Article!",
        "date": datetime.datetime.now(),
        "category": baseReader.process_metadata("category", "fromAPI"),
        "tags": baseReader.process_metadata("tags", "tagA, tagB"),
        "authors": baseReader.process_metadata("authors", "aatagA, aatagB"),
    })

    articleGenerator.articles.insert(0, newArticle)
def addCat(articleGenerator):
    for article in articleGenerator.articles:
        if article.fpath == articleGenerator.settings.get('LANDING_PATH').lower():
            landing_article=article
    kws=BaseReader.process_metadata('category', "fromAPI")
    # setattr(landing_article,'category',kws)  
    setattr(landing_article,'fpath','ttttttt')  


def register():
    signals.article_generator_pretaxonomy.connect(addArticle)
    # signals.article_generator_pretaxonomy.connect(addCat)