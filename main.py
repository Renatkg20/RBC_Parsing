import requests 
from bs4 import BeautifulSoup
import re
import pandas as pd
url = "http://www.akipress.kg"
user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
res = (requests.get(url, headers = user_agent, timeout = 6 )).text
with open("html.txt", 'w') as file: 
     res1 = file.write(res)
links_lst = []
soup = BeautifulSoup(res, 'html.parser')
soup = soup.find('table', {'id': 'maintbl'}).find_all('a')
for i in soup:
    t = i.get('href')
    web = ("http:" + t)
    if len(web) > 13:
      links_lst.append(web)
    




def get_data(links):
    user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
    
    links.remove("http:http://www.aki.kg")
    for urls in links:
        url = urls
        res1 = requests.get(url, headers = user_agent, timeout = 2.5)
        print(res1)
        if str(res1) == "<Response [200]>":
            res2 = res1.content
            soup = BeautifulSoup(res2, 'html.parser')
            soup = soup.get_text(" ")
            t = re.sub(r'\s+', ' ', soup)
     
            with open("data.txt", "a") as file:
                 file.write(t)
             
t = get_data(links_lst)
print(t)

 
with open("data.txt", "r") as f:
  st1 = f.read()
result = []
result1 = []
sent1 = st1.split(" ")
for i in sent1:
  result.append(st1.count(i))
  
  result1.append(i)

# print(result)
final = []
for a, i in zip(result, result1):
  final.append(i + " " + str(a))
  
# res123 = max(result)
# index1 = result.index(res123)
# print(max(result), min(result))



def del_dub(x):
  lis1 = []
  for i in x:
    if i not in lis1:
      lis1.append(i)

  return lis1

result = (del_dub(final))

print(result)

df = pd.DataFrame({"Data": result})

print(df)

df.to_excel("output.xlsx", "UTF-8") 

with open("excel.csv", "w" ) as f1:
     f1.write(str(df))
"""
"https://hakin9.org/crack-wpa-wpa2-wi-fi-routers-with-aircrack-ng-and-hashcat/"

"""

