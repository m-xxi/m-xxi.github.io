# -*- coding: utf-8 -*-
"""
Plugin for Pelican
====================================


"""
import datetime
import pytz #timezone

import logging
from pelican import signals
from pelican.readers import BaseReader

log = logging.getLogger(__name__)

def test(sender):
    log.debug("%s initialized !!", sender)

KW_types=['category','tags','authors']


def fromListToCSV(mlist):
    mstr=''
    for i,item in enumerate(mlist):
        if item != '':
            print(item)
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


def set_landing_attr_old(generator):
    for article in generator.articles:
        if hasattr(article,'landing') and article.landing == 'True':
            setattr(article,'landing',True)
        else:
            setattr(article,'landing',False)

def set_landing_date_with_touch(generator):
    #pelican needs to run twice, since this runs after sorting articles
    #do not know how to run before it sorts articles.
    for article in generator.articles:
        if hasattr(article,'landing') and article.landing == 'True':
            import subprocess
            subprocess.run(["touch", str(article)])

def set_landing_date(generator, metadata):
    if metadata.get('landing'):
        now= datetime.datetime.now(pytz.timezone(generator.settings.get('TIMEZONE'))) 
        metadata['date']=now
        metadata['modified']=now
        # setattr(article,'locale_date',now.strftime(article.date_format))     



def set_landing_date_old(generator):
    settings = generator.settings
    for article in generator.articles:
        if article.landing:
            now= datetime.datetime.now(pytz.timezone(settings.get('TIMEZONE'))) 
            setattr(article,'modified',now)
            setattr(article,'locale_date',now.strftime(article.date_format))     
            return


def set_landing_key_words(generator):
    settings = generator.settings
    # Author, category, and tags are objects, not strings, so they need to
    # be handled using BaseReader's process_metadata() function.
    baseReader = BaseReader(settings)
    landing_article=None
    for kw_type in KW_types:
        kws=[];
        for article in generator.articles:
            if article.in_default_lang:
                kws+=get_key_words(article,kw_type)
                if article.landing:
                # if article.fpath == settings.get('LANDING_PATH').lower():
                   landing_article=article
        kws=list( dict.fromkeys(kws) )
        kws=baseReader.process_metadata(kw_type, fromListToCSV(kws))
        setattr(landing_article,kw_type,kws)

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
    for kw_type in KW_types:
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
    # set_landing_key_words(generator)


def set_landing_articles(generator,metadata):
    set_landing_attr(generator,metadata)
    set_landing_date(generator,metadata)


def register():
    signals.initialized.connect(test)
    # signals.article_generator_pretaxonomy.connect(set_landing_date_with_touch)
    # signals.article_generator_pretaxonomy.connect(set_landing_attr)
    signals.article_generator_context.connect(set_landing_articles)
    # signals.article_generator_pretaxonomy.connect(set_landing_date)
    signals.article_generator_pretaxonomy.connect(set_landing_key_words)
    signals.article_generator_finalized.connect(kwrelated)
