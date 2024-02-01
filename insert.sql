-- HURRICANE IDA 2022 CHANGE ORDERS
-- KELLY

/*
SELECT PARID, A.TAXYR, A.VAL04 OLD_LANDASMT, A.VAL05 OLD_BLDGASMT, A.VAL06 OLD_TOTASMT, A.VAL08 OLD_HEAMT, 
N.VAL01 NEW_LANDASMT, N.VAL02 NEW_BLDGASMT, N.VAL01 + N.VAL02 NEW_TOTASMT, A.VAL08 NEW_HEAMT
--APR_LAND, APR_BLDG, n.val01, n.val02, n.char01, A.VAL04, VAL05, VAL08
FROM NOA_PARID_CHANGE_ORDERS N
INNER JOIN ASMT A USING (PARID)
WHERE TAXYR =2022 AND CUR ='Y' 
and n.val01+ n.val02 <>  a.val06;
*/

/*
delete from noa_parid3 
where char01 is null;

update noa_parid3 p
set parid = (select parid from altidindx i where taxyr =2017 and  altid =  p.char01);
commit;


select parid, A.VAL01, A.val02, A.val03, A.val04, A.val05, val06, flag4, flag7, flag8, LUC, VALCLASS
from asmt a
INNER JOIN NOA_PARID3 N USING (PARID)
where taxyr =2017 and cur ='Y' 

*/


DELETE FROM NOA_LTC_CHANGE_ORDERS_RE_BATCH ;


COMMIT;

--DROP SEQUENCE change_order_seq;

--CREATE SEQUENCE change_order_seq  START WITH  1 INCREMENT BY 1;

INSERT INTO NOA_LTC_CHANGE_ORDERS_RE_BATCH
(
SELECT 
SUBSTR(AI.ALTID,1,1) JUR
,A.PARID
,NULL
,NULL
,A.TAXYR   --  2022 CHANGE ORDER   
-- taxyear of the change order
-- fips code
,DECODE(SUBSTR(ai.altid,1,1),'1',22171
            ,'2',22172
            ,'3',22173
            ,'4',22174
            ,'5',22175
            ,'6',22176
            ,'7',22177
            ,'0',DECODE(l.taxdist,'01',22171,
                 '02',22171,
                 '03',22171,
                 '04',22171,
                 '05',22171,
                 '06',22172,
                 '07',22172,
                 '08',22172,
                 '7W',22173,
                 '8W',22173,
                 '9W',22173,
                 '11',22174,
                 '12',22174,
                 '13',22175,
                 '14',22176,
                 '15',22176,
                 '16',22177,
					  '17',22177,99999)) fips_code
,ai.altid
-- ward based on substr(altid,2,2) 
,DECODE(substr(ai.altid,1,1), '2', '05',
		         '3', SUBSTR(ai.altid,2,2),
		  			'4', SUBSTR(ai.altid,2,2),
					'5', SUBSTR(ai.altid,2,2),
		  			'6', SUBSTR(ai.altid,2,2),
					'7', SUBSTR(ai.altid,2,2),
		         '1', SUBSTR(ai.altid,2,2)) 		  

--,CASE WHEN l.taxdist IS NULL THEN SUBSTR(ai.altid,2,2) ELSE trim(l.taxdist) END ward  -- ward
--,LPAD(TO_CHAR(change_order_seq.NEXTVAL),4,'0')   -- batch no. and assessor ref no
,'&&batchno'|| LPAD(TO_CHAR(change_order_seq.NEXTVAL),4,'0')   -- batch no. and assessor ref no
--,'&&batchno'|| '-'||trim(l.user2)||'-'||trim(l.user3)||'-'||trim(l.user4)   -- batch no. and assessor ref no (bk/folio/line)
-- place_fips
/*
,DECODE(l.taxdist,'01',96001,
                 '02',96002,
                 '03',96003,
                 '04',96004,
                 '05',96005,
                 '06',96006,
                 '07',96007,
                 '08',96008,
                 '7W',96007,
                 '8W',96008,
                 '9W',96009,
                 '11',96011,
                 '12',96012,
                 '13',96013,
                 '14',96014,
                 '15',96015,
                 '16',96016,
					  '17',96017,99999) place_fis
*/
,DECODE(SUBSTR(ai.altid,2,2),'01',96001,
                 '02',96002,
                 '03',96003,
                 '04',96004,
                 '05',96005,
                 '06',96006,
                 '07',96007,
                 '08',96008,
                 '7W',96007,
                 '8W',96008,
                 '9W',96009,
                 '11',96011,
                 '12',96012,
                 '13',96013,
                 '14',96014,
                 '15',96015,
                 '16',96016,
					  '17',96017,99999) place_fis
					  
-- parcel address
,A.PARID
/*
CASE WHEN P.adrdir IS NULL THEN (P.ADRNO || ' ' || P.ADRSTR || ' ' || P.ADRSUF) 
		ELSE (P.ADRNO ||' '|| P.ADRDIR ||' '|| P.ADRSTR ||' '|| P.ADRSUF ) 
		END ||
 CASE WHEN P.unitno IS NOT NULL THEN ' UNIT ' || P.unitno END
 */		   
,DECODE(a.jur,'0','PS','RE')
-- assessment status
,'AC' --'AC'  -- status active 'EX' EXEMPT
,CASE 
    WHEN A.FLAG7 IS NOT NULL THEN 2 
    WHEN A.FLAG4 IS NOT NULL THEN 1
    ELSE 0
 END HE_EXEMPT
    
-- DECODE(a.flag7,'Y',2,DECODE(a.flag4,'Y',1,0)) homeexcept

, CASE WHEN A.FLAG4 IS NOT NULL THEN 100 ELSE 0 END HE_PCT

--DECODE(DECODE(a.flag7,'Y',2,DECODE(a.flag4,'Y',1,0)),0,0,100)
,'N'
--,trim(o.own1)
,O.OWN1 
,CASE WHEN o.marstat = 0 THEN SUBSTR(o.careof,1,50) ELSE NULL END contact_name
--,case when o.addr1 is not null then SUBSTR(o.addr1,1,40) else SUBSTR(o.addr2,1,50) end
--,case when o.addr1 is not null then SUBSTR(o.addr2,1,40) else null end
--,SUBSTR(o.cityname || ' ' || o.statecode  ||' ' ||o.zip1,1,40)
,O.ADDR1 
,O.ADDR2 
,O.CITYNAME || ', ' || O.STATECODE || ' ' || O.ZIP1
,'N'
,'IMPROVEMENT DECREASE VALUE, ERROR IN SQUARE FEET AND OR CLASSIFICATION CALCULATION'  -- REASON CODE 
 
,'0'
,0
,case when p.user3 is not null then p.user3 else '01' end landcode
,case when p.user3 is not null then p.user3 else '01' end landcode
--,'01'   -- CHECK LTC PROPERTY CLASS CODE
--,'01'
,1
,1
,'L'
,'L'
,0   -- OTHER EXEMPT OLD
,0   --CASE WHEN NVL(A.VAL04,0)<>0 THEN 3 ELSE 0 END   -- OTHER EXEMPT NEW  = institutional
,A.val04   -- PRESENT LAND ASMT TOTAL  for taxyear of change order, e.g., 2011 
,N.val01 -- NEW LAND ASMT TOTAL -- after update asmt using noa_aprval_temp_file
,0   -- PRESENT EXEMPTION  TOTAL (will calculate share between land and improvement in next sql
,0 --,N.VAL01      -- new exeption total - 0 exempt
,A.VAL04         -- calculate old assessment share next sql  
,N.val01  --  taxpayer new asmt share 
-- NOTE:  FOR EXEMPT PROPERTIES, LTC UPLOAD DOES NOT ACCEPT 0 VALUE FOR TAXPAYER SHARE FOR  LAND AND IMPROVEMENT
-- WILL HAVE TO CONFIRM IF AFTER SAVING THE CHANGE ORDER THE TAXPAYER SHARE WILL CHANGE THIS VALUES

-- second record for improvement

--,'02'   -- CHECK LTC PROPERTY CLASS CODE
--,'02'
,case when p.user4 is not null then p.user4 else '02' end bldgcode
,case when p.user4 is not null then p.user4 else '02' end bldgcode
,1
,1
,'I'
,'I'
,0   -- OTHER EXEMPT OLD
,0 -- CASE WHEN NVL(A.VAL05,0)<>0 THEN 3 ELSE 0 END   -- OTHER EXEMPT NEW  = institutional
,A.val05   -- PRESENT IMPROVEMENT ASMT TOTAL
,N.val02 -- NEW improvement ASMT TOTAL
,A.val08   -- PRESENT EXEMPTION  TOTAL (will calculate share between land and improvement in next sql
,a.val08         -- new exemption total
,NVL(A.VAL05,0) - NVL(A.VAL08,0) -- calculate old assessment share next sql  
,NVL(N.val02,0) - NVL(a.VAL08,0)  --,A.VAL05  -- taxpayer new asmt share
-- PROP DESC000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
,trim(l.legal1)|| ' ' || trim(l.legal2) || ' ' || trim(l.legal3)


--FROM IAS4.ASMT a, IAS4.ALTIDINDX ai, IAS4.LEGDAT l, IAS4.OWNDAT o
-- astm ab = current assessment
-- asmt a = taxyear of change order

FROM  asmt a, ALTIDINDX ai, LEGDAT l, OWNDAT o, noa_parid_CHANGE_ORDERS  n, pardat p --, ASMT B
WHERE 
--O.OWN1 LIKE 'UNITED STATES DEPARTMENT OF LABOR' AND

A.PARID = N.parid and 
A.rolltype = 'REAL' AND A.CUR = 'Y' AND -- a.jur = '3' AND
A.taxyr = 2022 AND 
 
--NVL(a.val01,0) > 0  AND   -- land total assessed  not = 0 (not yet exempt land still has a value) 
--a.val09 = 0 AND
--TRUNC(s.saledt) >= TO_DATE('01-jan-07', 'dd-mon-yy') AND 
--a.flag11 IS NULL AND  -- if not null, change order was already generated

a.jur = ai.jur     AND
a.parid = ai.parid AND
a.taxyr = ai.taxyr AND
ai.altid IS NOT NULL AND
(ai.ROWID = (SELECT MAX(x.ROWID) FROM IAS4.ALTIDINDX x 
            WHERE x.jur = ai.jur AND x.parid = ai.parid AND
                x.taxyr = ai.taxyr )) AND 

a.jur = l.jur     AND
a.parid = l.parid AND
a.taxyr = l.taxyr AND
a.cur = l.cur          AND

a.jur = p.jur     AND
a.parid = p.parid AND
A.taxyr = p.taxyr  AND
a.cur = p.cur 	   AND


A.jur = o.jur     AND
A.parid = o.parid AND
A.taxyr = O.taxyr AND
A.cur = o.cur);


COMMIT;

/*
UPDATE NOA_LTC_CHANGE_ORDERS_RE_BATCH 
SET value_old_hs1 = (CASE WHEN value_old_hs1 > 0 THEN
                               CASE WHEN value_old_total1 <= 7500 THEN value_old_total1 ELSE  7500	 END
								  ELSE 0  
							END)
WHERE value_old_hs1 > 0 AND SUBSTR(assessor_ref_no,1,2) = '&&batchno' ;

COMMIT;

UPDATE NOA_LTC_CHANGE_ORDERS_RE_BATCH
SET value_old_hs2 = 0
WHERE value_old_hs2 > 0 AND SUBSTR(assessor_ref_no,1,2) = '&&batchno' ;

COMMIT;

*/
/*

UPDATE NOA_LTC_CHANGE_ORDERS_RE_BATCH
SET value_old_tp1 = NVL((value_old_total1 - value_old_hs1),0)
WHERE SUBSTR(assessor_ref_no,1,2) = '&&batchno' ;

COMMIT;

UPDATE NOA_LTC_CHANGE_ORDERS_RE_BATCH
SET value_old_tp2 = NVL((value_old_total2 - value_old_hs2),0)
WHERE SUBSTR(assessor_ref_no,1,2) = '&&batchno'; 
*/
/*
UPDATE NOA_LTC_CHANGE_ORDERS_RE_BATCH
SET value_new_hs1 = 0,
	value_new_hs2 = 0,
	value_new_tp1 = 0,
	value_new_tp2 = 0
WHERE SUBSTR(assessor_ref_no,1,2) = '&&batchno' ;
*/

COMMIT; 

SELECT * FROM NOA_LTC_CHANGE_ORDERS_RE_BATCH
 WHERE
 fips_code = 99999 AND SUBSTR(assessor_ref_no,1,2) = '&&batchno'; 
 
SELECT *  FROM NOA_LTC_CHANGE_ORDERS_RE_BATCH
 WHERE
 fips_place_code = 99999 AND SUBSTR(assessor_ref_no,1,2) = '&&batchno'; 
 
 SELECT assessment_type, COUNT(*) FROM NOA_LTC_CHANGE_ORDERS_RE_BATCH
 WHERE SUBSTR(assessor_ref_no,1,2) = '&&batchno' 
 GROUP BY assessment_type ;
 
SELECT assessment_status, COUNT(*) FROM NOA_LTC_CHANGE_ORDERS_RE_BATCH
WHERE SUBSTR(assessor_ref_no,1,2) = '&&batchno'
 GROUP BY assessment_status;

SELECT * FROM NOA_LTC_CHANGE_ORDERS_RE_BATCH;