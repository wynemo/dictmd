#!/usr/bin/env python
# coding: utf-8

import web
from config import settings
import google_dict_to_markdown

render = settings.render

class dictmd:
    def GET(self,para):
        i = web.input()
        word = i.get('word',None)
        md_str = None
        if word is not None:
            try:
                md_str = google_dict_to_markdown.get_markdown(word.encode('utf-8'))
            except:
                return 'error getting defination'
        return render.dictmd(md_str)
