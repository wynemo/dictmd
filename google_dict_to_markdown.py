import mk_dict
import re

def r1(pattern1,str1):
    import re
    o1 = re.search(pattern1,str1,re.I|re.S)
    return o1.group(1)

def get_header(str1):
    rv = ''
    pattern1 = r'<em>(.+?)</em>'#noun
    pattern2 = r'</em>(.+?)<span'#/tel/
    span_pattern = r'<span[^>]*>([^>]+?)</span>'#tells,plural
    rv += '**' + r1(pattern1,str1) + '**' + ' '
    rv += r1(pattern2,str1) + '\n\n'
    o1 = re.finditer(span_pattern,str1,re.I|re.S)
    str2 = ''
    if o1 is not None:
        for each in o1:
            str2 += each.group(1)
            #print 'ttt',each.group(1)
        if len(str2) != 0:
            rv += '*' + str2 + '*\n\n'
    return rv

def get_list(str1):
    rv = ''
    li_pattern = r'<li[^>]*>([^<>]+)<div.*?</li>'
    o1 = re.finditer(li_pattern,str1,re.I|re.S)
    if o1 is not None:
        for i,each in enumerate(o1):
            rv += str(i+1) + '. ' + each.group(1) + '\n'
            #print 'ttt',each.group(1)
    rv += '\n'
    return rv


def get_markdown():
    rv = ''
    str1 = mk_dict.get_dict_html_str()
    ires_pattern = r'<div id="ires">(.+)</div>'
    ires_str = r1(ires_pattern,str1)
    title_pattern = r'<span[^>]*>\s*<em>(.+?)</em></span>'
    title_str = r1(title_pattern,ires_str)
    rv += '###' + title_str
    rv += '\n'
    define_pattern = r'<p[^>]*>(.+?)</p><div[^>]*>\s*<ol>(.*?)</ol>\s*</div>'
    o1 = re.finditer(define_pattern,ires_str,re.I|re.S)
    if o1 is not None:
        for each in o1:
            rv += get_header(each.group(1))
            rv +=  get_list(each.group(2))
    return rv

def main():
    print get_markdown()

if __name__=="__main__":
    main()
    
