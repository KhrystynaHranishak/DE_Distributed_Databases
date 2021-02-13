## Two-phase commit transactions

Imitation of a distributed system using PostgreSQL and realisation of two-phase commit transactions.  

* `create_tabels.sql` - create 3 DBs in one PostgreSQL Server  
* `two-phase-commit.py` - implementation of two-phase commit transactions  
* `check_dbs_values.py` - select all data that are in 3 DBs and print it  
* `check_stuck_transactions.py` - check if there are stuck transactions and delete them if it is specified.  

