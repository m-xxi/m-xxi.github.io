# -*- coding: utf-8 -*-
"""
Plugin for Pelican
====================================


"""
import datetime
import pytz #timezone

from pelican import signals
from pelican.readers import BaseReader

#====================================
from inflect import engine
p = engine()
def PLURALIZE(mlist):
    return [p.plural(item) for item in mlist]

KW_TYPES_SING=['tag','author']
KW_TYPES=KW_TYPES_SING+PLURALIZE(KW_TYPES_SING)


def fromListToCSV(mlist):
    mstr=''
    for i,item in enumerate(mlist):
        if item != '':
            # print(item)
            mstr+= str(item)
            if i<len(mlist)-1:
                mstr+=','
    return mstr 

from six import text_type


def set_landing_attr(generator, metadata):
    if(text_type(metadata.get('landing'))=='True'):
        metadata['landing'] = True
    else:
        metadata['landing'] = False

def set_landing_date(generator, metadata):
    if metadata.get('landing'):
        now= datetime.datetime.now(pytz.timezone(generator.settings.get('TIMEZONE'))) 
        metadata['date']=now
        metadata['modified']=now
        # setattr(article,'locale_date',now.strftime(article.date_format))     





def set_landing_key_words(generator):
    #Landing pages only have Categories attribute (more than one category)
    settings = generator.settings
    # Author, category, and tags are objects, not strings, so they need to
    # be handled using BaseReader's process_metadata() function.
    baseReader = BaseReader(settings)
    landing_article=None
    for kw_type in KW_TYPES:
        # print('=======',kw_type)
        kws=[];
        for article in generator.articles:
            if article.in_default_lang:
                kws+=get_key_words(article,kw_type)
                if article.landing:
                # if article.fpath == settings.get('LANDING_PATH').lower():
                   landing_article=article
        #Eliminate duplicates:
        kws=list( dict.fromkeys(kws) )
        if kw_type != p.plural(kw_type) and len(kws)>1 and kw_type in KW_TYPES_SING:
            # print(kw_type,'changes to ')
            kw_type = p.plural(kw_type)

        if kw_type in ['category','author','authors','tags']:
            kws=baseReader.process_metadata(kw_type, fromListToCSV(kws))
        # print(kw_type,type(kws),kws)
        kw_list=[]
        if hasattr(landing_article,kw_type): 
            kw_list=getattr(landing_article,kw_type,'')
        all_kws=kw_list+kws
        all_kws=list( dict.fromkeys(all_kws) )   
        setattr(landing_article,kw_type,all_kws)

def get_key_words(article,kw_type):
    if hasattr(article,kw_type):
        kw_list=getattr(article, kw_type, '')
        if not isinstance(kw_list,list):
            kw_list=[kw_list];
        return kw_list if kw_list != ''  else []
    else:
        return []

def get_all_key_words(article):
    kws=[];
    for kw_type in KW_TYPES:
        kws+=get_key_words(article,kw_type)    
    return kws;

def kwrelated(generator):
    for article in generator.articles:
        related_articles=[]
        kws=get_all_key_words(article)
        for article0 in generator.articles:
            if (article0 != article) and (article0.lang == generator.settings.get('DEFAULT_LANG')):
                # if hasattr(article,'landing'):
                #     if article.landing == True:
                if article.fpath == generator.settings.get('LANDING_PATH').lower():
                    #landing article relates with everybody
                    related_articles+=[article0.slug];
                else:
                    kws0=get_all_key_words(article0)  
                    if any([True if kw in kws0 else False for kw in kws]):
                        related_articles+=[article0.slug];
        setattr(article,'kwrelated',related_articles)

def set_landing_articles(generator,metadata):
    set_landing_attr(generator,metadata)
    set_landing_date(generator,metadata)

def create_landing_page(generator):
    # Where to output the generated files. 
    home=generator.settings.get('OUTPUT_PATH')
    import subprocess
    import time
    for article in generator.articles:
        if article.in_default_lang and article.landing:
            src=home+'/'+article.save_as
            print(src)
            print(home)
            subprocess.run(["cp", src, home])

    # subprocess.run(["pelican", "-s","pelicanconf.py"])
import re
from slugify import slugify
CLEANR = re.compile('<.*?>') 

def cleanhtml(raw_html):
  return re.sub(CLEANR, '', raw_html)

def create_landing_page(pelican_object):
    # Where to output the generated files. 
    home=pelican_object.settings.get('OUTPUT_PATH')+'/'
    title=slugify(cleanhtml(pelican_object.settings.get('TITLE').lower()))
    src=home+"situs/"+title+"/index.html"
    import subprocess
    print(src)
    print(home)
    subprocess.run(["cp", src, home])

def register():
    signals.article_generator_context.connect(set_landing_articles)
    signals.article_generator_pretaxonomy.connect(set_landing_key_words)
    signals.article_generator_finalized.connect(kwrelated)
    signals.finalized.connect(create_landing_page)
    # signals.article_generator_finalized.connect(create_landing_page)
