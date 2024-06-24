import time
import base64
from io import BytesIO
import os
import requests

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from webdriver_manager.chrome import ChromeDriverManager
import requests
from PIL import Image

import json

cwd = os.getcwd()
IMAGE_FOLDER = 'download'

os.makedirs(
    name=f'{cwd}/{IMAGE_FOLDER}',
    exist_ok=True
)


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(
    service=service
)

SLEEP_TIME = 1

image_data = {
        "images": []
}

def download_google_images(search_query: str) -> str:
    '''Download google images with this function\n
       Takes -> search_query, number_of_images\n
       Returns -> None
    '''    

    os.makedirs(
    name=f'{cwd}/{IMAGE_FOLDER}',
    exist_ok=True
    )
    

    url = 'https://images.google.com/'

    driver.get(
        url=url
    )
    print(By.XPATH)
    box = driver.find_element(
        by=By.XPATH,
        value="//textarea[contains(@class,'gLFyf')]"
    )

    box.send_keys(search_query)
    box.send_keys(Keys.ENTER)
    time.sleep(SLEEP_TIME)

    img_result = driver.find_element(
        by=By.XPATH,
        value="//img[contains(@class,'YQ4gaf') and not(contains(@class, ' '))]"
    )

    img_url = img_result.get_attribute('src')

    count = 0
    try:
        src =''
        if 'https://encrypted' in img_result.get_attribute('src'):
            pass
        elif 'http' in img_result.get_attribute('src'):
            src += img_result.get_attribute('src')
        else:
            pass
        if src == '' and 'base' in img_result.get_attribute('src'):
            src += img_result.get_attribute('src')
        if 'https://' in src:
            file_path = f'{IMAGE_FOLDER}/{search_query}.jpeg'

            try:
                result = requests.get(src, allow_redirects=True, timeout=10)
                open(file_path, 'wb').write(result.content)

                img_data = {
                    "href": src,
                    "image_path": file_path
                }
                image_data["images"].append(img_data)

                img = Image.open(file_path)
                img = img.convert('RGB')
                img.save(file_path, 'JPEG')
                print(f'Count - {count} - Image saved from https.')
                print(src)
            except:
                print('Bad image.')
                try:
                    os.unlink(file_path)
                except:
                    pass
                count -= 1
        else:
            img_data = src.split(',')

            file_path = f'{IMAGE_FOLDER}/{search_query}.jpeg'
            try:
                img = Image.open(BytesIO(base64.b64decode(img_data[1])))
                img = img.convert('RGB')
                img.save(file_path, 'JPEG')
                print(f'Count - {count} - Image saved from Base64.')

                img_data = {
                    "href": src,
                    "image_path": file_path
                }
                image_data["images"].append(img_data)

            except:
                print('Bad image.')
                count -= 1
    except ElementClickInterceptedException as e:
            count -= 1
            print(e)
            print('Image is not clickable.')            
     
tags = [
        "Battle of Chaul",
        "Mamluk–Portuguese conflicts",
        "Battle of Diu",
        "Battle of Gagron",
        "Battle of Khatoli",
        "Battle of Dholpur",
        "Battle of Raichur",
        "First Battle of Panipat",
        "Battle of Khanwa",
        "Battle of Chausa",
        "Battle of Tughlaqabad",
        "Second Battle of Panipat",
        "Battle of Talikota",
        "Paradesi Synagogue",
        "List of battles in Rajasthan#Against the Mughal Empires",
        "East India Company",
        "Battle of Rohilla",
        "Battle of Amritsar (1634)",
        "Battle of Lahira",
        "Battle of Kartarpur",
        "Battle of Pratapgarh",
        "Siege of Panhala",
        "Battle of Pavan Khind",
        "Battle of Surat",
        "Treaty of Purandar",
        "Gokula Battle of Tilpat",
        "Battle of Sinhagad",
        "Battle of Saraighat",
        "Battle of Salher",
        "Battle of Itakhuli",
        "Mughal invasions of Konkan (1684)",
        "Battle of Wai",
        "Deccan wars Maratha capital moved to Jinji",
        "Battle of Nadaun",
        "Battle of Guler (1696)",
        "Danish India",
        "Battle of Anandpur (1700)",
        "Battle of Nirmohgarh (1702)",
        "Battle of Chappar Chiri",
        "Attingal Outbreak",
        "Battle of Palkhed",
        "Battle of Bundelkhand",
        "Battle of Dabhoi",
        "Battle of Bhopal",
        "Battle of Vasai",
        "Battle of Colachel",
        "Marthanda Varma Treaty of Mavelikkara (1753)",
        "Dutch East India Company",
        "Battle of Kumher",
        "Black Hole of Calcutta",
        "Battle of Narela",
        "Battle of Plassey",
        "Battle of Delhi (1757)",
        "Carnatic wars Third Carnatic War (1756–1763)",
        "Capture of Peshawar (1758)",
        "French India",
        "First Battle of Lahore (1759)",
        "Battle of Wandiwash",
        "Third Battle of Panipat",
        "Capture of Agra",
        "Battle of Sialkot (1761)",
        "Battle of Gujranwala (1761)",
        "Vadda Ghalughara",
        "Battle of Harnaulgarh",
        "Battle of Rakshasbhuvan",
        "Battle of Sirhind (1764)",
        "Battle of Buxar",
        "First Anglo-Mysore War",
        "Great Bengal famine of 1770",
        "Regulating Act 1773",
        "First Anglo-Maratha War",
        "Battle of Mandan",
        "Battle of Wadgaon",
        "Treaty of Salbai",
        "Second Anglo-Mysore War",
        "Bhor Ghat History",
        "Treaty of Mangalore",
        "Captivity of Mangalorean Catholics at Seringapatam",
        "Maratha–Mysore wars",
        "Third Anglo-Mysore War",
        "Battle of Patan",
        "Battle of Nedumkotta",
        "Bengal Renaissance",
        "Fourth Anglo-Mysore War",
        "Polygar Wars",
        "Second Anglo-Maratha War",
        "Siege of Multan (1818)",
        "Battle of Shopian",
        "Anglo-Burmese Wars",
        "Battle of Nowshera",
        "British rule in Burma",
        "Kol uprising",
        "Battle of Balakot",
        "Capture of Peshawar (1834)",
        "Battle of Jamrud",
        "First Anglo-Afghan War",
        "First Anglo-Sikh war",
        "Battle of Ramnagar",
        "Battle of Chillianwala",
        "Santhal rebellion",
        "Hindu Widows' Remarriage Act, 1856",
        "Indian Rebellion of 1857",
        "University of Mumbai",
        "University of Madras",
        "University of Calcutta",
        "British Raj",
        "Prarthana Samaj",
        "Satyashodhak Samaj",
        "Aligarh Muslim University",
        "Arya Samaj",
        "Deccan Riots",
        "Delhi Durbar",
        "Indian National Congress",
        "Anglo-Manipur War",
        "Anushilan Samiti",
        "British expedition to Tibet",
        "Partition of Bengal (1905)",
        "Jugantar",
        "All-India Muslim League",
        "Surat Split",
        "Emperor vs Aurobindo Ghosh and others",
        "Indian Councils Act 1909",
        "Delhi conspiracy case",
        "Ghadar Movement",
        "Hindu–German Conspiracy",
        "Ghadar Mutiny",
        "Provisional Government of India",
        "Lucknow Pact",
        "Champaran Satyagraha",
        "Justice Party (India)",
        "Kheda Satyagraha of 1918",
        "Jallianwala Bagh massacre",
        "Montagu–Chelmsford Reforms",
        "Rowlatt Act",
        "Non-cooperation movement",
        "Khilafat Movement",
        "Chauri Chaura incident",
        "Hindustan Socialist Republican Association",
        "Kakori conspiracy",
        "Rashtriya Swayamsevak Sangh",
        "Mahad Satyagraha",
        "Simon Commission",
        "Bardoli Satyagraha",
        "Purna Swaraj",
        "Salt March",
        "Round Table Conferences (India)",
        "Gandhi–Irwin Pact",
        "Poona Pact",
        "Government of India Act 1935",
        "1937 Indian provincial elections",
        "All India Forward Bloc",
        "Lahore Resolution",
        "All-India Jamhur Muslim League",
        "August Offer",
        "Cripps Mission",
        "Quit India Movement",
        "Indian National Army",
        "Azad Hind",
        "Simla Conference",
        "Royal Indian Navy mutiny",
        "1946 Cabinet Mission to India",
        "Direct Action Day",
        "Noakhali riots",
        "Indian Independence Act 1947",
        "Third Front (India) National",
        "Partition of India",
        "Indo-Pakistani war of 1947–1948",
        "Line of Control",
        "Kargil War",
        "States Reorganisation Act, 1956",
        "Indo-Pakistani war of 1965",
        "ISRO",
        "Indo-Pakistani war of 1971",
        "Smiling Buddha",
        "The Emergency (India)",
        "Communist Party of India (Marxist)",
        "Operation Blue Star",
        "1984 anti-Sikh riots",
        "Securities and Exchange Board of India",
        "Exodus of Kashmiri Hindus",
        "Liberation Tigers of Tamil Eelam",
        "Economic liberalization",
        "Demolition of the Babri Masjid",
        "Bombay riots",
        "1996 Amarnath Yatra tragedy",
        "1999 Odisha cyclone",
        "2001 Gujarat earthquake",
        "2004 Indian Ocean earthquake and tsunami",
        "2005 Kashmir earthquake",
        "2008 Mumbai attacks",
        "2010 Pune bombing",
        "2013 Indian helicopter bribery scandal",
        "2013 Hyderabad blasts",
        "Mars Orbiter Mission",
        "Goods and Services Tax (India)",
        "2019 Balakot airstrike",
        "Vienna Convention on the Law of Treaties",
        "Article 370 of the Constitution of India",
        "Citizenship (Amendment) Act, 2019",
        "COVID-19 pandemic in India",
        "Chandrayaan-3",
        "Aditya-L1",
        "2023 Cricket World Cup",
]

for tag in tags:
    print(f'{"="*10} Downloding for the tag - {tag} {"="*10}')
    download_google_images(
        tag,
        
    )
    print(f'{"="*10} Finished downloding for the tag - {tag} {"="*10}')

driver.quit()

json_data = json.dumps(image_data, indent=4)

print('\n\n\n')
print(json_data)
print('\n\n\n\n')

with open('image_data.json', 'w') as file:
    file.write(json_data)