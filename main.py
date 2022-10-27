import statistics
from lxml import html
from bs4 import BeautifulSoup, Comment
import pandas as pd
import requests

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


teams_adress = {'palmeiras' : 'palmeiras/1963', 'internacional' : 'internacional/1966', 'flamengo' : 'flamengo/5981', 'fluminense' : 'fluminense/1961',
'corinthians' : 'corinthians/1957', 'athletico paranaense' : 'athletico/1967', 'atletico mineiro' : 'atletico-mineiro/1977',
'america mineiro' : 'america-mineiro/1973', 'fortaleza' : 'fortaleza/2020', 'botafogo' : 'botafogo/1958', 'santos' : 'santos/1968',
'sao paulo' : 'sao-paulo/1981', 'bragantino' : 'red-bull-bragantino/1999', 'goias' : 'goias/1960', 'coritiba' : 'coritiba/1982',
'ceara' : 'ceara/2001', 'cuiaba' : 'cuiaba/49202', 'atletico goianiense' : 'atletico-goianiense/7314', 'avai' : 'avai/7315', 'juventude' : 'juventude/1980'}

base_url = 'https://www.sofascore.com/team/football/'

def team_search(time:str):

    
    driver = webdriver.Chrome(ChromeDriverManager().install())
    
    url = base_url + teams_adress[time]

    driver.get(url)

    soup = BeautifulSoup(driver.page_source, 'lxml')

    test = str(soup)

    tree = html.fromstring(test)

    data_dict = {}

    for i in range(2, 7):
        base_xpath = f'//*[@id="__next"]/div/main/div/div[2]/div[2]/div/div[2]/div[3]/div[{i}]/div[2]/div[*]/'
        elements_1 = tree.xpath(base_xpath + 'span[1]')
        elements_2 = tree.xpath(base_xpath + 'span[2]')
        for data in range(len(elements_1)):
            if data == 0: 
                data_dict['Time'] = time.title()
            data_dict[elements_1[data].text] = elements_2[data].text
    

    return data_dict

    
# dictfinal = {}
# listao = []
# for key, value in teams_adress.items():
#   listao.append(team_search(key))

# dataframe = pd.DataFrame(listao[5].values(), listao[5].keys(), columns=['Valores'])




browsers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \(KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"}

base_api = 'https://api.sofascore.com/api/v1/team/'
middle_api = '/unique-tournament/325/season/'
end_api = '/statistics/overall'

enpoint_17 = '13100'
enpoint_18 = '16183'
enpoint_19 = '22931'
enpoint_20 = '27591'
enpoint_21 = '36166'
enpoint_22 = '40557'


def escolhe_time(time:str):

    data_list = []
    cont_url_list = 0
    cont_data_list = 0

    id_time = teams_adress[time][-4:]

    url_17 = base_api + id_time + middle_api + enpoint_17 + end_api
    url_18 = base_api + id_time + middle_api + enpoint_18 + end_api
    url_19 = base_api + id_time + middle_api + enpoint_19 + end_api
    url_20 = base_api + id_time + middle_api + enpoint_20 + end_api
    url_21 = base_api + id_time + middle_api + enpoint_21 + end_api
    url_22 = base_api + id_time + middle_api + enpoint_22 + end_api

    urls_list = [url_17, url_18, url_19, url_20, url_21, url_22]

    for url in urls_list:
        api_link = requests.get(url, headers = browsers).json()
        if not 'error' in api_link:
            data_list.append(api_link['statistics'])
            if urls_list.index(urls_list[cont_url_list]) == 0:
                data_list[cont_data_list]['ano'] = 2017
            elif urls_list.index(urls_list[cont_url_list]) == 1:
                data_list[cont_data_list]['ano'] = 2018
            elif urls_list.index(urls_list[cont_url_list]) == 2:
                data_list[cont_data_list]['ano'] = 2019
            elif urls_list.index(urls_list[cont_url_list]) == 3:
                data_list[cont_data_list]['ano'] = 2020
            elif urls_list.index(urls_list[cont_url_list]) == 4:
                data_list[cont_data_list]['ano'] = 2021
            elif urls_list.index(urls_list[cont_url_list]) == 5:
                data_list[cont_data_list]['ano'] = 2022
            cont_data_list+=1
        cont_url_list+=1

    return data_list


# pages_list = []
# id_time = teams_adress['flamengo'][-4:]
# url_17 = base_api + id_time + middle_api + enpoint_17 + end_api
# url_18 = base_api + id_time + middle_api + enpoint_18 + end_api
# pages_list.append(requests.get(url_17, headers = browsers).json())
# pages_list.append(requests.get(url_18, headers = browsers).json())


   
# Palmeiras


# 20/21
# https://api.sofascore.com/api/v1/team/1963/unique-tournament/325/season/27591/statistics/overall
# https://api.sofascore.com/api/v1/unique-tournament/325/season/27591/top-teams/overall

# 21
# https://api.sofascore.com/api/v1/team/1963/unique-tournament/325/season/36166/statistics/overall
# https://api.sofascore.com/api/v1/unique-tournament/325/season/36166/top-teams/overall

# 22
# https://api.sofascore.com/api/v1/team/1963/unique-tournament/325/season/40557/statistics/overall
# https://api.sofascore.com/api/v1/unique-tournament/325/season/40557/top-teams/overall



# Flamengo


# 20/21
# https://api.sofascore.com/api/v1/team/5981/unique-tournament/325/season/27591/statistics/overall
# https://api.sofascore.com/api/v1/unique-tournament/325/season/27591/top-teams/overall

# 21
# https://api.sofascore.com/api/v1/team/5981/unique-tournament/325/season/36166/statistics/overall
# https://api.sofascore.com/api/v1/unique-tournament/325/season/36166/top-teams/overall

# 22
# https://api.sofascore.com/api/v1/team/5981/unique-tournament/325/season/40557/statistics/overall
# https://api.sofascore.com/api/v1/unique-tournament/325/season/40557/top-teams/overall