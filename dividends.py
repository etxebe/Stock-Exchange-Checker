from bs4 import BeautifulSoup
from urllib.request import urlopen

# variables that stores dividends' informations for each company
DIVIDEND_COMPANY = []
DIVIDEND_DATE = []
INTEREST = []
PAY_DATE = []
DIVIDEND = []


def get_dividend_for_company(companies_arr):
    stock_site = "https://strefainwestorow.pl/dane/dywidendy/lista-dywidend/2017"
    page = urlopen(stock_site)
    soup = BeautifulSoup(page, "html.parser")
    all_tr_items = soup.find_all('tr')

    for item in all_tr_items:
        a_item = item.find('a')
        if a_item is not None:
            for company in companies_arr:
                if a_item.find(text=True) == company:
                    td_items = item.findAll('td')
                    DIVIDEND_COMPANY.append(a_item.find(text=True))
                    DIVIDEND_DATE.append(td_items[3].find(text=True).strip())
                    INTEREST.append(td_items[4].find(text=True).strip())
                    PAY_DATE.append(td_items[5].find(text=True).strip())
                    DIVIDEND.append(td_items[6].find(text=True).strip())

if __name__ == '__main__':
    get_dividend_for_company(["PZU", "PGE", "GPW", "PGNIG", "PKOBP"])
    print(DIVIDEND_COMPANY)
    print(DIVIDEND_DATE)
    print(INTEREST)
    print(PAY_DATE)
    print(DIVIDEND)