# Scrapy-for-mtime
<br>Get actors\` documentation
## Personal document
<br>Using actors links retrieved from mongodb database to grab actors\` personal document
<br>
## Main codes
* Connectors.py <br>
connect mongodb database and retrieve URLs 
* mtimePosition.oy
  <br>  retrieve actors\` documentation and then yield one item to seetings for storage
* items.py
	<br>  define item`s content
* settings.py
	<br>  receive items and then store it into database
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
<br>Input:
	<br>scrapy crawl mtimePosition

## Bullet points
<br>Key skills that I` ve learned
* Using scarpy frame work
* json, set()
* modify parameters of traditional package function

## Case:
* Take [周润发Yun-Fat Chow](http://people.mtime.com/893535/details.html) as an example.
* Get his page link from the database first, and then enter his personal documentation items.

### Each item
<br>basic information: brithday, height, constellation, Blood type. etc
<br>personal introduction: a introductory passage for the actor
<br>social relationship: most director, most actor, most actress, Top10 paitners
<br>personal experience: year + history content

### Save as json file
dict [‘name’] = name
<br>dict [‘per_id’] = pid
<br>dict [‘information’] = information
<br>dict [‘introduction’] = introduction
<br>dict [‘relationship’] = relationship
<br>dict [‘experience’] = experience

