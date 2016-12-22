import stockchecker
import tkinter.simpledialog
from tkinter import *


class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Stock Exchange Checker")
        self.create_menu()
        self.create_window()

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

    def create_window(self):
        color = "green"
        photo_file = "stock_down.png"
        self.headline = Label(self.master, bg="#b3ccff", text="GPW", font="Verdana 10 bold")
        self.headline.grid(row=0, column=0)
        row = 1
        for i in range(len(stockchecker.MY_COMPANIES)):
            if stockchecker.CHANGE[i][0] == '-':
                color = "red"
                photo_file = "stock_down.png"
            if stockchecker.CHANGE[i] == '0,00':
                color = "black"
            column = 0
            self.company = Label(self.master, bg="#b3ccff", text=stockchecker.COMPANY[i], font="Verdana 10 bold", fg=color)
            self.company.grid(row=row, column=column)
            column += 1
            self.price = Label(self.master, bg="#b3ccff", text=stockchecker.PRICE[i], font="Verdana 10 bold", fg=color)
            self.price.grid(row=row, column=column)
            column += 1
            self.change = Label(self.master, bg="#b3ccff", text=stockchecker.CHANGE[i], font="Verdana 10 bold", fg=color)
            self.change.grid(row=row, column=column)
            column += 1
            photo = PhotoImage(file=photo_file)
            self.photo_label = Label(self.master, image=photo)
            self.photo_label.photo = photo
            self.photo_label.grid(row=row, column=column)
            column += 1
            self.percentage = Label(self.master, bg="#b3ccff", text=stockchecker.PERCENTAGE_CHANGE[i], font="Verdana 10 bold", fg=color)
            self.percentage.grid(row=row, column=column)
            column += 1
            self.date = Label(self.master, bg="#b3ccff", text=stockchecker.DATE[i], font="Verdana 10 bold", fg=color)
            self.date.grid(row=row, column=column)
            row += 1

    def getCompany(self):
        add_company = tkinter.simpledialog.askstring("Add company", "Company name:", parent=self.master)
        file_companies = open('companies.txt', 'a')
        file_companies.write(add_company + '\n')
        file_companies.close()

    def deleteCompany(self):
        delete_company = tkinter.simpledialog.askstring("Delete company", "Company name:", parent=self.master)
        file_companies = open('companies.txt', 'r+')
        file_lines = file_companies.readlines()
        file_companies.seek(0)
        for line in file_lines:
            if line.strip() != delete_company:
                file_companies.write(line)
                # print(line.strip())
        file_companies.truncate()
        file_companies.close()

    def refresh(self):
        stockchecker.clear_informations()
        stockchecker.get_my_companies_info()
        self.create_window()


def main():
    root = Tk()
    root.geometry("450x350+750+600")
    root.configure(background="#b3ccff")
    app = GUI(root)
    root.mainloop()

if __name__ == '__main__':
    stockchecker.get_my_companies_info()
    # print(stockchecker.MY_COMPANIES)
    # print(stockchecker.COMPANY)
    # print(stockchecker.PRICE)
    # print(stockchecker.CHANGE)
    # print(stockchecker.PERCENTAGE_CHANGE)
    # print(stockchecker.DATE)
    main()
