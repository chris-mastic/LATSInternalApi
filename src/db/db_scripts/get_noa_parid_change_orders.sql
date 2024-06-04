SELECT parid
FROM noa_parid_change_orders
WHERE parid = :parid 
AND who = :who 
AND taxyr = :taxyr