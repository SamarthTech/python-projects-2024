from tinydb import TinyDB, Query


db = TinyDB('contact-book.json')
db.default_table_name = 'contact-book'
ContactQuery = Query()
