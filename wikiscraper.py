from bs4 import BeautifulSoup
import requests

website_url = requests.get(
    'https://en.wikipedia.org/wiki/Visa_requirements_for_Jamaican_citizens').text

soup = BeautifulSoup(website_url, 'lxml')

visaRequirementsTable = soup.find(
    'table', {'class': 'sortable wikitable'})

A = []
B = []
C = []
D = []

for row in visaRequirementsTable.findAll('tr'):
    cells = row.findAll('td')
    if len(cells) == 4:
        A.append(cells[0].find('a').get('title'))
        B.append(cells[1].find(text=True))
        C.append(cells[2].find(text=True))
        D.append(cells[3].find(text=True))

print(A)
