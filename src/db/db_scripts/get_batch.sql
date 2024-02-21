
SELECT a.parid, a.taxyr, ai.altid, o.own1
FROM ASMT a
INNER JOIN OWNDAT o ON o.parid = a.parid AND o.taxyr = a.taxyr
INNER JOIN ALTIDINDX ai ON ai.parid = a.parid AND ai.taxyr = a.taxyr
WHERE a.parid = :1 AND a.taxyr = :2 AND a.cur = :3
