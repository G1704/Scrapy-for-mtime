# Scrapy-for-mtime
<br>Get actors\` documentation
## Personal document
<br>Using actors links retrieved from mongodb database to grab actors\` personal document
<br>
## Main codes
* Connectors.py <br>
connect mongodb database and retrieve URLs 
* mtimePosition.oy
	<br>  Retrieve actors\` documentation and then yield one item to seetings for storage
* items.py
	<br>  Define item`s content
* settings.py
	<br>  Receive items and then store it into database
* Store_urls.txt
	<br>  A storage for valid URLs
* Wrong_urls.txt
	<br>  A storage for invalid URLs


## Operating environment
<br>Based on python3.5 and scrapy framework, first need to install:
* scrapy
* requests
* bs4 for BeautifulSoup
* pymongo
* json

## Operating Instructions
<br>Open the terminal in the directory where the project file is stored.
<br>Input: scrapy crawl mtimePosition

## Bullet points
<br>Key skills that I` ve learned
* Using scarpy frame work
* json, set()
* modify parameters of traditional package function

## Case:
* Take [周润发Yun-Fat Chow](http://people.mtime.com/893535/details.html) as an example.
* Get his page link from the database first, and then enter his personal documentation items.

### Each item
<br>Basic information: brithday, height, constellation, Blood type. etc<br>
![](https://github.com/G1704/Scrapy-for-mtime/blob/master/%E5%9F%BA%E6%9C%AC%E8%B5%84%E6%96%99.png "Profile")
<br>
<br>Personal introduction: a introductory passage for the actor<br>
![](https://github.com/G1704/Scrapy-for-mtime/blob/master/%E4%BA%BA%E7%89%A9%E5%B0%8F%E4%BC%A0.png "Biography")
<br>
<br>Social relationship: most director, most actor, most actress, Top10 paitners<br>
![](https://github.com/G1704/Scrapy-for-mtime/blob/master/%E4%BA%BA%E7%89%A9%E5%85%B3%E7%B3%BB.png "Relationship")
<br>
<br>Personal experience: year + history content<br>
![](https://github.com/G1704/Scrapy-for-mtime/blob/master/%E6%BC%94%E8%89%BA%E7%BB%8F%E5%8E%86.png "Career")
<br>


### Save as json file
dict [‘name’] = name
<br>dict [‘per_id’] = pid
<br>dict [‘information’] = information
<br>dict [‘introduction’] = introduction
<br>dict [‘relationship’] = relationship
<br>dict [‘experience’] = experience
![](https://github.com/G1704/Scrapy-for-mtime/blob/master/terminal.png "Career")
<br>
![](https://github.com/G1704/Scrapy-for-mtime/blob/master/result.png "Career")
