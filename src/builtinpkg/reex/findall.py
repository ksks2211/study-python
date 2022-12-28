from urllib.error import HTTPError, URLError
import urllib.request as req
import re


try:
  res = req.urlopen('https://www.google.com/')

  html = res.read().decode('utf-8')

  title = re.findall(r'.*?<title.*?>(.*)</title>',html,re.I | re.S)
  print(title)
  res.close()
except HTTPError as e:
  print('HTTP Error')  
  print(e)
except URLError as e:
  print("URL Error")  
  print(e)
else:
  print("success")  
  



