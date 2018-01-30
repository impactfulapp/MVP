#populate postgres database with information from Charity Navigator API

import requests, json, psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

#connect to postgres
#conn = psycopg2.connect(host="localhost", database="niravsuraiya")
conn = psycopg2.connect(dbname='postgres', user='postgres', host='localhost', password='postgres')
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = conn.cursor()

#create user and new database
userCommand = "CREATE USER admin SUPERUSER"
cur.execute(userCommand)
conn.commit()
dbCommand = "CREATE DATABASE charity_db"
cur.execute(dbCommand)
cur.close()
conn.close()

#switch to new database
conn = psycopg2.connect(host="localhost", dbname="charity_db", user="postgres", password='postgres')
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

#get data from Charity Navigator
print("Page: 1")
r = requests.get("https://api.data.charitynavigator.org/v2/Organizations", \
    params={'app_id': 'c544881e', 'app_key': 'fa592b85da3249ff1d05814cb0a2c34a',\
    'rated': True, 'pageSize': 1000, 'pageNum': 1})
d = json.loads(r.content)

#loop through pages until it gets an empty request with errorMessage
pageNum = 2
while True:
    print ("Page:", pageNum)
    r = requests.get("https://api.data.charitynavigator.org/v2/Organizations", \
        params={'app_id': 'c544881e', 'app_key': 'fa592b85da3249ff1d05814cb0a2c34a',\
        'rated': True, 'pageSize': 1000, 'pageNum': pageNum})
    f = json.loads(r.content)
    if 'errorMessage' in f:
        break
    d.extend(f)
    pageNum = pageNum + 1

#parse through dictionary and add desired info to database
for charity in d:
    try:
        category = charity['category']['categoryName']
        cause = charity['cause']['causeName']
        name = charity['charityName']
        url = charity['charityNavigatorURL']
        rating = str(charity['currentRating']['rating'])
        ein = charity['ein']
        tagline = charity['tagLine']
    except Exception:
        #print("Exception caught")
        continue
    sql = "INSERT INTO all_charities VALUES(%s, %s, %s, %s, %s, %s, %s)"
    cur.execute(sql, (name, cause, category, ein, tagline, rating, url))

#save
conn.commit()
cur.close()
conn.close()
    
