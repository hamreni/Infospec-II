select initcap(dnev) from dolgozo
where lower (foglalkozas) like '%a%';

select initcap(dnev) from dolgozo
where instr (lower(foglalkozas),'a',1,2)>0 ;


select initcap(dnev), foglalkozas, belepes from dolgozo
where belepes<= TO_DATE ('1981.05.01', 'YYYY.MM.DD') ;

select initcap(dnev), foglalkozas,
TO_CHAR(belepes, 'YYYY.Month.Day', 'NLS_DATE_LANGUAGE = Japanese') datum, 
round(sysdate-belepes, 0) nap, 
round(months_between (sysdate,belepes), 0) honap 
from dolgozo
where belepes<= TO_DATE('1981.05.01', 'YYYY.MM.DD') ;

select initcap(dnev), foglalkozas,
TO_CHAR(belepes, 'YYYY.Month.Day', 'NLS_DATE_LANGUAGE = Hungarian') datum, 
round(sysdate-belepes, 0) nap, 
round(months_between (sysdate,belepes), 0) honap 
from dolgozo
where to_char(belepes, 'Day') like '%Péntek%' ;

select dnev, fizetes*12 "eves fizetes", jutalek, 
nvl(jutalek,0), 12*(fizetes+nvl(jutalek,0)) "eves jovedelem"
from dolgozo;

SELECT product_id, list_price, min_price,
   COALESCE(0.9*list_price, min_price, 5) "Sale"
   FROM oe.product_information
   WHERE supplier_id = 102050
   ORDER BY product_id;

