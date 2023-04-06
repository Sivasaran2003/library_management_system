from django.db import models

# Create your models here.

# create table db.user(
# userID int primary key,
# uname varchar(20),
# Pno int,
# num_book int
# );

# create table db.book(
# ISBN int primary key,
# title varchar(20),
# price int,
# pubYear int,
# pubID int,
# author varchar(20),
# category varchar(20)
# );

# create table db.borrowed(
# userID int,
# bookID int,
# due_date date,
# primary key(userID,bookID)
# );

# create table publisher(
# pubID int primary key,
# pubName varchar(20)
# );

# create table available(
# bookID int primary key,
# available int
# );

# insert into user values(101,'name1',1234567890,2);
# insert into user values(102,'name2',1234567891,2);
# insert into user values(103,'name3',1234567892,3);
# insert into user values(104,'name4',1234567893,1);
# insert into user values(105,'name5',1234567894,0);

# insert into borrowed values(101,201,'2023-04-05');
# insert into borrowed values(101,202,'2023-04-05');
# insert into borrowed values(102,203,'2023-04-05');
# insert into borrowed values(102,204,'2023-04-05');
# insert into borrowed values(104,205,'2023-04-05');

# insert into book values(201,'title1',900,2020,301,'author1','c1');
# insert into book values(202,'title2',1000,2020,301,'author2','c1');
# insert into book values(203,'title3',550,2020,302,'author3','c2');
# insert into book values(204,'title4',400,2020,304,'author4','c3');
# insert into book values(205,'title5',700,2020,303,'author5','c2');

# insert into publisher values(301,'pub1');
# insert into publisher values(302,'pub2');
# insert into publisher values(303,'pub3');
# insert into publisher values(304,'pub4');

# insert into available values(201,50);
# insert into available values(202,100);
# insert into available values(203,37);
# insert into available values(204,120);
# insert into available values(205,80);

# alter table borrowed add constraint fkey0
# foreign key(userID) references user(userID) on delete cascade;

# alter table borrowed add constraint fkey1
# foreign key(bookID) references book(ISBN) on delete cascade;

# alter table available add constraint fkey2
# foreign key(bookID) references book(ISBN) on delete cascade;

# alter table book add constraint fkey3
# foreign key(pubID) references publisher(pubID) on delete cascade;

# select * from db.book;
# select * from publisher;
# select * from borrowed;
# select * from available;
# select * from db.user;

