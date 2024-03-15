--Query 1

SELECT references_index_2, paper_title_, index_1, Author_name, venue_name  FROM RESEARCH_PAPER_ INNER JOIN references_ ON RESEARCH_PAPER_.index = references_.index_1 INNER JOIN authorship ON authorship.index = RESEARCH_PAPER_.index


--Query 2

SELECT index_1, paper_title_,references_index_2, Author_name, venue_name  FROM RESEARCH_PAPER_ INNER JOIN references_ ON RESEARCH_PAPER_.index = references_.references_index_2 INNER JOIN authorship ON authorship.index = RESEARCH_PAPER_.index


--Query 3

SELECT T_2.references_index_2, paper_title_, T_1.index_1, Author_name, venue_name FROM references_ as T_1 INNER JOIN references_ as T_2 ON T_1.references_index_2 = T_2.index_1 INNER JOIN RESEARCH_PAPER_ ON RESEARCH_PAPER_.index = T_1.index_1 INNER JOIN authorship ON authorship.index = RESEARCH_PAPER_.index


--Query 4

select references_index_2 from references_ group by references_index_2 order by count(index_1) limit 20


--Query 5

CREATE VIEW multiauth AS
(SELECT alp.author_name as i1, bet.author_name as i2, alp.index 
from authorship as alp INNER JOIN authorship as bet 
ON alp.index = bet.index AND alp.author_name != bet.author_name)

CREATE VIEW author_pair AS
(SELECT i1, i2, count(*) as hook 
from multiauth GROUP BY i1, i2)
 
select i1, i2 from author_pair where hook > 1

--still some logic to be added as shown in the python file
--the number of rows will be of 146544


--Query 6

CREATE view triplets_ AS
(SELECT T1.index_1, T1.references_index_2, T3.index_1
FROM references_ as T1 
JOIN references_ as T2 ON T1.references_index_2 = T2.index_1 
JOIN references_ as T3 ON (T2.references_index_2 = T3.index_1 AND T3.references_index_2 = T1.index_1)
UNION
SELECT T1.index_1, T1.references_index_2, T2.references_index_2
FROM references_ as T1 
JOIN references_ as T2 ON T1.references_index_2 = T2.index_1 
JOIN references_ as T3 ON (T2.references_index_2 = T3.references_index_2 AND T3.index_1 = T1.index_1))

create view triplet_authors as
(select A1.Author_name as t1, A2.Author_name as t2, A3.Author_name as t3 FROM triplets_ 
JOIN authorship as A1 ON A1.index = triplets_.i1 
JOIN authorship as A2 ON A2.index = triplets_.i2
JOIN authorship as A3 ON A3.index = triplets_.i3
AND A1.Author_name != A2.Author_name
AND A1.Author_name != A3.Author_name
AND A2.Author_name != A3.Author_name)

select t1, t2, t3, count(*) from triplet_authors group by t1, t2, t3

--still some logic to be added as shown in the python file
--And the number of rows it spits out will be of 3478154