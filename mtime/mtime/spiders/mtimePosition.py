# -*- coding: utf-8 -*-
import scrapy
import re
import requests
from mtime import settings
from bs4 import BeautifulSoup
from mtime.items import MtimeItem
from connectors import *

class MtimepositionSpider(scrapy.Spider):
    name = "mtimePosition"
    allowed_domains = ["mtime.com"]
    s1 = Connectors()
    s2 = set()
    s3 = set()
    start_urls = []

    # 数据库链接完毕
    with open('Store_urls.txt', 'r') as f:  # 已爬数据
        rs = f.readlines()
        for r in rs:
            s2.add(r.strip('\n'))
        f.close()
    with open('Wrong_urls.txt', 'r') as f:  # 错误url
        rs = f.readlines()
        for r in rs:
            s3.add(r.strip('\n'))
        f.close()
    s1 = s1.difference(s2)
    s1 = s1.difference(s3)
    for t in s1:  # set<urls>
        start_urls.append(t)  # 获取到所有新的url

    def start_requests(self):
        for url in self.start_urls:
            content = requests.get(url=url, headers=settings.DEFAULT_REQUEST_HEADERS)
            j = re.findall('<title>(.*?)</title>', content.text)[0]
            print(j)
            if j == '很抱歉，你要访问的页面不存在':
                with open('Wrong_urls.txt', 'a') as f1:
                    f1.write(url + '\n')
                    f1.close()
                continue
            else:
                yield self.make_requests_from_url(url=url)

    # print(start_urls)
    def get_information(self, response):
        try:
            infos = re.findall('<div class="per_info_l">(.*?)</p>            </div>', response)[0]
            ils = re.findall('<dt><strong>(.*?)</strong>(.*?)</d', infos)
            info = dict()
            for i in ils:
                # The element of attributes is not none, restore it
                if i[1] != '':
                    info[str(i[0]).strip('：')] = str(i[1]).strip()

                # The element of attributes is none, research it
                if i[1] == '':
                    # Get element
                    # Family members
                    try:
                        info1 = re.findall('<dt><strong>家庭成员：</strong></dt><dd>(.*?)</dd>', str(infos))[0]
                        # Process and make a dict
                        ttmp = dict()
                        for each in info1.split('，'):  # Each item
                            t = re.findall('(.*?)<a href=".*?" target="_blank">(.*?)</a>', str(each))
                            for tmp in t:
                                # Elementary dict
                                ttmp[tmp[0].strip('：')] = tmp[1]
                        info['家庭成员'] = ttmp
                    except:
                        print('No family members')

                    # Education background
                    try:
                        info2 = re.findall('<dt><strong>教育背景：</strong></dt><dd>(.*?)</dd>', str(infos))[0]
                        info2s = []
                        try:
                            for k in info2.split('b'):
                                try:
                                    kk = re.findall('r/>(.*?)<', k)[0]
                                    info2s.append(kk)
                                except:
                                   pass
                        except:
                            pass
                        info['教育背景'] = ';'.join(info2s)
                    except:
                        print('No education background')
            print('First step')
            print()
            return info
        except:
            return '空'

    def get_introduction(self, response):
        try:
            intros = re.findall('<div style="display:none;" id="lblAllGraphy">(.*?)</div>', response)[0]
            soup = BeautifulSoup(intros, 'lxml')
            text = soup.stripped_strings
            print('Second step')
            print()
            return ''.join(text)
        except:
            return '空'

    def get_relationship(self, response):
        try:
            every = dict()
            relas = \
            re.findall('<dl class="per_relalist"> (.*?)<div id="lblPersonList" style="display:none;"></div>', response)[
                0]
            # Most ones
            for each in relas.split('</dd>'):
                one = dict()
                d1 = re.findall('<dt>(.*?)</dt>', str(each))[0]
                soup = BeautifulSoup(d1, 'lxml')
                title = soup.stripped_strings
                title = ''.join(title)
                if title == '合作两次以上的影人TOP10展开':
                    break
                name = re.findall('<a href=".*" target="_blank">(.*?)</a>.*</h3><span class="fl ml15">', each)[0]
                one['姓名'] = name
                attris = re.findall('<span class="fl ml15">(.*?)</span>', each)[0]
                one['职业'] = attris
                work = re.findall('<p>合作作品(.*?)</p>(.*?)</p>', str(each))[0]
                soup = BeautifulSoup(work[1], 'lxml')
                wwork = soup.stripped_strings  # all films
                wwork = ''.join(wwork)
                films = dict()
                films['合作作品' + str(work[0].strip('：'))] = wwork
                one['works'] = films
                every[str(title)] = one
        except:
            return '空'
        # Top10
        lists = re.findall('合作两次以上的影人TOP10(.*?)<div id="lblPersonList" style="display:none;"></div>', response)[0]
        tmp = []
        for ll in lists.split('</dd>'):
            try:
                shell = dict()
                name = re.findall('<a href=".*" target="_blank">(.*?)</a>.*</h3>', ll)[0]
                shell['姓名'] = name
                attris = re.findall('<span class="fl ml15">(.*?)</span>', ll)[0]
                shell['职业'] = attris
                work = re.findall('<p>合作作品(.*?)</p>(.*?)</p>', str(ll))[0]
                soup = BeautifulSoup(work[1], 'lxml')
                wwork = soup.stripped_strings  # all films
                wwork = ''.join(wwork)
                films = dict()
                films['合作作品' + str(work[0].strip('：'))] = wwork
                shell['作品'] = films
                tmp.append(shell)
            except:
                pass
        every['合作两次以上的影人TOP10'] = tmp
        print('Third step')
        print()
        return (every)

    def get_experience(self, response):
        tmp = []
        try:
            expers = re.findall('<div class="per_career">(.*?)<div id="M13_B_DB_Person_FooterTopTG">', response)[0]
            for exper in expers.split('</dd>'):
                try:
                    expp = dict()
                    year = re.findall('<i class="year_tag">(.*?)</i>', str(exper))[0]
                    expp['年份'] = year
                    headline = re.findall('<h3>(.*?)</h3>', exper)[0].strip()
                    expp['标题'] = headline
                    content_tmp = re.findall('<p class="mt20">(.*?)</p>', exper)[0]
                    ss = BeautifulSoup(content_tmp, 'lxml')
                    content = ''.join(ss.stripped_strings)
                    expp['内容'] = content
                    tmp.append(expp)
                except Exception as e:
                    pass
        except:
            pass
        print('Forth step')
        print()
        if tmp == []:
            return '空'
        return tmp

    def get_name(self, response):
        try:
            name = re.findall('<h2 style="font-size:40px;" class="__r_c_" pan="M14_Person_Index_PersonName"><a href=".*">(.*?)</a></h2>', response)[0]
            return name
        except:
            name = re.findall('<h2 style="font-size:24px;" class="__r_c_" pan="M14_Person_Index_PersonName"><a href=".*">(.*?)</a></h2>', response)[0]
            return name

    def get_id(self, response):
        pid = re.findall('http://people.mtime.com/(.*?)/details.html', str(response.url))[0]
        return pid

    def parse(self, response):
        return MtimeItem(
            name=self.get_name(response.text),
            per_id= self.get_id(response),
            information=self.get_information(response.text),
            introduction=self.get_introduction(response.text),
            relationship=self.get_relationship(response.text),
            experience=self.get_experience(response.text),
        )
        pass
