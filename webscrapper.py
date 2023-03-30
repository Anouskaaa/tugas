#import library
from bs4 import BeautifulSoup
import requests
#request to website and download HTML contents
url='https://id.jobsdb.com/id'
req=requests.get(url)
content=req.text
print(content)
