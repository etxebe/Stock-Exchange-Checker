import os.path
from bs4 import BeautifulSoup
from urllib.request import urlopen

# variables that stores information for each company
COMPANY = []
PRICE = []
CHANGE = []
PERCENTAGE_CHANGE = []
DATE = []

# variable that stores what company shares you own
MY_COMPANIES = []


def get_stock_info(company):
    stock_site = "http://notowania.pb.pl/stocktable/GPWAKCJE"
    page = urlopen(stock_site)
    soup = BeautifulSoup(page, "html.parser")

    all_tr_items = soup.find_all('tr')
    for item in all_tr_items:
        a_item = item.find('a')
        if a_item is not None:
            if a_item.find(text=True) == company:
                COMPANY.append(a_item.find(text=True))
                td_items = item.findAll('td')
                PRICE.append(td_items[1].find(text=True))
                CHANGE.append(td_items[2].find(text=True))
                PERCENTAGE_CHANGE.append(td_items[3].find(text=True))
                DATE.append(td_items[9].find(text=True))


def get_my_companies_info():
    if os.path.isfile('companies.txt'):
        file_companies = open('companies.txt', 'r')
        for company in file_companies:
            company = company.split(":")[0]
            if len(company.strip()) > 0:
                MY_COMPANIES.append(company.strip())
                get_stock_info(company.strip())
        file_companies.close()


def clear_informations():
    del MY_COMPANIES[:]
    del COMPANY[:]
    del PRICE[:]
    del CHANGE[:]
    del PERCENTAGE_CHANGE[:]
    del DATE[:]

if __name__ == '__main__':
    get_my_companies_info()

    print(COMPANY)
    print(PRICE)
    print(CHANGE)
    print(PERCENTAGE_CHANGE)
    print(DATE)
