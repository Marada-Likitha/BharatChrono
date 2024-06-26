import requests
from bs4 import BeautifulSoup
import csv

wiki_links = [
    # Add all the Wikipedia links here
    "https://en.wikipedia.org/wiki/Battle_of_Chaul",
    "https://en.wikipedia.org/wiki/Mamluk%E2%80%93Portuguese_conflicts",
    "https://en.wikipedia.org/wiki/Battle_of_Diu",
    "https://en.wikipedia.org/wiki/Battle_of_Gagron",
    "https://en.wikipedia.org/wiki/Battle_of_Khatoli",
    "https://en.wikipedia.org/wiki/Battle_of_Dholpur",
    "https://en.wikipedia.org/wiki/Battle_of_Raichur",
    "https://en.wikipedia.org/wiki/First_Battle_of_Panipat",
    "https://en.wikipedia.org/wiki/Battle_of_Khanwa",
    "https://en.wikipedia.org/wiki/Battle_of_Chausa",
    "https://en.wikipedia.org/wiki/Battle_of_Tughlaqabad",
    "https://en.wikipedia.org/wiki/Second_Battle_of_Panipat",
    "https://en.wikipedia.org/wiki/Battle_of_Talikota",
    "https://en.wikipedia.org/wiki/Paradesi_Synagogue",
    "https://en.wikipedia.org/wiki/List_of_battles_in_Rajasthan#Against_the_Mughal_Empires",
    "https://en.wikipedia.org/wiki/East_India_Company",
    "https://en.wikipedia.org/wiki/Battle_of_Rohilla",
    "https://en.wikipedia.org/wiki/Battle_of_Amritsar_(1634)",
    "https://en.wikipedia.org/wiki/Battle_of_Lahira",
    "https://en.wikipedia.org/wiki/Battle_of_Kartarpur",
    "https://en.wikipedia.org/wiki/Battle_of_Pratapgarh",
    "https://en.wikipedia.org/wiki/Shivaji#Siege_of_Panhala",
    "https://en.wikipedia.org/wiki/Battle_of_Pavan_Khind",
    "https://en.wikipedia.org/wiki/Battle_of_Surat",
    "https://en.wikipedia.org/wiki/Battle_of_Purandar#Treaty_of_Purandar",
    "https://en.wikipedia.org/wiki/Gokula#Battle_of_Tilpat",
    "https://en.wikipedia.org/wiki/Battle_of_Sinhagad",
    "https://en.wikipedia.org/wiki/Battle_of_Saraighat",
    "https://en.wikipedia.org/wiki/Battle_of_Salher",
    "https://en.wikipedia.org/wiki/Battle_of_Itakhuli",
    "https://en.wikipedia.org/wiki/Mughal_invasions_of_Konkan_(1684)",
    "https://en.wikipedia.org/wiki/Battle_of_Wai",
    "https://en.wikipedia.org/wiki/Deccan_wars#Maratha_capital_moved_to_Jinji",
    "https://en.wikipedia.org/wiki/Battle_of_Nadaun",
    "https://en.wikipedia.org/wiki/Battle_of_Guler_(1696)",
    "https://en.wikipedia.org/wiki/Danish_India",
    "https://en.wikipedia.org/wiki/Battle_of_Anandpur_(1700)",
    "https://en.wikipedia.org/wiki/Battle_of_Nirmohgarh_(1702)",
    "https://en.wikipedia.org/wiki/Battle_of_Chappar_Chiri",
    "https://en.wikipedia.org/wiki/Attingal_Outbreak",
    "https://en.wikipedia.org/wiki/Battle_of_Palkhed",
    "https://en.wikipedia.org/wiki/Battle_of_Bundelkhand",
    "https://en.wikipedia.org/wiki/Battle_of_Dabhoi",
    "https://en.wikipedia.org/wiki/Battle_of_Bhopal",
    "https://en.wikipedia.org/wiki/Battle_of_Vasai",
    "https://en.wikipedia.org/wiki/Battle_of_Colachel",
    "https://en.wikipedia.org/wiki/Marthanda_Varma#Treaty_of_Mavelikkara_(1753)",
    "https://en.wikipedia.org/wiki/Dutch_East_India_Company",
    "https://en.wikipedia.org/wiki/Battle_of_Kumher",
    "https://en.wikipedia.org/wiki/Black_Hole_of_Calcutta",
    "https://en.wikipedia.org/wiki/Battle_of_Narela",
    "https://en.wikipedia.org/wiki/Battle_of_Plassey",
    "https://en.wikipedia.org/wiki/Battle_of_Delhi_(1757)",
    "https://en.wikipedia.org/wiki/Carnatic_wars#Third_Carnatic_War_(1756%E2%80%931763)",
    "https://en.wikipedia.org/wiki/Capture_of_Peshawar_(1758)",
    "https://en.wikipedia.org/wiki/French_India",
    "https://en.wikipedia.org/wiki/First_Battle_of_Lahore_(1759)",
    "https://en.wikipedia.org/wiki/Battle_of_Wandiwash",
    "https://en.wikipedia.org/wiki/Third_Battle_of_Panipat",
    "https://en.wikipedia.org/wiki/Capture_of_Agra",
    "https://en.wikipedia.org/wiki/Battle_of_Sialkot_(1761)",
    "https://en.wikipedia.org/wiki/Battle_of_Gujranwala_(1761)",
    "https://en.wikipedia.org/wiki/Vadda_Ghalughara",
    "https://en.wikipedia.org/wiki/Battle_of_Harnaulgarh",
    "https://en.wikipedia.org/wiki/Battle_of_Rakshasbhuvan",
    "https://en.wikipedia.org/wiki/Battle_of_Sirhind_(1764)",
    "https://en.wikipedia.org/wiki/Battle_of_Buxar",
    "https://en.wikipedia.org/wiki/First_Anglo-Mysore_War",
    "https://en.wikipedia.org/wiki/Great_Bengal_famine_of_1770",
    "https://en.wikipedia.org/wiki/Regulating_Act_1773",
    "https://en.wikipedia.org/wiki/First_Anglo-Maratha_War",
    "https://en.wikipedia.org/wiki/Battle_of_Mandan",
    "https://en.wikipedia.org/wiki/Battle_of_Wadgaon",
    "https://en.wikipedia.org/wiki/Treaty_of_Salbai",
    "https://en.wikipedia.org/wiki/Second_Anglo-Mysore_War",
    "https://en.wikipedia.org/wiki/Bhor_Ghat#History",
    "https://en.wikipedia.org/wiki/Treaty_of_Mangalore",
    "https://en.wikipedia.org/wiki/Captivity_of_Mangalorean_Catholics_at_Seringapatam",
    "https://en.wikipedia.org/wiki/Maratha%E2%80%93Mysore_wars",
    "https://en.wikipedia.org/wiki/Third_Anglo-Mysore_War",
    "https://en.wikipedia.org/wiki/Battle_of_Patan",
    "https://en.wikipedia.org/wiki/Battle_of_Nedumkotta",
    "https://en.wikipedia.org/wiki/Bengal_Renaissance",
    "https://en.wikipedia.org/wiki/Fourth_Anglo-Mysore_War",
    "https://en.wikipedia.org/wiki/Polygar_Wars",
    "https://en.wikipedia.org/wiki/Second_Anglo-Maratha_War",
    "https://en.wikipedia.org/wiki/Siege_of_Multan_(1818)",
    "https://en.wikipedia.org/wiki/Battle_of_Shopian",
    "https://en.wikipedia.org/wiki/Anglo-Burmese_Wars",
    "https://en.wikipedia.org/wiki/Battle_of_Nowshera",
    "https://en.wikipedia.org/wiki/British_rule_in_Burma",
    "https://en.wikipedia.org/wiki/Kol_uprising",
    "https://en.wikipedia.org/wiki/Battle_of_Balakot",
    "https://en.wikipedia.org/wiki/Capture_of_Peshawar_(1834)",
    "https://en.wikipedia.org/wiki/Battle_of_Jamrud",
    "https://en.wikipedia.org/wiki/First_Anglo-Afghan_War",
    "https://en.wikipedia.org/wiki/First_Anglo-Sikh_war",
    "https://en.wikipedia.org/wiki/Battle_of_Ramnagar",
    "https://en.wikipedia.org/wiki/Battle_of_Chillianwala",
    "https://en.wikipedia.org/wiki/Santhal_rebellion",
    "https://en.wikipedia.org/wiki/Hindu_Widows%27_Remarriage_Act,_1856",
    "https://en.wikipedia.org/wiki/Indian_Rebellion_of_1857",
    "https://en.wikipedia.org/wiki/University_of_Mumbai",
    "https://en.wikipedia.org/wiki/University_of_Madras",
    "https://en.wikipedia.org/wiki/University_of_Calcutta",
    "https://en.wikipedia.org/wiki/British_Raj",
    "https://en.wikipedia.org/wiki/Prarthana_Samaj",
    "https://en.wikipedia.org/wiki/Satyashodhak_Samaj",
    "https://en.wikipedia.org/wiki/Aligarh_Muslim_University",
    "https://en.wikipedia.org/wiki/Arya_Samaj",
    "https://en.wikipedia.org/wiki/Deccan_Riots",
    "https://en.wikipedia.org/wiki/Delhi_Durbar",
    "https://en.wikipedia.org/wiki/Indian_National_Congress",
    "https://en.wikipedia.org/wiki/Anglo-Manipur_War",
    "https://en.wikipedia.org/wiki/Anushilan_Samiti",
    "https://en.wikipedia.org/wiki/British_expedition_to_Tibet",
    "https://en.wikipedia.org/wiki/Partition_of_Bengal_(1905)",
    "https://en.wikipedia.org/wiki/Jugantar",
    "https://en.wikipedia.org/wiki/All-India_Muslim_League",
    "https://en.wikipedia.org/wiki/Surat_Split",
    "https://en.wikipedia.org/wiki/Emperor_vs_Aurobindo_Ghosh_and_others",
    "https://en.wikipedia.org/wiki/Indian_Councils_Act_1909",
    "https://en.wikipedia.org/wiki/Delhi_conspiracy_case",
    "https://en.wikipedia.org/wiki/Ghadar_Movement",
    "https://en.wikipedia.org/wiki/Hindu%E2%80%93German_Conspiracy",
    "https://en.wikipedia.org/wiki/Ghadar_Mutiny",
    "https://en.wikipedia.org/wiki/Provisional_Government_of_India",
    "https://en.wikipedia.org/wiki/Lucknow_Pact",
    "https://en.wikipedia.org/wiki/Champaran_Satyagraha",
    "https://en.wikipedia.org/wiki/Justice_Party_(India)",
    "https://en.wikipedia.org/wiki/Kheda_Satyagraha_of_1918",
    "https://en.wikipedia.org/wiki/Jallianwala_Bagh_massacre",
    "https://en.wikipedia.org/wiki/Montagu%E2%80%93Chelmsford_Reforms",
    "https://en.wikipedia.org/wiki/Rowlatt_Act",
    "https://en.wikipedia.org/wiki/Non-cooperation_movement",
    "https://en.wikipedia.org/wiki/Khilafat_Movement",
    "https://en.wikipedia.org/wiki/Chauri_Chaura_incident",
    "https://en.wikipedia.org/wiki/Hindustan_Socialist_Republican_Association",
    "https://en.wikipedia.org/wiki/Kakori_conspiracy",
    "https://en.wikipedia.org/wiki/Rashtriya_Swayamsevak_Sangh",
    "https://en.wikipedia.org/wiki/Mahad_Satyagraha",
    "https://en.wikipedia.org/wiki/Simon_Commission",
    "https://en.wikipedia.org/wiki/Bardoli_Satyagraha",
    "https://en.wikipedia.org/wiki/Purna_Swaraj",
    "https://en.wikipedia.org/wiki/Salt_March",
    "https://en.wikipedia.org/wiki/Round_Table_Conferences_(India)",
    "https://en.wikipedia.org/wiki/Gandhi%E2%80%93Irwin_Pact",
    "https://en.wikipedia.org/wiki/Poona_Pact",
    "https://en.wikipedia.org/wiki/Government_of_India_Act_1935",
    "https://en.wikipedia.org/wiki/1937_Indian_provincial_elections",
    "https://en.wikipedia.org/wiki/All_India_Forward_Bloc",
    "https://en.wikipedia.org/wiki/Lahore_Resolution",
    "https://en.wikipedia.org/wiki/All-India_Jamhur_Muslim_League",
    "https://en.wikipedia.org/wiki/August_Offer",
    "https://en.wikipedia.org/wiki/Cripps_Mission",
    "https://en.wikipedia.org/wiki/Quit_India_Movement",
    "https://en.wikipedia.org/wiki/Indian_National_Army",
    "https://en.wikipedia.org/wiki/Azad_Hind",
    "https://en.wikipedia.org/wiki/Simla_Conference",
    "https://en.wikipedia.org/wiki/Royal_Indian_Navy_mutiny",
    "https://en.wikipedia.org/wiki/1946_Cabinet_Mission_to_India",
    "https://en.wikipedia.org/wiki/Direct_Action_Day",
    "https://en.wikipedia.org/wiki/Noakhali_riots",
    "https://en.wikipedia.org/wiki/Indian_Independence_Act_1947",
    "https://en.wikipedia.org/wiki/Third_Front_(India)#National_",
    "https://en.wikipedia.org/wiki/Partition_of_India",
    "https://en.wikipedia.org/wiki/Indo-Pakistani_war_of_1947%E2%80%931948",
    "https://en.wikipedia.org/wiki/Line_of_Control",
    "https://en.wikipedia.org/wiki/Kargil_War",
    "https://en.wikipedia.org/wiki/States_Reorganisation_Act,_1956",
    "https://en.wikipedia.org/wiki/Indo-Pakistani_war_of_1965",
    "https://en.wikipedia.org/wiki/ISRO",
    "https://en.wikipedia.org/wiki/Indo-Pakistani_war_of_1971",
    "https://en.wikipedia.org/wiki/Smiling_Buddha",
    "https://en.wikipedia.org/wiki/The_Emergency_(India)",
    "https://en.wikipedia.org/wiki/Communist_Party_of_India_(Marxist)",
    "https://en.wikipedia.org/wiki/Operation_Blue_Star",
    "https://en.wikipedia.org/wiki/1984_anti-Sikh_riots",
    "https://en.wikipedia.org/wiki/Securities_and_Exchange_Board_of_India",
    "https://en.wikipedia.org/wiki/Exodus_of_Kashmiri_Hindus",
    "https://en.wikipedia.org/wiki/Liberation_Tigers_of_Tamil_Eelam",
    "https://en.wikipedia.org/wiki/Economic_liberalization",
    "https://en.wikipedia.org/wiki/Demolition_of_the_Babri_Masjid",
    "https://en.wikipedia.org/wiki/Bombay_riots",
    "https://en.wikipedia.org/wiki/1996_Amarnath_Yatra_tragedy",
    "https://en.wikipedia.org/wiki/1999_Odisha_cyclone",
    "https://en.wikipedia.org/wiki/2001_Gujarat_earthquake",
    "https://en.wikipedia.org/wiki/2004_Indian_Ocean_earthquake_and_tsunami",
    "https://en.wikipedia.org/wiki/2005_Kashmir_earthquake",
    "https://en.wikipedia.org/wiki/2008_Mumbai_attacks",
    "https://en.wikipedia.org/wiki/2010_Pune_bombing",
    "https://en.wikipedia.org/wiki/2013_Indian_helicopter_bribery_scandal",
    "https://en.wikipedia.org/wiki/2013_Hyderabad_blasts",
    "https://en.wikipedia.org/wiki/Mars_Orbiter_Mission",
    "https://en.wikipedia.org/wiki/Goods_and_Services_Tax_(India)",
    "https://en.wikipedia.org/wiki/2019_Balakot_airstrike",
    "https://en.wikipedia.org/wiki/Vienna_Convention_on_the_Law_of_Treaties",
    "https://en.wikipedia.org/wiki/Article_370_of_the_Constitution_of_India",
    "https://en.wikipedia.org/wiki/Citizenship_(Amendment)_Act,_2019",
    "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_India",
    "https://en.wikipedia.org/wiki/Chandrayaan-3",
   " https://en.wikipedia.org/wiki/Aditya-L1",
    "https://en.wikipedia.org/wiki/2023_Cricket_World_Cup",
]

def scrape_wikipedia_links(links, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Event Name', 'Important Info']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        for link in links:
            response = requests.get(link)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            event_name = soup.find('h1', id='firstHeading').text.strip()
            
            important_info = ""
            paragraphs = soup.find_all('p')
            paragraphs_to_extract = 6  # Number of paragraphs to extract
            extracted_paragraphs = 0
            
            for paragraph in paragraphs:
                if paragraph.text.strip():
                    important_info += paragraph.text.strip() + "\n\n"  # Concatenate with newline
                    extracted_paragraphs += 1
                    if extracted_paragraphs >= paragraphs_to_extract:
                        break
            
            writer.writerow({'Event Name': event_name, 'Important Info': important_info})

if __name__ == "__main__":
    output_file = 'data2.csv'
    scrape_wikipedia_links(wiki_links, output_file)
