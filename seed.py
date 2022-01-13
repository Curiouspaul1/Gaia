import requests
import re
from core.extensions import db
from bs4 import BeautifulSoup
import uuid

url = "https://saveourplanet.org/donate-to-a-project/"
page_ = requests.get(url).text
soup = BeautifulSoup(page_, 'html.parser')
projects = list(db.project.find({}))

cards_ = soup.find_all("article", class_=re.compile('[.^post project_post item-]'))

projects = []
# dict_ = ['air','environment',]
for card in cards_:
    project_url = requests.get(card.find('h3').find('a')['href']).text
    project_page = BeautifulSoup(project_url, 'html.parser')
    try:
        obj_ = {
            '_id':str(uuid.uuid4()),
            'project_headline': project_page.find('main').find('p').string,
            'paypal_value': card.find('form').find('input', attrs={'name': 'hosted_button_id'})['value'],
            "project_url": card.find('h3').find('a')['href'],
            "name": card.find('h3').find('a').string,
            "image_url": card.find('img')['src'],
            "paypal_url": card.find('form').get_attribute_list('action')[0]
        }
        db.project.insert_one(obj_)
        projects.append(obj_)
    except Exception:
        print(card, end="Has issue!")




# print(cards_[0].find('form').get_attribute_list('action'))
# print(projects)
print(len(projects))
