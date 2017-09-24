#!/usr/bin/python
import MySQLdb
import sql_service
import collaborative_filtering as filter
from recommendation_data import dataset
from datetime import datetime


db = sql_service.connect()
start=datetime.now()
cur = db.cursor()
cur.execute("SELECT * FROM `BX-Book-Ratings` LIMIT 10000000")

# print all the first cell of all the rows
rows = cur.fetchall()
dataset = {}

def merge_two_dicts(x, y):
    """Given two dicts, merge them into a new dict as a shallow copy."""
    z = x.copy()
    z.update(y)
    return z

for row in rows:
    key = str(row[0])
    k = str(row[1])
    value = float(row[2]) / 2
    # import pdb;pdb.set_trace()
    if value == 0L:
        continue
    else:
        if key in dataset:
            dts = dict()
            dts[k] = value
            dataset[key] = merge_two_dicts(dataset[key], dts)
        else:
            dataset[key] = {k:value}

print type(dataset)

filter.dataset = dataset
from recommendation_data import dataset as dt
print dt

print dataset
print datetime.now()-start
for dts in dataset:
    user = dts
    print '------------------o-------------------------'
    print user
    print filter.user_recommendations(user)
    # print filter.most_similar_users(user, 5)
    print '------------------o-------------------------'
db.close()
