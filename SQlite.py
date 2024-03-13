import sqlite3
import random

category = ""

horror = ("Dracula", "The Shining", "Frankenstein", "The Exorcist", "IT")

detective = ("Sherlock Holmes", "Gone Girl", "The Girl With Dragon Tattoo", "The Da Vinci Code",
             "The Murder of Roger Ackroyd")

fiction = ("To Kill a Mockingbird", "1948", "The Great Gatsby", "The Catcher In The Rye", "The Alchemist")

romance = ("Pride and Prejudice", "The Notebook", "Outlander", "Me Before You", "The Fault In Our Stars")

s_fiction = ("Dune", "Neuromancer", "Ender's Game", "Foundation", "The Hitchhiker's Guide To The Galaxy")


def generate_name():
    cat = {"1": "Horror", "2": "Detective", "3": "Fiction", "4": "Romance", "5": "Science fiction"}
    rd = str(random.randint(1, 5))
    global category
    category = cat.get(rd)
    name = ""

    if rd == "1":
        name = horror[random.randint(0, 4)]
    elif rd == "2":
        name = detective[random.randint(0, 4)]
    elif rd == "3":
        name = detective[random.randint(0, 4)]
    elif rd == "4":
        name = detective[random.randint(0, 4)]
    elif rd == "5":
        name = detective[random.randint(0, 4)]

    return name


def pages():
    pg = random.randint(20, 200)
    return pg


def cover():
    c_type = {"1": "Illustrated Cover", "2": "Photographic Cover", "3": "Abstract Cover", "4": "Minimalist Cover",
              "5": "Vintage Cover"}
    type_key = str(random.randint(1, 5))
    return c_type.get(type_key)


conn = sqlite3.connect('Library.DB')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS books (
             name text,
             pages int,
             cover_type text,
             category text)""")

for _ in range(10):
    c.execute("INSERT INTO books VALUES (?, ?, ?, ?)", (generate_name(), pages(), cover(), category))

rec = c.execute("SELECT AVG(pages) FROM books")
print(f"Average number of pages is {rec.fetchone()}")
rec = c.execute("SELECT name FROM books WHERE pages = (SELECT MAX(pages) FROM books)")
print(f"Biggest book in the library is {rec.fetchone()}")
