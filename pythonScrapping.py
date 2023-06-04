import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint

url = 'https://www.amazon.com/s?k=asus+laptop&crid=YUKIQZKT7NQ5&sprefix=asus+laptop%2Caps%2C360&ref=nb_sb_noss_1'

num_pages = 5

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

file = open('asus_laptops.csv', 'w', newline='', encoding='UTF-8')
csv_writer = csv.writer(file)
csv_writer.writerow(['Name', 'Price'])

for page in range(1, num_pages + 1):
    page_url = url + '&page=' + str(page)

    
    response = requests.get(page_url, headers=headers)
    content = response.text

   
    soup = BeautifulSoup(content, 'html.parser')

    product_items = soup.find_all('div', class_='s-result-item')

    for item in product_items:
        name_element = item.find('span', class_='a-size-medium')
        if name_element is not None:
            name = name_element.text.strip()

            price_element = item.find('span', class_='a-price')
            if price_element is not None:
                price = price_element.find('span', class_='a-offscreen').text.strip()
            else:
                price = 'N/A'

            print(name, price)

            csv_writer.writerow([name, price])

    sleep(randint(1, 5))

file.close()
