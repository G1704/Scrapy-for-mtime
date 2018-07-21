# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import re

def get_information(response):
    try:
        info_con = re.findall('<div class="per_info_l">(.*?)</p>            </div>', response)[0]
        i1 = re.findall('<dt><strong>(.*?)</strong>(.*?)</d', str(info_con))
        info = dict()
        for i in i1:
            # The element of attributes is not none, restore it
            if i[1] != '':
                info[str(i[0]).strip('：')] = str(i[1]).strip()

            # The element of attributes is none, research it
            if i[1] == '':
                # Get element
                # Family members
                try:
                    info1 = re.findall('<dt><strong>家庭成员：</strong></dt><dd>(.*?)</dd>', str(info_con))[0]
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
                    info2 = re.findall('<dt><strong>教育背景：</strong></dt><dd>(.*?)</dd>', str(info_con))[0]
                    infos = []
                    try:
                        for k in info2.split('b'):
                            try:
                                kk = re.findall('r/>(.*?)<',k)[0]
                                infos.append(kk)
                            except:
                                pass
                    except:
                        pass

                    info['教育背景'] = ';'.join(infos)
                except:
                    print('No education background')
        print('First step')
        print()
        return (info)
    except:
        return '空'
def get_introduction(response):
    intros = re.findall('<div style="display:none;" id="lblAllGraphy">(.*?)</div>', response)[0]
    soup = BeautifulSoup(intros, 'lxml')
    text = soup.stripped_strings
    # print(''.join(text))
    print('Second step')
    print()
    return ''.join(text).strip(' ')
def get_relationship(response):
    every = dict()
    relas = re.findall('<dl class="per_relalist"> (.*?)<div id="lblPersonList" style="display:none;"></div>', response)[
        0]
    # Most ones
    for each in relas.split('</dd>'):
        one = dict()
        d1 = re.findall('<dt>(.*?)</dt>', each)[0]
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
def get_experience(response):
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

if __name__ == '__main__':
    url = 'http://people.mtime.com/1251032/details.html'
    print(url)
    response = requests.get(url).text
    # response
    All = dict()
    All['基本资料'] = get_information(response)
    All['人物小传'] = get_introduction(response)
    All['人物关系'] = get_relationship(response)
    All['演艺经历'] = get_experience(response)
    print(All)
    # browser.close()



