
SELECT a.parid, a.taxyr, ai.altid, p.adrno, p.adradd , p.adrdir , p.adrstr , p.adrsuf,  
    a.flag4, o.own1, o.addr1, o.addr2, o.addr3
FROM IASWORK.ASMT a
INNER JOIN IASWORK.OWNDAT o
    ON(o.parid = a.parid AND o.cur = 'Y' AND o.taxyr = a.taxyr)
INNER JOIN IASWORK.PARDAT p
    ON (p.parid = a.parid AND p.cur = 'Y' AND p.taxyr = a.taxyr)
INNER JOIN IASWORK.ALTIDINDX ai
    ON (ai.parid = a.parid AND ai.taxyr = a.taxyr)
WHERE a.parid = :1 AND a.taxyr = :2 AND a.cur = :3 AND ai.altid = :4 

