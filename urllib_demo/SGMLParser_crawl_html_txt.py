#coding:utf-8

import urllib,chardet,re
from sgmllib import SGMLParser
from BeautifulSoup import BeautifulSoup

'''爬取网页新闻的黑标题下的网页正文部分，保存在txt文档里
以黑标题的名字作为txt文档的名字
这个黑标题不是网页打开之后的正文标题
'''

class URLLister_1(SGMLParser):

    def reset(self):

        self.is_a= ""
        self.urls = []
        self.name = []
        SGMLParser.reset(self)

    def start_a(self, attrs):

        self.is_a = 1
        href = [v for k, v in attrs if k == 'href']
        if href:
            self.urls.extend(href)

    def end_a(self):

        self.is_a = ""

    def handle_data(self, text):

        if self.is_a:
            self.name.append(text)

class URLLister_2(SGMLParser):

    def reset(self):

        self.is_p = ""
        self.text = []
        SGMLParser.reset(self)

    def start_p(self,attrs):

        self.is_p = 1

    def end_p(self):

        self.is_p = ""

    def handle_data(self, text):

        if self.is_p:
            self.text.append(text)

if __name__ == "__main__":

    string_getContent = ''
    content = urllib.urlopen("http://news.163.com/")
    soup = BeautifulSoup(content)
    getContent = soup.find('div',{"id" : "news"})
    getContent = getContent.findAll('a')
    #print getContent
    for each in getContent:
        each = str(each)
        string_getContent += each
    #print string_getContent
    lister = URLLister_1()
    lister.feed(string_getContent)
    if len(lister.urls) == len(lister.name):
        length =  len(lister.urls)
    for every_html in range(length):
        lister.name[every_html] = re.sub(r'[:<>?/"]','_',lister.name[every_html])
        lister.name[every_html] = lister.name[every_html].decode('utf-8') + '.txt'
        page = urllib.urlopen(lister.urls[every_html])
        page_content = page.read()
        paper = re.compile('(<div id="endText">.).+?(<div class="ep-source cDGray">)',re.I|re.S)
        data = paper.search(page_content)
        if data:
            data = data.group()
            lister_text = URLLister_2()
            lister_text.feed(data)
            file = open('D:\data/'+lister.name[every_html],'a')
            for each in lister_text.text:
                each = each.replace('宋体'.decode('utf-8').encode('gbk'),'')
                each = re.sub('\n','',each)
                each = re.sub('[a-z]','',each)
                each = re.sub('[A-Z]','',each)
                each = re.sub('[=:;{}_]','',each)
                each = re.sub("['\/]",'',each)
                file.write(each)
        else:
            file = open('D:\data/'+lister.name[every_html],'w')
            file.write('Notext')





