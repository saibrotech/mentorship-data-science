# Import libraries
import os
import json
from bs4 import BeautifulSoup

html_file = 'job-etl/data/html/1231621951.html'


with open(html_file, 'r') as html_file:
    soup = BeautifulSoup(html_file, 'html.parser')
    source = soup.find('link')
    detail = soup.find_all('span', class_='description__job-criteria-text')            
    date = soup.find('script', type='application/ld+json').string
    jsondata = json.loads(date)
        
    dict = {
        'id': id,
        'date': jsondata['datePosted'],
        'company': soup.find('span', class_='topcard__flavor').text.strip(),
        'title': soup.find('h1').text,
        'location': soup.find(class_='topcard__flavor--bullet').text.strip(),
        'link': source.get('href'),
        'description': soup.find('div', class_='show-more-less-html__markup').text.strip(),
        'level': '',
        'type': '',
        'occupation': '',
        'sector': ''
    }
        
   
    try:
        dict['level'] = detail[0].text.strip()
        dict['type'] = detail[1].text.strip()
        dict['occupation'] = detail[2].text.strip()
        dict['sector'] = detail[3].text.strip()
    except:
        pass

print(dict)