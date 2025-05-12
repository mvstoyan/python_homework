import sqlite3

with sqlite3.connect("../db/magazines.db") as conn:
    print("Database connected successfully.")
    cursor = conn.cursor()
    conn.execute("PRAGMA foreign_keys = 1")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS publishers (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS magazines (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        publisher_id INTEGER NOT NULL,
        FOREIGN KEY (publisher_id) REFERENCES publishers (id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscribers (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        address TEXT NOT NULL,
        UNIQUE(name, address)
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscribers (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        address TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscriptions (
        id INTEGER PRIMARY KEY,
        subscriber_id INTEGER NOT NULL,
        magazine_id INTEGER NOT NULL,
        expiration_date TEXT NOT NULL,
        FOREIGN KEY (subscriber_id) REFERENCES subscribers (id),
        FOREIGN KEY (magazine_id) REFERENCES magazines (id),
        UNIQUE(subscriber_id, magazine_id)
    )
    """)

cursor.execute("SELECT * FROM subscribers")
cursor.execute("SELECT * FROM magazines ORDER BY name ASC")
publisher_name = 'Tech Monthly'
print(f"\nMagazines by Publisher: {publisher_name}")
cursor.execute('''
   SELECT magazines.* 
   FROM magazines
   JOIN publishers ON magazines.publisher_id = publishers.id
   WHERE publishers.name = ?
''', (publisher_name,))


rows = cursor.fetchall()

#    print(row)

def add_publisher(cursor, name):
    try:
        cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

def add_magazin(cursor, name, publisher_id):
    try:
        cursor.execute("INSERT INTO magazines (name, publisher_id) VALUES (?,?)", (name, publisher_id))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

def add_subscriber(cursor, name, address):
    try:
        cursor.execute("INSERT INTO subscribers (name, address) VALUES (?,?)", (name, address))
    except sqlite3.IntegrityError:
        print(f"{name}, {address} is already in the database.")  
def add_subscriptions(cursor, subscriber_id, magazine_id, expiration_date):
    try:
        cursor.execute("INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?,?,?)", (subscriber_id, magazine_id, expiration_date))
    except sqlite3.IntegrityError:
        print(f"Subscription for subscriber {subscriber_id} to magazine {magazine_id} already exists.")   

add_publisher(cursor, 'Tech Monthly')
add_publisher(cursor, 'Another One')
add_publisher(cursor, 'Technicolor')

add_magazin(cursor, 'One Magazine', 1)
add_magazin(cursor, 'Another Magazine', 1)
add_magazin(cursor, 'Two Magazine', 2)
add_magazin(cursor, 'Three Magazine', 3)
add_subscriber(cursor, 'John Doe', '123 Main St')
add_subscriber(cursor, 'Jane Smith', '456 Elm St')
add_subscriber(cursor, 'John Doe', '789 Oak St')
add_subscriber(cursor, 'Bob Brown', '456 Elm St')
add_subscriber(cursor, 'John Doe', '123 Main St')
add_subscriptions(cursor, 1, 1, '2024-01-01')
add_subscriptions(cursor, 1, 2, '2024-02-01')
add_subscriptions(cursor, 2, 1, '2024-03-01')
add_subscriptions(cursor, 2, 2, '2024-04-01')
conn.commit()