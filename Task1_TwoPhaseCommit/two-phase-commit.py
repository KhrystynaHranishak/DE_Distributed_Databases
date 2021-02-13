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

print('\n')

cur_fly = conn_fly.cursor()
cur_hotel = conn_hotel.cursor()
cur_account = conn_account.cursor()

# Queries
sql_fly = """INSERT INTO fly (client_name, fly_number, from_, to_, date_) 
              VALUES (%s, %s, %s, %s, %s);"""
data_fly = ('Nick', 'KLM 1382', 'KBP', 'AMS', '2020-05-01')

sql_hotel = """INSERT INTO hotel (client_name, hotel_name, arrival, departure) 
              VALUES (%s, %s, %s, %s);"""
data_hotel = ('Nick', 'Hilton', '2020-05-01', '2020-05-07')

price = 100
sql_account = """ UPDATE account SET amount = amount - %s WHERE client_name = %s"""
data_account = (price, data_fly[0])

id_1, id_2, id_3 = random.sample(range(1, 10**5), 3)
conn_fly.tpc_begin(conn_fly.xid(id_1, 'transaction ID1', 'connection 1'))
conn_hotel.tpc_begin(conn_hotel.xid(id_2, 'transaction ID2', 'connection 2'))
conn_account.tpc_begin(conn_account.xid(id_3, 'transaction ID3', 'connection 3'))

# Two-phase transaction
try:
    cur_fly.execute(sql_fly, data_fly)
    conn_fly.tpc_prepare()
    print('Prepared transaction for Fly')
    cur_fly.close()

    cur_hotel.execute(sql_hotel, data_hotel)
    conn_hotel.tpc_prepare()
    print('Prepared transaction for Hotel')
    cur_hotel.close()

    cur_account.execute(sql_account, data_account)
    conn_account.tpc_prepare()
    print('Prepared transaction for Account')
    cur_account.close()
except psycopg2.DatabaseError:
    conn_fly.tpc_rollback()
    conn_hotel.tpc_rollback()
    conn_account.tpc_rollback()
    print('\n')
    print('Rollback all transactions')
else:
    conn_account.tpc_commit()
    conn_fly.tpc_commit()
    conn_hotel.tpc_commit()
    print('\n')
    print('All transactions are committed')
finally:
    if conn_fly is not None:
        conn_fly.close()
    if conn_hotel is not None:
        conn_hotel.close()
    if conn_account is not None:
        conn_account.close()