# Import the required library
import requests
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

JOB_LIST_URL = 'https://www.linkedin.com/jobs/search/?currentJobId=3231313649&f_E=1%2C2&f_I=96%2C4&f_TPR=r2592000&geoId=106057199&keywords=junior&location=Brazil&refresh=true&sortBy=DD'

BASE_PATH = os.path.abspath(__file__ + '/../')
DATA_PATH = f'{BASE_PATH}/data/'
RAW_PATH = DATA_PATH + 'raw/'

def create_folder_if_not_exists(path):
    """
    Create a new folder if it doesn't exists
    """
    print(f'Creating folder: {path}')
    os.makedirs(os.path.dirname(path), exist_ok=True)

def create_folders():
    create_folder_if_not_exists(RAW_PATH)

def get_job_list():
    jobs = []

    # Setup chromedriver 
    wd = webdriver.Chrome()
    wd.get(JOB_LIST_URL)

    # Get the number of jobs available
    no_of_jobs = int(wd.find_element(By.CSS_SELECTOR, value='h1>span').get_attribute('innerText'))
    print(f'Total of Jobs: {no_of_jobs}')

    # Browse all the jobs
    i = 2
    while i <= int(no_of_jobs/25)+1: 
        wd.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        i = i + 1
        try:
            wd.find_element(By.XPATH, value='/html/body/main/div/section/button').click()
            time.sleep(5)
        except:
            pass
            time.sleep(5)
            
    # Find all the jobs
    job_lists = wd.find_element(By.CLASS_NAME, value='jobs-search__results-list')
    # return a list
    jobs_elements = job_lists.find_elements(By.TAG_NAME, value='li') 
    
    # Check the number of jobs on the list
    print(f'Jobs found: {len(jobs_elements)}')

    for job in jobs_elements:
        id = job.find_element(By.CLASS_NAME, value='base-card').get_attribute('data-entity-urn')
        id =  id.split(':')[-1]
        url = job.find_element(By.CSS_SELECTOR, value='a').get_attribute('href')
        jobs.append({'id': id, 'url': url})
    
    return jobs

def get_job(id, url):

    file_path = f'{RAW_PATH}{id}.html'

    if os.path.exists(file_path):
        print(f'Job exists {id}')
        return

    print(f'Downloading page: {id} {url}')
    # Get page with job list
    response = requests.get(url)

    # Print the status code
    print(f"Status code: {response.status_code}")

    if response.status_code == 200:
        # Save the file locally (more about open() in the next lesson)

        print(f"Saving: {file_path}")   
        with open(file_path, "wb") as f:
            f.write(response.content)

def find_jobs():
    jobs = get_job_list()
    for job in jobs:
        try:
            get_job(job['id'], job['url'])
            time.sleep(5)
        except:
            pass
            time.sleep(5)

# Main function called inside the execute.py script
def main():
    print("[Extract] Start")
    create_folders()
    find_jobs()    
    print("[Extract] End")