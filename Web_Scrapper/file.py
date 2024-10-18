import requests
from bs4 import BeautifulSoup
import csv
import sqlite3

def scrape_books(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    books = []

    for book in soup.find_all('div', class_='book'):
        title = book.find('h2', class_='title').text.strip()
        author = book.find('p', class_='author').text.strip()
        price = book.find('span', class_='price').text.strip()
        books.append({'title': title, 'author': author, 'price': price})

    return books

def save_to_csv(books, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['title', 'author', 'price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for book in books:
            writer.writerow(book)

def save_to_database(books, db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
         title TEXT,
         author TEXT,
         price TEXT)
    ''')

    for book in books:
        cursor.execute('''
            INSERT INTO books (title, author, price)
            VALUES (?, ?, ?)
        ''', (book['title'], book['author'], book['price']))

    conn.commit()
    conn.close()

def main():
    url = 'http://books.toscrape.com/'
    books = scrape_books(url)

    save_to_csv(books, 'books.csv')
    print("Data saved to books.csv")

    save_to_database(books, 'books.db')
    print("Data saved to books.db")

if __name__ == '__main__':
    main()