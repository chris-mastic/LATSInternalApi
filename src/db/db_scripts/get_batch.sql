SELECT 
SUBSTR(AI.ALTID,1,1) JUR
,A.PARID
,NULL AS SALEDT
,NULL AS RECORDDT
,A.TAXYR  AS TAX_YEAR
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
					  '17',22177,99999)) AS FIPS_CODE
,ai.altid AS ASSESSMENT_NO
,DECODE(substr(ai.altid,1,1), '2', '05',
		         '3', SUBSTR(ai.altid,2,2),
		  			'4', SUBSTR(ai.altid,2,2),
					'5', SUBSTR(ai.altid,2,2),
		  			'6', SUBSTR(ai.altid,2,2),
					'7', SUBSTR(ai.altid,2,2),
		         '1', SUBSTR(ai.altid,2,2)) AS WARD 
,'IT'|| LPAD(TO_CHAR(change_order_seq.NEXTVAL),4,'0') AS ASSESSOR_REF_NO
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
					  '17',96017,99999) AS FIPS_PLACE_CODE
,A.PARID AS PARCEL_ADDRESS
,DECODE(a.jur,'0','PS','RE') AS ASSESSMENT_TYPE       
,decode(a.valclass, 
    'C', 'AC', 
    'R', 'AC',
    'E', 'EX',
    'ER', 'EX') AS ASSESSMENT_STATUS
,CASE 
    WHEN A.FLAG7 IS NOT NULL THEN 2
    WHEN A.FLAG4 IS NOT NULL THEN 1
    ELSE 0
 END HOMSTEAD_EXEMPT 
, CASE WHEN A.FLAG4 IS NOT NULL THEN 100 ELSE 0 END HOMESTEAD_PERCENT
,'N' AS RESTORATION_TAX_ABATEMENT
,O.OWN1 AS TAXPAYER_NAME
,CASE WHEN o.marstat = '0' THEN SUBSTR(o.careof,1,50) ELSE NULL END CONTRACT_NAME
,O.ADDR1 AS TAXPAYER_ADDR1
,O.ADDR2 AS TAXPAYER_ADDR2
,O.CITYNAME || ', ' || O.STATECODE || ' ' || O.ZIP1 AS TAXPAYER_ADDR3
,'N' AS TC_FEE_PD
, null
,'0' AS CHECK_NO
,0 AS CHECK_AMOUNT
,case when p.user3 is not null then p.user3 else '01' end LTC_SUB_CLASS_OLD1
,case when p.user3 is not null then p.user3 else '01' end LTC_SUB_CLASS_NEW1
,1 AS QUANTITY_OLD1
,1 AS QUANTITY_NEW1
,'L' AS UNITS_OLD1
,'L' AS UNITS_NEW1
,0  OTHER_EXEMPT_OLD1
,0  OTHER_EXEMPT_NEW1
,A.val04 AS VALUE_OLD_TOTAL1
,N.val01 AS VALUE_NEW_TOTAL1
,0 AS VALUE_OLD_HS1
,0 AS VALUE_NEW_HS1
,A.VAL04 AS VALUE_OLD_TP1
,N.val01 AS VALUE_NEW_TP1
,case when p.user4 is not null then p.user4 else '02' end AS LTC_SUB_CLASS_OLD2
,case when p.user4 is not null then p.user4 else '02' end AS LTC_SUB_CLASS_NEW2
,1 AS QUANTITY_OLD2
,1 AS QUANTITY_NEW2
,'I' AS UNITS_0LD2
,'I' AS UNITS_NEW2
,0 AS OTHER_EXEMPT_OLD2
,0  AS OTHER_EXEMPT_NEW2
,A.val05 AS VALUE_OLD_TOTAL2
,N.val02 AS VALUE_NEW_TOTAL2
,A.val08 AS VALUE_OLD_HS2
,a.val08 AS VALUE_NEW_HS2
,NVL(A.VAL05,0) - NVL(A.VAL08,0) VALUE_OLD_TP2
,NVL(N.val02,0) - NVL(a.VAL08,0) VALUE_NEW_TP2
,trim(l.legal1)|| ' ' || trim(l.legal2) || ' ' || trim(l.legal3) AS PROPER_DESC
FROM  asmt a, ALTIDINDX ai, LEGDAT l, OWNDAT o, noa_parid_CHANGE_ORDERS  n, pardat p 
WHERE 
A.PARID = TRIM(N.parid) and 
A.rolltype = 'REAL' AND A.CUR = 'Y' AND 
A.taxyr = 2024 AND 
a.jur = ai.jur     AND
a.parid = ai.parid AND
a.taxyr = ai.taxyr AND
ai.altid IS NOT NULL AND
(ai.ROWID = (SELECT MAX(x.ROWID) FROM ALTIDINDX x 
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
A.cur = o.cur

