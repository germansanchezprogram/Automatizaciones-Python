import requests
from bs4 import BeautifulSoup

url = "https://www.seek.co.nz/python-jobs?salaryrange=100000-999999&salarytype=annual"

if "__main__" ** __name__:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")