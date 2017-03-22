select * from sila.folyok;

select dnev, 
to_char(belepes, 'Day') 
from dolgozo;

SELECT product_id, list_price, min_price,
COALESCE(0.9*list_price, min_price, 5) "Sale"
FROM oe.product_information
WHERE supplier_id = 102050
ORDER BY product_id;

SELECT last_name, salary,
       NVL2(commission_pct, salary + (salary * commission_pct), salary) income
  FROM hr.employees
  WHERE last_name like 'B%'
  ORDER BY last_name;
  
select dnev, nvl2(jutalek,fizetes+jutalek,fizetes) jövedelem from dolgozo;

select round (avg(fizetes), 1) atlag,
count (distinct foglalkozas),
to_char (max(belepes), 'YYYY') év,
min (jutalek),
sum (fizetes)
from dolgozo;

select count(*),count (all foglalkozas), count (distinct foglalkozas) from dolgozo;

select oazon, foglalkozas, round (avg(fizetes), 1) atlag,
count (distinct foglalkozas),
to_char (max(belepes), 'YYYY') év,
min (jutalek),
sum (fizetes)
from dolgozo
group by oazon, foglalkozas
having count(*) >=2
order by oazon, foglalkozas;

drop table employees;
drop table departments;
drop table locations;
drop table countries;
drop table regions;
drop table jobs;
drop table job_history;

create or replace synonym employees for hr.employees;
create or replace synonym departments for hr.departments;
create or replace synonym locations for hr.locations;
create or replace synonym countries for hr.countries;
create or replace synonym regions for hr.regions;
create or replace synonym jobs for hr.jobs;
create or replace synonym job_history for hr.job_history;

select oazon, count (*) letszam, avg(fizetes) from dolgozo group by oazon having count (*) >= 3;

select oazon, count (*) letszam, min(fizetes) from dolgozo 
group by oazon 
having min (fizetes) >= (select min(fizetes) from dolgozo
where oazon = 30);

(select min(fizetes) from dolgozo
where oazon = 30);

select avg(fizetes) from dolgozo
where foglalkozas = 'CLERK'
group by oazon
having count (*) >= 2;