import requests
from bs4 import BeautifulSoup

url = "https://ua.sinoptik.ua"
def get_html(url):
    response = requests.get(url)
    html_doc = response.content
    soup = BeautifulSoup (html_doc, 'html.parser')
    #print(soup.prettify())
    print(soup.find_all("span"))
    return response.text
get_html(url)
