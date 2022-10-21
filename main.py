from lxml import html
from bs4 import BeautifulSoup, Comment
from selenium.webdriver import Chrome

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


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
# listao.append(team_search(key))