import requests
import re
from core.extensions import db
from bs4 import BeautifulSoup
import uuid

url = "https://saveourplanet.org/donate-to-a-project/"
page_ = requests.get(url).text
soup = BeautifulSoup(page_, 'html.parser')

cards_ = soup.find_all("article", class_=re.compile('[.^post project_post item-]'))

projects = []
# dict_ = ['air','environment',]
for card in cards_:
    try:
        obj_ = {
            "_id": str(uuid.uuid4()),
            "project_url": card.find('h3').find('a')['href'],
            "name": card.find('h3').find('a').string,
            "image_url": card.find('img')['src'],
            "paypal_url": card.find('form').get_attribute_list('action')[0]
        }
        db.projects.insert_one(obj_)
        projects.append(obj_)
    except Exception:   
        print(card, end="Has issue!")



# print(cards_[0].find('form').get_attribute_list('action'))
print(projects) 
print(len(projects))