select oazon from dolgozo; -- vetítés csak egy bizonyos rész kivétele, multihalmaz

select distinct foglalkozas from dolgozo;

select * from dolgozo
where fizetés>2800;

select dnev, dkod from dolgozo
where fizetes>=2000
and fizetes<=4500;

select fizetes*12 "éves fizu" from dolgozo;

select * from dolgozo
where fizetes between 2000 and 4500;

select * from dolgozo
where oazon in (10, 20);

select dkod "dolgozo kodja" from dolgozo
where oazon=10
or oazon=20;

select * from dolgozo
where dnev = 'KING';

select * from dolgozo
where dnev like 'S%';


