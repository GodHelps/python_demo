"crawl.py"
'''
本实例实现抓取Web 的开始页面地址（URL），下载该页面和其它后续链接页面，
但是仅限于那些与开始页面有着相同域名的页面。如果没有这个限制的话，硬盘将会
被耗尽！
'''
from sys import argv
import os
from os import makedirs, unlink, sep
from os.path import dirname, exists, isdir, splitext
#from string import replace, find, lower #已经被str中的方法替代
from html.parser import HTMLParser
from urllib.request import urlretrieve
from urllib.parse import urlparse, urljoin
from formatter import DumbWriter, AbstractFormatter
from io import StringIO
import encodings
from urllib.parse import unquote

class Retriever(object):# download Web pages
    def __init__(self, url):
        self.url = url
        self.file = self.filename(url)
        print('self.file:',self.file)

    def filename(self, url, deffile='index.html'):
        parsedurl = urlparse(url, 'http:', 0) ## parse path
        path = parsedurl[1] + parsedurl[2]
        ext = splitext(path)
        print('ext:',ext)
        if ext[1] == '': # no file, use default
            if path[-1] == '/':
                path += deffile
            else:
                path += '/' + deffile
            ldir = dirname(path) # local directory
            if sep != '/': # os-indep. path separator
                ldir = ldir.replace('/', sep)
            if not isdir(ldir): # create archive dir if nec.
                if exists(ldir): unlink(ldir)
            if not os.path.exists(ldir):
                print("dir:",dir)
                makedirs(ldir)
        else:
            if not os.path.exists(ext[0]):
                    print("dir:",ext[0])
                    makedirs(ext[0])
        print('path:',path)
        return path

    def download(self): # download Web page
        try:
            retval = urlretrieve(self.url, self.file)
        except IOError:
            retval = ('*** ERROR: invalid URL "%s"' %\
        self.url,)
        return retval

    def parseAndGetLinks(self):# parse HTML, save links
        '''writers=DumbWriter(StringIO())
        self.para=AbstractFormatter(writers)
        print(self.para)
        self.parser = HTMLParser(self.para)
        self.parser.feed(open(self.file).read())
        self.parser.close()
        return self.parser.anchorlist'''
        self.urllist=[]
        self.parser = MyParser()
        try:#不能固定encoding 编码格式
        #例如:open(self.file,'r',encoding='utf_8'),固定一种格式不能满足所有值
            fileread=open(self.file,'r')
            reader=fileread.read()
        except Exception as e:
            fileread=open(self.file,'r',encoding='utf_8')
            reader=fileread.read()
        #fileread=unquote(fileread)
        #reader=fileread.read()
        self.parser.feed(reader)
        self.parser.close()
        return self.urllist
    
class MyParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)               
    def handle_starttag(self, tag, attrs):
        # 这里重新定义了处理开始标签的函数
        if tag =='a':
            # 判断标签<a>的属性
            for name,value in attrs:
                if name == 'href':
                    print(value)

class Crawler(object):# manage entire crawling process
    count = 0 # static downloaded page counter
    def __init__(self, url):
        self.q = [url]
        self.seen = []
        self.dom = urlparse(url)[1]

    def getPage(self, url):
        r = Retriever(url)
        retval = r.download()
        if retval[0] == '*': # error situation, do not parse
            print(retval, '... skipping parse')
            return
        Crawler.count += 1
        print( '\n(', Crawler.count, ')')
        print('URL:', url)
        print('FILE:', retval[0])
        self.seen.append(url)
        links = r.parseAndGetLinks() # get and process links
        '''for eachLink in links:
            if eachLink[:4] != 'http' and \
            find(eachLink, '://') == -1:
                eachLink = urljoin(url, eachLink)
                print('* ', eachLink)
                if find(lower(eachLink), 'mailto:') != -1:
                    print('... discarded, mailto link')
                    continue

            if eachLink not in self.seen:
                if find(eachLink, self.dom) == -1:
                    print ('... discarded, not in domain')
                else:
                    if eachLink not in self.q:
                        self.q.append(eachLink)
                        print( '... new, added to Q')
                    else:
                        print('... discarded, already in Q')
            else:
                print('... discarded, already processed')'''
            
    def go(self):# process links in queue
        while self.q:
            url = self.q.pop()
            self.getPage(url)

def main():
    "test main method"
    if len(argv) > 1:
        url = argv[1]
    else:
        try:
            url = input('Enter starting URL: ')
        except (KeyboardInterrupt, EOFError):
            url = ''
    if not url: return
    robot = Crawler(url)
    robot.go()

if __name__ == '__main__':
    main()
