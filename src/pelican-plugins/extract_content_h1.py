# -*- coding: utf-8 -*-
"""
Extract Table of Content
========================

A Pelican plugin to extract table of contents (ToC) from `article.content` and
place it in its own `article.toc` variable for use in templates.
"""

from os import path
from bs4 import BeautifulSoup
from pelican import signals, readers, contents
import logging

logger = logging.getLogger(__name__)


def extract_toc(content):
    if isinstance(content, contents.Static):
        return

    soup = BeautifulSoup(content._content, 'html.parser')
    filename = content.source_path
    extension = path.splitext(filename)[1][1:]
    toc = None

    # default Markdown reader
    if not toc and readers.MarkdownReader.enabled and extension in readers.MarkdownReader.file_extensions:
        # toc = soup.find('div', class_='toc')
        toc = soup.find_all('div', class_='mytoccc')
        print("TOC:")
        print(toc)
        print("")
        for i,div in enumerate(toc):
           if toc[i]:
                toc[i].find('id')
                print(toc[i])
                print(type(toc[i]),toc[i].id)
                print("$$$$$$$$$$$$$$$$$$")
                toc[i].extract()
                print(type(toc[i]),toc[i].id)
                print("####################")
                aux=toc[i].find_all('li')
                [print(a,'\n===\n') for a in aux]

                for a in aux:
                    if toc[i].id in a:
                        print(a,'\n****\n')
                        # if type(a.string)=="<class 'bs4.element.NavigableString'>":
                        #     a.string.replace_with("")
                if toc[i].find_next('ul')!=None:
                    if len(toc[i].find_next('ul').find_all('li')) == 0:
                        toc[i] = None

    if toc:
        # toc.extract()
        content._content = soup.decode()
        content.h1=[];
    for i,div in enumerate(toc):
       if toc[i]:
            content.h1.append(toc[i].decode())
            if content.h1[i].startswith('<html>'):
                content.h1[i] = content.h1[i][12:-14]


def register():
    signals.content_object_init.connect(extract_toc)
