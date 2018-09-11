import requests
from bs4 import BeautifulSoup
import csv

f = csv.writer(open('com_book.csv', 'w'), delimiter=';', quoting=csv.QUOTE_ALL)
f.writerow(['Name', 'URL', 'Author', 'Price',
            'Number of Ratings', 'Average Rating'])

links = ["https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/"]
links.append("https://www.amazon.com/best-sellers-boo\ks-Amazon\
           /zgbs/books/ref=zg_bs_pg_2/143-0924735-3162352?_encoding=UTF8&pg=2")
links.append("https://www.amazon.com/best-sellers-books-Amazon\
           /zgbs/books/ref=zg_bs_pg_3/143-0924735-3162352?_encoding=UTF8&pg=3")
links.append("https://www.amazon.com/best-sellers-books-Amazon\
           /zgbs/books/ref=zg_bs_pg_4/143-0924735-3162352?_encoding=UTF8&pg=4")
links.append("https://www.amazon.com/best-sellers-books-Amazon\
           /zgbs/books/ref=zg_bs_pg_5/143-0924735-3162352?_encoding=UTF8&pg=5")

for link in links:
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    books = soup.find_all(class_="zg_itemImmersion")

    for book in books:

        temp = book.find(class_="p13n-sc-truncate")
        if temp is None:
            name = "Not available"
        else:
            name = temp.get_text()

        temp = book.find('a')
        if 'href' in temp.attrs:
            url = "https://www.amazon.com"+temp['href']
        else:
            url = "Not available"

        temp = book.find(class_="a-size-small a-link-child")
        if temp is None:
            temp = book.find(class_="a-size-small a-color-base")
            if temp is None:
                author = "Not available"
            else:
                author = temp.get_text()
        else:
            author = temp.get_text()

        temp = book.find(class_="p13n-sc-price")
        if temp is None:
            price = "Not available"
        else:
            price = temp.get_text()

        temp = book.find(class_="a-size-small a-link-normal")
        if temp is None:
            number_of_rating = "Not available"
        else:
            number_of_rating = temp.get_text()

        x = book.find(class_="a-icon-row a-spacing-none")
        temp = book.find(class_="a-icon-alt")
        if x is None:
            average_rating = "Not available"
        else:
            average_rating = temp.get_text()

        f.writerow([name, url, author, price,
                    number_of_rating, average_rating])
