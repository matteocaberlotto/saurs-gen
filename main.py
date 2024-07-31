import requests
from bs4 import BeautifulSoup
import random

# Fetch the content of the Wikipedia page
url = "https://en.wikipedia.org/wiki/List_of_commonly_used_taxonomic_affixes"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Parse the content to extract taxonomic affixes
tables = soup.find_all('div', class_='mw-body-content')

prefixes = []
suffixes = []

for table in tables:
    uls = table.find_all('ul')
    for ul in uls:
        lis = ul.find_all('li')
        for li in lis:
            bs = li.find_all('b')
            for affix in bs:  # Skip the header row
                if affix:
                    text = affix.text.strip()
                    if text.endswith('-'):
                        prefixes.append(text[:-1])  # Remove the trailing hyphen
                    elif text.startswith('-'):
                        suffixes.append(text[1:])  # Remove the leading hyphen

# Generate dinosaur names using the affixes
def generate_dinosaur_name():
    prefix = random.choice(prefixes)
    suffix = random.choice(suffixes)
    return prefix.capitalize() + suffix.capitalize() + "saurus"

# Generate a list of dinosaur names
dinosaur_names = [generate_dinosaur_name() for _ in range(10)]

# Print the generated dinosaur names
for name in dinosaur_names:
    print(name)

