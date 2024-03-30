import requests
from bs4 import BeautifulSoup

def scrape_business_contacts(keyword, location):
    url = f'https://example.com/business-directory/?keyword={keyword}&location={location}'
    headers = {'User-Agent': 'Your User Agent Here'}  # Add your user agent to mimic a real browser
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extracting contact information
        contacts = []
        business_cards = soup.find_all('div', class_='business-card')
        for card in business_cards:
            name = card.find('h2').text.strip()
            address = card.find('p', class_='address').text.strip()
            phone = card.find('p', class_='phone').text.strip()
            contacts.append({'Name': name, 'Address': address, 'Phone': phone})
        
        return contacts
    else:
        print('Failed to scrape data.')
        return None

# Example usage
keyword = 'cleaning services'
location = 'New York'
contacts = scrape_business_contacts(keyword, location)
if contacts:
    for contact in contacts:
        print(contact)
else:
    print('No contacts found.')

