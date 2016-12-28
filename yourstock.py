import stockchecker
import math

# stores stock information in format: key=company name, value=[quantity of shares, average price]
STOCK = {}
# stores profits informations about every company the user share in format: key=company name, value=[total price user
# bought the shares, current total price of shares]
STOCK_PROFITS = {}


def fill_user_stock():
    f = open('companies.txt')
    for line in f:
        splitted_line = line.strip().split(":")
        STOCK[splitted_line[0]] = [splitted_line[1], splitted_line[2]]
    f.close()


def calculate_interest(get_info=False):
    if get_info:
        stockchecker.get_my_companies_info()
    for company in stockchecker.MY_COMPANIES:
        buy_value = int(STOCK[company][0]) * float(STOCK[company][1])
        idx = stockchecker.COMPANY.index(company)
        current_value = int(STOCK[company][0]) * float(stockchecker.PRICE[idx].replace(',', '.'))
        STOCK_PROFITS[company] = [math.ceil(buy_value*100)/100, math.ceil(current_value*100)/100]
        # print(company)
        # print(buy_value)
        # print(current_value)


def clear_stock_informations():
    STOCK.clear()
    STOCK_PROFITS.clear()

if __name__ == '__main__':
    fill_user_stock()
    print(STOCK)
    calculate_interest()
    # print(stockchecker.COMPANY)
    # print(stockchecker.PRICE)
    print(STOCK_PROFITS)
