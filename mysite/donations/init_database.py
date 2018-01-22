#populate postgres database with information from Charity Navigator API

import requests, json, psycopg2

#connect to database
conn = psycopg2.connect(host="localhost", database="niravsuraiya")
cur = conn.cursor()

#create new table for all charities
createCommand = "CREATE TABLE all_charities (" + \
            "name VARCHAR(255) NOT NULL," + \
            "cause VARCHAR(255) NOT NULL," + \
            "category VARCHAR(255) NOT NULL," + \
            "ein VARCHAR(255) PRIMARY KEY NOT NULL," + \
            "tagline VARCHAR(255)," + \
            "rating INTEGER NOT NULL," + \
            "url VARCHAR(255) NOT NULL )"

cur.execute(createCommand)
conn.commit()
cur.close()
conn.close()
    
