import psycopg2
import random

# Create connections to 3 DBs
conn_fly = psycopg2.connect(
    host="localhost",
    database="db1",
    user="postgres",
    password="myPassword")
print('Connected to DB_1 "Fly"')
conn_fly.autocommit=False

conn_hotel = psycopg2.connect(
    host="localhost",
    database="db2",
    user="postgres",
    password="myPassword")
print('Connected to DB_2 "Hotel"')
conn_hotel.autocommit=False

conn_account = psycopg2.connect(
    host="localhost",
    database="db3",
    user="postgres",
    password="myPassword")
cur_account = conn_account.cursor()
print('Connected to DB_3 "Account"')
conn_account.autocommit=False

cur_fly = conn_fly.cursor()
cur_hotel = conn_hotel.cursor()
cur_account = conn_account.cursor()

# Queries
sql_fly = """SELECT * FROM fly"""
sql_hotel = """SELECT * FROM hotel"""
sql_account = """SELECT * FROM account"""

# Two-phase transaction
conn_hotel.tpc_begin(conn_hotel.xid(random.randint(1, 10**5), 'transaction ID1', 'connection 1'))
conn_fly.tpc_begin(conn_fly.xid(random.randint(1, 10**5), 'transaction ID2', 'connection 2'))
conn_account.tpc_begin(conn_account.xid(random.randint(1, 10**5), 'transaction ID3', 'connection 3'))


cur_fly.execute(sql_fly)
cur_hotel.execute(sql_hotel)
cur_account.execute(sql_account)
print('Fly data')
for t in cur_fly.fetchall():
    print(t)
print('\n')

print('Hotel data')
for t in cur_hotel.fetchall():
    print(t)
print('\n')

print('Account data')
for t in cur_account.fetchall():
    print(t)
print('\n')