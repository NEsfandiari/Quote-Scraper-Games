from bs4 import BeautifulSoup
import requests
import csv
res = requests.get('https://www.rithmschool.com/blog')
soup = BeautifulSoup(res.text, 'html.parser')
articles = soup.find_all("article")

with open('blogs.csv', 'w') as f:
    csv_w = csv.writer(f)
    csv_w.writerow(['title', 'link', 'date'])
    for article in articles:
        title = article.find('a').get_text()
        link = article.find('a')['href']
        date = article.find('time')['datetime']
        csv_w.writerow([title, link, date])
