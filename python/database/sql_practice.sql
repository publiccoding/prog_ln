
create table dept_table(dno int, dname varchar2(20), loc varchar2(20));

insert into dept_table values(10,'accounting','new york');
insert into dept_table values(10,'research','dallas');
insert into dept_table values(10,'sales','chicago');
insert into dept_table values(10,'operation','boston');

commit;

desc atm_loc
select count(amt) as amt_count, atm_loc from atm_loc where atm_loc = 'bangalore' and amt = 50000 group by atm_loc having count(amt)>2;
select * from customers;
desc uacc
select u.id,u.name,u.loc,a.amt,a.atm_loc,a.id from uacc u left join  atm_loc a on a.id=u.id;
create table emp_data(id int, name varchar2(20),addr varchar2(20));
insert into emp_data values(100,'thimma','varaganappalil');
insert into emp_data values(200,'lakshmi','rayakottai');
insert into emp_data values(300,'kumar','bangalore');
insert into emp_data values(200,'vasantha','rayakottai');
select * from emp_data;
create table dept(dep_id int , dep_name varchar2(20),mgr_id int);
insert into dept values(10,'software',200);
insert into dept values(20,'development',100);
insert into dept values(30,'testing',200);
insert into dept values(40,'operations',100);
select * from dept;
SELECT distinct(id), name , addr , dep_id, dep_name, mgr_id from emp_data right outer join dept on id=mgr_id;
select * from emp_data

-- *************************************************

--alter table emp_data
alter table emp_data add salary int;

-- *************************************************

-- Update table data 
update  emp_data set salary=2000 where id=100;
update  emp_data set salary=4000 where id=200;
update  emp_data set salary=5000 where id=300;
update  emp_data set salary=6000 where id=400;

select * from emp_data where name like 'th%';
select name , salary , salary +500 from emp_data;

-- *************************************************

-- second highest salary 
select max(salary) from emp_data where not salary=(select max(salary) from emp_data )
-- *************************************************


--SQL TOP, LIMIT and ROWNUM Example
select * from emp_data where rownum <=3;
SELECT name , round(salary/4) FROM emp_data ORDER BY salary DESC;
select top 2 from emp_data order by name;
select * from emp_data limit 2;
commit;

select name, ROUND((salary*12)/365) from emp_data;
select distinct id,salary from emp_data;
-- *************************************************

--VIEW Operation table 

create view vemp_data as select * from emp_data;
create view test_view as (select e.id, e.name,d.dep_name from emp_data e ,dept d ) 
select * from vemp_data;
select * from test_view;
insert into test_view values(600,'noname','testing')  -- will not work because of multiple base table . 
delete from vemp_data where id=400
drop view vemp_data;

select * from dept;
select * from emp_data;
select e.id, e.name,d.dep_name from emp_data e ,dept d;

select * from test_view ;
select id,name,addr, sum(salary) from emp_data group by addr;
select count(id), amt from atm_loc group by amt having count(atm_loc) > 2;
select count(id), amt,atm_loc, count(atm_loc) from atm_loc group by amt,atm_loc having count(atm_loc) > 2;

-- *************************************************

--creating public database link 

create  public database link test2db using 'localhost:1521/test2db';
drop public database link dblink;
CREATE PUBLIC DATABASE LINK dblink CONNECT TO thimma identified by thimma using  test2db;

-- creating local db link 
create  database link test2db connect to thimma identified by 'thimma' using 'localhost:1521/test2db';
create user thimma identified by thimma;

-- Grant user priviledges 

grant create session to thimma;
grant sysdba to thimma;
grant create database link to thimma;
grant dba to thimma identified by thimma

-- *************************************************
-- Materialized view. 
-- MV can be one of the following(Read-only/updatable/writable) and types of MV (primary-key/object/rowid/complex)
create materialized view mv_name
build [immediate|deferred]
refresh[fast|complete|force]
on [commit|demand]
[[enable|disable] query rewrite]
as select * from emp;

--build [immediate|deferred]  as soon as mv created if immediate data will storein MV , deferred only after first DB refresh data will store in MV 
--refresh [fast|complete|force] fast only the changed data on the master will get refelected on MV , on complete MV table data will truncated and repopulated , force - will try to do fast refresh if not then it will do complete refresh
-- for refresh fast MV's master table should create log table so that whenever the refresh fast happenes MV get data from the logs
-- on commit automatically refresh(more stresh) once master table data is saved , on demand will refresh the data on mv only after giving manual refresh command 
-- [[enable|disable] query rewrite]


select * from emp_data;
insert into emp_data values(500,'suman','krishnagiri',20000);
create materialized view mat_view as select id, sum(salary) from emp_data group by id;

execute dbms_mview.refresh('mat_view');
select * from mat_view;
desc atm_loc;

create materialized view mv_dept 
build immediate 
refresh complete 
on demand 
disable query rewrite 
as 
select * from dept_table;

select * from mv_dept

drop materialized view mv_dept
execute dbms_mview.refresh('mv_dept');

--create materialized view logs

create materialized view log on dept

alter session set query_rewrite_enabled=true;
alter session set query_rewrite_integrity=trusted;

---*******************************************************************************
-- ORACLE Tablespaces 
create tablespace thimma datafile 'thimma.dat' size 100M reuse autoextend on next 10M maxsize 200M;


select owner,table_name from all_tables;
select * from user_tables where table_name='emp_data';
select owner,table_name from all_tables where table_name like 'emp_%';
select 'alter table sys.'|| object_name || ' move tablespace '||'THIMMA;' from all_objects where owner = 'SYS' and object_type = 'TABLE' and object_id in (73634,73529,73530,73439,73440,73441,73449,73859);
select * from all_objects where object_type ='TABLE' and owner='SYS' and object_id in (73634,73529,73530,73439,73440,73441,73449,73859);
desc all_tables;
select * from cols where table_name like 'EMP';
select * from v$tablespace;
select * from tab where tabtype='TABLE';


alter table sys.EMP move tablcreate table thimma.emp as select * from emp;
select username from v$session;
select user from dual;


SELECT SUM(BYTES) FROM USER_SEGMENTS WHERE SEGMENT_TYPE='EMP_DATA';
espace THIMMA;
alter table sys.UACC move tablespace THIMMA;
alter table sys.ATM_LOC move tablespace THIMMA;
alter table sys.CUSTOMERS move tablespace THIMMA;
alter table sys.EMP_DATA move tablespace THIMMA;
alter table sys.DEPT move tablespace THIMMA;
alter table sys.MAT_VIEW move tablespace THIMMA;
alter table sys.MV_DEPT move tablespace THIMMA;

select 'alter table thimma.'|| object_name || 'move tablespace '||'thimma;' from all_objects where owner = 'thimma' and object_type = 'table' <> 'thimma'
alter index OWNER.PK_INDEX rebuild tablespace CORRECT_TS_NAME;
select object_name from all_objects where object_type='table' and owner='sys';
select owner,table_name from all_tables where table_name like 'emp_%';
select * from cols where table_name like 'emp';

---*******************************************************************************


-- cursors in oracle creates temporary memory area (context area) for processing sql stmt PLSQL controls the context area through cursor 
--implicit cursors - it will automatically created whenever sql stmt is executed  if no explicit cursor then programmer cannot control it ( whenever DML is issued implicit cursor is associated with it ) 
-- SQL cursor, which always has attributes such as %FOUND, %ISOPEN, %NOTFOUND, and %ROWCOUNT. The SQL cursor has additional attributes, %BULK_ROWCOUNT and %BULK_EXCEPTIONS, designed for use with the FORALL statement.
--explicit cursors - Explicit cursors are programmer-defined cursors for gaining more control over the context area. An explicit cursor should be defined in the declaration section of the PL/SQL Block. It is created on a SELECT Statement which returns more than one row
--Declaring the cursor for initializing the memory
--Opening the cursor for allocating the memory
--Fetching the cursor for retrieving the data
--Closing the cursor to release the allocated memory

--The syntax for the CURSOR FOR LOOP in Oracle/PLSQL is:

FOR record_index in cursor_name
LOOP
   {...statements...}
END LOOP;

EXIT [WHEN boolean_condition];

LOOP
   monthly_value := daily_value * 31;
   EXIT WHEN monthly_value > 4000;
END LOOP;

IF condition1 THEN
   {...statements to execute when condition1 is TRUE...}

ELSIF condition2 THEN
   {...statements to execute when condition2 is TRUE...}

END IF;
IF condition THEN
   {...statements to execute when condition is TRUE...}

ELSE
   {...statements to execute when condition is FALSE...}

END IF;

WHILE monthly_value <= 4000
LOOP
   monthly_value := daily_value * 31;
END LOOP;

FOR Lcntr IN REVERSE 1..15
LOOP
   LCalc := Lcntr * 31;
END LOOP;

--Implicit cursor example 

SET SERVEROUTPUT ON
 
BEGIN
 Dbms_Output.Put_Line(Systimestamp);
END;

declare 
total_rows number;
begin 
  update emp_data 
  set salary = salary + 500;
  if sql%notfound then 
      dbms_output.put_line('no customer found');
  elsif sql%found then 
      total_rows := sql%rowcount;
      dbms_output.put_line(total_rows ||' Customer Selected');
  end if;
end;
  
select * from emp_data;

SET SERVEROUTPUT ON;

declare 
    cid emp_data.id%type;
    cname emp_data.name%type;
    caddr emp_data.addr%type;
    csal emp_data.salary%type;
    cursor c_emp_data is select * from emp_data;

begin
  
    open c_emp_data ;
    loop 
    fetch c_emp_data into cid,cname,caddr,csal ;
        exit when c_emp_data%notfound;
        dbms_output.put_line(cid ||' '||cname||' '||caddr||' '||csal);
    end loop;
    close c_emp_data;
end;    

--******************************************************

-- PLSQL Records
--A record is a data structure that can hold data items of different kinds. Records consist of different fields, similar to a row of a database table.
--Table-based (%ROWTYPE)
--Cursor-based records
--User-defined records


--Table-based (%ROWTYPE)
declare 
    t_rec emp_data%rowtype;
begin 
    select * into t_rec from emp_data where salary=6500;
    dbms_output.put_line(t_rec.id||' '||t_rec.name||' '||t_rec.addr||' '||t_rec.salary);
end;
    
--Cursor-based records

declare 
    cursor cur_emp_data is select * from emp_data;
    rec_emp_data cur_emp_data%rowtype;
begin 
    open cur_emp_data ;
    loop 
        fetch cur_emp_data into rec_emp_data;
        exit when cur_emp_data%notfound;
        dbms_output.put_line(rec_emp_data.id||' '||rec_emp_data.name||' '||rec_emp_data.addr||' '||rec_emp_data.salary);
    end loop;
    dbms_output.put_line('DONE')
end;


--********************************************************************************************
-- trigger can't create on sys user

conn thimma

select user from dual

create table trigger_test(id number, description varchar2(50)) tablespace thimma;

drop  table trigger_test

create or replace trigger trigger_follow_test 
before insert on trigger_test 
for each row 
begin
dbms_output.put_line("TRIGGER FOLLOW TEST -Executed');
end;

set serveroutput on    

CREATE OR REPLACE PROCEDURE greetings 
AS 
BEGIN 
   dbms_output.put_line('Hello World!'); 
END;

EXECUTE greetings;


BEGIN 
   greetings; 
END; 


DECLARE 
   a number; 
   b number; 
   c number;

PROCEDURE findMin(x IN number, y IN number, z OUT number) IS 
BEGIN 
   IF x < y THEN 
      z:= x; 
   ELSE 
      z:= y; 
   END IF; 
END;   
BEGIN 
   a:= 23; 
   b:= 45; 
   findMin(a, b, c); 
   dbms_output.put_line(' Minimum of (23, 45) : ' || c); 
END; 

CREATE OR REPLACE FUNCTION totalCustomers( name INOUT varchar2, 
RETURN number IS 
   total number(2) := 0; 
BEGIN 
   SELECT count(*) into total 
   FROM emp_data; 
    
   RETURN total; 
END;

DECLARE 
   c number(2); 
BEGIN 
   c := totalCustomers(); 
   dbms_output.put_line('Total no. of Customers: ' || c); 
END; 

select * from emp_data;

