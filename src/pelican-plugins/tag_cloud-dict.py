'''
tag_cloud
===================================

This plugin generates a tag cloud from available tags
'''
from __future__ import unicode_literals

from collections import defaultdict
from operator import itemgetter

import logging
import math
import random

from pelican import signals

logger = logging.getLogger(__name__)


def set_default_settings(settings):
    settings.setdefault('TAG_CLOUD_STEPS', 4)
    settings.setdefault('TAG_CLOUD_MAX_ITEMS', 100)
    settings.setdefault('TAG_CLOUD_SORTING', 'random')
    settings.setdefault('TAG_CLOUD_BADGE', True)


def init_default_config(pelican):
    from pelican.settings import DEFAULT_CONFIG
    set_default_settings(DEFAULT_CONFIG)
    if(pelican):
            set_default_settings(pelican.settings)

from slugify import slugify

def generate_clouds(generator):
    
    # generator.tag_cloud =generate_cloud(generator,'tag')
    # generator._update_context(['tag_cloud'])
    
    # generator.author_cloud = generate_cloud(generator,'author')
    # generator._update_context(['author_cloud'])

    clouds={
    # 'keywords': generate_cloud(generator,['keywords']),
    'categories': generate_cloud(generator,['categories']),
    'tags': generate_cloud(generator,['tags']),
    'authors':generate_cloud(generator,['authors']),
    # 'keyw':generate_cloud(generator,['tags','authors'])
    }
    # print(clouds)
    # generator.clouds=clouds;
    generator.context['clouds']=clouds;
    # generator._update_context(['clouds'])

def generate_cloud(generator,article_attrs):
    tag_cloud = defaultdict(int)
    for article in generator.articles:
        # for tag in getattr(article, 'tags', []):
        # for tag in getattr(article, article_attrs, []):
        #     tag_cloud[tag] += 1
        for attr in article_attrs:
            attr_list=getattr(article, attr, [])
            if isinstance(attr_list, str):
                tag_cloud[attr_list] += 1
            else:
                for tag in attr_list:
                    tag_cloud[tag] += 1

    tag_cloud = sorted(tag_cloud.items(), key=itemgetter(1), reverse=True)
    tag_cloud = tag_cloud[:generator.settings.get('TAG_CLOUD_MAX_ITEMS')]

    tags = list(map(itemgetter(1), tag_cloud))
    if tags:
        max_count = tags[0]
        min_count = tags[-1]
    steps = generator.settings.get('TAG_CLOUD_STEPS')


    # calculate word sizes
    def generate_tag(tag_name, index, count):
        tag = (
            str(tag_name),
            int(math.floor(steps - (steps - 1) * math.log(count - min_count + 1)
                / (math.log(max_count - min_count + 1) or 1)))
        )
        # Le agrego un lugar a la tupla para poner el index para usarlo de referencia única (id)
        tag += (index,slugify(str(tag_name)),)
        # if generator.settings.get('TAG_CLOUD_BADGE'):
        tag += (count,)
        return tag

    # tag_cloud = [
    #     generate_tag(tag, count)
    #     for tag, count in tag_cloud
    # ]

    tag_cloud_list = [];
    index=0;
    for tag, count in tag_cloud:
        tag_cloud_list.append(generate_tag(tag,index,count))
        index=index+1;
    


    sorting = generator.settings.get('TAG_CLOUD_SORTING')

    if sorting == 'alphabetically':
        tag_cloud_list.sort(key=lambda elem: elem[0].name)
    elif sorting == 'alphabetically-rev':
        tag_cloud_list.sort(key=lambda elem: elem[0].name, reverse=True)
    elif sorting == 'size':
        tag_cloud_list.sort(key=lambda elem: elem[1])
    elif sorting == 'size-rev':
        tag_cloud_list.sort(key=lambda elem: elem[1], reverse=True)
    elif sorting == 'random':
        random.shuffle(tag_cloud_list)
    else:
        logger.warning("setting for TAG_CLOUD_SORTING not recognized: %s, "
                       "falling back to 'random'", sorting)
        random.shuffle(tag_cloud_list)

    # print(type(tag_cloud))
    # for i in range(len(tag_cloud)):
    #     tag_cloud[i][2]=i


    def convert_tuple_to_dict(mytuple,mykeys):
        mydict={}
        for i,key in enumerate(mykeys):
            mydict[key]=mytuple[i];
        return mydict;

    mykeys = ['name','size','index','slug','count']
    tag_cloud_list=[convert_tuple_to_dict(tag,mykeys) for tag in tag_cloud_list]



    # make available in context
    # generator.tag_cloud = tag_cloud_list
    # generator._update_context(['tag_cloud'])
    # generator[article_attr+'_cloud']= tag_cloud_list
    # generator._update_context([article_attr+'_cloud'])

    #Es una lista de tuplas:
    # print(tag_cloud_list)
    return tag_cloud_list

def register():
    signals.initialized.connect(init_default_config)
    signals.article_generator_finalized.connect(generate_clouds)
