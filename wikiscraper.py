from bs4 import BeautifulSoup
import re
import requests
import pandas as pd

website_url = requests.get(
    'https://en.wikipedia.org/wiki/Visa_requirements_for_Jamaican_citizens').text

soup = BeautifulSoup(website_url, 'lxml')

visaRequirementsTable = soup.find(
    'table', {'class': 'sortable wikitable'})

country = []
visaRequirement = []
allowedStay = []
notes = []

for row in visaRequirementsTable.findAll('tr'):
    cells = row.findAll('td')
    if len(cells) == 4:
        country.append(cells[0].find('a').get('title'))
        visaRequirement.append(cells[1].find(text=True))
        allowedStay.append(cells[2].find(text=True))
        notes.append(cells[3].find('li'))


regex = re.findall('\n', allowedStay[0])
for x in regex:
    allowedStay = [r.replace(x, '') for r in allowedStay]


df = pd.DataFrame()
df['Country'] = country
df['Visa Requirement'] = visaRequirement
df['Allowed Stay'] = allowedStay
df['Notes'] = notes


df.to_csv(r'./output.csv')
print(notes)
