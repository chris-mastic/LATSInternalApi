SELECT  
SUBSTR(AI.ALTID,1,1) AS 
jur,
ai.altid AS 
altid,
a.taxyr AS tax_year,
            DECODE(SUBSTR(ai.altid,1,1),'1',22171
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
					  '17',22177,99999)) AS
fips_code,
'assessment number' AS
assessment_number,
            DECODE(substr(ai.altid,1,1), '2', '05',
		         '3', SUBSTR(ai.altid,2,2),
		  			'4', SUBSTR(ai.altid,2,2),
					'5', SUBSTR(ai.altid,2,2),
		  			'6', SUBSTR(ai.altid,2,2),
					'7', SUBSTR(ai.altid,2,2),
		         '1', SUBSTR(ai.altid,2,2)) AS 
ward,
'TODO' AS
assessor_ref_no,
        DECODE(SUBSTR(ai.altid,2,2),'01',96001,
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
					  '17',96017,99999) AS
place_fips,
a.parid AS parcel_address,
'TODO' AS
assessment_type,

    DECODE(a.jur,'0','PS','RE') AS
assessment_status,
     CASE 
        WHEN A.FLAG7 IS NOT NULL THEN 2 
        WHEN A.FLAG4 IS NOT NULL THEN 1
        ELSE 0
      END
homestead_exempt,
     CASE WHEN A.FLAG4 IS NOT NULL THEN 100 ELSE 0 END
homestead_percent,
'N' AS
restoration_tax_exempt,
o.own1 AS taxpayer_name,
o.careof AS contact_name,
o.addr1 AS taxpayer_addr1,
o.addr2 AS taxpayer_addr2, 
o.addr3 AS taxpayer_addr3,
o.cityname AS city, 
o.statecode AS state,
o.zip1 AS zipcode,
'N' AS
tc_fee_pd,
'TODO' AS
reason,
'TODO' AS
check_no,
'TODO' AS
check_amount,
'4020' AS
building_ltc_subclass_old,
'4020' AS
building_ltc_subclass_new,
0 AS
building_quantity_old,
0 AS
building_quantity_new,
'L' AS
building_units_old,
'L' AS
building_units_new,
0 AS
building_other_exempt_old,
0 AS
building_other_exempt_new,
0 AS
building_value_old_total,
0 AS
building_value_new_total,
0 AS
building_value_old_hs,
0 AS
building_value_new_hs,
0 AS
building_value_old_tp,
0 AS
building_value_new_tp,
'3400' AS
land_ltc_subclass_old,
'3400' AS
land_ltc_subclass_new,
0 AS
land_quantity_old,
0 AS
land_quantity_new,
'L' AS
land_units_old,
'L' AS
land_units_new,
0 AS
land_other_exempt_old,
0 AS
land_other_exempt_new,
0 AS
land_value_old_total,
0 AS
land_value_new_total,
0 AS
land_value_old_hs,
0 AS
land_value_new_hs,
0 AS
land_value_old_tp,
0 AS
land_value_new_tp	

FROM IAS4TEST.ASMT a 
INNER JOIN IAS4TEST.ALTIDINDX ai
ON (ai.parid = a.parid AND ai.taxyr = a.taxyr)
INNER JOIN IAS4TEST.OWNDAT o
ON (o.parid = a.parid AND o.taxyr = a.taxyr AND o.cur = 'Y')
INNER JOIN IAS4TEST.LEGDAT l
ON (l.parid = a.parid AND l.taxyr = a.taxyr)
WHERE a.parid = :1 AND a.taxyr = :2
