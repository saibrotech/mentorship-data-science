# Import the required library
import requests

JOB_LIST_URL = 'https://www.linkedin.com/jobs/search/?currentJobId=3231313649&f_E=1%2C2&f_I=96%2C4&f_TPR=r2592000&geoId=106057199&keywords=junior&location=Brazil&refresh=true&sortBy=DD'
RAW_PATH = 'data/raw/'

def get_job_list():
    # Get page with job list
    response = requests.get(JOB_LIST_URL)

    # Print the status code
    print(f"Status code: {response.status_code}")

    # Save the file locally (more about open() in the next lesson)
    file = "job-list.html"
    with open(RAW_PATH + file, "wb") as f:
        f.write(response.content)



# Main function called inside the execute.py script
def main():
    print("[Extract] Start")
    get_job_list()
    print("[Extract] End")