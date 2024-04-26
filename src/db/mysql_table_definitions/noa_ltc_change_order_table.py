from sqlalchemy import MetaData, Table, Column, String, Numeric

metadata = MetaData()

noa_ltc_change_order_table = Table('noa_ltc_change_order', metadata,
                        Column('auth_token', String(32)),
                        Column('tax_year', String(4)),
                        Column('fips_code', String(5)),
                        Column('assessment_no', String(20)),
                        Column('id_com', String(25)),
                        Column('batch_no', String(12)),
                        Column('ltc_nbr_total', String(20)),
                        Column('batch_created', String(22)),
                        Column('status', String(10)),
                        Column('batch_updated', String(22)),
                        Column('batch_submitted', String(22)),
                        Column('batch_approved', String(22)),
                        Column('batch_rejected', String(22)),
                        Column('reject_reason', String(22)),
                        Column('approved_by', String(20)),
                        Column('received_by', String(20)),
                        Column('batch_submitted_by', String(20)),
                        Column('co_detail_id', String(25)),
                        Column('fk_co_master', String(15)),
                        Column('status_cod', String(10)),
                        Column('status_date', String(22),),
                        Column('ltc_comment', String(100)),
                        Column('batch_item_no', String(10)),
                        Column('ward', String(4)),
                        Column('assessment_type', String(2)),
                        Column('taxpayer_name', String(50)),
                        Column('contact_name', String(50)),
                        Column('taxpayer_addr1', String(40)),
                        Column('taxpayer_addr2', String(40)),
                        Column('taxpayer_addr3', String(40)),
                        Column('tc_fee_pd', String(1)),
                        Column('reason', String(255)),
                        Column('chk_no', String(20)),
                        Column('chk_amt', String(9)),
                        Column('prop_desc', String(255)),
                        Column('parcel_add', String(50)),
                        Column('place_fips', String(5)),
                        Column('assessor_ref_no', String(15)),
                        Column('assessment_status', String(2)),
                        Column('homestead_exempt', String(1)),
                        Column('homestead_percent', String(3)),
                        Column('restoration_tax_expmt', String(1)),
                        Column('co_submitted_by', String(20)),
                        Column('id_cav', String(25)),
                        Column('changeordersdetailsid', String(25)),
                        Column('presentdescription', String(30)),
                        Column('presentexempt', String(7)),
                        Column('presenttotalassessed', Numeric(
                            precision=10, scale=2), default=0.0),
                        Column('presenthomesteadcredit', Numeric(
                            precision=10, scale=2), default=0.0),
                        Column('presenttaxpayershare', Numeric(
                            precision=15, scale=2), default=0.0),
                        Column('presentquantity', String(8)),
                        Column('presentunits', String(255)),
                        Column('reviseddescription', String(50)),
                        Column('revisedexempt', String(7)),
                        Column('revisedtotalassessed', Numeric(
                            precision=10, scale=2), default=0.0),
                        Column('revisedhomesteadcredit',
                               Numeric(precision=10, scale=2)),
                        Column('revisedtaxpayershare',
                               Numeric(precision=10, scale=2)),
                        Column('revisedunits', String(1)),
                        Column('revisedquantity', String(8))

)
