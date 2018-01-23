#update postgres database with information from Charity Navigator API

import requests, json, psycopg2

#get dictionary of all rated charities
#get first page
print("Page: 1")
r = requests.get("https://api.data.charitynavigator.org/v2/Organizations", \
    params={'app_id': 'c544881e', 'app_key': 'fa592b85da3249ff1d05814cb0a2c34a',\
    'rated': True, 'pageSize': 1000, 'pageNum': 1})
d = json.loads(r.content)

#loop through pages until it gets an empty request with errorMessage
pageNum = 2
while True:
    print("Page:", pageNum)
    r = requests.get("https://api.data.charitynavigator.org/v2/Organizations", \
        params={'app_id': 'c544881e', 'app_key': 'fa592b85da3249ff1d05814cb0a2c34a',\
        'rated': True, 'pageSize': 1000, 'pageNum': pageNum})
    f = json.loads(r.content)
    if 'errorMessage' in f:
        break
    d.extend(f)
    pageNum = pageNum + 1


#connect to database
conn = psycopg2.connect(host="localhost", database="charity_db")
cur = conn.cursor()

"""
#drop table
dropCommand = "DROP TABLE all_charities"
cur.execute(dropCommand)
conn.commit()

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

"""

#delete data in table
deleteCommand = "DELETE FROM all_charities"
cur.execute(deleteCommand)
conn.commit()



#parse through dictionary and add desired info to database
#charityNumber = 1
for charity in d:
    #print("Charity Number: " + str(charityNumber))
    #charityNumber = charityNumber + 1;
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
    

"""
#delete data in table
deleteCommand = "DELETE FROM all_charities"
cur.execute(deleteCommand)
conn.commit()

#test individual charities
category = d[221]['category']['categoryName']
cause = d[221]['cause']['causeName']
name = d[221]['charityName']
url = d[221]['charityNavigatorURL']
rating = str(d[221]['currentRating']['rating'])
ein = d[221]['ein']
tagline = d[221]['tagLine']
sql = "INSERT INTO all_charities VALUES(%s, %s, %s, %s, %s, %s, %s)"
cur.execute(sql, (name, cause, category, ein, tagline, rating, url))

"""

#save
conn.commit() 
cur.close()
conn.close()
    
