from bs4 import BeautifulSoup
import requests
url='https://id.jobsdb.com/id'
req=requests.get(url)
content=req.text
print(content)
