#!/usr/bin/env python
#coding:utf-8
import re
import urllib2
std_headers = {
    'User-Agent': 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.12) Gecko/20101028 Firefox/3.6.12',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-us,en;q=0.5',
                }
                
bootstrap_css = '<link rel="stylesheet" href="http://twitter.github.com/bootstrap/assets/css/bootstrap.css">'
def get_dict_html_str(word):
    flag = re.S|re.I|re.X
    url1='http://www.google.com/search?hl=en&tbs=dfn:1&q='
    request = urllib2.Request(url1 + word, None, std_headers)
    i1 = urllib2.urlopen(request)
    str1=i1.read()
    i1.close()
    pattern1=r'<\s*?div\s+?id\s*?=\s*?"\s*?ires\s*?".+<\s*?/\s*?ol\s*?>\s*?<\s*?/div\s*?>'
    pattern2=r'<\s*?h5.+?>\s*?Web\s+definitions.+?(?=</ol>)'
    rv = ''
    o1=re.search(pattern1,str1,flag)
    if o1:
        g1=o1.group()
        pattern2 = re.compile(pattern2,flag)
        rt_str = re.sub(pattern2,'',g1,1)
        rv += '<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><title>' + word + '</title>' + bootstrap_css + '</head><body>'
        rv += rt_str 
        rv += '</body></html>'
    return rv

def main():
    import sys
    print get_dict_html_str(sys.argv[1])

if __name__=="__main__":
    main() 

