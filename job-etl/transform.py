# Import libraries
import os
import json
from bs4 import BeautifulSoup

BASE_PATH = os.path.abspath(__file__ + '/../')
DATA_PATH = f'{BASE_PATH}/data/'
RAW_PATH = DATA_PATH + 'raw/'

jobs = {}
    
def access_html_files():
    """
    Accesses extracted files and calls conversor
    """
    raw_list = os.listdir(RAW_PATH)
    
    for filename in raw_list:
        with open(f'{RAW_PATH}/{filename}', 'r') as file:
            html_conversor()


def html_conversor():
    """
    Converts html data from file into dictionary using beautifulsoup
    """
    raw_list = os.listdir(RAW_PATH)
 
    for filename in raw_list:
        with open(f'{RAW_PATH}/{filename}', 'r') as file:
            soup = BeautifulSoup(file, 'html.parser')
            name, extension = os.path.splitext(filename)
            source = soup.find('link')
            detail = soup.find_all('span', class_='description__job-criteria-text')        
        
        jobs = {'id': name,
                'date': soup.find(class_='posted-time-ago__text').text.strip(),
                'company' : soup.find('span', class_='topcard__flavor').text.strip(),
                'title': soup.find('h1').text,
                'location': soup.find(class_='topcard__flavor--bullet').text.strip(),
                'link': source.get('href'),
                'description' : soup.find('div', class_='show-more-less-html__markup').text.strip(),
                'level': detail[0].text.strip(),
                'type': detail[1].text.strip(),
                'occupation': detail[2].text.strip(),
                'sector': detail[3].text.strip()            
        }
        for key, value in jobs.items():
            print(key,':', value)

#def json_conversor():
    """
    Saves dictionary into a json file
    """
    #with open('jobs.json', 'w') as save_file:
    #    json.dump(jobs, save_file, indent=2)


#def transform_and_save_new_data():
    """
    Processes transformation to newly acquired data
    """
#    with open(RAW_PATH, mode="r", encoding="windows-1252") as csv_file:
        # Read the new .csv snapshot ready to be processed
#        reader = csv.DictReader(csv_file)
        # Initialize an empty list for our PprRawAll objects
#        job_raw_objects = []
#        for row in reader:
            # Apply transformations and save as PprRawAll object
#            job_raw_objects.append(
#                JobRawAll(
#                    title = update_title(row['title'])
 #                   date_posted = update_date_posted(row['date_posted'])
#                )
#            )
        # Bulk save all new processed objects and commit
        #session.bulk_save_objects(job_raw_objects)
        #session.commit()

# Main function called inside the execute.py script
def main():
    print("[Transform] Start")
    access_html_files()
    #json_conversor()
    print("[Transform] End")