#!/usr/bin/python3
from xmldt import XmlDt, toxml
import sys

class proc (XmlDt):
    _types_ = {"item":"map"}
    
    def __default__(s, e): 
        return f"{e.c}"
    
    def begin(s):
        s.items= []
    # def rss(s, e):   # 1 version(1)
    # def channel(s, e):   # 1 
    def title(s, e):   # 12  PCDATA
        e.tag = "Titulo"
        return e.xml
    # def link(s, e):   # 13 rel(1) href(1) type(1) PCDATA
    # def description(s, e):   # 11  PCDATA
    # def lastBuildDate(s, e):   # 1  PCDATA
    # def language(s, e):   # 1  PCDATA
    # def updatePeriod(s, e):   # 1  PCDATA
    # def updateFrequency(s, e):   # 1  PCDATA
    # def generator(s, e):   # 1  PCDATA
    # def image(s, e):   # 1 
    # def url(s, e):   # 1  PCDATA
    # def width(s, e):   # 1  PCDATA
    # def height(s, e):   # 1  PCDATA
    def item(s, e):   # 10 
        s.items.append(e.c)
    # def comments(s, e):   # 20  PCDATA
    # def creator(s, e):   # 10  PCDATA
    # def pubDate(s, e):   # 10  PCDATA
    # def category(s, e):   # 62  PCDATA
    # def guid(s, e):   # 10 isPermaLink(10) PCDATA
    # def commentRss(s, e):   # 10  PCDATA

file = sys.argv[1]
print(proc(filename=file))    # , empty=True
