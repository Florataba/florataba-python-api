import sqlite3
import random
import datetime


IMG = ["assets/flowers/flowers1.png",
       "assets/flowers/flowers2.png",
       "assets/flowers/flowers3.png",
       "assets/flowers/flowers4.png",
       "assets/flowers/flowers5.png",
       "assets/flowers/flowers6.png",
       "assets/flowers/flowers7.png",
       "assets/flowers/flowers8.png",
       "assets/flowers/flowers9.png",
       "assets/flowers/flowers10.png"]

TITLES = ["Red Roses",
          "White Roses",
          "Yellow Roses",
          "Green Roses",
          "Poppies",
          "Purple Tulips",
          "Orange Tulips",
          "White Tulips",
          "Purple Tulips",
          "Violets"]

EVENT_TYPES = ["Wedding",
               "Funeral",
               "Valentines Day",
               "Birthday"]

DESCRIPTION = ["Beautiful bouquet for your special event"]

try:
    sqlite_connection = sqlite3.connect('db.sqlite3')
    cursor = sqlite_connection.cursor()

    for _ in range(10):
        sqlite_insert_query = """INSERT INTO domain_bouquet
                              (id, created, updated, title, event_type_bouquet, description, price, is_single_bouquet, available_quantity, img_url)
                               VALUES
                              ({0}, {1}, {2}, "{3}", "{4}", "{5}", {6}, {7}, {8}, "{9}")"""\
            .format(_, str(datetime.datetime.now().timestamp()), str(datetime.datetime.now().timestamp()), TITLES[_], random.choice(EVENT_TYPES), DESCRIPTION[0], random.randint(1, 10) + 0.99, True, random.randint(10,100), IMG[_])
        count = cursor.execute(sqlite_insert_query)
        sqlite_connection.commit()
    cursor.close()

except sqlite3.Error as error:
    print("Failed to insert data into sqlite table", error)
finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("The SQLite connection is closed")

