-- d)feladat
select modell from Nyomtato
where szines='igen' 
and tipus='lézer';

--e)
select gyarto from termek
where tipus='laptop'
minus
select gyarto from termek
where tipus='pc';

--f)
select * from pc, termek; --direkt szorzat, minden attribútumot elérsz, közösekre szúrhetsz


select distinct p1.merevlemez from pc p1, pc p2 -- replikátum szûrés distinct
where p1.merevlemez=p2.merevlemez
and p1.modell<>p2.modell; --ne legyen ugyanaz, önmagát ne számolja 2x

--leggyorsabb pc)
select modell, sebesseg from pc
minus
select distinct p1.modell, p1.sebesseg 
from pc p1, pc p2 --szorzattábla
where p1.sebesseg<p2.sebesseg;
