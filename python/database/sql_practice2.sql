create table dept(dno int, dname varchar2(20), loc varchar2(20));

insert into dept values(10,'accounting','new york');
insert into dept values(10,'research','dallas');
insert into dept values(10,'sales','chicago');
insert into dept values(10,'operation','boston');

commit;

-- create user 

create user thimma identified by thimma;
grant create session to thimma;
grant sysdba to thimma;
grant create database link to thimma;
create materialized view log on dept