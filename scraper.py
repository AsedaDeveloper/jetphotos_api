
import requests
from bs4 import BeautifulSoup

def scrape_jetphotos(reg=None, aircraft_type=None, airline=None, serial=None):
    base_url = 'https://www.jetphotos.com/photo/keyword/'
    query_params = []

    if reg:
        query_params.append(reg)
    if aircraft_type:
        query_params.append(aircraft_type)
    if airline:
        query_params.append(airline)
    if serial:
        query_params.append(serial)

    search_url = base_url + '+'.join(query_params)
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    results = []
    # TODO: Parse images and metadata from JetPhotos HTML
    return results
