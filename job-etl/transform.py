# Import libraries
import os
import json
import datetime as dt
from bs4 import BeautifulSoup

BASE_PATH = os.path.abspath(__file__ + '/../')
DATA_PATH = f'{BASE_PATH}/data/'
HTML_PATH = DATA_PATH + 'html/'
JSON_PATH = DATA_PATH + 'json/'

def create_folder_if_not_exists(path):
    """
    Create a new folder if it doesn't exist
    """
    print(f'Creating folder: {path}')
    os.makedirs(os.path.dirname(path), exist_ok=True)

def create_folder():
    create_folder_if_not_exists(JSON_PATH)

def transform_and_save_new_data():
    """
    Processes transformation to newly acquired data
    """
    raw_list = os.listdir(HTML_PATH)
    for html_file in raw_list:
        id, extension = os.path.splitext(html_file)
        json_path = f'{JSON_PATH}{id}.json'

        if os.path.exists(json_path):
            print(f'Job {id} exists in JSON data')
        else:
            html_conversor(id)

def html_conversor(id):
    """
    Converts html data from file into dictionary using beautifulsoup
    """
    html_path = f'{HTML_PATH}{id}.html'
    print(f'Reading {html_path}')

    with open(html_path, 'r') as html_file:
        soup = BeautifulSoup(html_file, 'html.parser')
        source = soup.find('link')
        detail = soup.find_all('span', class_='description__job-criteria-text')            
        
        dict = {
            'id': id,
            'company': soup.find('span', class_='topcard__flavor').text.strip(),
            'title': soup.find('h1').text,
            'location': soup.find(class_='topcard__flavor--bullet').text.strip(),
            'link': source.get('href'),
            'description': soup.find('div', class_='show-more-less-html__markup').text.strip(),
            'e_date' : os.path.getmtime(html_path),
            't_date' : dt.datetime.today().strftime('%d/%m/%Y'),
            'l_date' : ''
        }

        try:
            script = soup.find('script', type='application/ld+json').string
            jsondata = json.loads(script)
            dict['date'] = jsondata['datePosted']
        except:
            pass
   
        try:
            dict['level'] = detail[0].text.strip()
            dict['type'] = detail[1].text.strip()
            dict['occupation'] = detail[2].text.strip()
            dict['sector'] = detail[3].text.strip()
        except:
            pass

        json_conversor(dict)



def json_conversor(dict):
    """
    Saves dictionary into a json file
    """
    with open(f'{JSON_PATH}/{dict["id"]}.json', 'w') as save_file:
        json.dump(dict, save_file, indent=2, ensure_ascii=False)
               

# Main function called inside the execute.py script
def main():
    print("[Transform] Start")
    create_folder()
    transform_and_save_new_data()
    print("[Transform] End")


if __name__ == "__main__":
    main()