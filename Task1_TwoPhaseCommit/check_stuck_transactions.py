import psycopg2
import subprocess

DELETE = True

conn_fly = psycopg2.connect(
    host="localhost",
    database="db1",
    user="postgres",
    password="myPassword")
print('Connected to DB_1 "Fly"')
conn_fly.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
curs = conn_fly.cursor()
curs.execute("SELECT gid FROM pg_prepared_xacts WHERE database = current_database()")
ids_1 = curs.fetchall()
print('Stuck transactions')
print(ids_1)
if DELETE and ids_1:
    for id_ in ids_1:
        try:
            curs.execute("ROLLBACK PREPARED %s", id_)
            curs.execute("COMMIT PREPARED %s", id_)
        except:
            continue
    print('DB1 "Fly": Stuck transactions are rollback')
print('\n')

conn_hotel = psycopg2.connect(
    host="localhost",
    database="db2",
    user="postgres",
    password="myPassword")
print('Connected to DB_2 "Hotel"')
conn_hotel.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
curs = conn_hotel.cursor()
curs.execute("SELECT gid FROM pg_prepared_xacts WHERE database = current_database()")
ids_2 = curs.fetchall()
print('Stuck transactions')
print(ids_2)
if DELETE and ids_2:
    for id_ in ids_2:
        try:
            curs.execute("ROLLBACK PREPARED %s", id_)
            curs.execute("COMMIT PREPARED %s", id_)
        except:
            continue
    print('DB2 "Hotel": Stuck transactions are rollback')
print('\n')

conn_account = psycopg2.connect(
    host="localhost",
    database="db3",
    user="postgres",
    password="myPassword")
print('Connected to DB_3 "Account"')
conn_account.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
curs = conn_account.cursor()
curs.execute("SELECT gid FROM pg_prepared_xacts WHERE database = current_database()")
ids_3 = curs.fetchall()
print('Stuck transactions')
print(ids_3)
if DELETE and ids_3:
    for id_ in ids_3:
        try:
            curs.execute("ROLLBACK PREPARED %s", id_)
            curs.execute("COMMIT PREPARED %s", id_)
        except:
            continue
    print('DB3 "Account": Stuck transactions are rollback')
print('\n')