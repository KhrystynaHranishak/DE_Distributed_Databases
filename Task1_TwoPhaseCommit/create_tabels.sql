DROP DATABASE IF EXISTS DB1;
CREATE DATABASE DB1;
\c db1
drop table if exists fly;
create table fly(
    booking_id serial primary key,
    client_name varchar(255) NOT NULL,
    fly_number  varchar(255) NOT NULL,
    from_ varchar(255) NOT NULL,
    to_ varchar(255) NOT NULL,
    date_ DATE NOT NULL
);


DROP DATABASE IF EXISTS DB2;
CREATE DATABASE DB2;
\c db2
drop table if exists hotel;
create table hotel(
    booking_id serial primary key,
    client_name varchar(255) NOT NULL,
    hotel_name  varchar(255) NOT NULL,
    arrival DATE NOT NULL,
    departure DATE NOT NULL
);

DROP DATABASE IF EXISTS DB3;
CREATE DATABASE DB3;
\c db3 
drop table if exists account;
create table account(
    account_id serial primary key,
    client_name varchar(255) NOT NULL,
    amount  numeric CHECK(amount > 0)
);
truncate table account;
insert into account(client_name, amount) 
values 
('Nick', 500), 
('Chris', 200);