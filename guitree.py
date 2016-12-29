import tkinter.simpledialog
from stockchecker import *
from yourstock import *
from dividends import *
from tkinter import *
from tkinter.ttk import *


class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Stock Exchange Checker")
        self.create_menu()
        self.initialize_interface_gpw()
        self.initalize_interface_profits()
        if DIVIDEND_COMPANY:
            self.initialize_dividends()

    def create_menu(self):
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        editmenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Add company", command=self.add_new_company)
        filemenu.add_command(label="Delete company", command=self.delete_company)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.master.quit)
        editmenu.add_command(label="Refresh", command=self.refresh)
        menubar.add_cascade(label="File", menu=filemenu)
        menubar.add_cascade(label="Edit", menu=editmenu)
        self.master.config(menu=menubar)

    def initialize_interface_gpw(self):
        self.gpw = Label(self.master, text="Notowania GPW", font="Verdana 10 bold")
        self.gpw.grid(row=0, column=0)

        self.gpw_table = Treeview(self.master, height=6, columns=("Kurs", "Zmiana", "Zmiana %", "Czas"))
        self.gpw_table.tag_configure('up', foreground='green', font="Verdana 10 bold")
        self.gpw_table.tag_configure('down', foreground='red', font="Verdana 10 bold")
        self.gpw_table.tag_configure('equal', foreground='black', font="Verdana 10 bold")

        self.gpw_table.heading('#0', text="Nazwa")
        self.gpw_table.heading('Kurs', text="Kurs")
        self.gpw_table.heading('Zmiana', text="Zmiana")
        self.gpw_table.heading('Zmiana %', text="Zmiana %")
        self.gpw_table.heading('Czas', text="Czas")
        self.gpw_table.column('#0', stretch=YES, anchor='center', width=120)
        self.gpw_table.column('Kurs', stretch=YES, anchor='center', width=150)
        self.gpw_table.column('Zmiana', stretch=YES, anchor='center', width=150)
        self.gpw_table.column('Zmiana %', stretch=YES, anchor='center', width=100)
        self.gpw_table.column('Czas', stretch=YES, anchor='center')
        self.gpw_table.grid(row=1, columnspan=3, sticky='nsew')
        for i in range(len(MY_COMPANIES)):
            if CHANGE[i][0] == '-':
                tag = ('down',)
            elif CHANGE[i] == '0,00':
                tag = ('equal',)
            else:
                tag = ('up',)
            self.gpw_table.insert('', 'end', text=MY_COMPANIES[i], values=(PRICE[i] + ' zl', CHANGE[i] + ' zl', PERCENTAGE_CHANGE[i], DATE[i]), tags=tag)

    def initalize_interface_profits(self):
        self.profit = Label(self.master, text="Rentownosc zakupionych spolek", font="Verdana 10 bold")
        self.profit.grid(row=12, column=0)

        self.profit_table = Treeview(self.master, height=6, columns=("Ilosc akcji", "Cena kupna akcji", "Aktualna cena akcji", "Wartosc wg cen kupna", "Wartosc wg aktualnej ceny", "Rentownosc"))
        self.profit_table.tag_configure('up', foreground='green', font="Verdana 10 bold")
        self.profit_table.tag_configure('down', foreground='red', font="Verdana 10 bold")
        self.profit_table.tag_configure('equal', foreground='black', font="Verdana 10 bold")

        self.profit_table.heading('#0', text="Nazwa")
        self.profit_table.heading('Ilosc akcji', text="Ilosc akcji")
        self.profit_table.heading('Cena kupna akcji', text="Cena kupna akcji")
        self.profit_table.heading('Aktualna cena akcji', text="Aktualna cena akcji")
        self.profit_table.heading('Wartosc wg cen kupna', text="Wartosc wg cen kupna")
        self.profit_table.heading('Wartosc wg aktualnej ceny', text="Wartosc wg aktualnej ceny")
        self.profit_table.heading('Rentownosc', text="Rentownosc")
        self.profit_table.column('#0', stretch=YES, anchor='center', width=120)
        self.profit_table.column('Ilosc akcji', stretch=YES, anchor='center', width=100)
        self.profit_table.column('Cena kupna akcji', stretch=YES, anchor='center', width=150)
        self.profit_table.column('Aktualna cena akcji', stretch=YES, anchor='center', width=150)
        self.profit_table.column('Wartosc wg cen kupna', stretch=YES, anchor='center', width=150)
        self.profit_table.column('Wartosc wg aktualnej ceny', stretch=YES, anchor='center', width=150)
        self.profit_table.column('Rentownosc', stretch=YES, anchor='center', width=120)
        self.profit_table.grid(row=13, columnspan=3, sticky='nsew')
        for share in MY_COMPANIES:
            idx = COMPANY.index(share)
            difference = math.ceil((STOCK_PROFITS[share][1]-STOCK_PROFITS[share][0])*100)/100
            if difference < 0:
                tag = ('down',)
            elif difference == 0:
                tag = ('equal',)
            else:
                tag = ('up',)
            self.profit_table.insert('', 'end', text=share, values=(STOCK[share][0], STOCK[share][1]+' zł', PRICE[idx]+' zł', str(STOCK_PROFITS[share][0])+' zł', str(STOCK_PROFITS[share][1])+' zł', str(difference) + ' zł'), tags=tag)

    def initialize_dividends(self):
        self.dividends = Label(self.master, text="Dywidendy", font="Verdana 10 bold")
        self.dividends.grid(row=20, column=0)

        self.dividends_table = Treeview(self.master, height=6, columns=("Data dywidendy", "Stopa", "Data wyplaty", "Dywidenda", "Calkowita wartosc dywidendy"))
        self.dividends_table.tag_configure('normal', foreground='black', font="Verdana 10 bold")
        self.dividends_table.heading('#0', text="Nazwa")
        self.dividends_table.heading('Data dywidendy', text="Data dywidendy")
        self.dividends_table.heading('Stopa', text="Stopa")
        self.dividends_table.heading('Data wyplaty', text="Data wyplaty")
        self.dividends_table.heading('Dywidenda', text="Dywidenda")
        self.dividends_table.heading('Calkowita wartosc dywidendy', text="Calkowita wartosc dywidendy")
        self.dividends_table.column('#0', stretch=YES, anchor='center', width=120)
        self.dividends_table.column('Data dywidendy', stretch=YES, anchor='center', width=100)
        self.dividends_table.column('Stopa', stretch=YES, anchor='center', width=150)
        self.dividends_table.column('Data wyplaty', stretch=YES, anchor='center', width=150)
        self.dividends_table.column('Dywidenda', stretch=YES, anchor='center', width=150)
        self.dividends_table.column('Calkowita wartosc dywidendy', stretch=YES, anchor='center', width=150)
        self.dividends_table.grid(row=21, columnspan=3, sticky='nsew')

        for share in MY_COMPANIES:
            idx = DIVIDEND_COMPANY.index(share)
            total_value = round(int(STOCK[share][0]) * float(DIVIDEND[idx][:4]) - round(int(STOCK[share][0]) * float(DIVIDEND[idx][:4]) * 0.19),2)
            self.dividends_table.insert('', 'end', text=share, values=(DIVIDEND_DATE[idx], INTEREST[idx], PAY_DATE[idx], DIVIDEND[idx], str(total_value)+' zł'), tags=('normal',))

    def add_new_company(self):
        AddCompanyDialog(self.master)

    def delete_company(self):
        delete_company = tkinter.simpledialog.askstring("Delete company", "Company name:", parent=self.master)
        file_companies = open('companies.txt', 'r+')
        file_lines = file_companies.readlines()
        file_companies.seek(0)
        for line in file_lines:
            if line.split(":")[0].strip() != delete_company:
                file_companies.write(line)
                # print(line.strip())
        file_companies.truncate()
        file_companies.close()

    def refresh(self):
        stockchecker.clear_informations()
        clear_stock_informations()
        stockchecker.get_my_companies_info()
        fill_user_stock()
        calculate_interest()
        self.initialize_interface_gpw()
        self.initalize_interface_profits()


class AddCompanyDialog:
    def __init__(self, parent):
        self.top = Toplevel(parent)
        self.top.wm_title("Add company")
        self.top.geometry("250x150")

        self.company_label = Label(self.top, text="Enter company name:")
        self.company_label.grid(row=0, column=2)
        self.company_entry = Entry(self.top)
        self.company_entry.grid(row=1, column=2)
        self.company_stock = Label(self.top, text="Enter your stock:")
        self.company_stock.grid(row=2, column=2)
        self.stock_entry = Entry(self.top)
        self.stock_entry.grid(row=3, column=2)
        self.company_price = Label(self.top, text="Enter your price for one share:")
        self.company_price.grid(row=4, column=2)
        self.price_entry = Entry(self.top)
        self.price_entry.grid(row=5, column=2)

        self.button_ok = Button(self.top, text="OK", command=self.click_ok)
        self.button_ok.grid(row=10, column=2, columnspan=1, rowspan=4)
        self.button_cancel = Button(self.top, text="Cancel", command=self.top.destroy)
        self.button_cancel.grid(row=10, column=3, columnspan=3, rowspan=4)

    def click_ok(self):
        name = self.company_entry.get()
        stock = self.stock_entry.get()
        price = self.price_entry.get()
        if name:
            file_companies = open('companies.txt', 'a')
            file_companies.write(name + ":" + stock + ":" + price + '\n')
            file_companies.close()
        self.top.destroy()

def main():
    root = Tk()
    app = GUI(root)
    root.mainloop()

if __name__ == '__main__':
    get_my_companies_info()
    fill_user_stock()
    calculate_interest()
    get_dividend_for_company(MY_COMPANIES)
    main()