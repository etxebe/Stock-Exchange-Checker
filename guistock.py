import stockchecker
import yourstock
import tkinter.simpledialog
import math
from tkinter import *


class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Stock Exchange Checker")
        self.gpw_frame, self.stock_frame = self.create_frames()
        self.create_menu()
        self.company = None
        self.price = None
        self.change = None
        self.photo_label = None
        self.percentage = None
        self.date = None
        self.stock_company = None
        self.shares = None
        self.stock_price = None
        self.stock_buy_value = None
        self.stock_current_value = None
        self.stock_profit = None
        self.create_gpw_window()
        self.create_stock_window()

    def create_frames(self):
        # gpw_frame = tkinter.Frame(self.master, bg="#b3ccff", bd=1, width=330, height=200, relief="solid")
        gpw_frame = tkinter.LabelFrame(self.master, bg="#b3ccff", bd=1, width=370, height=200, relief="raised", text="GPW")
        gpw_frame.grid(row=1, column=1, padx=10, pady=5)
        gpw_frame.grid_propagate(False)
        stock_frame = tkinter.LabelFrame(self.master, bg="#b3ccff", bd=1, width=370, height=200, relief="raised", text="My Stock")
        stock_frame.grid(row=8, column=1, padx=10, pady=5)
        stock_frame.grid_propagate(False)
        return gpw_frame, stock_frame

    def create_menu(self):
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        editmenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Add company", command=self.getCompany)
        filemenu.add_command(label="Delete company", command=self.deleteCompany)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.master.quit)
        editmenu.add_command(label="Refresh", command=self.refresh)
        menubar.add_cascade(label="File", menu=filemenu)
        menubar.add_cascade(label="Edit", menu=editmenu)
        self.master.config(menu=menubar)

    def create_gpw_window(self):
        photo_file = "stock_down.png"
        # self.headline = Label(self.gpw_frame, bg="#b3ccff", text="GPW", font="Verdana 10 bold")
        # self.headline.grid(row=0, column=0)
        row = 1
        for i in range(len(stockchecker.MY_COMPANIES)):
            color = "green"
            if stockchecker.CHANGE[i][0] == '-':
                color = "red"
                photo_file = "stock_down.png"
            if stockchecker.CHANGE[i] == '0,00':
                color = "black"
            column = 0
            self.company = Label(self.gpw_frame, bg="#b3ccff", text=stockchecker.COMPANY[i], font="Verdana 10 bold", fg=color)
            self.company.grid(row=row, column=column)
            column += 1
            self.price = Label(self.gpw_frame, bg="#b3ccff", text=stockchecker.PRICE[i], font="Verdana 10 bold", fg=color)
            self.price.grid(row=row, column=column)
            column += 1
            self.change = Label(self.gpw_frame, bg="#b3ccff", text=stockchecker.CHANGE[i], font="Verdana 10 bold", fg=color)
            self.change.grid(row=row, column=column)
            column += 1
            photo = PhotoImage(file=photo_file)
            self.photo_label = Label(self.gpw_frame, image=photo)
            self.photo_label.photo = photo
            self.photo_label.grid(row=row, column=column)
            column += 1
            self.percentage = Label(self.gpw_frame, bg="#b3ccff", text=stockchecker.PERCENTAGE_CHANGE[i], font="Verdana 10 bold", fg=color)
            self.percentage.grid(row=row, column=column)
            column += 1
            self.date = Label(self.gpw_frame, bg="#b3ccff", text=stockchecker.DATE[i], font="Verdana 10 bold", fg=color)
            self.date.grid(row=row, column=column)
            row += 1

    def create_stock_window(self):
        row = 9
        for share in stockchecker.MY_COMPANIES:
            if yourstock.STOCK_PROFITS[share][1] > yourstock.STOCK_PROFITS[share][0]:
                color = "green"
            elif yourstock.STOCK_PROFITS[share][1] == yourstock.STOCK_PROFITS[share][0]:
                color = "black"
            else:
                color = "red"
            column = 2
            self.stock_company = Label(self.stock_frame, bg="#b3ccff", text=share, font="Verdana 10 bold", fg=color)
            self.stock_company.grid(row=row, column=column)
            column += 1
            self.shares = Label(self.stock_frame, bg="#b3ccff", text=yourstock.STOCK[share][0], font="Verdana 10 bold", fg=color)
            self.shares.grid(row=row, column=column)
            column += 1
            self.stock_price = Label(self.stock_frame, bg="#b3ccff", text=yourstock.STOCK[share][1], font="Verdana 10 bold", fg=color)
            self.stock_price.grid(row=row, column=column)
            column += 2
            self.stock_buy_value = Label(self.stock_frame, bg="#b3ccff", text=yourstock.STOCK_PROFITS[share][0], font="Verdana 10 bold", fg=color)
            self.stock_buy_value.grid(row=row, column=column)
            column += 1
            self.stock_current_value = Label(self.stock_frame, bg="#b3ccff", text=yourstock.STOCK_PROFITS[share][1], font="Verdana 10 bold", fg=color)
            self.stock_current_value.grid(row=row, column=column)
            column += 1
            self.stock_profit = Label(self.stock_frame, bg="#b3ccff", text=math.ceil((yourstock.STOCK_PROFITS[share][1]-yourstock.STOCK_PROFITS[share][0])*100)/100, font="Verdana 10 bold", fg=color)
            self.stock_profit.grid(row=row, column=column)
            row += 1

    def getCompany(self):
        AddCompanyDialog(self.master)
        # add_company = tkinter.simpledialog.askstring("Add company", "Company name:", parent=self.master)
        # add_quantity = tkinter.simpledialog.askstring("Add company", "Number of your shares:", parent=self.master)

    def deleteCompany(self):
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
        yourstock.clear_stock_informations()
        stockchecker.get_my_companies_info()
        yourstock.fill_user_stock()
        yourstock.calculate_interest()
        self.create_gpw_window()
        self.create_stock_window()


class AddCompanyDialog:
    def __init__(self, parent):
        self.top = Toplevel(parent)
        self.top.wm_title("Add company")
        self.top.geometry("230x150")

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
        self.button_ok.grid(row=7, column=2)
        self.button_cancel = Button(self.top, text="Cancel", command=self.top.destroy)
        self.button_cancel.grid(row=7, column=3)

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
    root.geometry("400x450+750+600")
    root.configure(background="#b3ccff")
    app = GUI(root)
    root.mainloop()

if __name__ == '__main__':
    stockchecker.get_my_companies_info()
    yourstock.fill_user_stock()
    yourstock.calculate_interest()
    # print(stockchecker.MY_COMPANIES)
    # print(stockchecker.COMPANY)
    # print(stockchecker.PRICE)
    # print(stockchecker.CHANGE)
    # print(stockchecker.PERCENTAGE_CHANGE)
    # print(stockchecker.DATE)
    main()
