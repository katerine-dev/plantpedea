import csv
from pathlib import Path
import mariadb


def connect():
    try:
        conn = mariadb.connect(
            user="plantpedia",
            password="plantpedia",
            host="127.0.0.1",
            port=3306,
            database="plantpedia"

        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")

    conn.autocommit = True

    return conn


def create_plant(cur, plant):
    try:
        cur.execute(
            """
            INSERT INTO plants (card_id, name, latin_name, solar_affinity, soil_type, water_amout, days_to_collect)  
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (plant.get('card_id'), plant.get('name'), plant.get('latin_name'), plant.get('solar_affinity'), plant.get('soil_type'), plant.get('water_amout'), plant.get('days_to_collect'))
        )
    except mariadb.Error as e:
        print(f"Error: {e}")

    return cur.lastrowid


def import_csv(path):
    with open(Path(__file__).parent / "../" / path) as csvfile:
        rows = csv.DictReader(csvfile)
        conn = connect()
        cur = conn.cursor(dictionary=True)
        for row in rows:
            create_plant(cur, row)


import_csv('data/plants.csv')


# cur.execute("SELECT card_id, name, latin_name, solar_affinity, soil_type, water_amout, days_to_collect FROM plants")

